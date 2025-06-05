#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
	"""
	Writes an object to a text file, using a JSON representation.

	Args:
		my_obj: The Python object to be serialized to JSON.
		filename (str): The name of the file to write the JSON to.
	"""
	with open(filename, 'w') as f:
		json.dump(my_obj, f)
