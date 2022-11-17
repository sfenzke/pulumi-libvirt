// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.libvirt.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetNetworkDnsSrvTemplatePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetNetworkDnsSrvTemplatePlainArgs Empty = new GetNetworkDnsSrvTemplatePlainArgs();

    @Import(name="domain")
    private @Nullable String domain;

    public Optional<String> domain() {
        return Optional.ofNullable(this.domain);
    }

    @Import(name="port")
    private @Nullable String port;

    public Optional<String> port() {
        return Optional.ofNullable(this.port);
    }

    @Import(name="priority")
    private @Nullable String priority;

    public Optional<String> priority() {
        return Optional.ofNullable(this.priority);
    }

    @Import(name="protocol", required=true)
    private String protocol;

    public String protocol() {
        return this.protocol;
    }

    @Import(name="service", required=true)
    private String service;

    public String service() {
        return this.service;
    }

    @Import(name="target")
    private @Nullable String target;

    public Optional<String> target() {
        return Optional.ofNullable(this.target);
    }

    @Import(name="weight")
    private @Nullable String weight;

    public Optional<String> weight() {
        return Optional.ofNullable(this.weight);
    }

    private GetNetworkDnsSrvTemplatePlainArgs() {}

    private GetNetworkDnsSrvTemplatePlainArgs(GetNetworkDnsSrvTemplatePlainArgs $) {
        this.domain = $.domain;
        this.port = $.port;
        this.priority = $.priority;
        this.protocol = $.protocol;
        this.service = $.service;
        this.target = $.target;
        this.weight = $.weight;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetNetworkDnsSrvTemplatePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetNetworkDnsSrvTemplatePlainArgs $;

        public Builder() {
            $ = new GetNetworkDnsSrvTemplatePlainArgs();
        }

        public Builder(GetNetworkDnsSrvTemplatePlainArgs defaults) {
            $ = new GetNetworkDnsSrvTemplatePlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder domain(@Nullable String domain) {
            $.domain = domain;
            return this;
        }

        public Builder port(@Nullable String port) {
            $.port = port;
            return this;
        }

        public Builder priority(@Nullable String priority) {
            $.priority = priority;
            return this;
        }

        public Builder protocol(String protocol) {
            $.protocol = protocol;
            return this;
        }

        public Builder service(String service) {
            $.service = service;
            return this;
        }

        public Builder target(@Nullable String target) {
            $.target = target;
            return this;
        }

        public Builder weight(@Nullable String weight) {
            $.weight = weight;
            return this;
        }

        public GetNetworkDnsSrvTemplatePlainArgs build() {
            $.protocol = Objects.requireNonNull($.protocol, "expected parameter 'protocol' to be non-null");
            $.service = Objects.requireNonNull($.service, "expected parameter 'service' to be non-null");
            return $;
        }
    }

}