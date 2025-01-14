// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.libvirt.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class DomainTpm {
    /**
     * @return Path to TPM device on the host, ex: `/dev/tpm0`
     * 
     */
    private @Nullable String backendDevicePath;
    /**
     * @return [Secret object](https://libvirt.org/formatsecret.html) for encrypting the TPM state
     * 
     */
    private @Nullable String backendEncryptionSecret;
    /**
     * @return Keep the TPM state when a transient domain is powered off or undefined
     * 
     */
    private @Nullable Boolean backendPersistentState;
    /**
     * @return TPM backend, either `passthrough` or `emulator` (default: `emulator`)
     * 
     */
    private @Nullable String backendType;
    /**
     * @return TPM version
     * 
     */
    private @Nullable String backendVersion;
    /**
     * @return TPM model provided to the guest
     * 
     */
    private @Nullable String model;

    private DomainTpm() {}
    /**
     * @return Path to TPM device on the host, ex: `/dev/tpm0`
     * 
     */
    public Optional<String> backendDevicePath() {
        return Optional.ofNullable(this.backendDevicePath);
    }
    /**
     * @return [Secret object](https://libvirt.org/formatsecret.html) for encrypting the TPM state
     * 
     */
    public Optional<String> backendEncryptionSecret() {
        return Optional.ofNullable(this.backendEncryptionSecret);
    }
    /**
     * @return Keep the TPM state when a transient domain is powered off or undefined
     * 
     */
    public Optional<Boolean> backendPersistentState() {
        return Optional.ofNullable(this.backendPersistentState);
    }
    /**
     * @return TPM backend, either `passthrough` or `emulator` (default: `emulator`)
     * 
     */
    public Optional<String> backendType() {
        return Optional.ofNullable(this.backendType);
    }
    /**
     * @return TPM version
     * 
     */
    public Optional<String> backendVersion() {
        return Optional.ofNullable(this.backendVersion);
    }
    /**
     * @return TPM model provided to the guest
     * 
     */
    public Optional<String> model() {
        return Optional.ofNullable(this.model);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(DomainTpm defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String backendDevicePath;
        private @Nullable String backendEncryptionSecret;
        private @Nullable Boolean backendPersistentState;
        private @Nullable String backendType;
        private @Nullable String backendVersion;
        private @Nullable String model;
        public Builder() {}
        public Builder(DomainTpm defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.backendDevicePath = defaults.backendDevicePath;
    	      this.backendEncryptionSecret = defaults.backendEncryptionSecret;
    	      this.backendPersistentState = defaults.backendPersistentState;
    	      this.backendType = defaults.backendType;
    	      this.backendVersion = defaults.backendVersion;
    	      this.model = defaults.model;
        }

        @CustomType.Setter
        public Builder backendDevicePath(@Nullable String backendDevicePath) {
            this.backendDevicePath = backendDevicePath;
            return this;
        }
        @CustomType.Setter
        public Builder backendEncryptionSecret(@Nullable String backendEncryptionSecret) {
            this.backendEncryptionSecret = backendEncryptionSecret;
            return this;
        }
        @CustomType.Setter
        public Builder backendPersistentState(@Nullable Boolean backendPersistentState) {
            this.backendPersistentState = backendPersistentState;
            return this;
        }
        @CustomType.Setter
        public Builder backendType(@Nullable String backendType) {
            this.backendType = backendType;
            return this;
        }
        @CustomType.Setter
        public Builder backendVersion(@Nullable String backendVersion) {
            this.backendVersion = backendVersion;
            return this;
        }
        @CustomType.Setter
        public Builder model(@Nullable String model) {
            this.model = model;
            return this;
        }
        public DomainTpm build() {
            final var o = new DomainTpm();
            o.backendDevicePath = backendDevicePath;
            o.backendEncryptionSecret = backendEncryptionSecret;
            o.backendPersistentState = backendPersistentState;
            o.backendType = backendType;
            o.backendVersion = backendVersion;
            o.model = model;
            return o;
        }
    }
}
