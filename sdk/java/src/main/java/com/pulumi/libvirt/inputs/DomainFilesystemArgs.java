// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.libvirt.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DomainFilesystemArgs extends com.pulumi.resources.ResourceArgs {

    public static final DomainFilesystemArgs Empty = new DomainFilesystemArgs();

    /**
     * specifies the security mode for accessing the source. By default
     * the `mapped` mode is chosen.
     * 
     */
    @Import(name="accessmode")
    private @Nullable Output<String> accessmode;

    /**
     * @return specifies the security mode for accessing the source. By default
     * the `mapped` mode is chosen.
     * 
     */
    public Optional<Output<String>> accessmode() {
        return Optional.ofNullable(this.accessmode);
    }

    /**
     * enables exporting filesystem as a readonly mount for guest, by
     * default read-only access is given.
     * 
     */
    @Import(name="readonly")
    private @Nullable Output<Boolean> readonly;

    /**
     * @return enables exporting filesystem as a readonly mount for guest, by
     * default read-only access is given.
     * 
     */
    public Optional<Output<Boolean>> readonly() {
        return Optional.ofNullable(this.readonly);
    }

    /**
     * the directory of the host to be shared with the guest.
     * 
     */
    @Import(name="source", required=true)
    private Output<String> source;

    /**
     * @return the directory of the host to be shared with the guest.
     * 
     */
    public Output<String> source() {
        return this.source;
    }

    /**
     * an arbitrary string tag that is exported to the guest as a hint for
     * where to mount the source.
     * 
     */
    @Import(name="target", required=true)
    private Output<String> target;

    /**
     * @return an arbitrary string tag that is exported to the guest as a hint for
     * where to mount the source.
     * 
     */
    public Output<String> target() {
        return this.target;
    }

    private DomainFilesystemArgs() {}

    private DomainFilesystemArgs(DomainFilesystemArgs $) {
        this.accessmode = $.accessmode;
        this.readonly = $.readonly;
        this.source = $.source;
        this.target = $.target;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DomainFilesystemArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DomainFilesystemArgs $;

        public Builder() {
            $ = new DomainFilesystemArgs();
        }

        public Builder(DomainFilesystemArgs defaults) {
            $ = new DomainFilesystemArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param accessmode specifies the security mode for accessing the source. By default
         * the `mapped` mode is chosen.
         * 
         * @return builder
         * 
         */
        public Builder accessmode(@Nullable Output<String> accessmode) {
            $.accessmode = accessmode;
            return this;
        }

        /**
         * @param accessmode specifies the security mode for accessing the source. By default
         * the `mapped` mode is chosen.
         * 
         * @return builder
         * 
         */
        public Builder accessmode(String accessmode) {
            return accessmode(Output.of(accessmode));
        }

        /**
         * @param readonly enables exporting filesystem as a readonly mount for guest, by
         * default read-only access is given.
         * 
         * @return builder
         * 
         */
        public Builder readonly(@Nullable Output<Boolean> readonly) {
            $.readonly = readonly;
            return this;
        }

        /**
         * @param readonly enables exporting filesystem as a readonly mount for guest, by
         * default read-only access is given.
         * 
         * @return builder
         * 
         */
        public Builder readonly(Boolean readonly) {
            return readonly(Output.of(readonly));
        }

        /**
         * @param source the directory of the host to be shared with the guest.
         * 
         * @return builder
         * 
         */
        public Builder source(Output<String> source) {
            $.source = source;
            return this;
        }

        /**
         * @param source the directory of the host to be shared with the guest.
         * 
         * @return builder
         * 
         */
        public Builder source(String source) {
            return source(Output.of(source));
        }

        /**
         * @param target an arbitrary string tag that is exported to the guest as a hint for
         * where to mount the source.
         * 
         * @return builder
         * 
         */
        public Builder target(Output<String> target) {
            $.target = target;
            return this;
        }

        /**
         * @param target an arbitrary string tag that is exported to the guest as a hint for
         * where to mount the source.
         * 
         * @return builder
         * 
         */
        public Builder target(String target) {
            return target(Output.of(target));
        }

        public DomainFilesystemArgs build() {
            $.source = Objects.requireNonNull($.source, "expected parameter 'source' to be non-null");
            $.target = Objects.requireNonNull($.target, "expected parameter 'target' to be non-null");
            return $;
        }
    }

}
