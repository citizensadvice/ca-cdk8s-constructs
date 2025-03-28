from numbers import Number
import cdk8s_plus_31 as kplus
from constructs import Construct


def ca_hpa(
    scope: Construct,
    max_replicas: int,
    target: kplus.IScalable,
    cpu_utilization: Number = 80,
    memory_utilization: Number = 80,
    min_replicas: int = 1,
) -> kplus.HorizontalPodAutoscaler:
    """Create a HorizontalPodAutoscaler for a target.

    This applies the same scaling logic to all containers in the target.

    Args:
        scope: The scope of the construct.
        max_replicas: The maximum number of replicas.
        target: The target to autoscale.
        cpu_utilization: The CPU utilization to target. Defaults to 80.
        memory_utilization: The memory utilization to target. Defaults to 80.
        min_replicas: The minimum number of replicas. Defaults to 1.

    Returns:
        A HorizontalPodAutoscaler.
    """
    if (
        cpu_utilization > 100
        or cpu_utilization < 1
        or memory_utilization > 100
        or memory_utilization < 1
    ):
        raise ValueError("Utilization values must be between 1 and 100")

    return kplus.HorizontalPodAutoscaler(
        scope,
        "hpa",
        max_replicas=max_replicas,
        min_replicas=min_replicas,
        target=target,
        metrics=[
            kplus.Metric.container_memory(
                container=container,
                target=kplus.MetricTarget.average_utilization(memory_utilization),
            )
            for container in target.containers
        ]
        + [
            kplus.Metric.container_cpu(
                container=container,
                target=kplus.MetricTarget.average_utilization(cpu_utilization),
            )
            for container in target.containers
        ],
    )
