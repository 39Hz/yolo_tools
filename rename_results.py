import os
import shutil

# set the source folder path
source_folder = r'folder'

# set the new folder path
target_folder = r'folder/results'

# travers subfolders and all the files
for subdir, _, files in os.walk(source_folder):
    for file in files:
        # if file name is results.txt
        if file == 'results.txt':
            # get name of the subdir
            subdir_name = os.path.basename(subdir)
            # generate new file name
            new_file_name = f'results_of_{subdir_name}.txt'
            # generate the fulll path
            file_path = os.path.join(subdir, file)
            new_file_path = os.path.join(subdir, new_file_name)
            # rename the file
            os.rename(file_path, new_file_path)
            # generate target apth
            target_path = os.path.join(target_path, new_file_name)
            # copy renamed_files to the target folder
            shutil.copyfile(new_file_path, target_path)
