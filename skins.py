import os

def get_part_txt():
	listdir = os.listdir("skins")

	folders = []

	for index in listdir:
		if (index[-5:] != ".json") and (index[-4:] != ".png"):
			folders.append(index)

	for part in folders:
		part_list = os.listdir("skins/" + part)
		part_file = open(part + ".txt", "w")
		for index in part_list:
			if index[:2] != "x_":
				part_file.write(index + "\n")
		part_file.close()

def get_part_list(part_name):
	part_list = []
	part_file = open(part_name + ".txt", "r")
	for index in part_file:
		part_list.append(part_file.readline()[:-1])
	part_list.pop()
	part_file.close()
	return part_list	
