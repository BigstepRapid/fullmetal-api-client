# -*- coding: utf-8 -*-

class ContainerArray(object):
	"""
	A ContainerArray is a group of containers which share the same workload
	(thus enabling scalability).
	"""

	def __init__(self):
		pass;


	"""
	The ContainerArray's unique label is used to create the
	<code>container_array_subdomain</code>. It is editable and can be used to
	call API functions.
	"""
	container_array_label = None;

	"""
	Automatically created based on <code>container_array_label</code>. It is a
	unique reference to the ContainerArray object.
	"""
	container_array_subdomain = None;

	"""
	The ID of the ContainerArray which can be used instead of the
	<code>container_array_label</code> or <code>container_array_subdomain</code>
	when calling the API functions. It is automatically generated and cannot be
	edited.
	"""
	container_array_id = None;

	"""
	The number of containers to be created on the ContainerArray.
	"""
	container_array_container_count = 1;

	"""
	The minimum RAM capacity of each container.
	"""
	container_array_ram_mbytes = 1024;

	"""
	The minimum cores of a CPU.
	"""
	container_array_processor_core_count = 1;

	"""
	Represents the infrastructure ID to which the ContainerArray belongs.
	"""
	infrastructure_id = None;

	"""
	The status of the ContainerArray.
	"""
	container_array_service_status = None;

	"""
	The operation type, operation status and modified ContainerArray object.
	"""
	container_array_operation = None;

	"""
	All <a:schema>ContainerArrayInterface</a:schema> objects. There are 2
	interfaces for ContainerArray, with indexes 0 and 1.
	"""
	container_array_interfaces = [];

	"""
	The ContainerArray is a child of a ContainerCluster.
	"""
	container_cluster_id = None;

	"""
	The application image on Docker server that will be installed on the
	Container.
	"""
	container_array_application_image = "bigstepinc/hello-world";

	"""
	The command that is executed when the Containers are deployed.
	"""
	container_entrypoint_command_override = None;

	"""
	An array of strings that represents an alternative mode of specifying the
	command to run.
	"""
	container_entrypoint_args = [];

	"""
	A list of services upon which this application depends.
	"""
	container_dependencies = [];

	"""
	All <a:schema>ContainerURI</a:schema> objects defined for the ContainerArray
	application.
	"""
	container_uris = [];

	"""
	A list of parameters received in the key/value format, used to configure the
	docker image.
	"""
	container_parameters = [];

	"""
	All <a:schema>ContainerEnvironmentVariable</a:schema> objects defined for
	the ContainerArray application.
	"""
	container_environment_variables = [];

	"""
	All <a:schema>ContainerVolume</a:schema> objects defined for the
	ContainerArray application.
	"""
	container_volumes = [];

	"""
	All <a:schema>ContainerVolume</a:schema> objects defined for the
	ContainerArray application and describe persistent volumes.
	"""
	container_persistent_volumes = [];

	"""
	All <a:schema>ContainerHealthcheck</a:schema> objects defined for the
	ContainerArray application.
	"""
	container_healthchecks = [];

	"""
	All <a:schema>ContainerPortMapping</a:schema> objects defined for the
	ContainerArray application.
	"""
	container_port_mappings = [];

	"""
	Reserved for GUI users.
	"""
	container_array_gui_settings_json = "";

	"""
	ISO 8601 timestamp which holds the date and time when the ContainerArray was
	created. Example format: 2013-11-29T13:00:01Z.
	"""
	container_array_created_timestamp = "0000-00-00T00:00:00Z";

	"""
	ISO 8601 timestamp which holds the date and time when the ContainerArray was
	edited. Example format: 2013-11-29T13:00:01Z.
	"""
	container_array_updated_timestamp = "0000-00-00T00:00:00Z";

	"""
	The schema type.
	"""
	type = None;

	"""
	This property helps ensure that edit operations don’t overwrite other,
	more recent changes made to the same object. It gets updated automatically
	after each successful edit operation.
	"""
	container_array_change_id = None;

	"""
	"""
	container_cluster_role_group = "none";
