import pulumi
import pulumi_azure_native as azure_native

# Set up of a Host Pool for Azure Virtual Desktop
host_pool = azure_native.desktopvirtualization.HostPool(
    "hostPool",
    host_pool_name="hostpool1",
    resource_group_name="resourcegroup1",
    friendly_name="hostpool1",
    description="Host Pool for Azure Virtual Desktop",
    host_pool_type=azure_native.desktopvirtualization.HostPoolType.Pooled,  # Can be Pooled or Personal
    load_balancer_type=azure_native.desktopvirtualization.LoadBalancerType.BreadthFirst,  # Can be BreadthFirst or DepthFirst
    location="East US",
    max_session_limit=10,
    vm_template="vmTemplate",
    start_v_m_on_connect=True,
    personal_desktop_assignment_type=azure_native.desktopvirtualization.PersonalDesktopAssignmentType.Automatic
    # You can add more properties as needed.
)

# Set up of a Workspace for Azure Virtual Desktop
workspace = azure_native.desktopvirtualization.Workspace(
    "workspace",
    workspace_name="workspace1",
    resource_group_name="resourcegroup1",
    friendly_name="workspace1",
    description="Workspace for Azure Virtual Desktop",
    application_group_references=[host_pool.id],
    location="East US",
    # You can add more properties as needed.
)

# Exporting the Host Pool id and Workspace id
pulumi.export("hostPoolId", host_pool.id)
pulumi.export("workspaceId", workspace.id)