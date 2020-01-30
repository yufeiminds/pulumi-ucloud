// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

let __config = new pulumi.Config("ucloud");

/**
 * ...
 */
export let baseUrl: string | undefined = __config.get("baseUrl");
/**
 * ...
 */
export let insecure: boolean | undefined = __config.getObject<boolean>("insecure");
/**
 * ...
 */
export let maxRetries: number | undefined = __config.getObject<number>("maxRetries");
/**
 * ...
 */
export let privateKey: string | undefined = __config.get("privateKey") || utilities.getEnv("UCLOUD_PRIVATE_KEY", "UCloud Private Key");
/**
 * ...
 */
export let profile: string | undefined = __config.get("profile") || utilities.getEnv("UCLOUD_PROFILE", "UCloud Profile Name");
/**
 * ...
 */
export let projectId: string | undefined = __config.get("projectId") || utilities.getEnv("UCLOUD_PROJECT_ID", "UCloud Project Id");
/**
 * ...
 */
export let publicKey: string | undefined = __config.get("publicKey") || utilities.getEnv("UCLOUD_PUBLIC_KEY", "UCloud Public Key");
/**
 * ...
 */
export let region: string | undefined = __config.get("region") || utilities.getEnv("UCLOUD_REGION", "UCLOUD_DEFAULT_REGION");
/**
 * ...
 */
export let sharedCredentialsFile: string | undefined = __config.get("sharedCredentialsFile") || utilities.getEnv("UCLOUD_SHARED_CREDENTIAL_FILE", "Path To The Shared Credentials File");