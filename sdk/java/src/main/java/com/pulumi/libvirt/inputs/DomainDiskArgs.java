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


public final class DomainDiskArgs extends com.pulumi.resources.ResourceArgs {

    public static final DomainDiskArgs Empty = new DomainDiskArgs();

    /**
     * The path to the host device to use as the block device for this disk.
     * 
     */
    @Import(name="blockDevice")
    private @Nullable Output<String> blockDevice;

    /**
     * @return The path to the host device to use as the block device for this disk.
     * 
     */
    public Optional<Output<String>> blockDevice() {
        return Optional.ofNullable(this.blockDevice);
    }

    /**
     * The filename to use as the block device for this disk (read-only)
     * 
     */
    @Import(name="file")
    private @Nullable Output<String> file;

    /**
     * @return The filename to use as the block device for this disk (read-only)
     * 
     */
    public Optional<Output<String>> file() {
        return Optional.ofNullable(this.file);
    }

    /**
     * Use a scsi controller for this disk.  The controller
     * model is set to `virtio-scsi`
     * 
     */
    @Import(name="scsi")
    private @Nullable Output<Boolean> scsi;

    /**
     * @return Use a scsi controller for this disk.  The controller
     * model is set to `virtio-scsi`
     * 
     */
    public Optional<Output<Boolean>> scsi() {
        return Optional.ofNullable(this.scsi);
    }

    /**
     * The http url to use as the block device for this disk (read-only)
     * 
     */
    @Import(name="url")
    private @Nullable Output<String> url;

    /**
     * @return The http url to use as the block device for this disk (read-only)
     * 
     */
    public Optional<Output<String>> url() {
        return Optional.ofNullable(this.url);
    }

    /**
     * The volume id to use for this disk.
     * 
     */
    @Import(name="volumeId")
    private @Nullable Output<String> volumeId;

    /**
     * @return The volume id to use for this disk.
     * 
     */
    public Optional<Output<String>> volumeId() {
        return Optional.ofNullable(this.volumeId);
    }

    /**
     * Specify a WWN to use for the disk if the disk is using
     * a scsi controller, if not specified then a random wwn is generated for the disk
     * 
     */
    @Import(name="wwn")
    private @Nullable Output<String> wwn;

    /**
     * @return Specify a WWN to use for the disk if the disk is using
     * a scsi controller, if not specified then a random wwn is generated for the disk
     * 
     */
    public Optional<Output<String>> wwn() {
        return Optional.ofNullable(this.wwn);
    }

    private DomainDiskArgs() {}

    private DomainDiskArgs(DomainDiskArgs $) {
        this.blockDevice = $.blockDevice;
        this.file = $.file;
        this.scsi = $.scsi;
        this.url = $.url;
        this.volumeId = $.volumeId;
        this.wwn = $.wwn;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DomainDiskArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DomainDiskArgs $;

        public Builder() {
            $ = new DomainDiskArgs();
        }

        public Builder(DomainDiskArgs defaults) {
            $ = new DomainDiskArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param blockDevice The path to the host device to use as the block device for this disk.
         * 
         * @return builder
         * 
         */
        public Builder blockDevice(@Nullable Output<String> blockDevice) {
            $.blockDevice = blockDevice;
            return this;
        }

        /**
         * @param blockDevice The path to the host device to use as the block device for this disk.
         * 
         * @return builder
         * 
         */
        public Builder blockDevice(String blockDevice) {
            return blockDevice(Output.of(blockDevice));
        }

        /**
         * @param file The filename to use as the block device for this disk (read-only)
         * 
         * @return builder
         * 
         */
        public Builder file(@Nullable Output<String> file) {
            $.file = file;
            return this;
        }

        /**
         * @param file The filename to use as the block device for this disk (read-only)
         * 
         * @return builder
         * 
         */
        public Builder file(String file) {
            return file(Output.of(file));
        }

        /**
         * @param scsi Use a scsi controller for this disk.  The controller
         * model is set to `virtio-scsi`
         * 
         * @return builder
         * 
         */
        public Builder scsi(@Nullable Output<Boolean> scsi) {
            $.scsi = scsi;
            return this;
        }

        /**
         * @param scsi Use a scsi controller for this disk.  The controller
         * model is set to `virtio-scsi`
         * 
         * @return builder
         * 
         */
        public Builder scsi(Boolean scsi) {
            return scsi(Output.of(scsi));
        }

        /**
         * @param url The http url to use as the block device for this disk (read-only)
         * 
         * @return builder
         * 
         */
        public Builder url(@Nullable Output<String> url) {
            $.url = url;
            return this;
        }

        /**
         * @param url The http url to use as the block device for this disk (read-only)
         * 
         * @return builder
         * 
         */
        public Builder url(String url) {
            return url(Output.of(url));
        }

        /**
         * @param volumeId The volume id to use for this disk.
         * 
         * @return builder
         * 
         */
        public Builder volumeId(@Nullable Output<String> volumeId) {
            $.volumeId = volumeId;
            return this;
        }

        /**
         * @param volumeId The volume id to use for this disk.
         * 
         * @return builder
         * 
         */
        public Builder volumeId(String volumeId) {
            return volumeId(Output.of(volumeId));
        }

        /**
         * @param wwn Specify a WWN to use for the disk if the disk is using
         * a scsi controller, if not specified then a random wwn is generated for the disk
         * 
         * @return builder
         * 
         */
        public Builder wwn(@Nullable Output<String> wwn) {
            $.wwn = wwn;
            return this;
        }

        /**
         * @param wwn Specify a WWN to use for the disk if the disk is using
         * a scsi controller, if not specified then a random wwn is generated for the disk
         * 
         * @return builder
         * 
         */
        public Builder wwn(String wwn) {
            return wwn(Output.of(wwn));
        }

        public DomainDiskArgs build() {
            return $;
        }
    }

}
