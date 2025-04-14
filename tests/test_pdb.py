from ca_cdk8s_constructs.pod_disruption_budget import ca_pod_disruption_budget as ca_pdb
from cdk8s_plus_32 import Deployment
from cdk8s import Chart
from cdk8s_plus_32.k8s import (
    KubePodDisruptionBudget,
)


def test_pdb_default(chart_fixture: Chart):
    deployment = Deployment(chart_fixture, "test")
    pdb = ca_pdb(chart_fixture, "pdb", target=deployment)
    assert isinstance(pdb, KubePodDisruptionBudget)
