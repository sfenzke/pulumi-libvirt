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
    public sealed class NetworkDnsmasqOptionsOption
    {
        public readonly string? OptionName;
        public readonly string? OptionValue;

        [OutputConstructor]
        private NetworkDnsmasqOptionsOption(
            string? optionName,

            string? optionValue)
        {
            OptionName = optionName;
            OptionValue = optionValue;
        }
    }
}
