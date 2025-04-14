from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *

import cdk8s as _cdk8s_d3d9af27
import constructs as _constructs_77d1e7e8


class VerticalPodAutoscaler(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iok8sautoscalingpoc.VerticalPodAutoscaler",
):
    '''
    :schema: VerticalPodAutoscaler
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["VerticalPodAutoscalerSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a "VerticalPodAutoscaler" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8824e1a883e7a1f61f1a884338de3e58e30ba4e6151aaa7017b26779c2029cfd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = VerticalPodAutoscalerProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["VerticalPodAutoscalerSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "VerticalPodAutoscaler".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: 
        '''
        props = VerticalPodAutoscalerProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "VerticalPodAutoscaler".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


class VerticalPodAutoscalerCheckpoint(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iok8sautoscalingpoc.VerticalPodAutoscalerCheckpoint",
):
    '''
    :schema: VerticalPodAutoscalerCheckpoint
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a "VerticalPodAutoscalerCheckpoint" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccdb876994794a2108545c71cad4d93dcfbae560ae03ea3f02dbc946373f7bcb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = VerticalPodAutoscalerCheckpointProps(metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "VerticalPodAutoscalerCheckpoint".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        '''
        props = VerticalPodAutoscalerCheckpointProps(metadata=metadata)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "VerticalPodAutoscalerCheckpoint".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iok8sautoscalingpoc.VerticalPodAutoscalerCheckpointProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class VerticalPodAutoscalerCheckpointProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metadata: 

        :schema: VerticalPodAutoscalerCheckpoint
        '''
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585ef17e78d32d952769a2381d8254425f58442d96127dbff12bb0a50f649c92)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata]:
        '''
        :schema: VerticalPodAutoscalerCheckpoint#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerticalPodAutoscalerCheckpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8sautoscalingpoc.VerticalPodAutoscalerProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class VerticalPodAutoscalerProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["VerticalPodAutoscalerSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: 

        :schema: VerticalPodAutoscaler
        '''
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = VerticalPodAutoscalerSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e3016446937ba71d67fbcc0908fe5c64410de051e3ce218bbf32c183841a5e8)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata]:
        '''
        :schema: VerticalPodAutoscaler#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["VerticalPodAutoscalerSpec"]:
        '''
        :schema: VerticalPodAutoscaler#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["VerticalPodAutoscalerSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerticalPodAutoscalerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8sautoscalingpoc.VerticalPodAutoscalerSpec",
    jsii_struct_bases=[],
    name_mapping={
        "selector": "selector",
        "resource_policy": "resourcePolicy",
        "update_policy": "updatePolicy",
    },
)
class VerticalPodAutoscalerSpec:
    def __init__(
        self,
        *,
        selector: typing.Any,
        resource_policy: typing.Optional[typing.Union["VerticalPodAutoscalerSpecResourcePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        update_policy: typing.Optional[typing.Union["VerticalPodAutoscalerSpecUpdatePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param selector: 
        :param resource_policy: 
        :param update_policy: 

        :schema: VerticalPodAutoscalerSpec
        '''
        if isinstance(resource_policy, dict):
            resource_policy = VerticalPodAutoscalerSpecResourcePolicy(**resource_policy)
        if isinstance(update_policy, dict):
            update_policy = VerticalPodAutoscalerSpecUpdatePolicy(**update_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__576227238228f9b9d4a29b91278e6fa1e01f77cc5523878843217167660f88d4)
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument resource_policy", value=resource_policy, expected_type=type_hints["resource_policy"])
            check_type(argname="argument update_policy", value=update_policy, expected_type=type_hints["update_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "selector": selector,
        }
        if resource_policy is not None:
            self._values["resource_policy"] = resource_policy
        if update_policy is not None:
            self._values["update_policy"] = update_policy

    @builtins.property
    def selector(self) -> typing.Any:
        '''
        :schema: VerticalPodAutoscalerSpec#selector
        '''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_policy(
        self,
    ) -> typing.Optional["VerticalPodAutoscalerSpecResourcePolicy"]:
        '''
        :schema: VerticalPodAutoscalerSpec#resourcePolicy
        '''
        result = self._values.get("resource_policy")
        return typing.cast(typing.Optional["VerticalPodAutoscalerSpecResourcePolicy"], result)

    @builtins.property
    def update_policy(self) -> typing.Optional["VerticalPodAutoscalerSpecUpdatePolicy"]:
        '''
        :schema: VerticalPodAutoscalerSpec#updatePolicy
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional["VerticalPodAutoscalerSpecUpdatePolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerticalPodAutoscalerSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8sautoscalingpoc.VerticalPodAutoscalerSpecResourcePolicy",
    jsii_struct_bases=[],
    name_mapping={"container_policies": "containerPolicies"},
)
class VerticalPodAutoscalerSpecResourcePolicy:
    def __init__(
        self,
        *,
        container_policies: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param container_policies: 

        :schema: VerticalPodAutoscalerSpecResourcePolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baafe59737656290f2638fdab13deca2bc4d9aa96d1de218888e28d37c7aa23a)
            check_type(argname="argument container_policies", value=container_policies, expected_type=type_hints["container_policies"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if container_policies is not None:
            self._values["container_policies"] = container_policies

    @builtins.property
    def container_policies(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VerticalPodAutoscalerSpecResourcePolicy#containerPolicies
        '''
        result = self._values.get("container_policies")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerticalPodAutoscalerSpecResourcePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8sautoscalingpoc.VerticalPodAutoscalerSpecUpdatePolicy",
    jsii_struct_bases=[],
    name_mapping={"update_mode": "updateMode"},
)
class VerticalPodAutoscalerSpecUpdatePolicy:
    def __init__(self, *, update_mode: typing.Optional[builtins.str] = None) -> None:
        '''
        :param update_mode: 

        :schema: VerticalPodAutoscalerSpecUpdatePolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b37e6e4254ebdf8b6fd0e4e62292b1a0fb975fd99ebf47e4bd7bb130223681ba)
            check_type(argname="argument update_mode", value=update_mode, expected_type=type_hints["update_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if update_mode is not None:
            self._values["update_mode"] = update_mode

    @builtins.property
    def update_mode(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VerticalPodAutoscalerSpecUpdatePolicy#updateMode
        '''
        result = self._values.get("update_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerticalPodAutoscalerSpecUpdatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VerticalPodAutoscaler",
    "VerticalPodAutoscalerCheckpoint",
    "VerticalPodAutoscalerCheckpointProps",
    "VerticalPodAutoscalerProps",
    "VerticalPodAutoscalerSpec",
    "VerticalPodAutoscalerSpecResourcePolicy",
    "VerticalPodAutoscalerSpecUpdatePolicy",
]

publication.publish()

def _typecheckingstub__8824e1a883e7a1f61f1a884338de3e58e30ba4e6151aaa7017b26779c2029cfd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    spec: typing.Optional[typing.Union[VerticalPodAutoscalerSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccdb876994794a2108545c71cad4d93dcfbae560ae03ea3f02dbc946373f7bcb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585ef17e78d32d952769a2381d8254425f58442d96127dbff12bb0a50f649c92(
    *,
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e3016446937ba71d67fbcc0908fe5c64410de051e3ce218bbf32c183841a5e8(
    *,
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    spec: typing.Optional[typing.Union[VerticalPodAutoscalerSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576227238228f9b9d4a29b91278e6fa1e01f77cc5523878843217167660f88d4(
    *,
    selector: typing.Any,
    resource_policy: typing.Optional[typing.Union[VerticalPodAutoscalerSpecResourcePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    update_policy: typing.Optional[typing.Union[VerticalPodAutoscalerSpecUpdatePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baafe59737656290f2638fdab13deca2bc4d9aa96d1de218888e28d37c7aa23a(
    *,
    container_policies: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b37e6e4254ebdf8b6fd0e4e62292b1a0fb975fd99ebf47e4bd7bb130223681ba(
    *,
    update_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
