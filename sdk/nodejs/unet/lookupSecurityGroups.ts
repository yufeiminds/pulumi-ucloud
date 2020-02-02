// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function lookupSecurityGroups(args?: LookupSecurityGroupsArgs, opts?: pulumi.InvokeOptions): Promise<LookupSecurityGroupsResult> & LookupSecurityGroupsResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<LookupSecurityGroupsResult> = pulumi.runtime.invoke("ucloud:unet/lookupSecurityGroups:lookupSecurityGroups", {
        "ids": args.ids,
        "nameRegex": args.nameRegex,
        "outputFile": args.outputFile,
        "type": args.type,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking lookupSecurityGroups.
 */
export interface LookupSecurityGroupsArgs {
    readonly ids?: string[];
    readonly nameRegex?: string;
    readonly outputFile?: string;
    readonly type?: string;
}

/**
 * A collection of values returned by lookupSecurityGroups.
 */
export interface LookupSecurityGroupsResult {
    readonly ids?: string[];
    readonly nameRegex?: string;
    readonly outputFile?: string;
    readonly securityGroups: outputs.unet.LookupSecurityGroupsSecurityGroup[];
    readonly totalCount: number;
    readonly type?: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}