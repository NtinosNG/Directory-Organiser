import os # Library required to work with files.
import shutil # Library required to move the files.

# Iterates the provided JSON data to find the extension of the
# provided file and returns its 'Extension', 'Category' and 'Description' information.
# If file extension is not found, it returns 'None'.
def GetFileExtensionInfo(file, JSONdata):
	for data in JSONdata:
		if file.lower() == data['extension'].lower():
			return data

# Checks if a the provided file from the
# provided path is a 'Folder', 'File' or something else.
def IsFolderCheck(file, cwd):
	currentPath = cwd + "\\" + file
	if os.path.isdir(currentPath):  
		return "folder"
	elif os.path.isfile(currentPath):
		return "file"
	else:  
		return "special"


# Iterates the provided JSON data to find the
# names of the categories for the provided extension
# and returns a list with the unique names of the 
# categories that this extension can be found in,
# as well as all the descriptions for each category.
def GetUniqueExtensionCategories(extension, JSONdata):
	extensionCategoriesList = []
	uniqueCategoryNames = []
	categoryNames = []

	GetExtensionCategoryNames(extension, JSONdata, extensionCategoriesList)

	uniqueCategoryNames = GetUniqueCategoryNames(extensionCategoriesList)

	ExtractCategoryNames(uniqueCategoryNames, categoryNames)

	# append the category names in the full list for the provided extension
	extensionCategoriesList.append(categoryNames) 

	return extensionCategoriesList



'''
 Iterates through the list with the categories for the current extension
 and rearranges it by the category title and their corresponding descriptions.

 For example, it changes the list from the following form: 

[
	{'category': 'Data Files', 'description': 'Piriform Key File', 'extension': '.DAT'},  
	{'category': 'Video Files', 'description': 'VCD Video File', 'extension': '.DAT'}
]

...like this:

{
'Data Files': 
 		['Data File', 'Piriform Key File', 'Porteus Save Container File', 'Nonimmigrant Visa Application Data File'], 
 'Video Files': 
 		['VCD Video File'] 
}
'''
def GetExtCategoriesAndDescriptions(uniqueCategories):
	categoryTitles = uniqueCategories[len(uniqueCategories)-1]
	uniqueCategories.pop()

	thisCat = {}
	i = 0
	while i < len(categoryTitles):
		if categoryTitles[i] == uniqueCategories[i]['category']:
			j = 0
			thisCat[categoryTitles[i]] = []
			while j < len(uniqueCategories):
				if categoryTitles[i] == uniqueCategories[j]['category']:
					thisCat[categoryTitles[i]].append(uniqueCategories[j]['description'])
				else:
					i += 1
					thisCat[categoryTitles[i]] = []
					thisCat[categoryTitles[i]].append(uniqueCategories[j]['description'])
				j += 1
		i += 1
		return thisCat


# Moves the provided file from its current working directory
# to the provided destination path.
def MoveToDir(cwd, filename, destpath):
	source = cwd + '\\' + filename
	destination = cwd + '\\' + destpath + '\\'

	if not os.path.exists(destpath):
		os.mkdir(destpath)

	dest = shutil.move(source, destination)


# Iterates the provided JSON data to find the
# names of the categories for the provided extension
# and collects them in an array.
def GetExtensionCategoryNames(extension, JSONdata, extCategories):
	for d in JSONdata:
		if d['extension'] == extension:
			extCategories.append(d)


''' 
The following function iterates the array with the category names
and removes the repetition of each category to find the unique names of each category.
	
For example, a file with extension '.DAT' can be found in the following categories:

[{'category': 'Data Files', 'description': 'Data File', 'extension': '.DAT'}, 
 {'category': 'Data Files', 'description': 'Piriform Key File', 'extension': '.DAT'},  
 {'category': 'Video Files', 'description': 'VCD Video File', 'extension': '.DAT'}, 
 {'category': 'Game Files', 'description': 'Minecraft Data File', 'extension': '.DAT'}, 
 {'category': 'Game Files', 'description': 'SimCity 4 Game Data File', 'extension': '.DAT'}, 
 {'category': 'System Files', 'description': 'Windows Registry Hive File', 'extension': '.DAT'}, 
 {'category': 'Misc Files', 'description': 'Inno Setup Uninstaller Data File', 'extension': '.DAT'}, 
 {'category': 'Misc Files', 'description': 'Piriform DAT File', 'extension': '.DAT'}
]

This function removes the repeated category names to extract the unique ones like so:

[{'category': 'Data Files', 'description': 'Data File', 'extension': '.DAT'}, 
 {'category': 'Video Files', 'description': 'VCD Video File', 'extension': '.DAT'}, 
 {'category': 'Game Files', 'description': 'Minecraft Data File', 'extension': '.DAT'}, 
 {'category': 'System Files', 'description': 'Windows Registry Hive File', 'extension': '.DAT'}, 
 {'category': 'Misc Files', 'description': 'Inno Setup Uninstaller Data File', 'extension': '.DAT'}
]

'''
def GetUniqueCategoryNames(extCategories):
	return list({v['category']:v for v in extCategories}.values())


# Iterates the array with the unique category names
# and removes the additional information to extract
# only the names of each category.
# 
# For example: 
# ['Data Files', 'Video Files', 'Game Files', 'System Files', 'Misc Files']
def ExtractCategoryNames(categories, uniqueCaterogies):
	for d in categories:
		uniqueCaterogies.append(d['category'])

