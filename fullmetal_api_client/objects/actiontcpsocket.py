# -*- coding: utf-8 -*-

class ActionTCPSocket(object):
	"""
	ContainerArray healthcheck based on opening TCP sockets.
	"""

	def __init__(self, action_port):
		self.action_port = action_port;


	"""
	Port to access on the container.
	"""
	action_port = None;

	"""
	The schema type.
	"""
	type = None;
