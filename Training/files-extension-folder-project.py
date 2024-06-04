import os
default_directory = "C:\\Users\\USER\\Desktop\\DevOps\\Sela Project\\pythonProject1\\filextesnionsproj"
used_directory = "C:\\Users\\USER\\Desktop\\DevOps\\Sela Project\\pythonProject1\\filextesnionsproj\\filextesnionsproj_copy"

def file_into_folder(source_folder=default_directory, to_folder=default_directory):
    ALL_FILES = os.listdir(source_folder)
    ALL_DEFAULT_FILES = os.listdir(to_folder)
    file_extensions = []
    file_extensions_new = []
    for file in ALL_FILES:
        helplist = file.split(".")
        file_extensions.append(helplist[-1])
    for extension in file_extensions:
        if extension not in file_extensions_new:
            file_extensions_new.append(extension)
    for file_extension in file_extensions_new:
        if file_extension in ALL_DEFAULT_FILES:
            print(f"Folder {file_extension} already exists")
            continue
        else:
            os.mkdir(to_folder + f"\\{file_extension}")
            print(f"Created folder named {file_extension}")
    for file_name in ALL_FILES:
        if "." not in file_name: 
            continue
        else:
            splittup = file_name.split(".")
            fextension = splittup[-1]
        os.replace(source_folder + f"\\{file_name}", to_folder + f"\\{fextension}\\{file_name}")
        print(f"Moved {file_name} to {fextension}")
    return


file_into_folder(used_directory, default_directory)
