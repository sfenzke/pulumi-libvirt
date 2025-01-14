// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package libvirt

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a VM network resource within libvirt. For more information see
// [the official documentation](https://libvirt.org/formatnetwork.html).
type Network struct {
	pulumi.CustomResourceState

	// A list of (0 or 1) IPv4 and (0 or 1) IPv6 subnets in
	// CIDR notation.  This defines the subnets associated to that network.
	// This argument is also used to define the address on the real host.
	// If `dhcp {  enabled = true }` addresses is also used to define the address range served by
	// the DHCP server.
	// No DHCP server will be started if `addresses` is omitted.
	Addresses pulumi.StringArrayOutput `pulumi:"addresses"`
	// Set to `true` to start the network on host boot up.
	// If not specified `false` is assumed.
	Autostart pulumi.BoolOutput `pulumi:"autostart"`
	// The bridge device defines the name of a bridge
	// device which will be used to construct the virtual network (when not provided,
	// it will be automatically obtained by libvirt in `none`, `nat`, `route` and `open` modes).
	Bridge pulumi.StringOutput `pulumi:"bridge"`
	// DHCP configuration.
	// You need to use it in conjuction with the adresses variable.
	Dhcp NetworkDhcpOutput `pulumi:"dhcp"`
	// configuration of DNS specific settings for the network
	Dns NetworkDnsOutput `pulumi:"dns"`
	// configuration of Dnsmasq options for the network
	// You need to provide a list of option name and value pairs.
	DnsmasqOptions NetworkDnsmasqOptionsPtrOutput `pulumi:"dnsmasqOptions"`
	// The domain used by the DNS server.
	Domain pulumi.StringPtrOutput `pulumi:"domain"`
	// One of:
	Mode pulumi.StringPtrOutput `pulumi:"mode"`
	// The MTU to set for the underlying network interfaces. When
	// not supplied, libvirt will use the default for the interface, usually 1500.
	// Libvirt version 5.1 and greater will advertise this value to nodes via DHCP.
	Mtu pulumi.IntPtrOutput `pulumi:"mtu"`
	// A unique name for the resource, required by libvirt.
	// Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// a list of static routes. A `cidr` and a `gateway` must
	// be provided. The `gateway` must be reachable via the bridge interface.
	Routes NetworkRouteArrayOutput `pulumi:"routes"`
	Xml    NetworkXmlPtrOutput     `pulumi:"xml"`
}

