// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class DomainConsoleGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// IP address to listen on. Defaults to 127.0.0.1.
        /// </summary>
        [Input("sourceHost")]
        public Input<string>? SourceHost { get; set; }

        /// <summary>
        /// Source path
        /// </summary>
        [Input("sourcePath")]
        public Input<string>? SourcePath { get; set; }

        /// <summary>
        /// Port number or a service name. Defaults to a
        /// random port.
        /// </summary>
        [Input("sourceService")]
        public Input<string>? SourceService { get; set; }

        /// <summary>
        /// Target port
        /// </summary>
        [Input("targetPort", required: true)]
        public Input<string> TargetPort { get; set; } = null!;

        /// <summary>
        /// for the first console and defaults to `serial`.
        /// Subsequent `console` blocks must have a different type - usually `virtio`.
        /// </summary>
        [Input("targetType")]
        public Input<string>? TargetType { get; set; }

        /// <summary>
        /// the type of graphics emulation (default is "spice")
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public DomainConsoleGetArgs()
        {
        }
        public static new DomainConsoleGetArgs Empty => new DomainConsoleGetArgs();
    }
}
