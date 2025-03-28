from cdk8s_plus_31 import ContainerResources, CpuResources, Cpu, MemoryResources
from cdk8s import Size
from numbers import Number


def ca_container_resources(
    cpu_requests: Number, memory_limit: Number, memory_request: Number
):
    """Create a ContainerResources object.

    It is not recommended to set cpu_limit so this value is not exposed.

    Args:
        cpu_requests: The CPU requests in millicores (1000 = 1 CPU core).
        memory_limit: The memory limit in mebibytes (1024 = 1 GiB).
        memory_request: The memory request in mebibytes (1024 = 1 GiB).
    """

    if memory_limit <= memory_request:
        raise ValueError("Memory limit must be greater than memory request")

    return ContainerResources(
        cpu=CpuResources(
            request=Cpu.millis(amount=cpu_requests),
        ),
        memory=MemoryResources(
            limit=Size.mebibytes(memory_limit),
            request=Size.mebibytes(memory_request),
        ),
    )
