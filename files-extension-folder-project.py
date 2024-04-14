import os
import inspect
default_directory = "C:\\Users\\USER\\Desktop\\DevOps\\Sela Project\\pythonProject1\\filextesnionsproj"


def given_folder(which_folder=default_directory):
    folderlist.append(which_folder)

#Don't forget to put the directory path at used directory variable!
folderlist = ['a']

given_folder()

used_directory = folderlist[-1]
print(used_directory)

def all_files_lister():
    ALL_FILES = os.listdir(used_directory)
    return ALL_FILES


def non_duplicates_extensions_list():
    file_extensions = []
    file_extensions_new = []
    for file in all_files_lister(used_directory):
        helplist = file.split(".")
        file_extensions.append(helplist[-1])
    for extension in file_extensions:
        if extension not in file_extensions_new:
            file_extensions_new.append(extension)
    return file_extensions_new


def folder_creator():
    for file_extension in non_duplicates_extensions_list(used_directory):
        if file_extension in all_files_lister(default_directory):
            print(f"Folder {file_extension} already exists")
            continue
        else:
            os.mkdir(default_directory + f"\\{file_extension}")
            print(f"Created folder named {file_extension}")
    return


def file_mover():
    for file_name in all_files_lister(used_directory):
        if "." not in file_name: 
            continue
        else:
            splittup = file_name.split(".")
            fextension = splittup[-1]
        os.replace(used_directory + f"\\{file_name}", default_directory + f"\\{fextension}\\{file_name}")
        print(f"Moved {file_name} to {fextension}")
    return

used_directory = "C:\\Users\\USER\\Desktop\\DevOps\\Sela Project\\pythonProject1\\filextesnionsproj\\filextesnionsproj_copy"
all_files_lister()
non_duplicates_extensions_list()
folder_creator()
file_mover()