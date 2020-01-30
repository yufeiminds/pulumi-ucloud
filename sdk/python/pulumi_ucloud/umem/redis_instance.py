# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class RedisInstance(pulumi.CustomResource):
    availability_zone: pulumi.Output[str]
    """
    Availability zone where Redis instance is located. Such as: "cn-bj2-02". You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist)
    """
    charge_type: pulumi.Output[str]
    """
    The charge type of Redis instance, possible values are: `year`, `month` and `dynamic` as pay by hour (specific permission required). (Default: `month`).
    """
    create_time: pulumi.Output[str]
    """
    The creation time of Redis instance, formatted by RFC3339 time string.
    """
    duration: pulumi.Output[float]
    """
    The duration that you will buy the Redis instance (Default: `1`). The value is `0` when pay by month and the instance will be valid till the last day of that month. It is not required when `dynamic` (pay by hour).
    """
    engine_version: pulumi.Output[str]
    """
    The version of engine of active-standby Redis. Possible values are: 3.0, 3.2 and 4.0.
    """
    expire_time: pulumi.Output[str]
    """
    The expiration time of Redis instance, formatted by RFC3339 time string.
    """
    instance_type: pulumi.Output[str]
    ip_sets: pulumi.Output[list]
    """
    ip_set is a nested type. ip_set documented below.
    
      * `ip` (`str`) - The virtual ip of Redis instance.
      * `port` (`float`) - The port on which Redis instance accepts connections, it is 6379 by default.
    """
    name: pulumi.Output[str]
    password: pulumi.Output[str]
    """
    The password for  active-standby Redis instance which should have 6-36 characters. It must contain at least 3 items of Capital letters, small letter, numbers and special characters. The special characters include `-_`. 
    """
    status: pulumi.Output[str]
    """
    The status of KV Redis instance.
    """
    subnet_id: pulumi.Output[str]
    """
    The ID of subnet linked to the Redis instance.
    """
    tag: pulumi.Output[str]
    """
    A tag assigned to Redis instance, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).
    """
    vpc_id: pulumi.Output[str]
    """
    The ID of VPC linked to the Redis instance.
    """
    def __init__(__self__, resource_name, opts=None, availability_zone=None, charge_type=None, duration=None, engine_version=None, instance_type=None, name=None, password=None, subnet_id=None, tag=None, vpc_id=None, __props__=None, __name__=None, __opts__=None):
        """
        The UCloud Redis instance is a key-value online storage service compatible with the Redis protocol.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: Availability zone where Redis instance is located. Such as: "cn-bj2-02". You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist)
        :param pulumi.Input[str] charge_type: The charge type of Redis instance, possible values are: `year`, `month` and `dynamic` as pay by hour (specific permission required). (Default: `month`).
        :param pulumi.Input[float] duration: The duration that you will buy the Redis instance (Default: `1`). The value is `0` when pay by month and the instance will be valid till the last day of that month. It is not required when `dynamic` (pay by hour).
        :param pulumi.Input[str] engine_version: The version of engine of active-standby Redis. Possible values are: 3.0, 3.2 and 4.0.
        :param pulumi.Input[str] password: The password for  active-standby Redis instance which should have 6-36 characters. It must contain at least 3 items of Capital letters, small letter, numbers and special characters. The special characters include `-_`. 
        :param pulumi.Input[str] subnet_id: The ID of subnet linked to the Redis instance.
        :param pulumi.Input[str] tag: A tag assigned to Redis instance, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).
        :param pulumi.Input[str] vpc_id: The ID of VPC linked to the Redis instance.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/redis_instance.html.markdown.
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

            if availability_zone is None:
                raise TypeError("Missing required property 'availability_zone'")
            __props__['availability_zone'] = availability_zone
            __props__['charge_type'] = charge_type
            __props__['duration'] = duration
            __props__['engine_version'] = engine_version
            if instance_type is None:
                raise TypeError("Missing required property 'instance_type'")
            __props__['instance_type'] = instance_type
            __props__['name'] = name
            __props__['password'] = password
            __props__['subnet_id'] = subnet_id
            __props__['tag'] = tag
            __props__['vpc_id'] = vpc_id
            __props__['create_time'] = None
            __props__['expire_time'] = None
            __props__['ip_sets'] = None
            __props__['status'] = None
        super(RedisInstance, __self__).__init__(
            'ucloud:umem/redisInstance:RedisInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, availability_zone=None, charge_type=None, create_time=None, duration=None, engine_version=None, expire_time=None, instance_type=None, ip_sets=None, name=None, password=None, status=None, subnet_id=None, tag=None, vpc_id=None):
        """
        Get an existing RedisInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: Availability zone where Redis instance is located. Such as: "cn-bj2-02". You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist)
        :param pulumi.Input[str] charge_type: The charge type of Redis instance, possible values are: `year`, `month` and `dynamic` as pay by hour (specific permission required). (Default: `month`).
        :param pulumi.Input[str] create_time: The creation time of Redis instance, formatted by RFC3339 time string.
        :param pulumi.Input[float] duration: The duration that you will buy the Redis instance (Default: `1`). The value is `0` when pay by month and the instance will be valid till the last day of that month. It is not required when `dynamic` (pay by hour).
        :param pulumi.Input[str] engine_version: The version of engine of active-standby Redis. Possible values are: 3.0, 3.2 and 4.0.
        :param pulumi.Input[str] expire_time: The expiration time of Redis instance, formatted by RFC3339 time string.
        :param pulumi.Input[list] ip_sets: ip_set is a nested type. ip_set documented below.
        :param pulumi.Input[str] password: The password for  active-standby Redis instance which should have 6-36 characters. It must contain at least 3 items of Capital letters, small letter, numbers and special characters. The special characters include `-_`. 
        :param pulumi.Input[str] status: The status of KV Redis instance.
        :param pulumi.Input[str] subnet_id: The ID of subnet linked to the Redis instance.
        :param pulumi.Input[str] tag: A tag assigned to Redis instance, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).
        :param pulumi.Input[str] vpc_id: The ID of VPC linked to the Redis instance.
        
        The **ip_sets** object supports the following:
        
          * `ip` (`pulumi.Input[str]`) - The virtual ip of Redis instance.
          * `port` (`pulumi.Input[float]`) - The port on which Redis instance accepts connections, it is 6379 by default.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/redis_instance.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["availability_zone"] = availability_zone
        __props__["charge_type"] = charge_type
        __props__["create_time"] = create_time
        __props__["duration"] = duration
        __props__["engine_version"] = engine_version
        __props__["expire_time"] = expire_time
        __props__["instance_type"] = instance_type
        __props__["ip_sets"] = ip_sets
        __props__["name"] = name
        __props__["password"] = password
        __props__["status"] = status
        __props__["subnet_id"] = subnet_id
        __props__["tag"] = tag
        __props__["vpc_id"] = vpc_id
        return RedisInstance(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

