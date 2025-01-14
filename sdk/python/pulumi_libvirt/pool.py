# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PoolArgs', 'Pool']

@pulumi.input_type
class PoolArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 allocation: Optional[pulumi.Input[int]] = None,
                 available: Optional[pulumi.Input[int]] = None,
                 capacity: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input['PoolXmlArgs']] = None):
        """
        The set of arguments for constructing a Pool resource.
        :param pulumi.Input[str] type: The type of the pool. Currently, only "dir" supported.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
        :param pulumi.Input[str] path: The directory where the pool will keep all its volumes. This is only relevant to (and required by)
               the "dir" type pools.
        """
        pulumi.set(__self__, "type", type)
        if allocation is not None:
            pulumi.set(__self__, "allocation", allocation)
        if available is not None:
            pulumi.set(__self__, "available", available)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if xml is not None:
            pulumi.set(__self__, "xml", xml)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the pool. Currently, only "dir" supported.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def allocation(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "allocation")

    @allocation.setter
    def allocation(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "allocation", value)

    @property
    @pulumi.getter
    def available(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "available")

    @available.setter
    def available(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "available", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name for the resource, required by libvirt.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The directory where the pool will keep all its volumes. This is only relevant to (and required by)
        the "dir" type pools.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def xml(self) -> Optional[pulumi.Input['PoolXmlArgs']]:
        return pulumi.get(self, "xml")

    @xml.setter
    def xml(self, value: Optional[pulumi.Input['PoolXmlArgs']]):
        pulumi.set(self, "xml", value)


@pulumi.input_type
class _PoolState:
    def __init__(__self__, *,
                 allocation: Optional[pulumi.Input[int]] = None,
                 available: Optional[pulumi.Input[int]] = None,
                 capacity: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input['PoolXmlArgs']] = None):
        """
        Input properties used for looking up and filtering Pool resources.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
        :param pulumi.Input[str] path: The directory where the pool will keep all its volumes. This is only relevant to (and required by)
               the "dir" type pools.
        :param pulumi.Input[str] type: The type of the pool. Currently, only "dir" supported.
        """
        if allocation is not None:
            pulumi.set(__self__, "allocation", allocation)
        if available is not None:
            pulumi.set(__self__, "available", available)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if xml is not None:
            pulumi.set(__self__, "xml", xml)

    @property
    @pulumi.getter
    def allocation(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "allocation")

    @allocation.setter
    def allocation(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "allocation", value)

    @property
    @pulumi.getter
    def available(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "available")

    @available.setter
    def available(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "available", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name for the resource, required by libvirt.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The directory where the pool will keep all its volumes. This is only relevant to (and required by)
        the "dir" type pools.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the pool. Currently, only "dir" supported.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def xml(self) -> Optional[pulumi.Input['PoolXmlArgs']]:
        return pulumi.get(self, "xml")

    @xml.setter
    def xml(self, value: Optional[pulumi.Input['PoolXmlArgs']]):
        pulumi.set(self, "xml", value)


class Pool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation: Optional[pulumi.Input[int]] = None,
                 available: Optional[pulumi.Input[int]] = None,
                 capacity: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input[pulumi.InputType['PoolXmlArgs']]] = None,
                 __props__=None):
        """
        Manages a storage pool in libvirt. Currently only directory-based storage pool are supported. For more information on
        storage pools in libvirt, see [the official documentation](https://libvirt.org/formatstorage.html).

        **WARNING:** This is experimental API and may change in the future.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_libvirt as libvirt

        # A pool for all cluster volumes
        cluster = libvirt.Pool("cluster",
            type="dir",
            path="/home/user/cluster_storage")
        opensuse_leap = libvirt.Volume("opensuseLeap",
            pool=cluster.name,
            source="http://download.opensuse.org/repositories/Cloud:/Images:/Leap_42.1/images/openSUSE-Leap-42.1-OpenStack.x86_64.qcow2")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
        :param pulumi.Input[str] path: The directory where the pool will keep all its volumes. This is only relevant to (and required by)
               the "dir" type pools.
        :param pulumi.Input[str] type: The type of the pool. Currently, only "dir" supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a storage pool in libvirt. Currently only directory-based storage pool are supported. For more information on
        storage pools in libvirt, see [the official documentation](https://libvirt.org/formatstorage.html).

        **WARNING:** This is experimental API and may change in the future.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_libvirt as libvirt

        # A pool for all cluster volumes
        cluster = libvirt.Pool("cluster",
            type="dir",
            path="/home/user/cluster_storage")
        opensuse_leap = libvirt.Volume("opensuseLeap",
            pool=cluster.name,
            source="http://download.opensuse.org/repositories/Cloud:/Images:/Leap_42.1/images/openSUSE-Leap-42.1-OpenStack.x86_64.qcow2")
        ```

        :param str resource_name: The name of the resource.
        :param PoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation: Optional[pulumi.Input[int]] = None,
                 available: Optional[pulumi.Input[int]] = None,
                 capacity: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input[pulumi.InputType['PoolXmlArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PoolArgs.__new__(PoolArgs)

            __props__.__dict__["allocation"] = allocation
            __props__.__dict__["available"] = available
            __props__.__dict__["capacity"] = capacity
            __props__.__dict__["name"] = name
            __props__.__dict__["path"] = path
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["xml"] = xml
        super(Pool, __self__).__init__(
            'libvirt:index/pool:Pool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocation: Optional[pulumi.Input[int]] = None,
            available: Optional[pulumi.Input[int]] = None,
            capacity: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            xml: Optional[pulumi.Input[pulumi.InputType['PoolXmlArgs']]] = None) -> 'Pool':
        """
        Get an existing Pool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
        :param pulumi.Input[str] path: The directory where the pool will keep all its volumes. This is only relevant to (and required by)
               the "dir" type pools.
        :param pulumi.Input[str] type: The type of the pool. Currently, only "dir" supported.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PoolState.__new__(_PoolState)

        __props__.__dict__["allocation"] = allocation
        __props__.__dict__["available"] = available
        __props__.__dict__["capacity"] = capacity
        __props__.__dict__["name"] = name
        __props__.__dict__["path"] = path
        __props__.__dict__["type"] = type
        __props__.__dict__["xml"] = xml
        return Pool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def allocation(self) -> pulumi.Output[int]:
        return pulumi.get(self, "allocation")

    @property
    @pulumi.getter
    def available(self) -> pulumi.Output[int]:
        return pulumi.get(self, "available")

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[int]:
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the resource, required by libvirt.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        """
        The directory where the pool will keep all its volumes. This is only relevant to (and required by)
        the "dir" type pools.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the pool. Currently, only "dir" supported.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def xml(self) -> pulumi.Output[Optional['outputs.PoolXml']]:
        return pulumi.get(self, "xml")

