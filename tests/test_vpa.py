from ca_cdk8s_constructs.vpa import ca_vpa
from ca_cdk8s_constructs.imports.io.k8s.autoscaling import VerticalPodAutoscaler
from cdk8s_plus_32 import Deployment
from cdk8s import Chart


def test_vpa_default(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    vpa = ca_vpa(chart_fixture, "vpa", target=deployment)
    assert isinstance(vpa, VerticalPodAutoscaler)
