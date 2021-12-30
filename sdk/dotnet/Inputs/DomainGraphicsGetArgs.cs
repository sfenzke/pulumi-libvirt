// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class DomainGraphicsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// defaults to "yes"
        /// </summary>
        [Input("autoport")]
        public Input<bool>? Autoport { get; set; }

        /// <summary>
        /// IP Address where the VNC listener should be started if
        /// `listen_type` is set to `address`. Defaults to 127.0.0.1
        /// </summary>
        [Input("listenAddress")]
        public Input<string>? ListenAddress { get; set; }

        /// <summary>
        /// "listen type", defaults to "none"
        /// </summary>
        [Input("listenType")]
        public Input<string>? ListenType { get; set; }

        /// <summary>
        /// Console device type. Valid values are "pty" and "tcp".
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// Port to listen on for VNC WebSocket functionality (-1 meaning auto-allocation)
        /// </summary>
        [Input("websocket")]
        public Input<int>? Websocket { get; set; }

        public DomainGraphicsGetArgs()
        {
        }
    }
}
