# -*- coding: utf-8 -*-

class ContainerPortMapping(object):
	"""
	A ContainerPortMapping is a group of required port resources and properties
	statically configured in containers.
	"""

	def __init__(self, container_port):
		self.container_port = container_port;


	"""
	The port the application listens to inside of the container.
	"""
	container_port = None;

	"""
	Random port from the range included in the resource offer.
	"""
	host_port = 0;

	"""
	Helper port intended for doing service discovery using a well-known port per
	service.
	"""
	service_port = None;

	"""
	The protocol used.
	"""
	protocol = "tcp";

	"""
	A list of labels (string keys and string values).
	"""
	labels = {"applicationProtocol":"unknown"};

	"""
	The schema type.
	"""
	type = None;
