# -*- coding: utf-8 -*-

class Dataset(object):
	"""
	Datasets are sources of data, that can be imported in a DataLake
	"""

	def __init__(self):
		pass;


	"""
	The ID of the dataset
	"""
	dataset_id = None;

	"""
	Long description for what the dataset contains
	"""
	dataset_description = None;

	"""
	List of tags representative for the dataset.
	"""
	dataset_tags = [];

	"""
	The actual source of the data (not necessarily the maintainer)
	"""
	dataset_source_display_name = None;

	"""
	Maintainer name to be displayed in the UI
	"""
	dataset_maintainer_display_name = None;

	"""
	The maintainer's user ID.
	"""
	dataset_maintainer_user_id = None;

	"""
	List of formats in which the dataset is available.
	"""
	dataset_formats = [];

	"""
	ISO 8601 timestamp which holds the date and time when the Dataset was last
	updated. Example format: 2013-11-29T13:00:01Z.
	"""
	dataset_updated_timestamp = None;

	"""
	ISO 8601 timestamp which holds the date and time when the Dataset was
	created. Example format: 2013-11-29T13:00:01Z.
	"""
	dataset_created_timestamp = None;

	"""
	The webhdfs URL of the dataset's directory. Example:
	'webhdfs://n59962-data-lake01-lab-master-bucharest.integration.bigstep.io:14000/data_lake/dl9006'
	"""
	dataset_datalake_path = None;

	"""
	The dataset size(for all formats), in megabytes.
	"""
	dataset_size_mbytes = 0;

	"""
	The ID of the parent datalake
	"""
	dataset_datalake_id = None;

	"""
	The schema type.
	"""
	type = None;
