import json
import os

def get_json(): # arguments url and skin

	url = "skins/"
	skin = "beaver.json"

	with open(url + skin, "r") as read_file:
		data = json.load(read_file)

	return data
