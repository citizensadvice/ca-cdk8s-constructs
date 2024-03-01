from hpa.hpa import build
from cdk8s_plus_27 import Deployment, HorizontalPodAutoscaler
from cdk8s import App, Chart
import pytest


@pytest.fixture(scope="function")
def chart_and_deployment() -> tuple[Chart, Deployment]:
    chart = Chart(App(), "test")
    deployment = Deployment(id="test", scope=chart)
    deployment.add_container(image="test")
    yield (chart, deployment)


def test_default(chart_and_deployment):
    chart, deployment = chart_and_deployment
    hpa = build(
        scope=chart,
        max_replicas=5,
        target=deployment,
    )
    assert hpa.api_version == "autoscaling/v2"
    assert hpa.max_replicas == 5
    assert hpa.min_replicas == 1


def test_utilizations(chart_and_deployment):
    chart, deployment = chart_and_deployment
    hpa = build(
        scope=chart,
        max_replicas=5,
        target=deployment,
        cpu_utilization=50,
        memory_utilization=50,
    )
    assert hpa.api_version == "autoscaling/v2"
    assert hpa.max_replicas == 5
    assert hpa.min_replicas == 1


def test_utilization_error(chart_and_deployment):
    chart, deployment = chart_and_deployment
    with pytest.raises(ValueError):
        build(
            scope=chart,
            max_replicas=5,
            target=deployment,
            cpu_utilization=101,
            memory_utilization=101,
        )
