// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package libvirt

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type Ignition struct {
	pulumi.CustomResourceState

	Content pulumi.StringOutput    `pulumi:"content"`
	Name    pulumi.StringOutput    `pulumi:"name"`
	Pool    pulumi.StringPtrOutput `pulumi:"pool"`
}

// NewIgnition registers a new resource with the given unique name, arguments, and options.
func NewIgnition(ctx *pulumi.Context,
	name string, args *IgnitionArgs, opts ...pulumi.ResourceOption) (*Ignition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Content == nil {
		return nil, errors.New("invalid value for required argument 'Content'")
	}
	var resource Ignition
	err := ctx.RegisterResource("libvirt:index/ignition:Ignition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIgnition gets an existing Ignition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIgnition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IgnitionState, opts ...pulumi.ResourceOption) (*Ignition, error) {
	var resource Ignition
	err := ctx.ReadResource("libvirt:index/ignition:Ignition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Ignition resources.
type ignitionState struct {
	Content *string `pulumi:"content"`
	Name    *string `pulumi:"name"`
	Pool    *string `pulumi:"pool"`
}

type IgnitionState struct {
	Content pulumi.StringPtrInput
	Name    pulumi.StringPtrInput
	Pool    pulumi.StringPtrInput
}

func (IgnitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*ignitionState)(nil)).Elem()
}

type ignitionArgs struct {
	Content string  `pulumi:"content"`
	Name    *string `pulumi:"name"`
	Pool    *string `pulumi:"pool"`
}

// The set of arguments for constructing a Ignition resource.
type IgnitionArgs struct {
	Content pulumi.StringInput
	Name    pulumi.StringPtrInput
	Pool    pulumi.StringPtrInput
}

func (IgnitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ignitionArgs)(nil)).Elem()
}

type IgnitionInput interface {
	pulumi.Input

	ToIgnitionOutput() IgnitionOutput
	ToIgnitionOutputWithContext(ctx context.Context) IgnitionOutput
}

func (*Ignition) ElementType() reflect.Type {
	return reflect.TypeOf((*Ignition)(nil))
}

func (i *Ignition) ToIgnitionOutput() IgnitionOutput {
	return i.ToIgnitionOutputWithContext(context.Background())
}

func (i *Ignition) ToIgnitionOutputWithContext(ctx context.Context) IgnitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IgnitionOutput)
}

func (i *Ignition) ToIgnitionPtrOutput() IgnitionPtrOutput {
	return i.ToIgnitionPtrOutputWithContext(context.Background())
}

func (i *Ignition) ToIgnitionPtrOutputWithContext(ctx context.Context) IgnitionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IgnitionPtrOutput)
}

type IgnitionPtrInput interface {
	pulumi.Input

	ToIgnitionPtrOutput() IgnitionPtrOutput
	ToIgnitionPtrOutputWithContext(ctx context.Context) IgnitionPtrOutput
}

type ignitionPtrType IgnitionArgs

func (*ignitionPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Ignition)(nil))
}

func (i *ignitionPtrType) ToIgnitionPtrOutput() IgnitionPtrOutput {
	return i.ToIgnitionPtrOutputWithContext(context.Background())
}

func (i *ignitionPtrType) ToIgnitionPtrOutputWithContext(ctx context.Context) IgnitionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IgnitionPtrOutput)
}

// IgnitionArrayInput is an input type that accepts IgnitionArray and IgnitionArrayOutput values.
// You can construct a concrete instance of `IgnitionArrayInput` via:
//
//          IgnitionArray{ IgnitionArgs{...} }
type IgnitionArrayInput interface {
	pulumi.Input

	ToIgnitionArrayOutput() IgnitionArrayOutput
	ToIgnitionArrayOutputWithContext(context.Context) IgnitionArrayOutput
}

type IgnitionArray []IgnitionInput

func (IgnitionArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Ignition)(nil))
}

func (i IgnitionArray) ToIgnitionArrayOutput() IgnitionArrayOutput {
	return i.ToIgnitionArrayOutputWithContext(context.Background())
}

func (i IgnitionArray) ToIgnitionArrayOutputWithContext(ctx context.Context) IgnitionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IgnitionArrayOutput)
}

// IgnitionMapInput is an input type that accepts IgnitionMap and IgnitionMapOutput values.
// You can construct a concrete instance of `IgnitionMapInput` via:
//
//          IgnitionMap{ "key": IgnitionArgs{...} }
type IgnitionMapInput interface {
	pulumi.Input

	ToIgnitionMapOutput() IgnitionMapOutput
	ToIgnitionMapOutputWithContext(context.Context) IgnitionMapOutput
}

type IgnitionMap map[string]IgnitionInput

func (IgnitionMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Ignition)(nil))
}

func (i IgnitionMap) ToIgnitionMapOutput() IgnitionMapOutput {
	return i.ToIgnitionMapOutputWithContext(context.Background())
}

func (i IgnitionMap) ToIgnitionMapOutputWithContext(ctx context.Context) IgnitionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IgnitionMapOutput)
}

type IgnitionOutput struct {
	*pulumi.OutputState
}

func (IgnitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Ignition)(nil))
}

func (o IgnitionOutput) ToIgnitionOutput() IgnitionOutput {
	return o
}

func (o IgnitionOutput) ToIgnitionOutputWithContext(ctx context.Context) IgnitionOutput {
	return o
}

func (o IgnitionOutput) ToIgnitionPtrOutput() IgnitionPtrOutput {
	return o.ToIgnitionPtrOutputWithContext(context.Background())
}

func (o IgnitionOutput) ToIgnitionPtrOutputWithContext(ctx context.Context) IgnitionPtrOutput {
	return o.ApplyT(func(v Ignition) *Ignition {
		return &v
	}).(IgnitionPtrOutput)
}

type IgnitionPtrOutput struct {
	*pulumi.OutputState
}

func (IgnitionPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Ignition)(nil))
}

func (o IgnitionPtrOutput) ToIgnitionPtrOutput() IgnitionPtrOutput {
	return o
}

func (o IgnitionPtrOutput) ToIgnitionPtrOutputWithContext(ctx context.Context) IgnitionPtrOutput {
	return o
}

type IgnitionArrayOutput struct{ *pulumi.OutputState }

func (IgnitionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Ignition)(nil))
}

func (o IgnitionArrayOutput) ToIgnitionArrayOutput() IgnitionArrayOutput {
	return o
}

func (o IgnitionArrayOutput) ToIgnitionArrayOutputWithContext(ctx context.Context) IgnitionArrayOutput {
	return o
}

func (o IgnitionArrayOutput) Index(i pulumi.IntInput) IgnitionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Ignition {
		return vs[0].([]Ignition)[vs[1].(int)]
	}).(IgnitionOutput)
}

type IgnitionMapOutput struct{ *pulumi.OutputState }

func (IgnitionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Ignition)(nil))
}

func (o IgnitionMapOutput) ToIgnitionMapOutput() IgnitionMapOutput {
	return o
}

func (o IgnitionMapOutput) ToIgnitionMapOutputWithContext(ctx context.Context) IgnitionMapOutput {
	return o
}

func (o IgnitionMapOutput) MapIndex(k pulumi.StringInput) IgnitionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Ignition {
		return vs[0].(map[string]Ignition)[vs[1].(string)]
	}).(IgnitionOutput)
}

func init() {
	pulumi.RegisterOutputType(IgnitionOutput{})
	pulumi.RegisterOutputType(IgnitionPtrOutput{})
	pulumi.RegisterOutputType(IgnitionArrayOutput{})
	pulumi.RegisterOutputType(IgnitionMapOutput{})
}
