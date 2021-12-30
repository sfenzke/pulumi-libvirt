// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface DomainBootDevice {
    devs?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface DomainConsole {
    /**
     * IP address to listen on. Defaults to 127.0.0.1.
     */
    sourceHost?: pulumi.Input<string>;
    /**
     * Source path
     */
    sourcePath?: pulumi.Input<string>;
    /**
     * Port number or a service name. Defaults to a
     * random port.
     */
    sourceService?: pulumi.Input<string>;
    /**
     * Target port
     */
    targetPort: pulumi.Input<string>;
    /**
     * for the first console and defaults to `serial`.
     * Subsequent `console` blocks must have a different type - usually `virtio`.
     */
    targetType?: pulumi.Input<string>;
    /**
     * Console device type. Valid values are "pty" and "tcp".
     */
    type: pulumi.Input<string>;
}

export interface DomainCpu {
    mode: pulumi.Input<string>;
}

export interface DomainDisk {
    /**
     * The path to the host device to use as the block device for this disk.
     */
    blockDevice?: pulumi.Input<string>;
    /**
     * The filename to use as the block device for this disk (read-only)
     */
    file?: pulumi.Input<string>;
    /**
     * Use a scsi controller for this disk.  The controller
     * model is set to `virtio-scsi`
     */
    scsi?: pulumi.Input<boolean>;
    /**
     * The http url to use as the block device for this disk (read-only)
     */
    url?: pulumi.Input<string>;
    /**
     * The volume id to use for this disk.
     */
    volumeId?: pulumi.Input<string>;
    /**
     * Specify a WWN to use for the disk if the disk is using
     * a scsi controller, if not specified then a random wwn is generated for the disk
     */
    wwn?: pulumi.Input<string>;
}

export interface DomainFilesystem {
    accessmode?: pulumi.Input<string>;
    readonly?: pulumi.Input<boolean>;
    source: pulumi.Input<string>;
    target: pulumi.Input<string>;
}

export interface DomainGraphics {
    /**
     * defaults to "yes"
     */
    autoport?: pulumi.Input<boolean>;
    /**
     * IP Address where the VNC listener should be started if
     * `listenType` is set to `address`. Defaults to 127.0.0.1
     */
    listenAddress?: pulumi.Input<string>;
    /**
     * "listen type", defaults to "none"
     */
    listenType?: pulumi.Input<string>;
    /**
     * Console device type. Valid values are "pty" and "tcp".
     */
    type?: pulumi.Input<string>;
    /**
     * Port to listen on for VNC WebSocket functionality (-1 meaning auto-allocation)
     */
    websocket?: pulumi.Input<number>;
}

export interface DomainNetworkInterface {
    /**
     * An IP address for this domain in this network.
     */
    addresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Provides a bridge from the VM directly to the LAN. This assumes
     * there is a bridge device on the host which has one or more of the hosts
     * physical NICs enslaved. The guest VM will have an associated _tun_ device
     * created and enslaved to the bridge. The IP range / network configuration is
     * whatever is used on the LAN. This provides the guest VM full incoming &
     * outgoing net access just like a physical machine.
     */
    bridge?: pulumi.Input<string>;
    /**
     * A hostname that will be assigned to this domain
     * resource in this network.
     */
    hostname?: pulumi.Input<string>;
    /**
     * The specific MAC address to use for this interface.
     */
    mac?: pulumi.Input<string>;
    /**
     * Packets whose destination is on the same host as where they
     * originate from are directly delivered to the target macvtap device. Both
     * origin and destination devices need to be in bridge mode for direct delivery.
     * If either one of them is in vepa mode, a VEPA capable bridge is required.
     */
    macvtap?: pulumi.Input<string>;
    networkId?: pulumi.Input<string>;
    networkName?: pulumi.Input<string>;
    /**
     * This feature attaches a virtual function of a SRIOV capable
     * NIC directly to a VM without losing the migration capability. All packets are
     * sent to the VF/IF of the configured network device. Depending on the
     * capabilities of the device additional prerequisites or limitations may apply;
     * for example, on Linux this requires kernel 2.6.38 or newer.
     */
    passthrough?: pulumi.Input<string>;
    /**
     * All VMs' packets are sent to the external bridge. Packets whose
     * destination is a VM on the same host as where the packet originates from are
     * sent back to the host by the VEPA capable bridge (today's bridges are
     * typically not VEPA capable).
     */
    vepa?: pulumi.Input<string>;
    /**
     * When creating the domain resource, wait until the
     * network interface gets a DHCP lease from libvirt, so that the computed IP
     * addresses will be available when the domain is up and the plan applied.
     */
    waitForLease?: pulumi.Input<boolean>;
}

