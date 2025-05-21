from enum import Enum

from cdk8s import JsonPatch
from cdk8s_plus_32 import Deployment, StatefulSet, Topology


class WhenUnsatisfiable(Enum):
    """Specifies how to deal with a pod if it doesn't satisfy the spread constraint.

    DO_NOT_SCHEDULE: Don't schedule the pod at all.
    SCHEDULE_ANYWAY: Schedule the pod anyway.
    """

    DO_NOT_SCHEDULE = "DoNotSchedule"
    SCHEDULE_ANYWAY = "ScheduleAnyway"


def add_topology_spread(
    target: Deployment | StatefulSet,
    when_unsatisfiable: WhenUnsatisfiable = WhenUnsatisfiable.SCHEDULE_ANYWAY,
):
    """Add topology spread constraints to a Deployment or StatefulSet.

    This function applies a topology spread constraint to a Deployment or
    StatefulSet to ensure pods are distributed across different Availability
    Zones to improve high availability and fault tolerance.

    Because we always have at least one node per zone, we set the minDomains to 3
    and setting maxSkew to 1 ensures an even distribution.
    """
    target._api_object.add_json_patch(
        JsonPatch.add(
            path="/spec/template/spec/topologySpreadConstraints",
            value=[
                {
                    "maxSkew": 1,
                    "minDomains": 3,
                    "topologyKey": Topology.ZONE,
                    "whenUnsatisfiable": when_unsatisfiable.value,
                    "labelSelector": {
                        "matchLabels": target.match_labels,
                    },
                }
            ],
        )
    )
