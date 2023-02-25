import os

# 指定文件夹路径
folder_path = 'RUNS'

# 遍历文件夹下的所有子文件夹和文件
for subdir, _, files in os.walk(folder_path):
    for file in files:
        # 如果文件名是results.txt
        if file == 'results.txt':
            # 获取子文件夹名，用于构造新的文件名
            subdir_name = os.path.basename(subdir)
            # 构造新的文件名
            new_file_name = f'results_of_{subdir_name}.txt'
            # 构造文件的完整路径
            file_path = os.path.join(subdir, file)
            new_file_path = os.path.join(subdir, new_file_name)
            # 重命名文件
            os.rename(file_path, new_file_path)
