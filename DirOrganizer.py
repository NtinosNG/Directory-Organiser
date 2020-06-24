import os # Library required to work with files.
import json # Required for handing JSON files.

# Library that contains necessary functions to  
# manipulate the provided JSON and organize the files.
import filemanager 

# Loads the extensions list from the JSON file.
f = open('AllFileTypes.json')
extensionsList = json.load(f)
f.close()

# Sets the directory of which files will be organised.
# Currently is set to the current working directory,
# which will be the folder where the script is located. 
os.chdir(".")

# Gets the current working directory path. 
# It should be the one chosen above.
cwd = os.getcwd();

# Scans all the files and folders in the chosen directory.
entries = os.listdir(cwd)

# Main loop that iterates through all the files in the cwd and organises them accordingly.
for entry in entries:

	# This check allows for the script and its corresponding files to remain  
	# on the cwd; if the the cwd is the one which its files will be organised.
	if entry != "DirOrganizer.py" and entry != "filemanager.py" and entry != "AllFileTypes.json":

		# Checks if the current entry is a folder.
		# Folders remain in the cwd and are not moved.
		currentEntry = filemanager.IsFolderCheck(entry, cwd)

		if currentEntry != "folder":

			# Gets the extension from the current file.
			fileExt = os.path.splitext(entry)[1].lower()

			# Gets all the information for the current extension from the provided JSON.
			filetocheck = filemanager.GetFileExtensionInfo(fileExt, extensionsList)

			if filetocheck != None:

				# Gets the unique names of the categories that this extension can be found in, as well as all the descriptions for each category.
				extensionCategories = filemanager.GetUniqueExtensionCategories(fileExt.upper(), extensionsList)

				#  Iterates through the above list and rearranges it by the category title and their corresponding descriptions.
				categoriesAndDescriptions = filemanager.GetExtCategoriesAndDescriptions(extensionCategories)

				# Checks if the current extension can be found in more than one categories
				# and prompts the user to choose which one describes best the current file.
				if len(categoriesAndDescriptions) > 1:

					# Stores the names of the categories
					categoryNames = []

					print(fileExt, "file extension could be found in the following categories: \n")

					for name, cat in categoriesAndDescriptions.items():
						categoryNames.append(name)
						print("\nCategory: ", name)
						print("\tDescriptions: ", cat)

					print("\nWhich category describes best", entry, "file?")
			
					chosenCategory = None

					while chosenCategory not in categoryNames:
						chosenCategory = input("\nType the name of the category: ")

					# Moves the current file from its current working directory 
					# to the provided destination path; in this case, the one chosen by the user.
					filemanager.MoveToDir(cwd, entry, chosenCategory)

				else:
					categoryNames = []

					# Iterates though the list to extract the category names only.
					for name, cat in categoriesAndDescriptions.items():
						categoryNames.append(name)

					# Moves the current file from its current working directory 
					# to the provided destination path; in this case, the only one in the list.
					filemanager.MoveToDir(cwd, entry, categoryNames[0])

			else:
				print("\nFILETYPE FOR " + "'" + entry + "'" + " IS UNKNOWN!")

				# If the extension cannot be found in the provided JSON list 
				# it will be moved in a folder named 'UNKNOWN-FILETYPES'.
				filemanager.MoveToDir(cwd, entry, "UNKNOWN-FILETYPES")

		else:
			print("\n" + entry + " is a folder.")
