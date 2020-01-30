// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vpc

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a VPC resource.
//
// > **Note**  The network segment can only be created or deleted, can not perform both of them at the same time.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/r/vpc.html.markdown.
type Vpc struct {
	s *pulumi.ResourceState
}

// NewVpc registers a new resource with the given unique name, arguments, and options.
func NewVpc(ctx *pulumi.Context,
	name string, args *VpcArgs, opts ...pulumi.ResourceOpt) (*Vpc, error) {
	if args == nil || args.CidrBlocks == nil {
		return nil, errors.New("missing required argument 'CidrBlocks'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["cidrBlocks"] = nil
		inputs["name"] = nil
		inputs["remark"] = nil
		inputs["tag"] = nil
	} else {
		inputs["cidrBlocks"] = args.CidrBlocks
		inputs["name"] = args.Name
		inputs["remark"] = args.Remark
		inputs["tag"] = args.Tag
	}
	inputs["createTime"] = nil
	inputs["networkInfos"] = nil
	inputs["updateTime"] = nil
	s, err := ctx.RegisterResource("ucloud:vpc/vpc:Vpc", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Vpc{s: s}, nil
}

// GetVpc gets an existing Vpc resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpc(ctx *pulumi.Context,
	name string, id pulumi.ID, state *VpcState, opts ...pulumi.ResourceOpt) (*Vpc, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["cidrBlocks"] = state.CidrBlocks
		inputs["createTime"] = state.CreateTime
		inputs["name"] = state.Name
		inputs["networkInfos"] = state.NetworkInfos
		inputs["remark"] = state.Remark
		inputs["tag"] = state.Tag
		inputs["updateTime"] = state.UpdateTime
	}
	s, err := ctx.ReadResource("ucloud:vpc/vpc:Vpc", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Vpc{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Vpc) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Vpc) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The CIDR blocks of VPC.
func (r *Vpc) CidrBlocks() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["cidrBlocks"])
}

// The time of creation for VPC, formatted in RFC3339 time string.
func (r *Vpc) CreateTime() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["createTime"])
}

func (r *Vpc) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// It is a nested type which documented below.
func (r *Vpc) NetworkInfos() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["networkInfos"])
}

// The remarks of the VPC. (Default: `""`).
func (r *Vpc) Remark() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["remark"])
}

// A tag assigned to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).
func (r *Vpc) Tag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tag"])
}

// The time whenever there is a change made to VPC, formatted in RFC3339 time string.
func (r *Vpc) UpdateTime() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["updateTime"])
}

// Input properties used for looking up and filtering Vpc resources.
type VpcState struct {
	// The CIDR blocks of VPC.
	CidrBlocks interface{}
	// The time of creation for VPC, formatted in RFC3339 time string.
	CreateTime interface{}
	Name       interface{}
	// It is a nested type which documented below.
	NetworkInfos interface{}
	// The remarks of the VPC. (Default: `""`).
	Remark interface{}
	// A tag assigned to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).
	Tag interface{}
	// The time whenever there is a change made to VPC, formatted in RFC3339 time string.
	UpdateTime interface{}
}

// The set of arguments for constructing a Vpc resource.
type VpcArgs struct {
	// The CIDR blocks of VPC.
	CidrBlocks interface{}
	Name       interface{}
	// The remarks of the VPC. (Default: `""`).
	Remark interface{}
	// A tag assigned to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).
	Tag interface{}
}
