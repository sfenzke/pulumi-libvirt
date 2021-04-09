// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt
{
    /// <summary>
    /// Manages a VM domain resource within libvirt. For more information see
    /// [the official documentation](https://libvirt.org/formatdomain.html).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Libvirt = Pulumi.Libvirt;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var @default = new Libvirt.Domain("default", new Libvirt.DomainArgs
    ///         {
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [LibvirtResourceType("libvirt:index/domain:Domain")]
    public partial class Domain : Pulumi.CustomResource
    {
        /// <summary>
        /// The architecture for the VM (probably x86_64 or i686),
        /// you normally won't need to set this unless you are building a special VM
        /// </summary>
        [Output("arch")]
        public Output<string> Arch { get; private set; } = null!;

        /// <summary>
        /// Set to `true` to start the domain on host boot up.
        /// If not specified `false` is assumed.
        /// </summary>
        [Output("autostart")]
        public Output<bool?> Autostart { get; private set; } = null!;

        /// <summary>
        /// A list of devices (dev) which defines boot order. Example
        /// below.
        /// </summary>
        [Output("bootDevices")]
        public Output<ImmutableArray<Outputs.DomainBootDevice>> BootDevices { get; private set; } = null!;

        /// <summary>
        /// The `libvirt.CloudInitDisk` disk that has to be used by
        /// the domain. This is going to be attached as a CDROM ISO. Changing the
        /// cloud-init won't cause the domain to be recreated, however the change will
        /// have effect on the next reboot.
        /// </summary>
        [Output("cloudinit")]
        public Output<string?> Cloudinit { get; private set; } = null!;

        /// <summary>
        /// Arguments to the kernel
        /// </summary>
        [Output("cmdlines")]
        public Output<ImmutableArray<ImmutableDictionary<string, object>>> Cmdlines { get; private set; } = null!;

        [Output("consoles")]
        public Output<ImmutableArray<Outputs.DomainConsole>> Consoles { get; private set; } = null!;

        /// <summary>
        /// The
        /// [libvirt.Ignition](https://www.terraform.io/docs/providers/libvirt/r/coreos_ignition.html) resource
        /// that is to be used by the CoreOS domain.
        /// </summary>
        [Output("coreosIgnition")]
        public Output<string?> CoreosIgnition { get; private set; } = null!;

        /// <summary>
        /// Configures CPU mode. See below for more
        /// details.
        /// </summary>
        [Output("cpu")]
        public Output<Outputs.DomainCpu?> Cpu { get; private set; } = null!;

        /// <summary>
        /// The description for domain.
        /// Changing this forces a new resource to be created.
        /// This data is not used by libvirt in any way, it can contain any information the user wants.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// An array of one or more disks to attach to the domain. The
        /// `disk` object structure is documented below.
        /// </summary>
        [Output("disks")]
        public Output<ImmutableArray<Outputs.DomainDisk>> Disks { get; private set; } = null!;

        /// <summary>
        /// The path of the emulator to use
        /// </summary>
        [Output("emulator")]
        public Output<string> Emulator { get; private set; } = null!;

        /// <summary>
        /// An array of one or more host filesystems to attach to
        /// the domain. The `filesystem` object structure is documented
        /// below.
        /// </summary>
        [Output("filesystems")]
        public Output<ImmutableArray<Outputs.DomainFilesystem>> Filesystems { get; private set; } = null!;

        /// <summary>
        /// The UEFI rom images for exercising UEFI secure boot in a qemu
        /// environment. Users should usually specify one of the standard _Open Virtual Machine
        /// Firmware_ (_OVMF_) images available for their distributions. The file will be opened
        /// read-only.
        /// </summary>
        [Output("firmware")]
        public Output<string?> Firmware { get; private set; } = null!;

        /// <summary>
        /// The name of the firmware config path where ignition file is stored: default is `opt/com.coreos/config`. If you are using [Flatcar Linux](https://docs.flatcar-linux.org/os/booting-with-libvirt/#creating-the-domain-xml), the value is `opt/org.flatcar-linux/config`.
        /// </summary>
        [Output("fwCfgName")]
        public Output<string?> FwCfgName { get; private set; } = null!;

        [Output("graphics")]
        public Output<Outputs.DomainGraphics?> Graphics { get; private set; } = null!;

        /// <summary>
        /// The path of the initrd to boot.
        /// </summary>
        [Output("initrd")]
        public Output<string?> Initrd { get; private set; } = null!;

        /// <summary>
        /// The path of the kernel to boot
        /// </summary>
        [Output("kernel")]
        public Output<string?> Kernel { get; private set; } = null!;

        /// <summary>
        /// The machine type,
        /// you normally won't need to set this unless you are running on a platform that
        /// defaults to the wrong machine type for your template
        /// </summary>
        [Output("machine")]
        public Output<string> Machine { get; private set; } = null!;

        /// <summary>
        /// The amount of memory in MiB. If not specified the domain
        /// will be created with 512 MiB of memory be used.
        /// </summary>
        [Output("memory")]
        public Output<int?> Memory { get; private set; } = null!;

        [Output("metadata")]
        public Output<string?> Metadata { get; private set; } = null!;

        /// <summary>
        /// A unique name for the resource, required by libvirt.
        /// Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// An array of one or more network interfaces to
        /// attach to the domain. The `network_interface` object structure is documented
        /// below.
        /// </summary>
        [Output("networkInterfaces")]
        public Output<ImmutableArray<Outputs.DomainNetworkInterface>> NetworkInterfaces { get; private set; } = null!;

        /// <summary>
        /// this block allows specifying the following attributes related to the _nvram_:
        /// </summary>
        [Output("nvram")]
        public Output<Outputs.DomainNvram?> Nvram { get; private set; } = null!;

        /// <summary>
        /// By default is disabled, set to true for enabling it. More info [qemu-agent](https://wiki.libvirt.org/page/Qemu_guest_agent).
        /// </summary>
        [Output("qemuAgent")]
        public Output<bool?> QemuAgent { get; private set; } = null!;

        /// <summary>
        /// Use `false` to turn off the instance. If not specified,
        /// true is assumed and the instance, if stopped, will be started at next apply.
        /// </summary>
        [Output("running")]
        public Output<bool?> Running { get; private set; } = null!;

        /// <summary>
        /// The amount of virtual CPUs. If not specified, a single CPU
        /// will be created.
        /// </summary>
        [Output("vcpu")]
        public Output<int?> Vcpu { get; private set; } = null!;

        [Output("video")]
        public Output<Outputs.DomainVideo?> Video { get; private set; } = null!;

        [Output("xml")]
        public Output<Outputs.DomainXml?> Xml { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs? args = null, CustomResourceOptions? options = null)
            : base("libvirt:index/domain:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
            : base("libvirt:index/domain:Domain", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, state, options);
        }
    }

    public sealed class DomainArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The architecture for the VM (probably x86_64 or i686),
        /// you normally won't need to set this unless you are building a special VM
        /// </summary>
        [Input("arch")]
        public Input<string>? Arch { get; set; }

        /// <summary>
        /// Set to `true` to start the domain on host boot up.
        /// If not specified `false` is assumed.
        /// </summary>
        [Input("autostart")]
        public Input<bool>? Autostart { get; set; }

        [Input("bootDevices")]
        private InputList<Inputs.DomainBootDeviceArgs>? _bootDevices;

        /// <summary>
        /// A list of devices (dev) which defines boot order. Example
        /// below.
        /// </summary>
        public InputList<Inputs.DomainBootDeviceArgs> BootDevices
        {
            get => _bootDevices ?? (_bootDevices = new InputList<Inputs.DomainBootDeviceArgs>());
            set => _bootDevices = value;
        }

        /// <summary>
        /// The `libvirt.CloudInitDisk` disk that has to be used by
        /// the domain. This is going to be attached as a CDROM ISO. Changing the
        /// cloud-init won't cause the domain to be recreated, however the change will
        /// have effect on the next reboot.
        /// </summary>
        [Input("cloudinit")]
        public Input<string>? Cloudinit { get; set; }

        [Input("cmdlines")]
        private InputList<ImmutableDictionary<string, object>>? _cmdlines;

        /// <summary>
        /// Arguments to the kernel
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Cmdlines
        {
            get => _cmdlines ?? (_cmdlines = new InputList<ImmutableDictionary<string, object>>());
            set => _cmdlines = value;
        }

        [Input("consoles")]
        private InputList<Inputs.DomainConsoleArgs>? _consoles;
        public InputList<Inputs.DomainConsoleArgs> Consoles
        {
            get => _consoles ?? (_consoles = new InputList<Inputs.DomainConsoleArgs>());
            set => _consoles = value;
        }

        /// <summary>
        /// The
        /// [libvirt.Ignition](https://www.terraform.io/docs/providers/libvirt/r/coreos_ignition.html) resource
        /// that is to be used by the CoreOS domain.
        /// </summary>
        [Input("coreosIgnition")]
        public Input<string>? CoreosIgnition { get; set; }

        /// <summary>
        /// Configures CPU mode. See below for more
        /// details.
        /// </summary>
        [Input("cpu")]
        public Input<Inputs.DomainCpuArgs>? Cpu { get; set; }

        /// <summary>
        /// The description for domain.
        /// Changing this forces a new resource to be created.
        /// This data is not used by libvirt in any way, it can contain any information the user wants.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("disks")]
        private InputList<Inputs.DomainDiskArgs>? _disks;

        /// <summary>
        /// An array of one or more disks to attach to the domain. The
        /// `disk` object structure is documented below.
        /// </summary>
        public InputList<Inputs.DomainDiskArgs> Disks
        {
            get => _disks ?? (_disks = new InputList<Inputs.DomainDiskArgs>());
            set => _disks = value;
        }

        /// <summary>
        /// The path of the emulator to use
        /// </summary>
        [Input("emulator")]
        public Input<string>? Emulator { get; set; }

        [Input("filesystems")]
        private InputList<Inputs.DomainFilesystemArgs>? _filesystems;

        /// <summary>
        /// An array of one or more host filesystems to attach to
        /// the domain. The `filesystem` object structure is documented
        /// below.
        /// </summary>
        public InputList<Inputs.DomainFilesystemArgs> Filesystems
        {
            get => _filesystems ?? (_filesystems = new InputList<Inputs.DomainFilesystemArgs>());
            set => _filesystems = value;
        }

        /// <summary>
        /// The UEFI rom images for exercising UEFI secure boot in a qemu
        /// environment. Users should usually specify one of the standard _Open Virtual Machine
        /// Firmware_ (_OVMF_) images available for their distributions. The file will be opened
        /// read-only.
        /// </summary>
        [Input("firmware")]
        public Input<string>? Firmware { get; set; }

        /// <summary>
        /// The name of the firmware config path where ignition file is stored: default is `opt/com.coreos/config`. If you are using [Flatcar Linux](https://docs.flatcar-linux.org/os/booting-with-libvirt/#creating-the-domain-xml), the value is `opt/org.flatcar-linux/config`.
        /// </summary>
        [Input("fwCfgName")]
        public Input<string>? FwCfgName { get; set; }

        [Input("graphics")]
        public Input<Inputs.DomainGraphicsArgs>? Graphics { get; set; }

        /// <summary>
        /// The path of the initrd to boot.
        /// </summary>
        [Input("initrd")]
        public Input<string>? Initrd { get; set; }

        /// <summary>
        /// The path of the kernel to boot
        /// </summary>
        [Input("kernel")]
        public Input<string>? Kernel { get; set; }

        /// <summary>
        /// The machine type,
        /// you normally won't need to set this unless you are running on a platform that
        /// defaults to the wrong machine type for your template
        /// </summary>
        [Input("machine")]
        public Input<string>? Machine { get; set; }

        /// <summary>
        /// The amount of memory in MiB. If not specified the domain
        /// will be created with 512 MiB of memory be used.
        /// </summary>
        [Input("memory")]
        public Input<int>? Memory { get; set; }

        [Input("metadata")]
        public Input<string>? Metadata { get; set; }

        /// <summary>
        /// A unique name for the resource, required by libvirt.
        /// Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.DomainNetworkInterfaceArgs>? _networkInterfaces;

        /// <summary>
        /// An array of one or more network interfaces to
        /// attach to the domain. The `network_interface` object structure is documented
        /// below.
        /// </summary>
        public InputList<Inputs.DomainNetworkInterfaceArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.DomainNetworkInterfaceArgs>());
            set => _networkInterfaces = value;
        }

        /// <summary>
        /// this block allows specifying the following attributes related to the _nvram_:
        /// </summary>
        [Input("nvram")]
        public Input<Inputs.DomainNvramArgs>? Nvram { get; set; }

        /// <summary>
        /// By default is disabled, set to true for enabling it. More info [qemu-agent](https://wiki.libvirt.org/page/Qemu_guest_agent).
        /// </summary>
        [Input("qemuAgent")]
        public Input<bool>? QemuAgent { get; set; }

        /// <summary>
        /// Use `false` to turn off the instance. If not specified,
        /// true is assumed and the instance, if stopped, will be started at next apply.
        /// </summary>
        [Input("running")]
        public Input<bool>? Running { get; set; }

        /// <summary>
        /// The amount of virtual CPUs. If not specified, a single CPU
        /// will be created.
        /// </summary>
        [Input("vcpu")]
        public Input<int>? Vcpu { get; set; }

        [Input("video")]
        public Input<Inputs.DomainVideoArgs>? Video { get; set; }

        [Input("xml")]
        public Input<Inputs.DomainXmlArgs>? Xml { get; set; }

        public DomainArgs()
        {
        }
    }

    public sealed class DomainState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The architecture for the VM (probably x86_64 or i686),
        /// you normally won't need to set this unless you are building a special VM
        /// </summary>
        [Input("arch")]
        public Input<string>? Arch { get; set; }

        /// <summary>
        /// Set to `true` to start the domain on host boot up.
        /// If not specified `false` is assumed.
        /// </summary>
        [Input("autostart")]
        public Input<bool>? Autostart { get; set; }

        [Input("bootDevices")]
        private InputList<Inputs.DomainBootDeviceGetArgs>? _bootDevices;

        /// <summary>
        /// A list of devices (dev) which defines boot order. Example
        /// below.
        /// </summary>
        public InputList<Inputs.DomainBootDeviceGetArgs> BootDevices
        {
            get => _bootDevices ?? (_bootDevices = new InputList<Inputs.DomainBootDeviceGetArgs>());
            set => _bootDevices = value;
        }

        /// <summary>
        /// The `libvirt.CloudInitDisk` disk that has to be used by
        /// the domain. This is going to be attached as a CDROM ISO. Changing the
        /// cloud-init won't cause the domain to be recreated, however the change will
        /// have effect on the next reboot.
        /// </summary>
        [Input("cloudinit")]
        public Input<string>? Cloudinit { get; set; }

        [Input("cmdlines")]
        private InputList<ImmutableDictionary<string, object>>? _cmdlines;

        /// <summary>
        /// Arguments to the kernel
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Cmdlines
        {
            get => _cmdlines ?? (_cmdlines = new InputList<ImmutableDictionary<string, object>>());
            set => _cmdlines = value;
        }

        [Input("consoles")]
        private InputList<Inputs.DomainConsoleGetArgs>? _consoles;
        public InputList<Inputs.DomainConsoleGetArgs> Consoles
        {
            get => _consoles ?? (_consoles = new InputList<Inputs.DomainConsoleGetArgs>());
            set => _consoles = value;
        }

        /// <summary>
        /// The
        /// [libvirt.Ignition](https://www.terraform.io/docs/providers/libvirt/r/coreos_ignition.html) resource
        /// that is to be used by the CoreOS domain.
        /// </summary>
        [Input("coreosIgnition")]
        public Input<string>? CoreosIgnition { get; set; }

        /// <summary>
        /// Configures CPU mode. See below for more
        /// details.
        /// </summary>
        [Input("cpu")]
        public Input<Inputs.DomainCpuGetArgs>? Cpu { get; set; }

        /// <summary>
        /// The description for domain.
        /// Changing this forces a new resource to be created.
        /// This data is not used by libvirt in any way, it can contain any information the user wants.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("disks")]
        private InputList<Inputs.DomainDiskGetArgs>? _disks;

        /// <summary>
        /// An array of one or more disks to attach to the domain. The
        /// `disk` object structure is documented below.
        /// </summary>
        public InputList<Inputs.DomainDiskGetArgs> Disks
        {
            get => _disks ?? (_disks = new InputList<Inputs.DomainDiskGetArgs>());
            set => _disks = value;
        }

        /// <summary>
        /// The path of the emulator to use
        /// </summary>
        [Input("emulator")]
        public Input<string>? Emulator { get; set; }

        [Input("filesystems")]
        private InputList<Inputs.DomainFilesystemGetArgs>? _filesystems;

        /// <summary>
        /// An array of one or more host filesystems to attach to
        /// the domain. The `filesystem` object structure is documented
        /// below.
        /// </summary>
        public InputList<Inputs.DomainFilesystemGetArgs> Filesystems
        {
            get => _filesystems ?? (_filesystems = new InputList<Inputs.DomainFilesystemGetArgs>());
            set => _filesystems = value;
        }

        /// <summary>
        /// The UEFI rom images for exercising UEFI secure boot in a qemu
        /// environment. Users should usually specify one of the standard _Open Virtual Machine
        /// Firmware_ (_OVMF_) images available for their distributions. The file will be opened
        /// read-only.
        /// </summary>
        [Input("firmware")]
        public Input<string>? Firmware { get; set; }

        /// <summary>
        /// The name of the firmware config path where ignition file is stored: default is `opt/com.coreos/config`. If you are using [Flatcar Linux](https://docs.flatcar-linux.org/os/booting-with-libvirt/#creating-the-domain-xml), the value is `opt/org.flatcar-linux/config`.
        /// </summary>
        [Input("fwCfgName")]
        public Input<string>? FwCfgName { get; set; }

        [Input("graphics")]
        public Input<Inputs.DomainGraphicsGetArgs>? Graphics { get; set; }

        /// <summary>
        /// The path of the initrd to boot.
        /// </summary>
        [Input("initrd")]
        public Input<string>? Initrd { get; set; }

        /// <summary>
        /// The path of the kernel to boot
        /// </summary>
        [Input("kernel")]
        public Input<string>? Kernel { get; set; }

        /// <summary>
        /// The machine type,
        /// you normally won't need to set this unless you are running on a platform that
        /// defaults to the wrong machine type for your template
        /// </summary>
        [Input("machine")]
        public Input<string>? Machine { get; set; }

        /// <summary>
        /// The amount of memory in MiB. If not specified the domain
        /// will be created with 512 MiB of memory be used.
        /// </summary>
        [Input("memory")]
        public Input<int>? Memory { get; set; }

        [Input("metadata")]
        public Input<string>? Metadata { get; set; }

        /// <summary>
        /// A unique name for the resource, required by libvirt.
        /// Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.DomainNetworkInterfaceGetArgs>? _networkInterfaces;

        /// <summary>
        /// An array of one or more network interfaces to
        /// attach to the domain. The `network_interface` object structure is documented
        /// below.
        /// </summary>
        public InputList<Inputs.DomainNetworkInterfaceGetArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.DomainNetworkInterfaceGetArgs>());
            set => _networkInterfaces = value;
        }

        /// <summary>
        /// this block allows specifying the following attributes related to the _nvram_:
        /// </summary>
        [Input("nvram")]
        public Input<Inputs.DomainNvramGetArgs>? Nvram { get; set; }

        /// <summary>
        /// By default is disabled, set to true for enabling it. More info [qemu-agent](https://wiki.libvirt.org/page/Qemu_guest_agent).
        /// </summary>
        [Input("qemuAgent")]
        public Input<bool>? QemuAgent { get; set; }

        /// <summary>
        /// Use `false` to turn off the instance. If not specified,
        /// true is assumed and the instance, if stopped, will be started at next apply.
        /// </summary>
        [Input("running")]
        public Input<bool>? Running { get; set; }

        /// <summary>
        /// The amount of virtual CPUs. If not specified, a single CPU
        /// will be created.
        /// </summary>
        [Input("vcpu")]
        public Input<int>? Vcpu { get; set; }

        [Input("video")]
        public Input<Inputs.DomainVideoGetArgs>? Video { get; set; }

        [Input("xml")]
        public Input<Inputs.DomainXmlGetArgs>? Xml { get; set; }

        public DomainState()
        {
        }
    }
}
