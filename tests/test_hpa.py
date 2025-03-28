from ca_cdk8s_constructs.hpa import ca_hpa
from cdk8s_plus_31 import Deployment
from cdk8s import Chart


def test_hpa_no_containers(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    hpa = ca_hpa(chart_fixture, max_replicas=3, target=deployment)
    assert hpa.max_replicas == 3
    assert len(hpa.metrics) == 0


def test_hpa_with_containers(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    deployment.add_container(
        image="nginx",
    )
    hpa = ca_hpa(chart_fixture, max_replicas=3, target=deployment)
    assert hpa.max_replicas == 3
    assert len(hpa.metrics) == 2


def test_hpa_with_multiple_containers(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    deployment.add_container(
        image="nginx",
    )
    deployment.add_container(
        image="alpine",
    )
    hpa = ca_hpa(chart_fixture, max_replicas=3, target=deployment)
    assert hpa.max_replicas == 3
    assert len(hpa.metrics) == 4
