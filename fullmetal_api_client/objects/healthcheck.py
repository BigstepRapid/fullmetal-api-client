# -*- coding: utf-8 -*-

class Healthcheck(object):
	"""
	ContainerArray check to perform in order to asses its health.
	"""

	def __init__(self, healthcheck_action_type, healthcheck_action):
		self.healthcheck_action_type = healthcheck_action_type;
		self.healthcheck_action = healthcheck_action;


	"""
	Healthcheck action type to perform.
	"""
	healthcheck_action_type = None;

	"""
	Healthcheck action to perform.
	"""
	healthcheck_action = None;

	"""
	Number of seconds after the container has started before the healthcheck is
	initiated.
	"""
	healthcheck_delay_seconds = 10;

	"""
	Time interval between consecutive healthchecks in seconds. Minimum value is
	1.
	"""
	healthcheck_interval_seconds = 10;

	"""
	Number of seconds after which the healthcheck times out. Minimum value is 1.
	"""
	healthcheck_timeout_seconds = 1;

	"""
	Minimum consecutive successes for the healthcheck to be considered
	successful after having failed. Minimum value is 1.
	"""
	healthcheck_success_threshold = 1;

	"""
	Minimum consecutive failures for the healthcheck to be considered failed
	after having succeeded. Minimum value is 1.
	"""
	healthcheck_failure_threshold = 3;

	"""
	The schema type.
	"""
	type = None;
