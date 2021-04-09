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
    public sealed class DomainNvram
    {
        /// <summary>
        /// The filename to use as the block device for this disk (read-only)
        /// </summary>
        public readonly string File;
        /// <summary>
        /// path to the file used to override variables from the master NVRAM
        /// store.
        /// </summary>
        public readonly string? Template;

        [OutputConstructor]
        private DomainNvram(
            string file,

            string? template)
        {
            File = file;
            Template = template;
        }
    }
}
