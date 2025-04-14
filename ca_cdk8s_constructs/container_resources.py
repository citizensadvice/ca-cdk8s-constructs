from cdk8s_plus_31 import ContainerResources, CpuResources, Cpu, MemoryResources
from cdk8s import Size
from numbers import Number


def ca_container_resources(cpu: Number, memory: Number):
    """Create a ContainerResources object.

    It is not recommended to set cpu limit so this value is not set by this construct.
    The memory limit will be set equal to the memory request.

    Args:
        cpu: The CPU requests in millicores (1000 = 1 CPU core).
        memory: The memory request in mebibytes (1024 = 1 GiB).
    """

    if cpu < 100:
        raise ValueError("CPU requests must be greater than or equal to 100 millicores")
    if memory < 256:
        raise ValueError(
            "Memory requests must be greater than or equal to 256 mebibytes"
        )

    return ContainerResources(
        cpu=CpuResources(
            request=Cpu.millis(amount=cpu),
        ),
        memory=MemoryResources(
            limit=Size.mebibytes(memory),
            request=Size.mebibytes(memory),
        ),
    )
