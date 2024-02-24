import pulumi
import pulumi_azure_native.resources as resources
import pulumi_azure_native.desktopvirtualization as desktopvirtualization

# Create a new resource group
resource_group = resources.ResourceGroup("resourceGroup")

# Create a new Host Pool for the Azure Virtual Desktop
host_pool = desktopvirtualization.HostPool("hostPool",
    host_pool_type="Pooled", # or "Personal"
    load_balancer_type="BreadthFirst", # or "DepthFirst" or "Persistent"
    location=resource_group.location,
    resource_group_name=resource_group.name,
    # Additional properties like description, friendly_name, etc.
    # can be set here as needed
)

# Create a new Application Group
app_group = desktopvirtualization.ApplicationGroup("appGroup",
    location=resource_group.location,
    resource_group_name=resource_group.name,
    host_pool_arm_path=host_pool.id,
    application_group_type="Desktop", # or "RemoteApp"
    # Set additional properties as needed
)

# Create a new Workspace for the Azure Virtual Desktop
workspace = desktopvirtualization.Workspace("workspace",
    location=resource_group.location,
    resource_group_name=resource_group.name,
    application_group_references=[app_group.id],
    # Additional properties like description, friendly_name, etc.
    # can be set here as needed
)

# Export the primary keys of the resources
pulumi.export('resource_group_id', resource_group.id)
pulumi.export('host_pool_id', host_pool.id)
pulumi.export('app_group_id', app_group.id)
pulumi.export('workspace_id', workspace.id)