# -*- coding: utf-8 -*-

class ContainerVolume(object):
	"""
	A ContainerVolume is a group of properties that describe a volume mounting
	point for Docker containers.
	"""

	def __init__(self, container_path):
		self.container_path = container_path;


	"""
	Container mount point.
	"""
	container_path = None;

	"""
	FMDL Storage path.
	"""
	host_path = "";

	"""
	The size of the persistent volume in MiBs
	"""
	container_volume_size_mbytes = 0;

	"""
	Volume mount mode: readonly(RO) or readwrite(RW). Currently, RW is the only
	possible value for persistent volumes.
	"""
	mode = "RO";

	"""
	The schema type.
	"""
	type = None;
