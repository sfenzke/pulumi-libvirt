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
    public sealed class DomainVideo
    {
        /// <summary>
        /// the type of graphics emulation (default is "spice")
        /// </summary>
        public readonly string? Type;

        [OutputConstructor]
        private DomainVideo(string? type)
        {
            Type = type;
        }
    }
}
