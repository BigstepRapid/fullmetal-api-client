# -*- coding: utf-8 -*-

class ActionExecuteCommand(object):
	"""
	ContainerArray healthcheck based on executing commands inside the container.
	"""

	def __init__(self, action_command):
		self.action_command = action_command;


	"""
	Command to execute inside the container. The command is not executed using a
	shell and the root of the container (/) is used as working directory. An
	exit status of 0 is treated as healthy and non-zero as unhealthy
	"""
	action_command = None;

	"""
	The schema type.
	"""
	type = None;
