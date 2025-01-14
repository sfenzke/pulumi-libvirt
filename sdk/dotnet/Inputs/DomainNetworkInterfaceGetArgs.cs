// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class DomainNetworkInterfaceGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("addresses")]
        private InputList<string>? _addresses;

        /// <summary>
        /// An IP address for this domain in this network.
        /// </summary>
        public InputList<string> Addresses
        {
            get => _addresses ?? (_addresses = new InputList<string>());
            set => _addresses = value;
        }

        /// <summary>
        /// Provides a bridge from the VM directly to the LAN. This assumes
        /// there is a bridge device on the host which has one or more of the hosts
        /// physical NICs enslaved. The guest VM will have an associated _tun_ device
        /// created and enslaved to the bridge. The IP range / network configuration is
        /// whatever is used on the LAN. This provides the guest VM full incoming &amp;
        /// outgoing net access just like a physical machine.
        /// </summary>
        [Input("bridge")]
        public Input<string>? Bridge { get; set; }

        /// <summary>
        /// A hostname that will be assigned to this domain
        /// resource in this network.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// The specific MAC address to use for this interface.
        /// </summary>
        [Input("mac")]
        public Input<string>? Mac { get; set; }

        /// <summary>
        /// Packets whose destination is on the same host as where they
        /// originate from are directly delivered to the target macvtap device. Both
        /// origin and destination devices need to be in bridge mode for direct delivery.
        /// If either one of them is in vepa mode, a VEPA capable bridge is required.
        /// </summary>
        [Input("macvtap")]
        public Input<string>? Macvtap { get; set; }

        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        [Input("networkName")]
        public Input<string>? NetworkName { get; set; }

        /// <summary>
        /// This feature attaches a virtual function of a SRIOV capable
        /// NIC directly to a VM without losing the migration capability. All packets are
        /// sent to the VF/IF of the configured network device. Depending on the
        /// capabilities of the device additional prerequisites or limitations may apply;
        /// for example, on Linux this requires kernel 2.6.38 or newer.
        /// </summary>
        [Input("passthrough")]
        public Input<string>? Passthrough { get; set; }

        /// <summary>
        /// All VMs' packets are sent to the external bridge. Packets whose
        /// destination is a VM on the same host as where the packet originates from are
        /// sent back to the host by the VEPA capable bridge (today's bridges are
        /// typically not VEPA capable).
        /// </summary>
        [Input("vepa")]
        public Input<string>? Vepa { get; set; }

        /// <summary>
        /// When creating the domain resource, wait until the
        /// network interface gets a DHCP lease from libvirt, so that the computed IP
        /// addresses will be available when the domain is up and the plan applied.
        /// </summary>
        [Input("waitForLease")]
        public Input<bool>? WaitForLease { get; set; }

        public DomainNetworkInterfaceGetArgs()
        {
        }
        public static new DomainNetworkInterfaceGetArgs Empty => new DomainNetworkInterfaceGetArgs();
    }
}
