# -*- coding: utf-8 -*-

class Container(object):
	"""
	A Container represents an application instance.
	"""

	def __init__(self):
		pass;


	"""
	The label is used to uniquely identify a certain Container. It is
	automatically generated and cannot be edited.
	"""
	container_label = None;

	"""
	The ID of the parent ContainerArray.
	"""
	container_array_id = None;

	"""
	The host on which the Container was created.
	"""
	container_host = None;

	"""
	The random host ports allocated by Marathon, mapped to the 8091 port that
	the Container listens to and to the port mappings defined by the user.
	"""
	container_ports = [];

	"""
	ISO 8601 timestamp which holds the date and time when the Container was
	staged. Example format: 2013-11-29T13:00:01Z.
	"""
	container_created_timestamp = "0000-00-00T00:00:00Z";

	"""
	ISO 8601 timestamp which holds the date and time when the Container was
	started. Example format: 2013-11-29T13:00:01Z.
	"""
	container_started_timestamp = "0000-00-00T00:00:00Z";

	"""
	ISO 8601 timestamp which holds the date and time of the Container version.
	Example format: 2013-11-29T13:00:01Z.
	"""
	container_version = "0000-00-00T00:00:00Z";

	"""
	The current status of the Container.
	"""
	container_status = None;

	"""
	The files of the Container.
	"""
	container_files = [];

	"""
	The schema type.
	"""
	type = None;
