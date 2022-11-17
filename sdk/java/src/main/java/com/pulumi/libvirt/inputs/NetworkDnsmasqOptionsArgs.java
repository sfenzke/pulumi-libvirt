// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.libvirt.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.libvirt.inputs.NetworkDnsmasqOptionsOptionArgs;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NetworkDnsmasqOptionsArgs extends com.pulumi.resources.ResourceArgs {

    public static final NetworkDnsmasqOptionsArgs Empty = new NetworkDnsmasqOptionsArgs();

    /**
     * a Dnsmasq option entry block. You can have one or more of these
     * blocks in your definition. You must specify both `option_name` and `option_value`.
     * 
     */
    @Import(name="options")
    private @Nullable Output<List<NetworkDnsmasqOptionsOptionArgs>> options;

    /**
     * @return a Dnsmasq option entry block. You can have one or more of these
     * blocks in your definition. You must specify both `option_name` and `option_value`.
     * 
     */
    public Optional<Output<List<NetworkDnsmasqOptionsOptionArgs>>> options() {
        return Optional.ofNullable(this.options);
    }

    private NetworkDnsmasqOptionsArgs() {}

    private NetworkDnsmasqOptionsArgs(NetworkDnsmasqOptionsArgs $) {
        this.options = $.options;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NetworkDnsmasqOptionsArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NetworkDnsmasqOptionsArgs $;

        public Builder() {
            $ = new NetworkDnsmasqOptionsArgs();
        }

        public Builder(NetworkDnsmasqOptionsArgs defaults) {
            $ = new NetworkDnsmasqOptionsArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param options a Dnsmasq option entry block. You can have one or more of these
         * blocks in your definition. You must specify both `option_name` and `option_value`.
         * 
         * @return builder
         * 
         */
        public Builder options(@Nullable Output<List<NetworkDnsmasqOptionsOptionArgs>> options) {
            $.options = options;
            return this;
        }

        /**
         * @param options a Dnsmasq option entry block. You can have one or more of these
         * blocks in your definition. You must specify both `option_name` and `option_value`.
         * 
         * @return builder
         * 
         */
        public Builder options(List<NetworkDnsmasqOptionsOptionArgs> options) {
            return options(Output.of(options));
        }

        /**
         * @param options a Dnsmasq option entry block. You can have one or more of these
         * blocks in your definition. You must specify both `option_name` and `option_value`.
         * 
         * @return builder
         * 
         */
        public Builder options(NetworkDnsmasqOptionsOptionArgs... options) {
            return options(List.of(options));
        }

        public NetworkDnsmasqOptionsArgs build() {
            return $;
        }
    }

}