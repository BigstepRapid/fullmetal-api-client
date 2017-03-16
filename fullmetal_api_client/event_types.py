"""
* BSI, API v100.1"""
class BSI_EventTypes(object):

	AUTHENTICATOR_ENABLED_NEW=251
	AUTHENTICATOR_REMOVED=252
	CLEANING_RESERVED_SERVERS_FINISHED=197
	CLEANING_RESERVED_SERVERS_STARTED=196
	CLUSTER_AUTOMATIC_MANAGEMENT_STATUS_SET=264
	CLUSTER_CREATED=153
	CLUSTER_DELETED=156
	CLUSTER_DEPLOY_STARTED=158
	CLUSTER_DEPLOYED=157
	CLUSTER_EDITED=154
	CLUSTER_PASSWORD_CHANGED=263
	CLUSTER_SOFTWARE_VERSION_AUTOMATIC_UPDATE=249
	CLUSTER_STARTED=171
	CLUSTER_STOPPED=155
	CLUSTER_SUSPENDED=206
	CLUSTERS_SAAS_LINKING_FINISHED=239
	CLUSTERS_SAAS_LINKING_STARTED=240
	CLUSTERS_SAAS_SETUP_FINISHED=195
	CLUSTERS_SAAS_SETUP_STARTED=194
	CONTAINER_ARRAY_CREATED=215
	CONTAINER_ARRAY_DELETED=220
	CONTAINER_ARRAY_DEPLOY_STARTED=221
	CONTAINER_ARRAY_DEPLOYED=222
	CONTAINER_ARRAY_EDITED=223
	CONTAINER_ARRAY_INTERFACE_CREATED=216
	CONTAINER_ARRAY_INTERFACE_DELETED=227
	CONTAINER_ARRAY_INTERFACE_DEPLOY_STARTED=231
	CONTAINER_ARRAY_INTERFACE_DEPLOYED=232
	CONTAINER_ARRAY_INTERFACE_EDITED=217
	CONTAINER_ARRAY_INTERFACE_STARTED=228
	CONTAINER_ARRAY_INTERFACE_STOPPED=229
	CONTAINER_ARRAY_INTERFACE_SUSPENDED=230
	CONTAINER_ARRAY_NOT_CONNECTED_TO_WAN=250
	CONTAINER_ARRAY_STARTED=224
	CONTAINER_ARRAY_STOPPED=225
	CONTAINER_ARRAY_SUSPENDED=226
	CONTAINER_CLUSTER_AUTOMATIC_MANAGEMENT_STATUS_SET=265
	CONTAINER_CLUSTER_CREATED=254
	CONTAINER_CLUSTER_DELETED=255
	CONTAINER_CLUSTER_DEPLOY_STARTED=256
	CONTAINER_CLUSTER_DEPLOYED=257
	CONTAINER_CLUSTER_EDITED=258
	CONTAINER_CLUSTER_SOFTWARE_VERSION_AUTOMATIC_UPDATE=266
	CONTAINER_CLUSTER_STARTED=259
	CONTAINER_CLUSTER_STOPPED=260
	CONTAINER_CLUSTER_SUSPENDED=261
	CONTAINER_PLATFORM_CREATED=207
	CONTAINER_PLATFORM_DELETED=208
	CONTAINER_PLATFORM_DEPLOY_STARTED=209
	CONTAINER_PLATFORM_DEPLOYED=210
	CONTAINER_PLATFORM_EDITED=211
	CONTAINER_PLATFORM_STARTED=212
	CONTAINER_PLATFORM_STOPPED=213
	CONTAINER_PLATFORM_SUSPENDED=214
	DATA_LAKE_CREATED=186
	DATA_LAKE_DELETED=187
	DATA_LAKE_DEPLOY_STARTED=188
	DATA_LAKE_DEPLOYED=189
	DATA_LAKE_EDITED=190
	DATA_LAKE_STARTED=191
	DATA_LAKE_STOPPED=192
	DCHP_LEASE_CREATED=56
	DEBUG_GENERAL=54
	DRIVE_ARRAY_CREATED=121
	DRIVE_ARRAY_DELETED=123
	DRIVE_ARRAY_DEPLOY_STARTED=129
	DRIVE_ARRAY_DEPLOYED=124
	DRIVE_ARRAY_DRIVE_COUNT_ZERO=150
	DRIVE_ARRAY_EDITED=118
	DRIVE_ARRAY_STARTED=119
	DRIVE_ARRAY_STOPPED=120
	DRIVE_ATTACHED_INSTANCE=90
	DRIVE_CREATED=73
	DRIVE_DELETED=75
	DRIVE_DEPLOY_STARTED=130
	DRIVE_DEPLOYED=32
	DRIVE_DETACHED_INSTANCE=94
	DRIVE_EDITED=97
	DRIVE_FREE_SPACE_RUNNING_LOW=147
	DRIVE_ROLLED_BACK_TO_SNAPSHOT=185
	DRIVE_STARTED=115
	DRIVE_STOPPED=114
	EVENT_DELETED=270
	EVENTS_DELETED=271
	EVENTS_EXPIRED=272
	FIREWALL_RULES_DEPLOYED=238
	INFRASTRUCTURE_CREATED=76
	INFRASTRUCTURE_DELETED=152
	INFRASTRUCTURE_DEPLOY_OVERVIEW_CONSULTED=253
	INFRASTRUCTURE_DEPLOY_STARTED=127
	INFRASTRUCTURE_DEPLOYED=39
	INFRASTRUCTURE_DESIGN_LOCKED=262
	INFRASTRUCTURE_DESIGN_UNLOCKED=273
	INFRASTRUCTURE_EDITED=159
	INFRASTRUCTURE_STARTED=234
	INFRASTRUCTURE_STOPPED=233
	INFRASTRUCTURE_USER_ADDED=77
	INFRASTRUCTURE_USER_REMOVED=80
	INFRASTRUCTURE_USER_UPDATED=79
	INSTANCE_ARRAY_CREATED=61
	INSTANCE_ARRAY_DELETED=64
	INSTANCE_ARRAY_DEPLOY_STARTED=125
	INSTANCE_ARRAY_DEPLOYED=12
	INSTANCE_ARRAY_EDITED=65
	INSTANCE_ARRAY_INSTANCE_COUNT_ZERO=49
	INSTANCE_ARRAY_INTERFACE_CREATED=68
	INSTANCE_ARRAY_INTERFACE_DELETED=103
	INSTANCE_ARRAY_INTERFACE_DEPLOY_STARTED=126
	INSTANCE_ARRAY_INTERFACE_DEPLOYED=16
	INSTANCE_ARRAY_INTERFACE_EDITED=88
	INSTANCE_ARRAY_INTERFACE_STARTED=173
	INSTANCE_ARRAY_INTERFACE_STOPPED=160
	INSTANCE_ARRAY_INTERFACE_SUSPENDED=205
	INSTANCE_ARRAY_NOT_CONNECTED_TO_WAN=57
	INSTANCE_ARRAY_STARTED=99
	INSTANCE_ARRAY_STOPPED=98
	INSTANCE_ARRAY_SUSPENDED=198
	INSTANCE_ARRAY_UNSUSPENDED=201
	INSTANCE_CREATED=63
	INSTANCE_DELETED=66
	INSTANCE_DEPLOY_STARTED=132
	INSTANCE_DEPLOYED=8
	INSTANCE_EDITED=67
	INSTANCE_INTERFACE_CREATED=70
	INSTANCE_INTERFACE_DELETED=116
	INSTANCE_INTERFACE_DEPLOY_STARTED=133
	INSTANCE_INTERFACE_DEPLOYED=20
	INSTANCE_INTERFACE_EDITED=71
	INSTANCE_INTERFACE_STARTED=175
	INSTANCE_INTERFACE_STOPPED=102
	INSTANCE_INTERFACE_SUSPENDED=204
	INSTANCE_LICENSE_CREATED=243
	INSTANCE_LICENSE_DELETED=244
	INSTANCE_LICENSE_DEPLOY_STARTED=241
	INSTANCE_LICENSE_DEPLOYED=242
	INSTANCE_LICENSE_EDITED=248
	INSTANCE_LICENSE_STARTED=245
	INSTANCE_LICENSE_STOPPED=246
	INSTANCE_LICENSE_SUSPENDED=247
	INSTANCE_MIGHT_NOT_BE_BOOTABLE=236
	INSTANCE_NOT_BOOTABLE=47
	INSTANCE_PUBLIC_KEY_RETRIEVED=268
	INSTANCE_SERVER_POWER_STATUS_SET=267
	INSTANCE_SERVER_TYPE_RESERVATION_CREATED=269
	INSTANCE_STARTED=172
	INSTANCE_STOPPED=101
	INSTANCE_SUSPENDED=199
	INSTANCE_UNSUSPENDED=202
	INSTANCE_WITH_LOCAL_DISKS_MIGHT_NOT_BE_BOOTABLE=237
	IP_CREATED=168
	IP_DELETED=169
	IP_DEPLOY_STARTED=176
	IP_DEPLOYED=177
	IP_EDITED=193
	IP_STARTED=235
	IP_STOPPED=170
	NETWORK_CREATED=81
	NETWORK_DELETED=83
	NETWORK_DEPLOY_STARTED=131
	NETWORK_DEPLOYED=24
	NETWORK_EDITED=82
	NETWORK_EQUIPMENT_LAYER3_INTERFACE_CREATED=104
	NETWORK_PROVISION_DEBUG=95
	NETWORK_SETUP_FINISHED=135
	NETWORK_SETUP_STARTED=134
	NETWORK_STARTED=107
	NETWORK_STOPPED=106
	NETWORK_SUSPENDED=200
	NETWORK_UNSUSPENDED=203
	PRODUCT_CURRENT_OPERATION_CANCELLED=78
	REMOTE_CONSOLE_ACCESSED=274
	SERVER_ALLOCATED_TO_INSTANCE=117
	SERVER_REGISTERED=136
	SERVER_SWAPPED=151
	SHARED_DRIVE_CONNECTED_TO_INSTANCE_ARRAY=179
	SHARED_DRIVE_CREATED=161
	SHARED_DRIVE_DELETED=162
	SHARED_DRIVE_DEPLOY_STARTED=166
	SHARED_DRIVE_DEPLOYED=163
	SHARED_DRIVE_DISCONNECTED_FROM_INSTANCE_ARRAY=181
	SHARED_DRIVE_EDITED=164
	SHARED_DRIVE_STARTED=165
	SHARED_DRIVE_STOPPED=167
	SHARED_DRIVE_WILL_BE_CONNECTED_TO_INSTANCE_ARRAY=178
	SHARED_DRIVE_WILL_BE_DISCONNECTED_FROM_INSTANCE_ARRAY=180
	SNAPSHOT_CREATED=183
	SNAPSHOT_DELETED=184
	STORAGE_PROVISION_DEBUG=96
	SUBNET_CLEARED=105
	SUBNET_CREATED=85
	SUBNET_DELETED=86
	SUBNET_DEPLOY_STARTED=128
	SUBNET_DEPLOYED=28
	SUBNET_EDITED=84
	SUBNET_NEEDS_START=149
	SUBNET_STARTED=174
	SUBNET_STOPPED=100
	USER_API_KEY_REGENERATED=110
	USER_AUTHENTICATED_PASSWORD=109
	USER_CREATED=93
	USER_DELEGATE_ADDED=91
	USER_DELEGATE_REMOVED=92
	USER_JWT_SALT_REGENERATED=182
	USER_LOGIN_EMAIL_UPDATED_VERIFICATION_URL=108
	USER_PASSWORD_CHANGED=111
	USER_SSH_KEY_CREATED=59
	USER_SSH_KEY_DELETED=89
	USER_SUSPENDED=218
	USER_UNSUSPENDED=219

	dictEventTypes = {
		AUTHENTICATOR_ENABLED_NEW:{
			'title':'New authenticator enabled',
			'message':'An authenticator was added to the account or the existing one was replaced.',
			'severity':'security',
			'visibility':'public',
		},
		AUTHENTICATOR_REMOVED:{
			'title':'Authenticator removed',
			'message':'The authenticator was removed from the account.',
			'severity':'security',
			'visibility':'public',
		},
		CLEANING_RESERVED_SERVERS_FINISHED:{
			'title':'Reserved servers cleaning finished',
			'message':'',
			'severity':'success',
			'visibility':'public',
		},
		CLEANING_RESERVED_SERVERS_STARTED:{
			'title':'Reserved servers cleaning started',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTER_AUTOMATIC_MANAGEMENT_STATUS_SET:{
			'title':'Cluster automatic management status set',
			'message':'The Cluster automatic management setting has been changed. The corresponding Cluster object property has been updated.',
			'severity':'info',
			'visibility':'private',
		},
		CLUSTER_CREATED:{
			'title':'Cluster created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTER_DELETED:{
			'title':'Cluster deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTER_DEPLOY_STARTED:{
			'title':'Cluster deploy started',
			'message':'Deploy started for Cluster operation.',
			'severity':'info',
			'visibility':'private',
		},
		CLUSTER_DEPLOYED:{
			'title':'Cluster deployed',
			'message':'Deploy completed for Cluster operation.',
			'severity':'success',
			'visibility':'public',
		},
		CLUSTER_EDITED:{
			'title':'Cluster edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTER_PASSWORD_CHANGED:{
			'title':'Cluster password changed',
			'message':'The cluster password has been changed. The corresponding cluster object property has been updated.',
			'severity':'security',
			'visibility':'private',
		},
		CLUSTER_SOFTWARE_VERSION_AUTOMATIC_UPDATE:{
			'title':'Cluster software version updated',
			'message':'A new cluster software version was detected. The corresponding cluster object property has been automatically updated.',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTER_STARTED:{
			'title':'Cluster started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTER_STOPPED:{
			'title':'Cluster stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTER_SUSPENDED:{
			'title':'Cluster suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned. All active Drives will remain provisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTERS_SAAS_LINKING_FINISHED:{
			'title':'Finished Cluster SaaS linking',
			'message':'',
			'severity':'success',
			'visibility':'public',
		},
		CLUSTERS_SAAS_LINKING_STARTED:{
			'title':'Started Cluster SaaS linking',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		CLUSTERS_SAAS_SETUP_FINISHED:{
			'title':'Finished Cluster SaaS setup',
			'message':'',
			'severity':'success',
			'visibility':'public',
		},
		CLUSTERS_SAAS_SETUP_STARTED:{
			'title':'Started Cluster SaaS setup',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_ARRAY_CREATED:{
			'title':'ContainerArray created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_ARRAY_DELETED:{
			'title':'ContainerArray deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_ARRAY_DEPLOY_STARTED:{
			'title':'ContainerArray deploy started',
			'message':'Deploy started for ContainerArray operation.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_DEPLOYED:{
			'title':'ContainerArray deployed',
			'message':'Deploy completed for ContainerArray operation.',
			'severity':'success',
			'visibility':'public',
		},
		CONTAINER_ARRAY_EDITED:{
			'title':'ContainerArray edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_ARRAY_INTERFACE_CREATED:{
			'title':'ContainerArrayInterface created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_INTERFACE_DELETED:{
			'title':'ContainerArrayInterface deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_INTERFACE_DEPLOY_STARTED:{
			'title':'ContainerArrayInterface deploy started',
			'message':'Deploy started for ContainerArrayInterface operation.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_INTERFACE_DEPLOYED:{
			'title':'ContainerArrayInterface deployed',
			'message':'Deploy completed for ContainerArrayInterface operation.',
			'severity':'success',
			'visibility':'private',
		},
		CONTAINER_ARRAY_INTERFACE_EDITED:{
			'title':'ContainerArrayInterface edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_INTERFACE_STARTED:{
			'title':'ContainerArrayInterface started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_INTERFACE_STOPPED:{
			'title':'ContainerArrayInterface stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_INTERFACE_SUSPENDED:{
			'title':'ContainerArrayInterface suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_ARRAY_NOT_CONNECTED_TO_WAN:{
			'title':'ContainerArray not connected to WAN',
			'message':'ContainerArray is not connected to WAN Network',
			'severity':'warning',
			'visibility':'public',
		},
		CONTAINER_ARRAY_STARTED:{
			'title':'ContainerArray started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_ARRAY_STOPPED:{
			'title':'ContainerArray stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_ARRAY_SUSPENDED:{
			'title':'ContainerArray suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_AUTOMATIC_MANAGEMENT_STATUS_SET:{
			'title':'ContainerCluster automatic management status set',
			'message':'The ContainerCluster automatic management setting has been changed. The corresponding ContainerCluster object property has been updated.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_CLUSTER_CREATED:{
			'title':'ContainerCluster created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_DELETED:{
			'title':'ContainerCluster deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_DEPLOY_STARTED:{
			'title':'ContainerCluster deploy started',
			'message':'Deploy started for ContainerCluster operation.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_CLUSTER_DEPLOYED:{
			'title':'ContainerCluster deployed',
			'message':'Deploy completed for ContainerCluster operation.',
			'severity':'success',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_EDITED:{
			'title':'ContainerCluster edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_SOFTWARE_VERSION_AUTOMATIC_UPDATE:{
			'title':'ContainerCluster software version updated',
			'message':'A new ContainerCluster software version was detected. The corresponding cluster object property has been automatically updated.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_STARTED:{
			'title':'ContainerCluster started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_STOPPED:{
			'title':'ContainerCluster stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_CLUSTER_SUSPENDED:{
			'title':'ContainerCluster suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_PLATFORM_CREATED:{
			'title':'ContainerPlatform created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_PLATFORM_DELETED:{
			'title':'ContainerPlatform deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_PLATFORM_DEPLOY_STARTED:{
			'title':'ContainerPlatform deploy started',
			'message':'Deploy started for ContainerPlatform operation.',
			'severity':'info',
			'visibility':'private',
		},
		CONTAINER_PLATFORM_DEPLOYED:{
			'title':'ContainerPlatform deployed',
			'message':'Deploy completed for ContainerPlatform operation.',
			'severity':'success',
			'visibility':'public',
		},
		CONTAINER_PLATFORM_EDITED:{
			'title':'ContainerPlatform edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_PLATFORM_STARTED:{
			'title':'ContainerPlatform started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_PLATFORM_STOPPED:{
			'title':'ContainerPlatform stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		CONTAINER_PLATFORM_SUSPENDED:{
			'title':'ContainerPlatform suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned. Active storage will remain provisioned.',
			'severity':'info',
			'visibility':'public',
		},
		DATA_LAKE_CREATED:{
			'title':'DataLake created.',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		DATA_LAKE_DELETED:{
			'title':'DataLake deleted.',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		DATA_LAKE_DEPLOY_STARTED:{
			'title':'DataLake deploy started',
			'message':'Deploy started for Data Lake operation.',
			'severity':'info',
			'visibility':'private',
		},
		DATA_LAKE_DEPLOYED:{
			'title':'DataLake deployed.',
			'message':'Deploy completed for Data Lake operation.',
			'severity':'success',
			'visibility':'public',
		},
		DATA_LAKE_EDITED:{
			'title':'DataLake edited.',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		DATA_LAKE_STARTED:{
			'title':'DataLake started.',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		DATA_LAKE_STOPPED:{
			'title':'DataLake stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		DCHP_LEASE_CREATED:{
			'title':'DHCP lease created',
			'message':'A DHCP lease was successfully created.',
			'severity':'success',
			'visibility':'private',
		},
		DEBUG_GENERAL:{
			'title':'Debug General',
			'message':'',
			'severity':'debug',
			'visibility':'private',
		},
		DRIVE_ARRAY_CREATED:{
			'title':'DriveArray created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_ARRAY_DELETED:{
			'title':'DriveArray deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_ARRAY_DEPLOY_STARTED:{
			'title':'DriveArray deploy started',
			'message':'Deploy started for Drive array operation.',
			'severity':'info',
			'visibility':'private',
		},
		DRIVE_ARRAY_DEPLOYED:{
			'title':'DriveArray deployed',
			'message':'Deploy completed for DriveArray operation.',
			'severity':'success',
			'visibility':'public',
		},
		DRIVE_ARRAY_DRIVE_COUNT_ZERO:{
			'title':'DriveArray Drive count is zero',
			'message':'DriveArray is configured with zero Drives.',
			'severity':'warning',
			'visibility':'public',
		},
		DRIVE_ARRAY_EDITED:{
			'title':'DriveArray edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_ARRAY_STARTED:{
			'title':'DriveArray started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_ARRAY_STOPPED:{
			'title':'DriveArray stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_ATTACHED_INSTANCE:{
			'title':'Drive attached to Instance',
			'message':'A Drive has been successfully attached to an Instance.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_CREATED:{
			'title':'Drive created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_DELETED:{
			'title':'Drive deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_DEPLOY_STARTED:{
			'title':'Drive deploy started',
			'message':'Deploy started for Drive operation.',
			'severity':'info',
			'visibility':'private',
		},
		DRIVE_DEPLOYED:{
			'title':'Drive deployed',
			'message':'Deploy completed for Drive operation.',
			'severity':'success',
			'visibility':'public',
		},
		DRIVE_DETACHED_INSTANCE:{
			'title':'Drive detached from Instance',
			'message':'A Drive has been successfully detached from an instance.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_EDITED:{
			'title':'Drive edited.',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_FREE_SPACE_RUNNING_LOW:{
			'title':'Drive free space running low',
			'message':'Free space on the Drive is less than 10% of the total disk size.',
			'severity':'warning',
			'visibility':'public',
		},
		DRIVE_ROLLED_BACK_TO_SNAPSHOT:{
			'title':'Drive was rolled back to a snapshot',
			'message':'The drive was rolled back to a snapshot.',
			'severity':'important',
			'visibility':'public',
		},
		DRIVE_STARTED:{
			'title':'Drive started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		DRIVE_STOPPED:{
			'title':'Drive stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		EVENT_DELETED:{
			'title':'Event deleted',
			'message':'Event was deleted.',
			'severity':'info',
			'visibility':'private',
		},
		EVENTS_DELETED:{
			'title':'Events deleted',
			'message':'Events were deleted.',
			'severity':'info',
			'visibility':'public',
		},
		EVENTS_EXPIRED:{
			'title':'Events expired',
			'message':'Events have expired.',
			'severity':'info',
			'visibility':'private',
		},
		FIREWALL_RULES_DEPLOYED:{
			'title':'Firewall rules deployed',
			'message':'Firewall rules have been successfully deployed on all instances.',
			'severity':'success',
			'visibility':'public',
		},
		INFRASTRUCTURE_CREATED:{
			'title':'Infrastructure created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_DELETED:{
			'title':'Infrastructure deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_DEPLOY_OVERVIEW_CONSULTED:{
			'title':'Infrastructure deploy overview was consulted',
			'message':'A user has consulted the infrastructure deploy overview. Use the JSON context of this event to resolve disputes over whether the user was properly informed before hitting deploy. The INFRASTRUCTURE_DEPLOY_STARTED event contains a second overview result, from within the deploy transaction. 

If this event is missing before a deploy, it probably means the user deployed the operation using an API client.',
			'severity':'info',
			'visibility':'private',
		},
		INFRASTRUCTURE_DEPLOY_STARTED:{
			'title':'Infrastructure deploy started',
			'message':'The infrastructure deploy is starting.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_DEPLOYED:{
			'title':'Infrastructure deployed',
			'message':'Deploy completed for every operation on the specified infrastructure.',
			'severity':'success',
			'visibility':'public',
		},
		INFRASTRUCTURE_DESIGN_LOCKED:{
			'title':'Infrastructure design was locked',
			'message':'The infrastructure design was locked. No edits, reverts or deploys are allowed on the infrastructure.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_DESIGN_UNLOCKED:{
			'title':'Infrastructure design was unlocked',
			'message':'The infrastructure design was unlocked.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_EDITED:{
			'title':'Infrastructure edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_STARTED:{
			'title':'Infrastructure started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_STOPPED:{
			'title':'Infrastructure stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		INFRASTRUCTURE_USER_ADDED:{
			'title':'Infrastructure user added',
			'message':'A user has been granted administrative privileges over an infrastructure.',
			'severity':'security',
			'visibility':'public',
		},
		INFRASTRUCTURE_USER_REMOVED:{
			'title':'Infrastructure user removed',
			'message':'A user\'s administrative privileges over an infrastructure have been revoked.',
			'severity':'security',
			'visibility':'public',
		},
		INFRASTRUCTURE_USER_UPDATED:{
			'title':'Infrastructure user updated',
			'message':'A user\'s privileges or security settings concerning an infrastructure have been modified.',
			'severity':'security',
			'visibility':'public',
		},
		INSTANCE_ARRAY_CREATED:{
			'title':'InstanceArray created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_ARRAY_DELETED:{
			'title':'InstanceArray deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_ARRAY_DEPLOY_STARTED:{
			'title':'InstanceArray deploy started',
			'message':'Deploy started for InstanceArray operation.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_DEPLOYED:{
			'title':'InstanceArray deployed',
			'message':'Deploy completed for InstanceArray operation.',
			'severity':'success',
			'visibility':'public',
		},
		INSTANCE_ARRAY_EDITED:{
			'title':'InstanceArray edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_ARRAY_INSTANCE_COUNT_ZERO:{
			'title':'InstanceArray instance count is zero',
			'message':'InstanceArray is configured with zero instances.',
			'severity':'warning',
			'visibility':'public',
		},
		INSTANCE_ARRAY_INTERFACE_CREATED:{
			'title':'InstanceArrayInterface created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_INTERFACE_DELETED:{
			'title':'InstanceArrayInterface deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_INTERFACE_DEPLOY_STARTED:{
			'title':'InstanceArrayInterface deploy started',
			'message':'Deploy started for InstanceArrayInterface operation.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_INTERFACE_DEPLOYED:{
			'title':'InstanceArrayInterface deployed',
			'message':'Deploy completed for InstanceArrayInterface operation.',
			'severity':'success',
			'visibility':'private',
		},
		INSTANCE_ARRAY_INTERFACE_EDITED:{
			'title':'InstanceArrayInterface edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_ARRAY_INTERFACE_STARTED:{
			'title':'InstanceArrayInterface started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_INTERFACE_STOPPED:{
			'title':'InstanceArrayInterface stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_INTERFACE_SUSPENDED:{
			'title':'InstanceArrayInterface suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_NOT_CONNECTED_TO_WAN:{
			'title':'InstanceArray not connected to the WAN Network',
			'message':'The InstanceArray does not have direct internet connectivity.',
			'severity':'warning',
			'visibility':'public',
		},
		INSTANCE_ARRAY_STARTED:{
			'title':'InstanceArray started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_ARRAY_STOPPED:{
			'title':'InstanceArray stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_ARRAY_SUSPENDED:{
			'title':'InstanceArray suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_ARRAY_UNSUSPENDED:{
			'title':'InstanceArray unsuspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be provisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_CREATED:{
			'title':'Instance created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_DELETED:{
			'title':'Instance deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_DEPLOY_STARTED:{
			'title':'Instance deploy started',
			'message':'Deploy started for Instance operation.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_DEPLOYED:{
			'title':'Instance deployed',
			'message':'Deploy completed for instance operation.',
			'severity':'success',
			'visibility':'public',
		},
		INSTANCE_EDITED:{
			'title':'Instance edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_INTERFACE_CREATED:{
			'title':'InstanceInterface created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_INTERFACE_DELETED:{
			'title':'InstanceInterface deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_INTERFACE_DEPLOY_STARTED:{
			'title':'InstanceInterface deploy started',
			'message':'Deploy started for InstanceInterface operation.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_INTERFACE_DEPLOYED:{
			'title':'InstanceInterface deployed',
			'message':'Deploy completed for InstanceInterface operation.',
			'severity':'success',
			'visibility':'private',
		},
		INSTANCE_INTERFACE_EDITED:{
			'title':'InstanceInterface edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_INTERFACE_STARTED:{
			'title':'InstanceInterface started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_INTERFACE_STOPPED:{
			'title':'InstanceInterface stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_INTERFACE_SUSPENDED:{
			'title':'InstanceInterface suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_LICENSE_CREATED:{
			'title':'InstanceLicense created',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_LICENSE_DELETED:{
			'title':'InstanceLicense deleted',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_LICENSE_DEPLOY_STARTED:{
			'title':'InstanceLicense deploy started',
			'message':'',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_LICENSE_DEPLOYED:{
			'title':'InstanceLicense deployed',
			'message':'',
			'severity':'success',
			'visibility':'public',
		},
		INSTANCE_LICENSE_EDITED:{
			'title':'InstanceLicense edited',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_LICENSE_STARTED:{
			'title':'InstanceLicense started',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_LICENSE_STOPPED:{
			'title':'InstanceLicense stopped',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_LICENSE_SUSPENDED:{
			'title':'InstanceLicense suspended',
			'message':'',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_MIGHT_NOT_BE_BOOTABLE:{
			'title':'Instance might not be bootable',
			'message':'An Instance is not connected to any Drives that have an OS template installed.',
			'severity':'warning',
			'visibility':'public',
		},
		INSTANCE_NOT_BOOTABLE:{
			'title':'Instance not bootable',
			'message':'Instance will not be able to boot. An OS template must be selected for the attached drive in order for the server to be able to boot.',
			'severity':'warning',
			'visibility':'public',
		},
		INSTANCE_PUBLIC_KEY_RETRIEVED:{
			'title':'Instance public key retrieved',
			'message':'Public key for instance was retrieved.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_SERVER_POWER_STATUS_SET:{
			'title':'Instance server power status was set',
			'message':'Power status was changed for the server associated to provided instance.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_SERVER_TYPE_RESERVATION_CREATED:{
			'title':'Instance server type reservation was created.',
			'message':'A new server type reservation for the provided instance was created.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_STARTED:{
			'title':'Instance started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_STOPPED:{
			'title':'Instance stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		INSTANCE_SUSPENDED:{
			'title':'Instance suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_UNSUSPENDED:{
			'title':'Instance unsuspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be provisioned.',
			'severity':'info',
			'visibility':'private',
		},
		INSTANCE_WITH_LOCAL_DISKS_MIGHT_NOT_BE_BOOTABLE:{
			'title':'Instance might not be bootable',
			'message':'Instance might not be able to boot. An OS template must be selected for the attached Drive in order for the server to be able to boot.',
			'severity':'info',
			'visibility':'public',
		},
		IP_CREATED:{
			'title':'IP created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		IP_DELETED:{
			'title':'IP deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		IP_DEPLOY_STARTED:{
			'title':'IP deploy started',
			'message':'Deploy started for IP operation.',
			'severity':'info',
			'visibility':'private',
		},
		IP_DEPLOYED:{
			'title':'IP deployed',
			'message':'Deploy completed for IP operation.',
			'severity':'success',
			'visibility':'public',
		},
		IP_EDITED:{
			'title':'IP edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'private',
		},
		IP_STARTED:{
			'title':'IP started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'private',
		},
		IP_STOPPED:{
			'title':'IP stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'private',
		},
		NETWORK_CREATED:{
			'title':'Network created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		NETWORK_DELETED:{
			'title':'Network deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		NETWORK_DEPLOY_STARTED:{
			'title':'Network deploy started',
			'message':'Deploy started for network operation.',
			'severity':'info',
			'visibility':'private',
		},
		NETWORK_DEPLOYED:{
			'title':'Network deployed',
			'message':'Deploy completed for network operation.',
			'severity':'success',
			'visibility':'public',
		},
		NETWORK_EDITED:{
			'title':'Network edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		NETWORK_EQUIPMENT_LAYER3_INTERFACE_CREATED:{
			'title':'Network equipment layer 3 interface created',
			'message':'A network equipment interface has been created. This is usually a gateway on the switch, set as a secondary ip on the interface. The primary ip is usually a private class ip eg: 169.x.x.x',
			'severity':'info',
			'visibility':'private',
		},
		NETWORK_PROVISION_DEBUG:{
			'title':'Network provision debugging.',
			'message':'',
			'severity':'debug',
			'visibility':'private',
		},
		NETWORK_SETUP_FINISHED:{
			'title':'Network setup finished',
			'message':'Network devices finished configuring.',
			'severity':'success',
			'visibility':'public',
		},
		NETWORK_SETUP_STARTED:{
			'title':'Network setup started',
			'message':'Setting up network devices.',
			'severity':'info',
			'visibility':'public',
		},
		NETWORK_STARTED:{
			'title':'Network started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		NETWORK_STOPPED:{
			'title':'Network stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		NETWORK_SUSPENDED:{
			'title':'Network suspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'important',
			'visibility':'private',
		},
		NETWORK_UNSUSPENDED:{
			'title':'Network unsuspended',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be provisioned.',
			'severity':'important',
			'visibility':'private',
		},
		PRODUCT_CURRENT_OPERATION_CANCELLED:{
			'title':'Product current operation cancelled',
			'message':'A product\'s current operation has been successfully cancelled.',
			'severity':'info',
			'visibility':'private',
		},
		REMOTE_CONSOLE_ACCESSED:{
			'title':'Remote console accessed',
			'message':'Remote console was accessed.',
			'severity':'security',
			'visibility':'public',
		},
		SERVER_ALLOCATED_TO_INSTANCE:{
			'title':'Server allocated to instance',
			'message':'A server was allocated to an instance during provisioning.',
			'severity':'success',
			'visibility':'private',
		},
		SERVER_REGISTERED:{
			'title':'Server registered',
			'message':'A server has been registered.',
			'severity':'success',
			'visibility':'private',
		},
		SERVER_SWAPPED:{
			'title':'Server hot swap',
			'message':'A server was hot swapped.',
			'severity':'important',
			'visibility':'public',
		},
		SHARED_DRIVE_CONNECTED_TO_INSTANCE_ARRAY:{
			'title':'A SharedDrive was connected to an InstanceArray',
			'message':'A SharedDrive was connected to an InstanceArray.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_CREATED:{
			'title':'SharedDrive created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_DELETED:{
			'title':'SharedDrive deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_DEPLOY_STARTED:{
			'title':'SharedDrive deploy started',
			'message':'Deploy started for SharedDrive operation.',
			'severity':'info',
			'visibility':'private',
		},
		SHARED_DRIVE_DEPLOYED:{
			'title':'SharedDrive deployed',
			'message':'Deploy completed for SharedDrive operation.',
			'severity':'success',
			'visibility':'public',
		},
		SHARED_DRIVE_DISCONNECTED_FROM_INSTANCE_ARRAY:{
			'title':'A SharedDrive was disconnected from an InstanceArray',
			'message':'A SharedDrive was disconnected from an InstanceArray.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_EDITED:{
			'title':'SharedDrive edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_STARTED:{
			'title':'SharedDrive started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_STOPPED:{
			'title':'SharedDrive stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_WILL_BE_CONNECTED_TO_INSTANCE_ARRAY:{
			'title':'A SharedDrive will be connected to an InstanceArray',
			'message':'The SharedDrive will be connected to an InstanceArray.',
			'severity':'info',
			'visibility':'public',
		},
		SHARED_DRIVE_WILL_BE_DISCONNECTED_FROM_INSTANCE_ARRAY:{
			'title':'A SharedDrive will be disconnected from an InstanceArray',
			'message':'A SharedDrive will be disconnected from an InstanceArray.',
			'severity':'info',
			'visibility':'public',
		},
		SNAPSHOT_CREATED:{
			'title':'Snapshot created',
			'message':'A snapshot was created from a drive.',
			'severity':'success',
			'visibility':'public',
		},
		SNAPSHOT_DELETED:{
			'title':'Snapshot deleted',
			'message':'A snapshot was deleted.',
			'severity':'important',
			'visibility':'public',
		},
		STORAGE_PROVISION_DEBUG:{
			'title':'Storage provision debugging',
			'message':'',
			'severity':'debug',
			'visibility':'private',
		},
		SUBNET_CLEARED:{
			'title':'Subnet cleared',
			'message':'Subnet\'s IP addresses were deallocated.',
			'severity':'info',
			'visibility':'public',
		},
		SUBNET_CREATED:{
			'title':'Subnet created',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		SUBNET_DELETED:{
			'title':'Subnet deleted',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		SUBNET_DEPLOY_STARTED:{
			'title':'Subnet deploy started',
			'message':'Deploy started for Subnet operation.',
			'severity':'info',
			'visibility':'private',
		},
		SUBNET_DEPLOYED:{
			'title':'Subnet deployed',
			'message':'Deploy completed for Subnet operation.',
			'severity':'success',
			'visibility':'public',
		},
		SUBNET_EDITED:{
			'title':'Subnet edited',
			'message':'The operation was performed in design mode. A deploy is required in order for the changes to take effect.',
			'severity':'info',
			'visibility':'public',
		},
		SUBNET_NEEDS_START:{
			'title':'Subnet needs start',
			'message':'At least one instance interface is associated to a stopped subnet. Start the subnet and deploy.',
			'severity':'warning',
			'visibility':'public',
		},
		SUBNET_STARTED:{
			'title':'Subnet started',
			'message':'The operation was performed in design mode. A deploy is required in order to provision hardware resources.',
			'severity':'info',
			'visibility':'public',
		},
		SUBNET_STOPPED:{
			'title':'Subnet stopped',
			'message':'The operation was performed in design mode. A deploy is required in order for hardware resources to be deprovisioned.',
			'severity':'info',
			'visibility':'public',
		},
		USER_API_KEY_REGENERATED:{
			'title':'User API key regenerated',
			'message':'An user\'s API key was regenerated.',
			'severity':'security',
			'visibility':'public',
		},
		USER_AUTHENTICATED_PASSWORD:{
			'title':'User authenticated with password',
			'message':'An user has been authenticated using his password.',
			'severity':'security',
			'visibility':'public',
		},
		USER_CREATED:{
			'title':'User created',
			'message':'A user has been successfully created.',
			'severity':'security',
			'visibility':'public',
		},
		USER_DELEGATE_ADDED:{
			'title':'User delegate added',
			'message':'A user has delegated another user to be his representative. The delegate can now create and deploy infrastructures on behalf of the represented user.',
			'severity':'security',
			'visibility':'public',
		},
		USER_DELEGATE_REMOVED:{
			'title':'User delegate removed',
			'message':'A user is no longer the delegate of another user.',
			'severity':'security',
			'visibility':'public',
		},
		USER_JWT_SALT_REGENERATED:{
			'title':'User JWT salt regenerated',
			'message':'An user\'s JWT salt was regenerated. This invalidates all logged-in existing sessions.',
			'severity':'security',
			'visibility':'public',
		},
		USER_LOGIN_EMAIL_UPDATED_VERIFICATION_URL:{
			'title':'User login email updated via verification URL',
			'message':'The login email change verification URL was accessed, and the user\'s login email address has been updated, while the user was logged-in already. The login email change does not happen if the user is not authenticated when accessing the URL.',
			'severity':'security',
			'visibility':'public',
		},
		USER_PASSWORD_CHANGED:{
			'title':'User password changed',
			'message':'The user\'s password has been updated.',
			'severity':'security',
			'visibility':'public',
		},
		USER_SSH_KEY_CREATED:{
			'title':'User SSH key successfully created',
			'message':'The user\'s SSH key has been successfully created.',
			'severity':'security',
			'visibility':'public',
		},
		USER_SSH_KEY_DELETED:{
			'title':'User SSH key deleted',
			'message':'The user\'s SSH key has been successfully deleted.',
			'severity':'security',
			'visibility':'public',
		},
		USER_SUSPENDED:{
			'title':'User suspended',
			'message':'A suspend reason has been created for a specific owner account.',
			'severity':'important',
			'visibility':'public',
		},
		USER_UNSUSPENDED:{
			'title':'User unsuspended',
			'message':'A suspend reason has been removed for a specific owner account. Unless all suspend reasons are removed, the account remains suspended.',
			'severity':'important',
			'visibility':'public',
		},
	}