import os
import shutil  # Library required to move the files
import re 	   # using regular expressions to identify copies of files

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
                    thisCat[categoryTitles[i]].append(
                        uniqueCategories[j]['description'])
                else:
                    i += 1
                    thisCat[categoryTitles[i]] = []
                    thisCat[categoryTitles[i]].append(
                        uniqueCategories[j]['description'])
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

    filesInDir = os.listdir(destination)

    # Checks if a given file exists in the
    # destination folder with the same name
    for fileInDir in filesInDir:
        if(filename == fileInDir):
            filename = CheckForCopies(filename, filesInDir)

    destination = destination + filename
    dest = shutil.move(source, destination)


# Checks if copies for a given file exist in the destination
# folder and renames that file with an incrementing number
def CheckForCopies(filename, filesInDestDir):
    matches = []

    # Splits the file at the extension e.g. test.sql -> [test, sql]
    file = filename.split('.')

    # Compiles the search term for the regular expression search
    mySearch = re.compile(re.escape(file[0]) + r"\s\(\d+\)" + "." + re.escape(file[1]))

    # If the file exists, identify if there are other copies of that file
    # e.g. "test (1).sql" "test (2).sql" etc.
    for fileInDir in filesInDestDir:
        try:
            x = re.search(mySearch, fileInDir)

            if x != None:
                # if matches exist, add them in an array
                matches.append(x.group())
        except Exception as e:
            print('An error has occured: ', e)
            exit()

    # If we have matched copies of a file, identify
    # how many by extracting the integers from
    # their names: e.g. extract 1 from "New Document (1).txt" etc.
    if matches:

        extractedNumStrings = []

        for match in matches:
            try:
                x = re.search("\(\d+\)", match)  # searches for (number)
            except Exception as e:
                print('An error has occured: ', e)
                exit()

            try:
                num = re.findall('\d+', x.group())  # finds numbers only
                extractedNumStrings.extend(num)
            except Exception as e:
                print('An error has occured: ', e)
                exit()

        # convert the numbers from strings to integers
        int_array = [int(numeric_string)
                     for numeric_string in extractedNumStrings]

        # Now that we have extracted the integers from those files
        # find the largest one and increase it by one
        increasedNum = max(int_array) + 1

        # construct the new file name of that copy with an increased number
        file = file[0] + " (" + str(increasedNum) + ")" + "." + file[1]

        return file

    else:
        # if we don't have matches of other copies,
        # it means we have to construct the second one
        file = file[0] + " (1)" + "." + file[1]
        return file


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
    return list({v['category']: v for v in extCategories}.values())


# Iterates the array with the unique category names
# and removes the additional information to extract
# only the names of each category
def ExtractCategoryNames(categories, uniqueCaterogies):
    for d in categories:
        uniqueCaterogies.append(d['category'])