// NewNetwork registers a new resource with the given unique name, arguments, and options.
func NewNetwork(ctx *pulumi.Context,
	name string, args *NetworkArgs, opts ...pulumi.ResourceOption) (*Network, error) {
	if args == nil {
		args = &NetworkArgs{}
	}

	var resource Network
	err := ctx.RegisterResource("libvirt:index/network:Network", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetwork gets an existing Network resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkState, opts ...pulumi.ResourceOption) (*Network, error) {
	var resource Network
	err := ctx.ReadResource("libvirt:index/network:Network", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Network resources.
type networkState struct {
	// A list of (0 or 1) IPv4 and (0 or 1) IPv6 subnets in
	// CIDR notation.  This defines the subnets associated to that network.
	// This argument is also used to define the address on the real host.
	// If `dhcp {  enabled = true }` addresses is also used to define the address range served by
	// the DHCP server.
	// No DHCP server will be started if `addresses` is omitted.
	Addresses []string `pulumi:"addresses"`
	// Set to `true` to start the network on host boot up.
	// If not specified `false` is assumed.
	Autostart *bool `pulumi:"autostart"`
	// The bridge device defines the name of a bridge
	// device which will be used to construct the virtual network (when not provided,
	// it will be automatically obtained by libvirt in `none`, `nat`, `route` and `open` modes).
	Bridge *string `pulumi:"bridge"`
	// DHCP configuration.
	// You need to use it in conjuction with the adresses variable.
	Dhcp *NetworkDhcp `pulumi:"dhcp"`
	// configuration of DNS specific settings for the network
	Dns *NetworkDns `pulumi:"dns"`
	// configuration of Dnsmasq options for the network
	// You need to provide a list of option name and value pairs.
	DnsmasqOptions *NetworkDnsmasqOptions `pulumi:"dnsmasqOptions"`
	// The domain used by the DNS server.
	Domain *string `pulumi:"domain"`
	// One of:
	Mode *string `pulumi:"mode"`
	// The MTU to set for the underlying network interfaces. When
	// not supplied, libvirt will use the default for the interface, usually 1500.
	// Libvirt version 5.1 and greater will advertise this value to nodes via DHCP.
	Mtu *int `pulumi:"mtu"`
	// A unique name for the resource, required by libvirt.
	// Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// a list of static routes. A `cidr` and a `gateway` must
	// be provided. The `gateway` must be reachable via the bridge interface.
	Routes []NetworkRoute `pulumi:"routes"`
	Xml    *NetworkXml    `pulumi:"xml"`
}

type NetworkState struct {
	// A list of (0 or 1) IPv4 and (0 or 1) IPv6 subnets in
	// CIDR notation.  This defines the subnets associated to that network.
	// This argument is also used to define the address on the real host.
	// If `dhcp {  enabled = true }` addresses is also used to define the address range served by
	// the DHCP server.
	// No DHCP server will be started if `addresses` is omitted.
	Addresses pulumi.StringArrayInput
	// Set to `true` to start the network on host boot up.
	// If not specified `false` is assumed.
	Autostart pulumi.BoolPtrInput
	// The bridge device defines the name of a bridge
	// device which will be used to construct the virtual network (when not provided,
	// it will be automatically obtained by libvirt in `none`, `nat`, `route` and `open` modes).
	Bridge pulumi.StringPtrInput
	// DHCP configuration.
	// You need to use it in conjuction with the adresses variable.
	Dhcp NetworkDhcpPtrInput
	// configuration of DNS specific settings for the network
	Dns NetworkDnsPtrInput
	// configuration of Dnsmasq options for the network
	// You need to provide a list of option name and value pairs.
	DnsmasqOptions NetworkDnsmasqOptionsPtrInput
	// The domain used by the DNS server.
	Domain pulumi.StringPtrInput
	// One of:
	Mode pulumi.StringPtrInput
	// The MTU to set for the underlying network interfaces. When
	// not supplied, libvirt will use the default for the interface, usually 1500.
	// Libvirt version 5.1 and greater will advertise this value to nodes via DHCP.
	Mtu pulumi.IntPtrInput
	// A unique name for the resource, required by libvirt.
	// Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// a list of static routes. A `cidr` and a `gateway` must
	// be provided. The `gateway` must be reachable via the bridge interface.
	Routes NetworkRouteArrayInput
	Xml    NetworkXmlPtrInput
}

func (NetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkState)(nil)).Elem()
}

type networkArgs struct {
	// A list of (0 or 1) IPv4 and (0 or 1) IPv6 subnets in
	// CIDR notation.  This defines the subnets associated to that network.
	// This argument is also used to define the address on the real host.
	// If `dhcp {  enabled = true }` addresses is also used to define the address range served by
	// the DHCP server.
	// No DHCP server will be started if `addresses` is omitted.
	Addresses []string `pulumi:"addresses"`
	// Set to `true` to start the network on host boot up.
	// If not specified `false` is assumed.
	Autostart *bool `pulumi:"autostart"`
	// The bridge device defines the name of a bridge
	// device which will be used to construct the virtual network (when not provided,
	// it will be automatically obtained by libvirt in `none`, `nat`, `route` and `open` modes).
	Bridge *string `pulumi:"bridge"`
	// DHCP configuration.
	// You need to use it in conjuction with the adresses variable.
	Dhcp *NetworkDhcp `pulumi:"dhcp"`
	// configuration of DNS specific settings for the network
	Dns *NetworkDns `pulumi:"dns"`
	// configuration of Dnsmasq options for the network
	// You need to provide a list of option name and value pairs.
	DnsmasqOptions *NetworkDnsmasqOptions `pulumi:"dnsmasqOptions"`
	// The domain used by the DNS server.
	Domain *string `pulumi:"domain"`
	// One of:
	Mode *string `pulumi:"mode"`
	// The MTU to set for the underlying network interfaces. When
	// not supplied, libvirt will use the default for the interface, usually 1500.
	// Libvirt version 5.1 and greater will advertise this value to nodes via DHCP.
	Mtu *int `pulumi:"mtu"`
	// A unique name for the resource, required by libvirt.
	// Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// a list of static routes. A `cidr` and a `gateway` must
	// be provided. The `gateway` must be reachable via the bridge interface.
	Routes []NetworkRoute `pulumi:"routes"`
	Xml    *NetworkXml    `pulumi:"xml"`
}

// The set of arguments for constructing a Network resource.
type NetworkArgs struct {
	// A list of (0 or 1) IPv4 and (0 or 1) IPv6 subnets in
	// CIDR notation.  This defines the subnets associated to that network.
	// This argument is also used to define the address on the real host.
	// If `dhcp {  enabled = true }` addresses is also used to define the address range served by
	// the DHCP server.
	// No DHCP server will be started if `addresses` is omitted.
	Addresses pulumi.StringArrayInput
	// Set to `true` to start the network on host boot up.
	// If not specified `false` is assumed.
	Autostart pulumi.BoolPtrInput
	// The bridge device defines the name of a bridge
	// device which will be used to construct the virtual network (when not provided,
	// it will be automatically obtained by libvirt in `none`, `nat`, `route` and `open` modes).
	Bridge pulumi.StringPtrInput
	// DHCP configuration.
	// You need to use it in conjuction with the adresses variable.
	Dhcp NetworkDhcpPtrInput
	// configuration of DNS specific settings for the network
	Dns NetworkDnsPtrInput
	// configuration of Dnsmasq options for the network
	// You need to provide a list of option name and value pairs.
	DnsmasqOptions NetworkDnsmasqOptionsPtrInput
	// The domain used by the DNS server.
	Domain pulumi.StringPtrInput
	// One of:
	Mode pulumi.StringPtrInput
	// The MTU to set for the underlying network interfaces. When
	// not supplied, libvirt will use the default for the interface, usually 1500.
	// Libvirt version 5.1 and greater will advertise this value to nodes via DHCP.
	Mtu pulumi.IntPtrInput
	// A unique name for the resource, required by libvirt.
	// Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// a list of static routes. A `cidr` and a `gateway` must
	// be provided. The `gateway` must be reachable via the bridge interface.
	Routes NetworkRouteArrayInput
	Xml    NetworkXmlPtrInput
}

func (NetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkArgs)(nil)).Elem()
}

