// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class NatGateway extends pulumi.CustomResource {
    /**
     * Get an existing NatGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NatGatewayState, opts?: pulumi.CustomResourceOptions): NatGateway {
        return new NatGateway(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ucloud:vpc/natGateway:NatGateway';

    /**
     * Returns true if the given object is an instance of NatGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NatGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NatGateway.__pulumiType;
    }

    public /*out*/ readonly createTime!: pulumi.Output<string>;
    public readonly eipId!: pulumi.Output<string>;
    public readonly enableWhiteList!: pulumi.Output<boolean>;
    public readonly name!: pulumi.Output<string>;
    public readonly remark!: pulumi.Output<string>;
    public readonly securityGroup!: pulumi.Output<string>;
    public readonly subnetIds!: pulumi.Output<string[]>;
    public readonly tag!: pulumi.Output<string | undefined>;
    public readonly vpcId!: pulumi.Output<string>;
    public readonly whiteLists!: pulumi.Output<string[] | undefined>;

    /**
     * Create a NatGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NatGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NatGatewayArgs | NatGatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NatGatewayState | undefined;
            inputs["createTime"] = state ? state.createTime : undefined;
            inputs["eipId"] = state ? state.eipId : undefined;
            inputs["enableWhiteList"] = state ? state.enableWhiteList : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["remark"] = state ? state.remark : undefined;
            inputs["securityGroup"] = state ? state.securityGroup : undefined;
            inputs["subnetIds"] = state ? state.subnetIds : undefined;
            inputs["tag"] = state ? state.tag : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
            inputs["whiteLists"] = state ? state.whiteLists : undefined;
        } else {
            const args = argsOrState as NatGatewayArgs | undefined;
            if (!args || args.eipId === undefined) {
                throw new Error("Missing required property 'eipId'");
            }
            if (!args || args.enableWhiteList === undefined) {
                throw new Error("Missing required property 'enableWhiteList'");
            }
            if (!args || args.securityGroup === undefined) {
                throw new Error("Missing required property 'securityGroup'");
            }
            if (!args || args.subnetIds === undefined) {
                throw new Error("Missing required property 'subnetIds'");
            }
            if (!args || args.vpcId === undefined) {
                throw new Error("Missing required property 'vpcId'");
            }
            inputs["eipId"] = args ? args.eipId : undefined;
            inputs["enableWhiteList"] = args ? args.enableWhiteList : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["remark"] = args ? args.remark : undefined;
            inputs["securityGroup"] = args ? args.securityGroup : undefined;
            inputs["subnetIds"] = args ? args.subnetIds : undefined;
            inputs["tag"] = args ? args.tag : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
            inputs["whiteLists"] = args ? args.whiteLists : undefined;
            inputs["createTime"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(NatGateway.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NatGateway resources.
 */
export interface NatGatewayState {
    readonly createTime?: pulumi.Input<string>;
    readonly eipId?: pulumi.Input<string>;
    readonly enableWhiteList?: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly remark?: pulumi.Input<string>;
    readonly securityGroup?: pulumi.Input<string>;
    readonly subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
    readonly tag?: pulumi.Input<string>;
    readonly vpcId?: pulumi.Input<string>;
    readonly whiteLists?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a NatGateway resource.
 */
export interface NatGatewayArgs {
    readonly eipId: pulumi.Input<string>;
    readonly enableWhiteList: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly remark?: pulumi.Input<string>;
    readonly securityGroup: pulumi.Input<string>;
    readonly subnetIds: pulumi.Input<pulumi.Input<string>[]>;
    readonly tag?: pulumi.Input<string>;
    readonly vpcId: pulumi.Input<string>;
    readonly whiteLists?: pulumi.Input<pulumi.Input<string>[]>;
}