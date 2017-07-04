# -*- coding: utf-8 -*-

class ContainerURI(object):
	"""
	A ContainerURI is a group of properties that describes the list of URIs to
	fetch before a Docker application starts.
	"""

	def __init__(self, uri):
		self.uri = uri;


	"""
	URI to be fetched by Mesos fetcher module.
	"""
	uri = None;

	"""
	Set fetched artifact as executable.
	"""
	executable = None;

	"""
	Extract fetched artifact if supported by Mesos fetcher module.
	"""
	extract = None;

	"""
	Cache fetched artifact if supported by Mesos fetcher module.
	"""
	cache = None;

	"""
	The schema type.
	"""
	type = None;
