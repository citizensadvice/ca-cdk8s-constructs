import pytest
from ca_cdk8s_constructs.container_resources import ca_container_resources
from cdk8s_plus_32 import Deployment
from cdk8s import Chart


def test_container_resources(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    container_resources = ca_container_resources(cpu=100, memory=512)
    deployment.add_container(
        image="nginx",
        resources=container_resources,
    )


def test_container_resources_error():
    with pytest.raises(ValueError):
        ca_container_resources(cpu=50, memory=125)