type NetworkInput interface {
	pulumi.Input

	ToNetworkOutput() NetworkOutput
	ToNetworkOutputWithContext(ctx context.Context) NetworkOutput
}

func (*Network) ElementType() reflect.Type {
	return reflect.TypeOf((**Network)(nil)).Elem()
}

func (i *Network) ToNetworkOutput() NetworkOutput {
	return i.ToNetworkOutputWithContext(context.Background())
}

func (i *Network) ToNetworkOutputWithContext(ctx context.Context) NetworkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkOutput)
}

// NetworkArrayInput is an input type that accepts NetworkArray and NetworkArrayOutput values.
// You can construct a concrete instance of `NetworkArrayInput` via:
//
//	NetworkArray{ NetworkArgs{...} }
type NetworkArrayInput interface {
	pulumi.Input

	ToNetworkArrayOutput() NetworkArrayOutput
	ToNetworkArrayOutputWithContext(context.Context) NetworkArrayOutput
}

type NetworkArray []NetworkInput

func (NetworkArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Network)(nil)).Elem()
}

func (i NetworkArray) ToNetworkArrayOutput() NetworkArrayOutput {
	return i.ToNetworkArrayOutputWithContext(context.Background())
}

func (i NetworkArray) ToNetworkArrayOutputWithContext(ctx context.Context) NetworkArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkArrayOutput)
}

// NetworkMapInput is an input type that accepts NetworkMap and NetworkMapOutput values.
// You can construct a concrete instance of `NetworkMapInput` via:
//
//	NetworkMap{ "key": NetworkArgs{...} }
type NetworkMapInput interface {
	pulumi.Input

	ToNetworkMapOutput() NetworkMapOutput
	ToNetworkMapOutputWithContext(context.Context) NetworkMapOutput
}

type NetworkMap map[string]NetworkInput

func (NetworkMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Network)(nil)).Elem()
}

func (i NetworkMap) ToNetworkMapOutput() NetworkMapOutput {
	return i.ToNetworkMapOutputWithContext(context.Background())
}

func (i NetworkMap) ToNetworkMapOutputWithContext(ctx context.Context) NetworkMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkMapOutput)
}

type NetworkOutput struct{ *pulumi.OutputState }

func (NetworkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Network)(nil)).Elem()
}

func (o NetworkOutput) ToNetworkOutput() NetworkOutput {
	return o
}

func (o NetworkOutput) ToNetworkOutputWithContext(ctx context.Context) NetworkOutput {
	return o
}

// A list of (0 or 1) IPv4 and (0 or 1) IPv6 subnets in
// CIDR notation.  This defines the subnets associated to that network.
// This argument is also used to define the address on the real host.
// If `dhcp {  enabled = true }` addresses is also used to define the address range served by
// the DHCP server.
// No DHCP server will be started if `addresses` is omitted.
func (o NetworkOutput) Addresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Network) pulumi.StringArrayOutput { return v.Addresses }).(pulumi.StringArrayOutput)
}

