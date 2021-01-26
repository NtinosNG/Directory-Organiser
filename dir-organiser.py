import os
import json
import filemanager # Custom library that contains necessary functions

# Loads the extensions list from the JSON file
extensionsListPath = os.getcwd() + '\AllFileTypes.json'
f = None
extensionsList = None

try:
	f = open(extensionsListPath)
	extensionsList = json.load(f)
	f.close()
except Exception as e:
	print("\nSomething went wrong when opening the file: \n", e)
	exit()

# Name of the main folder where all files will be organised in
mainfolder = "STUFF"

# Prompts the user to enter the path of the folder they want to organise
path = str(input("Welcome to Directory Organiser!\n\nYou are currently in the " + "\'" + os.getcwd() + "\'" + " directory.\n\nType '.' if you want the current path or enter the correct path of the directory you'd like to organise: "))

if(os.path.exists(path)):
	os.chdir(path)
	print("\nChanged directory to " + os.getcwd())
else:
	print("\nThe path is not correct! Please re-run the script and add a correct path.")
	exit()

# Gets the current working directory path
cwd = os.getcwd()

# Scans all the files and folders in the chosen directory
entries = os.listdir(cwd)

 # Main loop that iterates through all the files in the cwd and organises them accordingly
for entry in entries:

	# This check allows for the script and its corresponding files to remain on the cwd
	if entry != "dir-organiser.py" and entry != "filemanager.py" and entry != "AllFileTypes.json" and entry != ".gitignore" and entry != "README.md" and entry != "TEST.zip":

		# Checks if the current entry is a folder - folders remain in the cwd and are not moved
		currentEntry = filemanager.IsFolderCheck(entry, cwd)

		if currentEntry != "folder":

			# Gets the extension from the current file
			fileExt = os.path.splitext(entry)[1].lower()

			# Gets all the information for the current extension from the provided JSON
			filetocheck = filemanager.GetFileExtensionInfo(fileExt, extensionsList)

			if filetocheck != None:

				# Gets the unique names of the categories that this extension can be found in, as well as all the descriptions for each category
				extensionCategories = filemanager.GetUniqueExtensionCategories(fileExt.upper(), extensionsList)

				#  Iterates through the above list and rearranges it by the category title and their corresponding descriptions
				categoriesAndDescriptions = filemanager.GetExtCategoriesAndDescriptions(extensionCategories)

				# Checks if the current extension can be found in more than one categories
				if len(categoriesAndDescriptions) > 1:

					categoryNames = []

					print(fileExt, "file extension could be found in the following categories: \n")

					for cat, name in categoriesAndDescriptions.items():
						print("Category: ", cat)
						print("Descriptions: ", name, "\n")
						categoryNames.append(cat)

					# Prompts the user to select a category for a given file
					print("Which category describes best", entry, "file?")

					chosenCategory = None

					for idx, val in enumerate(categoryNames):
						print(idx, val)

					while chosenCategory not in categoryNames:
						try:
							userInput = int(input("\nType the number for the name of your choosing: "))
						except ValueError:
							print("Not an integer! Try again.")
							continue
						for idx, val in enumerate(categoryNames):
							if idx == userInput:
								chosenCategory = val
								break

					# Moves the current file from its current working directory to the provided destination path
					filemanager.MoveToDir(cwd, entry, mainfolder, chosenCategory)

				else:
					categoryNames = []

					# Iterates though the list to extract the category names only
					for cat, name in categoriesAndDescriptions.items():
						categoryNames.append(cat)

					filemanager.MoveToDir(cwd, entry, mainfolder, categoryNames[0])

			else:
				print("\nFILETYPE FOR " + "'" + entry + "'" + " IS UNKNOWN!")

				# If the extension cannot be found in the provided JSON list it will be moved in a folder named 'UNKNOWN-FILETYPES'
				filemanager.MoveToDir(cwd, entry, mainfolder, "UNKNOWN-FILETYPES")

		else:
			print("") # + entry + " is a folder."