export interface DomainNvram {
    /**
     * The filename to use as the block device for this disk (read-only)
     */
    file: pulumi.Input<string>;
    /**
     * path to the file used to override variables from the master NVRAM
     * store.
     */
    template?: pulumi.Input<string>;
}

export interface DomainTpm {
    /**
     * Path to TPM device on the host, ex: `/dev/tpm0`
     */
    backendDevicePath?: pulumi.Input<string>;
    /**
     * [Secret object](https://libvirt.org/formatsecret.html) for encrypting the TPM state
     */
    backendEncryptionSecret?: pulumi.Input<string>;
    /**
     * Keep the TPM state when a transient domain is powered off or undefined
     */
    backendPersistentState?: pulumi.Input<boolean>;
    /**
     * TPM backend, either `passthrough` or `emulator` (default: `emulator`)
     */
    backendType?: pulumi.Input<string>;
    /**
     * TPM version
     */
    backendVersion?: pulumi.Input<string>;
    /**
     * TPM model provided to the guest
     */
    model?: pulumi.Input<string>;
}

export interface DomainVideo {
    /**
     * Console device type. Valid values are "pty" and "tcp".
     */
    type?: pulumi.Input<string>;
}

export interface DomainXml {
    xslt?: pulumi.Input<string>;
}

export interface NetworkDhcp {
    /**
     * when false, disable the DHCP server
     */
    enabled?: pulumi.Input<boolean>;
}

export interface NetworkDns {
    /**
     * when false, disable the DHCP server
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * Either `address`, `domain`, or both must be set
     */
    forwarders?: pulumi.Input<pulumi.Input<inputs.NetworkDnsForwarder>[]>;
    /**
     * a DNS host entry block. You can have one or more of these
     * blocks in your DNS definition. You must specify both `ip` and `hostname`.
     */
    hosts?: pulumi.Input<pulumi.Input<inputs.NetworkDnsHost>[]>;
    /**
     * true/false: true means 'do not forward unresolved requests for this domain to the part DNS server
     */
    localOnly?: pulumi.Input<boolean>;
    /**
     * a DNS SRV entry block. You can have one or more of these blocks
     * in your DNS definition. You must specify `service` and `protocol`.
     */
    srvs?: pulumi.Input<pulumi.Input<inputs.NetworkDnsSrv>[]>;
}

export interface NetworkDnsForwarder {
    address?: pulumi.Input<string>;
    /**
     * The domain used by the DNS server.
     */
    domain?: pulumi.Input<string>;
}

export interface NetworkDnsHost {
    hostname?: pulumi.Input<string>;
    ip?: pulumi.Input<string>;
}

export interface NetworkDnsSrv {
    /**
     * The domain used by the DNS server.
     */
    domain?: pulumi.Input<string>;
    port?: pulumi.Input<string>;
    priority?: pulumi.Input<string>;
    protocol?: pulumi.Input<string>;
    service?: pulumi.Input<string>;
    target?: pulumi.Input<string>;
    weight?: pulumi.Input<string>;
}

export interface NetworkDnsmasqOptions {
    /**
     * a Dnsmasq option entry block. You can have one or more of these
     * blocks in your definition. You must specify both `optionName` and `optionValue`.
     */
    options?: pulumi.Input<pulumi.Input<inputs.NetworkDnsmasqOptionsOption>[]>;
}

export interface NetworkDnsmasqOptionsOption {
    optionName?: pulumi.Input<string>;
    optionValue?: pulumi.Input<string>;
}

export interface NetworkRoute {
    cidr: pulumi.Input<string>;
    gateway: pulumi.Input<string>;
}

export interface NetworkXml {
    xslt?: pulumi.Input<string>;
}

export interface PoolXml {
    xslt?: pulumi.Input<string>;
}

export interface VolumeXml {
    xslt?: pulumi.Input<string>;
}

