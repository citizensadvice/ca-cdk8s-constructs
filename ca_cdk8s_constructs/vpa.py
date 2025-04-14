from typing import Literal
import cdk8s_plus_32 as kplus
from constructs import Construct
from ca_cdk8s_constructs.imports.io.k8s.autoscaling import (
    VerticalPodAutoscaler,
    VerticalPodAutoscalerSpec,
    VerticalPodAutoscalerSpecTargetRef,
    VerticalPodAutoscalerSpecUpdatePolicy,
    VerticalPodAutoscalerSpecUpdatePolicyUpdateMode,
    VerticalPodAutoscalerSpecResourcePolicy,
    VerticalPodAutoscalerSpecResourcePolicyContainerPolicies,
    VerticalPodAutoscalerSpecResourcePolicyContainerPoliciesMinAllowed,
)


def ca_vpa(
    scope: Construct,
    id: str,
    target: kplus.IScalable,
    min_allowed_cpu: int = 100,
    update_mode: Literal["auto", "off", "initial", "recreate"] = "auto",
) -> VerticalPodAutoscaler:
    """Returns a VerticalPodAutoscaler for a target.

    The different modes are:
    - Off: VPA will only provide the recommendations, and it will not automatically change resource requirements.
    - Initial: VPA only assigns resource requests on pod creation and never changes them later.
    - Recreate: VPA assigns resource requests on pod creation time and updates them on existing pods by evicting and recreating them.
    - Auto: It recreates the pod based on the recommendation.

    The minimum allowed CPU is the minimum CPU that the VPA will assign to the pod. This is applied to all containers in the pod.

    Args:
        scope: The scope of the construct.
        target: The target to autoscale.
        min_allowed_cpu: The minimum allowed CPU in millicores. Defaults to 100.
        update_mode: The update mode to use. Defaults to "auto".

    Returns:
        A VerticalPodAutoscaler.
    """

    if update_mode == "off":
        update_mode = VerticalPodAutoscalerSpecUpdatePolicyUpdateMode.OFF
    elif update_mode == "initial":
        update_mode = VerticalPodAutoscalerSpecUpdatePolicyUpdateMode.INITIAL
    elif update_mode == "recreate":
        update_mode = VerticalPodAutoscalerSpecUpdatePolicyUpdateMode.RECREATE
    else:
        update_mode = VerticalPodAutoscalerSpecUpdatePolicyUpdateMode.AUTO

    return VerticalPodAutoscaler(
        scope,
        id,
        spec=VerticalPodAutoscalerSpec(
            target_ref=VerticalPodAutoscalerSpecTargetRef(
                api_version=target.api_version,
                kind=target.kind,
                name=target.name,
            ),
            update_policy=VerticalPodAutoscalerSpecUpdatePolicy(update_mode=update_mode),
            resource_policy=VerticalPodAutoscalerSpecResourcePolicy(
                container_policies=[
                    VerticalPodAutoscalerSpecResourcePolicyContainerPolicies(
                        container_name=name,
                        min_allowed={
                            "cpu": VerticalPodAutoscalerSpecResourcePolicyContainerPoliciesMinAllowed.from_number(
                                min_allowed_cpu
                            )
                        },
                    )
                    for name in target.containers
                ]
            ),
        ),
    )
