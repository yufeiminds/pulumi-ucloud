# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class UdpnConnection(pulumi.CustomResource):
    bandwidth: pulumi.Output[float]
    """
    Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). range from 2 - 1000M. The default value is "1"
    """
    charge_type: pulumi.Output[str]
    """
    Charge type. Possible values are: "year" as pay by year, "month" as pay by month, "dynamic" as pay by hour. The default value is "month".
    """
    create_time: pulumi.Output[str]
    """
    The time of creation for UDPN connection, formatted by RFC3339 time string.
    """
    duration: pulumi.Output[float]
    """
    The duration that you will buy the resource, the default value is "1". It is not required when "dynamic" (pay by hour), the value is "0" when pay by month and the instance will be valid till the last day of that month.
    """
    expire_time: pulumi.Output[str]
    """
    The expiration time for UDPN connection, formatted by RFC3339 time string.
    """
    peer_region: pulumi.Output[str]
    """
    The correspondent region of dedicated connection, please refer to the region and [availability zone list](https://docs.ucloud.cn/api/summary/regionlist) and [UDPN price list](https://docs.ucloud.cn/network/udpn/udpn_price).
    """
    def __init__(__self__, resource_name, opts=None, bandwidth=None, charge_type=None, duration=None, peer_region=None, __props__=None, __name__=None, __opts__=None):
        """
        UDPN (UCloud Dedicated Private Network)，you can use Dedicated Private Network to achieve high-speed, stable, secure, and dedicated communications between different data centers. The most frequent scenario is to create network connection of clusters across regions.
        
        > **VPC Peering Connections with UDPN Connection** The cross-region Dedicated Private Network must be established if the two VPCs located in different regions are expected to be connected.
        
        > **Note** The additional packet head will be added and included in the overall length of packet due to the tunneling UDPN adopted. Since the number of the bytes of packet head is fixed, the bigger data packet is, the less usage will be taken for the packet head.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] bandwidth: Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). range from 2 - 1000M. The default value is "1"
        :param pulumi.Input[str] charge_type: Charge type. Possible values are: "year" as pay by year, "month" as pay by month, "dynamic" as pay by hour. The default value is "month".
        :param pulumi.Input[float] duration: The duration that you will buy the resource, the default value is "1". It is not required when "dynamic" (pay by hour), the value is "0" when pay by month and the instance will be valid till the last day of that month.
        :param pulumi.Input[str] peer_region: The correspondent region of dedicated connection, please refer to the region and [availability zone list](https://docs.ucloud.cn/api/summary/regionlist) and [UDPN price list](https://docs.ucloud.cn/network/udpn/udpn_price).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/udpn_connection.html.markdown.
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

            __props__['bandwidth'] = bandwidth
            __props__['charge_type'] = charge_type
            __props__['duration'] = duration
            if peer_region is None:
                raise TypeError("Missing required property 'peer_region'")
            __props__['peer_region'] = peer_region
            __props__['create_time'] = None
            __props__['expire_time'] = None
        super(UdpnConnection, __self__).__init__(
            'ucloud:udpn/udpnConnection:UdpnConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, bandwidth=None, charge_type=None, create_time=None, duration=None, expire_time=None, peer_region=None):
        """
        Get an existing UdpnConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] bandwidth: Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). range from 2 - 1000M. The default value is "1"
        :param pulumi.Input[str] charge_type: Charge type. Possible values are: "year" as pay by year, "month" as pay by month, "dynamic" as pay by hour. The default value is "month".
        :param pulumi.Input[str] create_time: The time of creation for UDPN connection, formatted by RFC3339 time string.
        :param pulumi.Input[float] duration: The duration that you will buy the resource, the default value is "1". It is not required when "dynamic" (pay by hour), the value is "0" when pay by month and the instance will be valid till the last day of that month.
        :param pulumi.Input[str] expire_time: The expiration time for UDPN connection, formatted by RFC3339 time string.
        :param pulumi.Input[str] peer_region: The correspondent region of dedicated connection, please refer to the region and [availability zone list](https://docs.ucloud.cn/api/summary/regionlist) and [UDPN price list](https://docs.ucloud.cn/network/udpn/udpn_price).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/udpn_connection.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["bandwidth"] = bandwidth
        __props__["charge_type"] = charge_type
        __props__["create_time"] = create_time
        __props__["duration"] = duration
        __props__["expire_time"] = expire_time
        __props__["peer_region"] = peer_region
        return UdpnConnection(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

