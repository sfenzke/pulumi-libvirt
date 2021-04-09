// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class NetworkDnsSrvGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The domain used by the DNS server.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        [Input("port")]
        public Input<string>? Port { get; set; }

        [Input("priority")]
        public Input<string>? Priority { get; set; }

        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        [Input("service")]
        public Input<string>? Service { get; set; }

        [Input("target")]
        public Input<string>? Target { get; set; }

        [Input("weight")]
        public Input<string>? Weight { get; set; }

        public NetworkDnsSrvGetArgs()
        {
        }
    }
}
