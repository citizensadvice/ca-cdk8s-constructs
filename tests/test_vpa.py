from ca_cdk8s_constructs.vpa import ca_vpa, VpaUpdateMode
from ca_cdk8s_constructs.imports.io.k8s.autoscaling import VerticalPodAutoscaler
from cdk8s_plus_32 import Deployment, Cpu
from cdk8s import Chart


def test_vpa_default(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    deployment.add_container(
        image="nginx:latest",
    )
    vpa = ca_vpa(chart_fixture, "vpa", target=deployment)
    assert isinstance(vpa, VerticalPodAutoscaler)
    manifest = chart_fixture.to_json()[1]
    assert manifest["kind"] == "VerticalPodAutoscaler"
    assert manifest["spec"]["targetRef"]["kind"] == "Deployment"
    assert manifest["spec"]["targetRef"]["name"] == deployment.name


def test_vpa_cpu_policy(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    deployment.add_container(
        image="nginx:latest",
    )
    vpa = ca_vpa(chart_fixture, "vpa", target=deployment, min_allowed_cpu=Cpu.millis(500))
    assert isinstance(vpa, VerticalPodAutoscaler)
    manifest = chart_fixture.to_json()[1]
    assert (
        manifest["spec"]["resourcePolicy"]["containerPolicies"][0]["minAllowed"]["cpu"]
        == "500m"
    )


def test_vpa_update_mode(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    deployment.add_container(
        image="nginx:latest",
    )
    vpa = ca_vpa(chart_fixture, "vpa", target=deployment, update_mode=VpaUpdateMode.OFF)
    assert isinstance(vpa, VerticalPodAutoscaler)
    manifest = chart_fixture.to_json()[1]
    print(manifest)
    assert manifest["spec"]["updatePolicy"]["updateMode"] == "Off"
