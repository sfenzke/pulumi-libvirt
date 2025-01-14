// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class DomainNvramGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// path to the file backing the NVRAM store for non-volatile variables. When provided,
        /// this file must be writable and specific to this domain, as it will be updated when running the
        /// domain. However, `libvirt` can  manage this automatically (and this is the recommended solution)
        /// if a mapping for the firmware to a _variables file_ exists in `/etc/libvirt/qemu.conf:nvram`.
        /// In that case, `libvirt` will copy that variables file into a file specific for this domain.
        /// </summary>
        [Input("file", required: true)]
        public Input<string> File { get; set; } = null!;

        /// <summary>
        /// path to the file used to override variables from the master NVRAM
        /// store.
        /// </summary>
        [Input("template")]
        public Input<string>? Template { get; set; }

        public DomainNvramGetArgs()
        {
        }
        public static new DomainNvramGetArgs Empty => new DomainNvramGetArgs();
    }
}
