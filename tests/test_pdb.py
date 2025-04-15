from ca_cdk8s_constructs.pod_disruption_budget import ca_pod_disruption_budget as ca_pdb
from cdk8s_plus_32 import Deployment
from cdk8s import Chart
from cdk8s_plus_32.k8s import (
    KubePodDisruptionBudget,
)


def test_pdb_default(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    deployment.add_container(
        image="nginx:latest",
    )
    pdb = ca_pdb(chart_fixture, "pdb", target=deployment)
    assert isinstance(pdb, KubePodDisruptionBudget)
    manifest = chart_fixture.to_json()[1]
    assert manifest["kind"] == "PodDisruptionBudget"
    assert manifest["spec"]["maxUnavailable"] == 1
    assert manifest["spec"]["selector"]["matchLabels"]["cdk8s.io/metadata.addr"].startswith(
        "test"
    )


def test_pdb_max_unavailable(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    deployment.add_container(
        image="nginx:latest",
    )
    pdb = ca_pdb(chart_fixture, "pdb", target=deployment, max_unavailable=2)
    assert isinstance(pdb, KubePodDisruptionBudget)
    manifest = chart_fixture.to_json()[1]
    assert manifest["spec"]["maxUnavailable"] == 2