// Set to `true` to start the network on host boot up.
// If not specified `false` is assumed.
func (o NetworkOutput) Autostart() pulumi.BoolOutput {
	return o.ApplyT(func(v *Network) pulumi.BoolOutput { return v.Autostart }).(pulumi.BoolOutput)
}

// The bridge device defines the name of a bridge
// device which will be used to construct the virtual network (when not provided,
// it will be automatically obtained by libvirt in `none`, `nat`, `route` and `open` modes).
func (o NetworkOutput) Bridge() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.Bridge }).(pulumi.StringOutput)
}

// DHCP configuration.
// You need to use it in conjuction with the adresses variable.
func (o NetworkOutput) Dhcp() NetworkDhcpOutput {
	return o.ApplyT(func(v *Network) NetworkDhcpOutput { return v.Dhcp }).(NetworkDhcpOutput)
}

// configuration of DNS specific settings for the network
func (o NetworkOutput) Dns() NetworkDnsOutput {
	return o.ApplyT(func(v *Network) NetworkDnsOutput { return v.Dns }).(NetworkDnsOutput)
}

// configuration of Dnsmasq options for the network
// You need to provide a list of option name and value pairs.
func (o NetworkOutput) DnsmasqOptions() NetworkDnsmasqOptionsPtrOutput {
	return o.ApplyT(func(v *Network) NetworkDnsmasqOptionsPtrOutput { return v.DnsmasqOptions }).(NetworkDnsmasqOptionsPtrOutput)
}

// The domain used by the DNS server.
func (o NetworkOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Network) pulumi.StringPtrOutput { return v.Domain }).(pulumi.StringPtrOutput)
}

// One of:
func (o NetworkOutput) Mode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Network) pulumi.StringPtrOutput { return v.Mode }).(pulumi.StringPtrOutput)
}

// The MTU to set for the underlying network interfaces. When
// not supplied, libvirt will use the default for the interface, usually 1500.
// Libvirt version 5.1 and greater will advertise this value to nodes via DHCP.
func (o NetworkOutput) Mtu() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Network) pulumi.IntPtrOutput { return v.Mtu }).(pulumi.IntPtrOutput)
}

// A unique name for the resource, required by libvirt.
// Changing this forces a new resource to be created.
func (o NetworkOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// a list of static routes. A `cidr` and a `gateway` must
// be provided. The `gateway` must be reachable via the bridge interface.
func (o NetworkOutput) Routes() NetworkRouteArrayOutput {
	return o.ApplyT(func(v *Network) NetworkRouteArrayOutput { return v.Routes }).(NetworkRouteArrayOutput)
}

func (o NetworkOutput) Xml() NetworkXmlPtrOutput {
	return o.ApplyT(func(v *Network) NetworkXmlPtrOutput { return v.Xml }).(NetworkXmlPtrOutput)
}

type NetworkArrayOutput struct{ *pulumi.OutputState }

func (NetworkArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Network)(nil)).Elem()
}

func (o NetworkArrayOutput) ToNetworkArrayOutput() NetworkArrayOutput {
	return o
}

func (o NetworkArrayOutput) ToNetworkArrayOutputWithContext(ctx context.Context) NetworkArrayOutput {
	return o
}

func (o NetworkArrayOutput) Index(i pulumi.IntInput) NetworkOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Network {
		return vs[0].([]*Network)[vs[1].(int)]
	}).(NetworkOutput)
}

type NetworkMapOutput struct{ *pulumi.OutputState }

func (NetworkMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Network)(nil)).Elem()
}

func (o NetworkMapOutput) ToNetworkMapOutput() NetworkMapOutput {
	return o
}

func (o NetworkMapOutput) ToNetworkMapOutputWithContext(ctx context.Context) NetworkMapOutput {
	return o
}

func (o NetworkMapOutput) MapIndex(k pulumi.StringInput) NetworkOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Network {
		return vs[0].(map[string]*Network)[vs[1].(string)]
	}).(NetworkOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkInput)(nil)).Elem(), &Network{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkArrayInput)(nil)).Elem(), NetworkArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkMapInput)(nil)).Elem(), NetworkMap{})
	pulumi.RegisterOutputType(NetworkOutput{})
	pulumi.RegisterOutputType(NetworkArrayOutput{})
	pulumi.RegisterOutputType(NetworkMapOutput{})
}
