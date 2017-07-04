# -*- coding: utf-8 -*-

class ContainerHealthcheck(object):
	"""
	A ContainerHealthcheck is an array of checks to be performed on running
	Containers to determine if they are operating as expected.
	"""

	def __init__(self):
		pass;


	"""
	Protocol of the requests to be performed.
	"""
	protocol = "HTTP";

	"""
	Path to endpoint exposed by the Container that will provide health status.
	Only used when the protocol is HTTP.
	"""
	path = "/";

	"""
	Health check failures are ignored within this number of seconds of the
	Container being started or until the Container becomes healthy for the first
	time.
	"""
	grace_period_seconds = 15;

	"""
	Number of seconds to wait between health checks.
	"""
	interval_seconds = 10;

	"""
	Index in this app's ports array to be used for health requests. An index is
	used so the app can use random ports, like "[0, 0, 0]" for example, and
	Containers could be started with port environment variables like $PORT1.
	"""
	port_index = 0;

	"""
	Number of seconds after which a health check is considered a failure
	regardless of the response.
	"""
	timeout_seconds = 20;

	"""
	Number of consecutive health check failures after which the unhealthy task
	should be killed.
	"""
	max_consecutive_failures = 3;

	"""
	Command to run in order to determine the health of a task. Only used when
	the protocol is COMMAND
	"""
	command = "";

	"""
	Ignore HTTP informational status codes 100 to 199.
	"""
	ignore_http_1xx = False;

	"""
	The schema type.
	"""
	type = None;
