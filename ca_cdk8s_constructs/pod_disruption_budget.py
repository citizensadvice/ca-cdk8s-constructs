from typing import Mapping
from cdk8s_plus_31.k8s import (
    KubePodDisruptionBudget,
    PodDisruptionBudgetSpec,
    LabelSelector,
    IntOrString,
)
from constructs import Construct


def ca_pod_disruption_budget(
    scope: Construct,
    id: str,
    match_labels: Mapping[str, str],
    max_unavailable: int = 1,
) -> KubePodDisruptionBudget:
    """Create a PodDisruptionBudget for a deployment.

    The match_labels can be extracted from a Deployment using the `match_labels` property.

    Args:
        scope: The scope of the construct.
        id: ID for the construct.
        match_labels: The labels to match for the PodDisruptionBudget.
        max_unavailable: The maximum number of unavailable pods. Defaults to 1.

    Returns:
        A PodDisruptionBudget.
    """
    return KubePodDisruptionBudget(
        scope,
        id,
        spec=PodDisruptionBudgetSpec(
            max_unavailable=IntOrString.from_number(max_unavailable),
            selector=LabelSelector(match_labels=match_labels),
        ),
    )
