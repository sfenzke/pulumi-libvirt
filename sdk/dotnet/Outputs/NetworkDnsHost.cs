// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Outputs
{

    [OutputType]
    public sealed class NetworkDnsHost
    {
        public readonly string? Hostname;
        public readonly string? Ip;

        [OutputConstructor]
        private NetworkDnsHost(
            string? hostname,

            string? ip)
        {
            Hostname = hostname;
            Ip = ip;
        }
    }
}
