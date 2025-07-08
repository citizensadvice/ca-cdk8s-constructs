from typing import Final

from cdk8s import Duration
from cdk8s_plus_32 import Ingress
from constructs import Construct

from ca_cdk8s_constructs.imports.com.coreos.monitoring import (
    Probe,
)
from ca_cdk8s_constructs.imports.com.coreos.monitoring import (
    ProbeSpec as Spec,
)
from ca_cdk8s_constructs.imports.com.coreos.monitoring import (
    ProbeSpecProber as Prober,
)
from ca_cdk8s_constructs.imports.com.coreos.monitoring import (
    ProbeSpecTargets as Targets,
)
from ca_cdk8s_constructs.imports.com.coreos.monitoring import (
    ProbeSpecTargetsIngress as IngressTarget,
)
from ca_cdk8s_constructs.imports.com.coreos.monitoring import (
    ProbeSpecTargetsIngressSelector as IngressSelector,
)
from ca_cdk8s_constructs.imports.com.coreos.monitoring import (
    ProbeSpecTargetsStaticConfig as StaticTarget,
)


def ca_blackbox_probe(
    scope: Construct,
    id: str,
    target: Ingress | str,
    interval: Duration = Duration.seconds(60),
    timeout: Duration | None = None,
) -> Probe:
    """Returns a blackbox probe for a target.

    The target can be an Ingress or a static URL.

    If the target is an Ingress, the ingress will have an additional label added
    to use as a label target for the blackbox exporter.

    Args:
        scope: The scope of the construct.
        id: The id of the probe.
        target: The target of the probe.
        interval: The interval on which the probe will be executed.
        timeout: The timeout of the probe. Defaults to cluster default.

    Returns:
        A Probe object.
    """

    LABEL_KEY: Final[str] = "app.kubernetes.io/blackbox-target"  # noqa:N806

    if isinstance(target, Ingress):
        """
        It is not guaranteed that the ingress will have an labels to select,
        so to ensure this we add a label to the ingress with the value
        being the generated name of the ingress. As the name is generated
        by cdk8s with a hashed suffix we can be sure that it is unique.
        """
        target.metadata.add_label(LABEL_KEY, f"{target.name}")
        target = Targets(
            ingress=IngressTarget(
                selector=IngressSelector(
                    match_labels={LABEL_KEY: target.metadata.get_label(LABEL_KEY)}
                )
            )
        )
    elif isinstance(target, str):
        target = Targets(static_config=StaticTarget(static=[target]))
    else:
        raise ValueError(f"Invalid target type: {type(target)}, must be Ingress or str")

    if timeout:
        scrape_timeout = f"{timeout.to_seconds(integral=True)}s"
    else:
        scrape_timeout = None

    probe = Probe(
        scope,
        id,
        spec=Spec(
            interval=f"{interval.to_seconds(integral=True)}s",
            scrape_timeout=scrape_timeout,
            module="http_2xx",
            prober=Prober(
                url="prometheus-blackbox-exporter.kube-monitoring.svc.cluster.local:9115",
                path="/probe",
            ),
            targets=target,
        ),
    )

    return probe
