// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vpc

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an VPC Peering Connection for establishing a connection between multiple VPC.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/vpc_peering_connection.html.markdown.
type VpcPeeringConnection struct {
	s *pulumi.ResourceState
}

// NewVpcPeeringConnection registers a new resource with the given unique name, arguments, and options.
func NewVpcPeeringConnection(ctx *pulumi.Context,
	name string, args *VpcPeeringConnectionArgs, opts ...pulumi.ResourceOpt) (*VpcPeeringConnection, error) {
	if args == nil || args.PeerVpcId == nil {
		return nil, errors.New("missing required argument 'PeerVpcId'")
	}
	if args == nil || args.VpcId == nil {
		return nil, errors.New("missing required argument 'VpcId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["peerProjectId"] = nil
		inputs["peerVpcId"] = nil
		inputs["vpcId"] = nil
	} else {
		inputs["peerProjectId"] = args.PeerProjectId
		inputs["peerVpcId"] = args.PeerVpcId
		inputs["vpcId"] = args.VpcId
	}
	s, err := ctx.RegisterResource("ucloud:vpc/vpcPeeringConnection:VpcPeeringConnection", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VpcPeeringConnection{s: s}, nil
}

// GetVpcPeeringConnection gets an existing VpcPeeringConnection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcPeeringConnection(ctx *pulumi.Context,
	name string, id pulumi.ID, state *VpcPeeringConnectionState, opts ...pulumi.ResourceOpt) (*VpcPeeringConnection, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["peerProjectId"] = state.PeerProjectId
		inputs["peerVpcId"] = state.PeerVpcId
		inputs["vpcId"] = state.VpcId
	}
	s, err := ctx.ReadResource("ucloud:vpc/vpcPeeringConnection:VpcPeeringConnection", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VpcPeeringConnection{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *VpcPeeringConnection) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *VpcPeeringConnection) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ID of accepter project of the specific VPC Peering Connection to retrieve.
func (r *VpcPeeringConnection) PeerProjectId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["peerProjectId"])
}

// The short ID of accepter VPC of the specific VPC Peering Connection to retrieve.
func (r *VpcPeeringConnection) PeerVpcId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["peerVpcId"])
}

// The short of ID of the requester VPC of the specific VPC Peering Connection to retrieve.
func (r *VpcPeeringConnection) VpcId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["vpcId"])
}

// Input properties used for looking up and filtering VpcPeeringConnection resources.
type VpcPeeringConnectionState struct {
	// The ID of accepter project of the specific VPC Peering Connection to retrieve.
	PeerProjectId interface{}
	// The short ID of accepter VPC of the specific VPC Peering Connection to retrieve.
	PeerVpcId interface{}
	// The short of ID of the requester VPC of the specific VPC Peering Connection to retrieve.
	VpcId interface{}
}

// The set of arguments for constructing a VpcPeeringConnection resource.
type VpcPeeringConnectionArgs struct {
	// The ID of accepter project of the specific VPC Peering Connection to retrieve.
	PeerProjectId interface{}
	// The short ID of accepter VPC of the specific VPC Peering Connection to retrieve.
	PeerVpcId interface{}
	// The short of ID of the requester VPC of the specific VPC Peering Connection to retrieve.
	VpcId interface{}
}
