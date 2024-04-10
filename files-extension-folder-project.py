import os
import inspect
default_directory = "C:\\Users\\USER\\Desktop\\DevOps\\Sela Project\\pythonProject1\\filextesnionsproj"
used_directory = "C:\\Users\\USER\\Desktop\\DevOps\\Sela Project\\pythonProject1\\filextesnionsproj\\filextesnionsproj_copy"



def all_files_lister(source_folder=default_directory):
    ALL_FILES = os.listdir(source_folder)
    return ALL_FILES


def non_duplicates_extensions_list(source_folder=default_directory):
    file_extensions = []
    file_extensions_new = []
    for file in all_files_lister(source_folder):
        helplist = file.split(".")
        file_extensions.append(helplist[-1])
    for extension in file_extensions:
        if extension not in file_extensions_new:
            file_extensions_new.append(extension)
    return file_extensions_new


def folder_creator(source_folder=default_directory):
    for file_extension in non_duplicates_extensions_list(source_folder):
        if file_extension in all_files_lister(default_directory):
            print(f"Folder {file_extension} already exists")
            continue
        else:
            os.mkdir(default_directory + f"\\{file_extension}")
            print(f"Created folder named {file_extension}")
    return


def file_mover(source_folder=default_directory ,to_folder=default_directory):
    for file_name in all_files_lister(source_folder):
        if "." not in file_name: 
            continue
        else:
            splittup = file_name.split(".")
            fextension = splittup[-1]
        os.replace(source_folder + f"\\{file_name}", to_folder + f"\\{fextension}\\{file_name}")
        print(f"Moved {file_name} to {fextension}")
    return


all_files_lister(used_directory)
non_duplicates_extensions_list(used_directory)
folder_creator(used_directory)
file_mover(used_directory)
