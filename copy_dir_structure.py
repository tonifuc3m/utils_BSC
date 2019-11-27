import os

def copy_dir_structure(path, input_path_old_files, output_path_new_files):
    for dirpath, dirnames, filenames in os.walk(path + input_path_old_files):
        structure = os.path.join(path + output_path_new_files, 
                                 dirpath[len(path + input_path_old_files):])
        if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            print("Folder does already exist!")
