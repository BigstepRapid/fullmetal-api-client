# -*- coding: utf-8 -*-

class ContainerEnvironmentVariable(object):
	"""
	A ContainerEnvironmentVariable is a key value pair that gets added to the
	environment variables of the Container process to start.
	"""

	def __init__(self, key, value):
		self.key = key;
		self.value = value;


	"""
	The key name.
	"""
	key = None;

	"""
	The value defined for the key.
	"""
	value = None;

	"""
	The schema type.
	"""
	type = None;
