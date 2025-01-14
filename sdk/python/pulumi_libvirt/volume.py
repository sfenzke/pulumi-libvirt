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

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 base_volume_id: Optional[pulumi.Input[str]] = None,
                 base_volume_name: Optional[pulumi.Input[str]] = None,
                 base_volume_pool: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input['VolumeXmlArgs']] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] base_volume_id: The backing volume (CoW) to use for this volume.
        :param pulumi.Input[str] base_volume_name: The name of the backing volume (CoW) to use
               for this volume. Note well: when `base_volume_pool` is not specified the
               volume is going to be searched inside of `pool`.
        :param pulumi.Input[str] base_volume_pool: The name of the storage pool containing the
               volume defined by `base_volume_name`.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] pool: The storage pool where the resource will be created.
               If not given, the `default` storage pool will be used.
        """
        if base_volume_id is not None:
            pulumi.set(__self__, "base_volume_id", base_volume_id)
        if base_volume_name is not None:
            pulumi.set(__self__, "base_volume_name", base_volume_name)
        if base_volume_pool is not None:
            pulumi.set(__self__, "base_volume_pool", base_volume_pool)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pool is not None:
            pulumi.set(__self__, "pool", pool)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if xml is not None:
            pulumi.set(__self__, "xml", xml)

    @property
    @pulumi.getter(name="baseVolumeId")
    def base_volume_id(self) -> Optional[pulumi.Input[str]]:
        """
        The backing volume (CoW) to use for this volume.
        """
        return pulumi.get(self, "base_volume_id")

    @base_volume_id.setter
    def base_volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_volume_id", value)

    @property
    @pulumi.getter(name="baseVolumeName")
    def base_volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backing volume (CoW) to use
        for this volume. Note well: when `base_volume_pool` is not specified the
        volume is going to be searched inside of `pool`.
        """
        return pulumi.get(self, "base_volume_name")

    @base_volume_name.setter
    def base_volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_volume_name", value)

    @property
    @pulumi.getter(name="baseVolumePool")
    def base_volume_pool(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage pool containing the
        volume defined by `base_volume_name`.
        """
        return pulumi.get(self, "base_volume_pool")

    @base_volume_pool.setter
    def base_volume_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_volume_pool", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name for the resource, required by libvirt.
        Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[str]]:
        """
        The storage pool where the resource will be created.
        If not given, the `default` storage pool will be used.
        """
        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def xml(self) -> Optional[pulumi.Input['VolumeXmlArgs']]:
        return pulumi.get(self, "xml")

    @xml.setter
    def xml(self, value: Optional[pulumi.Input['VolumeXmlArgs']]):
        pulumi.set(self, "xml", value)


@pulumi.input_type
class _VolumeState:
    def __init__(__self__, *,
                 base_volume_id: Optional[pulumi.Input[str]] = None,
                 base_volume_name: Optional[pulumi.Input[str]] = None,
                 base_volume_pool: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input['VolumeXmlArgs']] = None):
        """
        Input properties used for looking up and filtering Volume resources.
        :param pulumi.Input[str] base_volume_id: The backing volume (CoW) to use for this volume.
        :param pulumi.Input[str] base_volume_name: The name of the backing volume (CoW) to use
               for this volume. Note well: when `base_volume_pool` is not specified the
               volume is going to be searched inside of `pool`.
        :param pulumi.Input[str] base_volume_pool: The name of the storage pool containing the
               volume defined by `base_volume_name`.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] pool: The storage pool where the resource will be created.
               If not given, the `default` storage pool will be used.
        """
        if base_volume_id is not None:
            pulumi.set(__self__, "base_volume_id", base_volume_id)
        if base_volume_name is not None:
            pulumi.set(__self__, "base_volume_name", base_volume_name)
        if base_volume_pool is not None:
            pulumi.set(__self__, "base_volume_pool", base_volume_pool)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pool is not None:
            pulumi.set(__self__, "pool", pool)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if xml is not None:
            pulumi.set(__self__, "xml", xml)

    @property
    @pulumi.getter(name="baseVolumeId")
    def base_volume_id(self) -> Optional[pulumi.Input[str]]:
        """
        The backing volume (CoW) to use for this volume.
        """
        return pulumi.get(self, "base_volume_id")

    @base_volume_id.setter
    def base_volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_volume_id", value)

    @property
    @pulumi.getter(name="baseVolumeName")
    def base_volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backing volume (CoW) to use
        for this volume. Note well: when `base_volume_pool` is not specified the
        volume is going to be searched inside of `pool`.
        """
        return pulumi.get(self, "base_volume_name")

    @base_volume_name.setter
    def base_volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_volume_name", value)

    @property
    @pulumi.getter(name="baseVolumePool")
    def base_volume_pool(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage pool containing the
        volume defined by `base_volume_name`.
        """
        return pulumi.get(self, "base_volume_pool")

    @base_volume_pool.setter
    def base_volume_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_volume_pool", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name for the resource, required by libvirt.
        Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[str]]:
        """
        The storage pool where the resource will be created.
        If not given, the `default` storage pool will be used.
        """
        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def xml(self) -> Optional[pulumi.Input['VolumeXmlArgs']]:
        return pulumi.get(self, "xml")

    @xml.setter
    def xml(self, value: Optional[pulumi.Input['VolumeXmlArgs']]):
        pulumi.set(self, "xml", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_volume_id: Optional[pulumi.Input[str]] = None,
                 base_volume_name: Optional[pulumi.Input[str]] = None,
                 base_volume_pool: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input[pulumi.InputType['VolumeXmlArgs']]] = None,
                 __props__=None):
        """
        Manages a storage volume in libvirt. For more information see
        [the official documentation](https://libvirt.org/formatstorage.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_libvirt as libvirt

        # Base OS image to use to create a cluster of different
        # nodes
        opensuse_leap = libvirt.Volume("opensuseLeap", source="http://download.opensuse.org/repositories/Cloud:/Images:/Leap_42.1/images/openSUSE-Leap-42.1-OpenStack.x86_64.qcow2")
        # volume to attach to the "master" domain as main disk
        master = libvirt.Volume("master", base_volume_id=opensuse_leap.id)
        # volumes to attach to the "workers" domains as main disk
        worker = []
        for range in [{"value": i} for i in range(0, var.workers_count)]:
            worker.append(libvirt.Volume(f"worker-{range['value']}", base_volume_id=opensuse_leap.id))
        ```

        > **Tip:** when provisioning multiple domains using the same base image, create
        a `Volume` for the base image and then define the domain specific ones
        as based on it. This way the image will not be modified and no extra disk space
        is going to be used for the base image.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_volume_id: The backing volume (CoW) to use for this volume.
        :param pulumi.Input[str] base_volume_name: The name of the backing volume (CoW) to use
               for this volume. Note well: when `base_volume_pool` is not specified the
               volume is going to be searched inside of `pool`.
        :param pulumi.Input[str] base_volume_pool: The name of the storage pool containing the
               volume defined by `base_volume_name`.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] pool: The storage pool where the resource will be created.
               If not given, the `default` storage pool will be used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VolumeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a storage volume in libvirt. For more information see
        [the official documentation](https://libvirt.org/formatstorage.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_libvirt as libvirt

        # Base OS image to use to create a cluster of different
        # nodes
        opensuse_leap = libvirt.Volume("opensuseLeap", source="http://download.opensuse.org/repositories/Cloud:/Images:/Leap_42.1/images/openSUSE-Leap-42.1-OpenStack.x86_64.qcow2")
        # volume to attach to the "master" domain as main disk
        master = libvirt.Volume("master", base_volume_id=opensuse_leap.id)
        # volumes to attach to the "workers" domains as main disk
        worker = []
        for range in [{"value": i} for i in range(0, var.workers_count)]:
            worker.append(libvirt.Volume(f"worker-{range['value']}", base_volume_id=opensuse_leap.id))
        ```

        > **Tip:** when provisioning multiple domains using the same base image, create
        a `Volume` for the base image and then define the domain specific ones
        as based on it. This way the image will not be modified and no extra disk space
        is going to be used for the base image.

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_volume_id: Optional[pulumi.Input[str]] = None,
                 base_volume_name: Optional[pulumi.Input[str]] = None,
                 base_volume_pool: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input[pulumi.InputType['VolumeXmlArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            __props__.__dict__["base_volume_id"] = base_volume_id
            __props__.__dict__["base_volume_name"] = base_volume_name
            __props__.__dict__["base_volume_pool"] = base_volume_pool
            __props__.__dict__["format"] = format
            __props__.__dict__["name"] = name
            __props__.__dict__["pool"] = pool
            __props__.__dict__["size"] = size
            __props__.__dict__["source"] = source
            __props__.__dict__["xml"] = xml
        super(Volume, __self__).__init__(
            'libvirt:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_volume_id: Optional[pulumi.Input[str]] = None,
            base_volume_name: Optional[pulumi.Input[str]] = None,
            base_volume_pool: Optional[pulumi.Input[str]] = None,
            format: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pool: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            source: Optional[pulumi.Input[str]] = None,
            xml: Optional[pulumi.Input[pulumi.InputType['VolumeXmlArgs']]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_volume_id: The backing volume (CoW) to use for this volume.
        :param pulumi.Input[str] base_volume_name: The name of the backing volume (CoW) to use
               for this volume. Note well: when `base_volume_pool` is not specified the
               volume is going to be searched inside of `pool`.
        :param pulumi.Input[str] base_volume_pool: The name of the storage pool containing the
               volume defined by `base_volume_name`.
        :param pulumi.Input[str] name: A unique name for the resource, required by libvirt.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] pool: The storage pool where the resource will be created.
               If not given, the `default` storage pool will be used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeState.__new__(_VolumeState)

        __props__.__dict__["base_volume_id"] = base_volume_id
        __props__.__dict__["base_volume_name"] = base_volume_name
        __props__.__dict__["base_volume_pool"] = base_volume_pool
        __props__.__dict__["format"] = format
        __props__.__dict__["name"] = name
        __props__.__dict__["pool"] = pool
        __props__.__dict__["size"] = size
        __props__.__dict__["source"] = source
        __props__.__dict__["xml"] = xml
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseVolumeId")
    def base_volume_id(self) -> pulumi.Output[Optional[str]]:
        """
        The backing volume (CoW) to use for this volume.
        """
        return pulumi.get(self, "base_volume_id")

    @property
    @pulumi.getter(name="baseVolumeName")
    def base_volume_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the backing volume (CoW) to use
        for this volume. Note well: when `base_volume_pool` is not specified the
        volume is going to be searched inside of `pool`.
        """
        return pulumi.get(self, "base_volume_name")

    @property
    @pulumi.getter(name="baseVolumePool")
    def base_volume_pool(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the storage pool containing the
        volume defined by `base_volume_name`.
        """
        return pulumi.get(self, "base_volume_pool")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[str]:
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the resource, required by libvirt.
        Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Output[Optional[str]]:
        """
        The storage pool where the resource will be created.
        If not given, the `default` storage pool will be used.
        """
        return pulumi.get(self, "pool")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def xml(self) -> pulumi.Output[Optional['outputs.VolumeXml']]:
        return pulumi.get(self, "xml")

