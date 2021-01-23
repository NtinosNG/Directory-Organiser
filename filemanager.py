import os
import shutil # Library required to move the files

# Iterates the provided JSON data to find the extension of the
# provided file and returns its 'Extension', 'Category' and 'Description' information.
# If file extension is not found, it returns 'None'
def GetFileExtensionInfo(file, JSONdata):
	for data in JSONdata:
		if file.lower() == data['extension'].lower():
			return data


# Checks if a the provided file from the
# provided path is a 'Folder', 'File' or something else
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
# as well as all the descriptions for each category
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


# Iterates through the list with the categories for the current extension
# and rearranges it by the category title and their corresponding descriptions
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
# to the provided destination path. All those files are
# moved in the mainfolder.
def MoveToDir(cwd, filename, mainfolder, destpath):

	if not os.path.exists(mainfolder):
		os.mkdir(mainfolder)

	movePath = mainfolder + '\\' + destpath + '\\'

	if not os.path.exists(movePath):
		os.mkdir(movePath)

	source = cwd + '\\' + filename
	destination = cwd + '\\' + movePath

	dest = shutil.move(source, destination)


# Iterates the provided JSON data to find the
# names of the categories for the provided extension
# and collects them in an array
def GetExtensionCategoryNames(extension, JSONdata, extCategories):
	for d in JSONdata:
		if d['extension'] == extension:
			extCategories.append(d)


# The following function iterates the array with the category names
# and removes the repetition of each category to find the unique names of each category
def GetUniqueCategoryNames(extCategories):
	return list({v['category']:v for v in extCategories}.values())


# Iterates the array with the unique category names
# and removes the additional information to extract
# only the names of each category
def ExtractCategoryNames(categories, uniqueCaterogies):
	for d in categories:
		uniqueCaterogies.append(d['category'])

