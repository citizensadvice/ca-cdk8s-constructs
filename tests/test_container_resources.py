from ca_cdk8s_constructs.container_resources import ca_container_resources
from cdk8s_plus_32 import Deployment, Cpu
from cdk8s import Chart, Size


def test_container_resources(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    container_resources = ca_container_resources(
        cpu=Cpu.millis(100), memory=Size.mebibytes(512)
    )
    deployment.add_container(
        image="nginx",
        resources=container_resources,
    )
