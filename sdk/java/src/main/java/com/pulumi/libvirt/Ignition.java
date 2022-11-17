// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.libvirt;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.libvirt.IgnitionArgs;
import com.pulumi.libvirt.Utilities;
import com.pulumi.libvirt.inputs.IgnitionState;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

@ResourceType(type="libvirt:index/ignition:Ignition")
public class Ignition extends com.pulumi.resources.CustomResource {
    @Export(name="content", type=String.class, parameters={})
    private Output<String> content;

    public Output<String> content() {
        return this.content;
    }
    /**
     * A unique name for the resource, required by libvirt.
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return A unique name for the resource, required by libvirt.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The pool where the resource will be created.
     * If not given, the `default` pool will be used.
     * 
     */
    @Export(name="pool", type=String.class, parameters={})
    private Output</* @Nullable */ String> pool;

    /**
     * @return The pool where the resource will be created.
     * If not given, the `default` pool will be used.
     * 
     */
    public Output<Optional<String>> pool() {
        return Codegen.optional(this.pool);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Ignition(String name) {
        this(name, IgnitionArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Ignition(String name, IgnitionArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Ignition(String name, IgnitionArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("libvirt:index/ignition:Ignition", name, args == null ? IgnitionArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Ignition(String name, Output<String> id, @Nullable IgnitionState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("libvirt:index/ignition:Ignition", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Ignition get(String name, Output<String> id, @Nullable IgnitionState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Ignition(name, id, state, options);
    }
}