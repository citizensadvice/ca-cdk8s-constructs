import cdk8s_plus_27 as kplus
from constructs import Construct


def build(
    scope: Construct,
    max_replicas: int,
    target: kplus.Deployment | kplus.StatefulSet,
    cpu_utilization: int = 80,
    memory_utilization: int = 80,
    min_replicas: int = 1,
) -> kplus.HorizontalPodAutoscaler:
    if cpu_utilization > 99 or memory_utilization > 99:
        raise ValueError("Utilization must be less than 100")

    return kplus.HorizontalPodAutoscaler(
        scope,
        "hpa",
        max_replicas=max_replicas,
        min_replicas=min_replicas,
        target=target,
        metrics=[
            kplus.Metric.container_memory(
                container=target.containers[0],
                target=kplus.MetricTarget.average_utilization(memory_utilization),
            ),
            kplus.Metric.container_cpu(
                container=target.containers[0],
                target=kplus.MetricTarget.average_utilization(cpu_utilization),
            ),
        ],
    )
