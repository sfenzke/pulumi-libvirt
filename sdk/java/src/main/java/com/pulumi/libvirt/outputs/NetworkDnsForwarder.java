// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.libvirt.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class NetworkDnsForwarder {
    private final @Nullable String address;
    /**
     * @return The domain used by the DNS server.
     * 
     */
    private final @Nullable String domain;

    @CustomType.Constructor
    private NetworkDnsForwarder(
        @CustomType.Parameter("address") @Nullable String address,
        @CustomType.Parameter("domain") @Nullable String domain) {
        this.address = address;
        this.domain = domain;
    }

    public Optional<String> address() {
        return Optional.ofNullable(this.address);
    }
    /**
     * @return The domain used by the DNS server.
     * 
     */
    public Optional<String> domain() {
        return Optional.ofNullable(this.domain);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(NetworkDnsForwarder defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private @Nullable String address;
        private @Nullable String domain;

        public Builder() {
    	      // Empty
        }

        public Builder(NetworkDnsForwarder defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.address = defaults.address;
    	      this.domain = defaults.domain;
        }

        public Builder address(@Nullable String address) {
            this.address = address;
            return this;
        }
        public Builder domain(@Nullable String domain) {
            this.domain = domain;
            return this;
        }        public NetworkDnsForwarder build() {
            return new NetworkDnsForwarder(address, domain);
        }
    }
}