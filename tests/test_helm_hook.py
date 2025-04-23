from cdk8s_plus_32 import Job
from ca_cdk8s_constructs.cdk8s_helm_chart import (
    apply_helm_hook,
    HelmHookType,
    HelmHookDeletePolicy,
)
from cdk8s import Chart


def test_apply_helm_hook_defaults(chart_fixture: Chart):
    job = Job(chart_fixture, "Job")
    apply_helm_hook(job, [HelmHookType.POST_INSTALL])
    metadata = job.metadata.to_json()
    assert metadata["annotations"]["helm.sh/hook"] == "post-install"
    assert metadata["annotations"]["helm.sh/hook-delete-policy"] == "before-hook-creation"


def test_apply_helm_hook_with_delete_policy(chart_fixture: Chart):
    job = Job(chart_fixture, "Job")
    apply_helm_hook(
        job,
        [HelmHookType.POST_INSTALL],
        hook_delete_policy=[HelmHookDeletePolicy.HOOK_SUCCEEDED],
    )
    metadata = job.metadata.to_json()
    assert metadata["annotations"]["helm.sh/hook-delete-policy"] == "hook-succeeded"


def test_apply_helm_hook_with_weight(chart_fixture: Chart):
    job = Job(chart_fixture, "Job")
    apply_helm_hook(job, [HelmHookType.POST_INSTALL], weight=10)
    metadata = job.metadata.to_json()
    assert metadata["annotations"]["helm.sh/hook-weight"] == "10"


def test_apply_helm_hook_with_multiple_hooks(chart_fixture: Chart):
    job = Job(chart_fixture, "Job")
    apply_helm_hook(job, [HelmHookType.POST_INSTALL, HelmHookType.POST_UPGRADE])
    metadata = job.metadata.to_json()
    assert metadata["annotations"]["helm.sh/hook"] == "post-install,post-upgrade"
