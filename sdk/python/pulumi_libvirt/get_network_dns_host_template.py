# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetNetworkDnsHostTemplateResult',
    'AwaitableGetNetworkDnsHostTemplateResult',
    'get_network_dns_host_template',
    'get_network_dns_host_template_output',
]

@pulumi.output_type
class GetNetworkDnsHostTemplateResult:
    """
    A collection of values returned by getNetworkDnsHostTemplate.
    """
    def __init__(__self__, hostname=None, id=None, ip=None, rendered=None):
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if rendered and not isinstance(rendered, dict):
            raise TypeError("Expected argument 'rendered' to be a dict")
        pulumi.set(__self__, "rendered", rendered)

    @property
    @pulumi.getter
    def hostname(self) -> str:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> str:
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def rendered(self) -> Mapping[str, str]:
        return pulumi.get(self, "rendered")


class AwaitableGetNetworkDnsHostTemplateResult(GetNetworkDnsHostTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkDnsHostTemplateResult(
            hostname=self.hostname,
            id=self.id,
            ip=self.ip,
            rendered=self.rendered)


def get_network_dns_host_template(hostname: Optional[str] = None,
                                  ip: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkDnsHostTemplateResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['hostname'] = hostname
    __args__['ip'] = ip
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('libvirt:index/getNetworkDnsHostTemplate:getNetworkDnsHostTemplate', __args__, opts=opts, typ=GetNetworkDnsHostTemplateResult).value

    return AwaitableGetNetworkDnsHostTemplateResult(
        hostname=__ret__.hostname,
        id=__ret__.id,
        ip=__ret__.ip,
        rendered=__ret__.rendered)


@_utilities.lift_output_func(get_network_dns_host_template)
def get_network_dns_host_template_output(hostname: Optional[pulumi.Input[str]] = None,
                                         ip: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkDnsHostTemplateResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
