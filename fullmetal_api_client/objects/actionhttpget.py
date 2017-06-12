# -*- coding: utf-8 -*-

class ActionHTTPGet(object):
	"""
	ContainerArray healthcheck based on HTTP Get requests.
	"""

	def __init__(self, action_port):
		self.action_port = action_port;


	"""
	Path to acccess on the HTTP server.
	"""
	action_path = "/";

	"""
	Port to access on the container.
	"""
	action_port = None;

	"""
	Host name to connect to. Defaults to the container IP.
	"""
	action_host = None;

	"""
	Scheme to use for connecting to the host.
	"""
	action_scheme = "http";

	"""
	The schema type.
	"""
	type = None;
