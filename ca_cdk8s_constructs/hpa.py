from numbers import Number
import cdk8s_plus_31 as kplus
from constructs import Construct


def ca_hpa(
    scope: Construct,
    id: str,
    target: kplus.IScalable,
    cpu_utilization_target: Number = 75,
    memory_utilization_target: Number = 75,
    max_replicas: int = 3,
    min_replicas: int = 1,
) -> kplus.HorizontalPodAutoscaler:
    """Returns a HorizontalPodAutoscaler for a target.

    The utilization targets are applied to the aggregate CPU and memory usage of all containers in the target workload.

    Args:
        scope: The scope of the construct.
        target: The target to autoscale.
        cpu_utilization_target: The CPU utilization to target. Must be between 50 and 90. Defaults to 75.
        memory_utilization_target: The memory utilization to target. Must be between 50 and 90. Defaults to 75.
        max_replicas: The maximum number of replicas. Defaults to 3.
        min_replicas: The minimum number of replicas. Defaults to 1.

    Returns:
        A HorizontalPodAutoscaler.
    """
    if (
        cpu_utilization_target > 90
        or cpu_utilization_target < 50
        or memory_utilization_target > 90
        or memory_utilization_target < 50
    ):
        raise ValueError("Utilization values must be between 1 and 100")

    return kplus.HorizontalPodAutoscaler(
        scope,
        id,
        max_replicas=max_replicas,
        min_replicas=min_replicas,
        target=target,
        metrics=[
            kplus.Metric.resource_cpu(
                target=kplus.MetricTarget.average_utilization(cpu_utilization_target)
            ),
            kplus.Metric.resource_memory(
                target=kplus.MetricTarget.average_utilization(memory_utilization_target)
            ),
        ],
    )
