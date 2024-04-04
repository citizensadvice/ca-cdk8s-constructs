import cdk8s_plus_27 as kplus
import cdk8s


def generate(cpu_requests: int, memory_limit: int, memory_request: int):
    return kplus.ContainerResources(
        cpu=kplus.CpuResources(
            request=kplus.Cpu.millis(amount=cpu_requests),
        ),
        memory=kplus.MemoryResources(
            limit=cdk8s.Size.mebibytes(memory_limit),
            request=cdk8s.Size.mebibytes(memory_request),
        ),
    )
