# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class EipAssociation(pulumi.CustomResource):
    eip_id: pulumi.Output[str]
    """
    The ID of EIP.
    """
    resource_id: pulumi.Output[str]
    """
    The ID of resource with EIP attached.
    """
    resource_type: pulumi.Output[str]
    """
    **Deprecated**, attribute `resource_type` is deprecated for optimizing parameters.
    """
    def __init__(__self__, resource_name, opts=None, eip_id=None, resource_id=None, resource_type=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an EIP Association resource for associating Elastic IP to UHost Instance, Load Balancer, etc.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] eip_id: The ID of EIP.
        :param pulumi.Input[str] resource_id: The ID of resource with EIP attached.
        :param pulumi.Input[str] resource_type: **Deprecated**, attribute `resource_type` is deprecated for optimizing parameters.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/eip_association.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if eip_id is None:
                raise TypeError("Missing required property 'eip_id'")
            __props__['eip_id'] = eip_id
            if resource_id is None:
                raise TypeError("Missing required property 'resource_id'")
            __props__['resource_id'] = resource_id
            __props__['resource_type'] = resource_type
        super(EipAssociation, __self__).__init__(
            'ucloud:unet/eipAssociation:EipAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, eip_id=None, resource_id=None, resource_type=None):
        """
        Get an existing EipAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] eip_id: The ID of EIP.
        :param pulumi.Input[str] resource_id: The ID of resource with EIP attached.
        :param pulumi.Input[str] resource_type: **Deprecated**, attribute `resource_type` is deprecated for optimizing parameters.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/eip_association.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["eip_id"] = eip_id
        __props__["resource_id"] = resource_id
        __props__["resource_type"] = resource_type
        return EipAssociation(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

