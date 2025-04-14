import pytest
from ca_cdk8s_constructs.hpa import ca_hpa
from cdk8s_plus_31 import Deployment
from cdk8s import Chart
from cdk8s_plus_31 import HorizontalPodAutoscaler


def test_hpa_default(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    hpa = ca_hpa(chart_fixture, target=deployment)
    assert isinstance(hpa, HorizontalPodAutoscaler)
    assert hpa.min_replicas == 1
    assert hpa.max_replicas == 3


def test_hpa_custom_values(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    hpa = ca_hpa(
        chart_fixture,
        max_replicas=5,
        min_replicas=2,
        cpu_utilization_target=80,
        memory_utilization_target=80,
        target=deployment,
    )
    assert hpa.max_replicas == 5
    assert hpa.min_replicas == 2


def test_hpa_invalid_values(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    with pytest.raises(ValueError):
        ca_hpa(chart_fixture, target=deployment, cpu_utilization_target=100)
    with pytest.raises(ValueError):
        ca_hpa(chart_fixture, target=deployment, cpu_utilization_target=20)
