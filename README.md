# Python Directory Organiser

## What this script does
This python script, organises the files on the selected working directory based on their extension in different categories that are provided from a JSON file list. For example, if there are 3 files that need to be organised such as, a **.PDF**, a **.DB** and a **.TXT**, the script will move them in corresponding folders named by the extension category type i.e. -> **Page Layout Files**, **Database Files** and **Text Files**. 

If a specific file extension exists in different file categories such as **.DAT** for example, the user will be presented with the different categories and descriptions and then they will be prompt to type the name of the category they believe this files belongs to.

The Script doesn't affect any existing folders in the selected directory; it only moves files. Additionally, if the script is located in the directory-to-be-organised, it will be skipped.

## What is required
In order for this script to work, the following are required:

* Python 3 globally installed
* DirOrganizer.py
* filemanager.py
* AllFileTypes.json

#### DirOrganizer.py Description
This is the entry point of this script. It scans all the files in the selected working directory that need to be organised and gets information for each one based on its extension. The script **will not** move any existing folders in the selected directory and **will not** move the aforementioned required files if they are in the selected directory as well.

#### filemanager.py Description
This file it's just a collection of specific functions that manipulate the JSON file accordingly so as the main script will move each file in appropriately named folders based on the file's category. It's sole purpose is to keep the code in the main script tidy.

#### AllFileTypes.json Description
This JSON file is the list that contains all the categories and descriptions for the different file extensions and it has the following structure:

```
[
    {
        "category": "Text Files",
        "description": "Text File",
        "extension": ".TXT"
    },
        {
        "category": "Page Layout Files",
        "description": "Portable Document Format File",
        "extension": ".PDF"
    },
        {
        "category": "Database Files",
        "description": "Structured Query Language Data File",
        "extension": ".SQL"
    },
    ...
]
```
## How to use it
The best way to use this script, is to test it first to see if it meets your criteria of "organising" files in the first place!
To do that, simply do the following:

1. Clone this repository on your desktop (or wherever you want) or click Download ZIP and unzip it.
2. Unzip the containing "TEST.zip" archive in the same folder where the script and all the other files are located.
3. Open the *DirOrganizer.py* file with a text editor of your choice and choose the test directory on line 16 by changing `os.chdir(".")` to `os.chdir("./TEST")`.
4. Open a terminal window (or cmd if you're on Windows) on the script's location folder and simply type:

```
python DirOrganizer.py
```

That's it! All you need to do now is simply type the category names (when prompted) that you believe each file belongs to. If you have a look on the TEST folder after you've finished, you'll notice that all the files have been moved to their corresponding directories:

> *TEST* folder before files have been organised.

 ![TEST folder after files have been organised](https://i.imgur.com/zKNkzhu.png)

> *TEST* folder after files have been organised.

 ![TEST folder after files have been organised](https://i.imgur.com/nfuyvF1.png)
 
Notice that, in the folder where the script is located (and being run from basically), after is run, a `__pycache__` folder will be automatically created because the `filemanager.py` file is being imported to the main script. This is normal, and you can safely delete that folder; just know that it will be re-created automatically whenever the script is run. Lastly, if you find this script useful, remember that you can organise whatever directory you want as long as you add the correct path to `os.chdir(".")` based on the script's location.
 
