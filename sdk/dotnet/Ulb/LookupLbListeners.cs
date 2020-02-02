// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ucloud.ulb
{
    public static partial class Invokes
    {
        /// <summary>
        /// This data source provides a list of Load Balancer Listener resources according to their Load Balancer Listener ID.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/d/lb_listeners.html.markdown.
        /// </summary>
        public static Task<LookupLbListenersResult> LookupLbListeners(LookupLbListenersArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<LookupLbListenersResult>("ucloud:ulb/lookupLbListeners:lookupLbListeners", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class LookupLbListenersArgs : Pulumi.InvokeArgs
    {
        [Input("ids")]
        private List<string>? _ids;

        /// <summary>
        /// A list of LB Listener IDs, all the LB Listeners belong to this region will be retrieved if the ID is `""`.
        /// </summary>
        public List<string> Ids
        {
            get => _ids ?? (_ids = new List<string>());
            set => _ids = value;
        }

        /// <summary>
        /// The ID of a load balancer.
        /// </summary>
        [Input("loadBalancerId", required: true)]
        public string LoadBalancerId { get; set; } = null!;

        /// <summary>
        /// A regex string to filter resulting lb listeners by name.
        /// </summary>
        [Input("nameRegex")]
        public string? NameRegex { get; set; }

        [Input("outputFile")]
        public string? OutputFile { get; set; }

        public LookupLbListenersArgs()
        {
        }
    }

    [OutputType]
    public sealed class LookupLbListenersResult
    {
        public readonly ImmutableArray<string> Ids;
        /// <summary>
        /// It is a nested type which documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.LookupLbListenersLbListenersResult> LbListeners;
        public readonly string LoadBalancerId;
        public readonly string? NameRegex;
        public readonly string? OutputFile;
        /// <summary>
        /// Total number of LB listeners that satisfy the condition.
        /// </summary>
        public readonly int TotalCount;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private LookupLbListenersResult(
            ImmutableArray<string> ids,
            ImmutableArray<Outputs.LookupLbListenersLbListenersResult> lbListeners,
            string loadBalancerId,
            string? nameRegex,
            string? outputFile,
            int totalCount,
            string id)
        {
            Ids = ids;
            LbListeners = lbListeners;
            LoadBalancerId = loadBalancerId;
            NameRegex = nameRegex;
            OutputFile = outputFile;
            TotalCount = totalCount;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class LookupLbListenersLbListenersResult
    {
        /// <summary>
        /// Health check domain checking.
        /// </summary>
        public readonly string Domain;
        /// <summary>
        /// Health check method. Possible values are `port` as port checking and `path` as http checking.
        /// </summary>
        public readonly string HealthCheckType;
        /// <summary>
        /// The ID of LB Listener.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Amount of time in seconds to wait for the response for in between two sessions if `listen_type` is `request_proxy`, range: 0-86400. Amount of time in seconds to wait for one session if `listen_type` is `packets_transmit`, range: 60-900. The session will be closed as soon as no response if it is `0`.
        /// </summary>
        public readonly int IdleTimeout;
        /// <summary>
        /// The type of LB Listener. Possible values are `request_proxy` and `packets_transmit`.
        /// </summary>
        public readonly string ListenType;
        /// <summary>
        /// The load balancer method in which the listener is. Possible values are: `roundrobin`, `source`, `consistent_hash`, `source_port` , `consistent_hash_port`, `weight_roundrobin` and `leastconn`. 
        /// - The `consistent_hash`, `source_port` , `consistent_hash_port`, `roundrobin`, `source` and `weight_roundrobin` are valid if `listen_type` is `packets_transmit`.
        /// - The `rundrobin`, `source` and `weight_roundrobin` and `leastconn` are vaild if `listen_type` is `request_proxy`.
        /// </summary>
        public readonly string Method;
        /// <summary>
        /// The name of LB Listener.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Health check path checking.
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// Indicate whether the persistence session is enabled, it is invaild if `persistence_type` is `none`, an auto-generated string will be exported if `persistence_type` is `server_insert`, a custom string will be exported if `persistence_type` is `user_defined`.
        /// </summary>
        public readonly string Persistence;
        /// <summary>
        /// The type of session persistence of LB Listener. Possible values are: `none` as disabled, `server_insert` as auto-generated string and `user_defined` as cutom string. (Default: `none`).
        /// </summary>
        public readonly string PersistenceType;
        /// <summary>
        /// Port opened on the LB Listener to receive requests, range: 1-65535.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// LB Listener protocol. Possible values: `http`, `https` if `listen_type` is `request_proxy`, `tcp` and `udp` if `listen_type` is `packets_transmit`.
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// LB Listener status. Possible values are: `allNormal` for all resource functioning well, `partNormal` for partial resource functioning well and `allException` for all resource functioning exceptional.
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private LookupLbListenersLbListenersResult(
            string domain,
            string healthCheckType,
            string id,
            int idleTimeout,
            string listenType,
            string method,
            string name,
            string path,
            string persistence,
            string persistenceType,
            int port,
            string protocol,
            string status)
        {
            Domain = domain;
            HealthCheckType = healthCheckType;
            Id = id;
            IdleTimeout = idleTimeout;
            ListenType = listenType;
            Method = method;
            Name = name;
            Path = path;
            Persistence = persistence;
            PersistenceType = persistenceType;
            Port = port;
            Protocol = protocol;
            Status = status;
        }
    }
    }
}