import os
import shutil

# 设置原始文件夹路径
source_folder = 'yolo'

# 设置目标文件夹路径
target_folder = 'yolo/results'

# 获取原始文件夹中的所有子文件夹
subfolders = [f.path for f in os.scandir(source_folder) if f.is_dir()]

for subfolder in subfolders:
    if os.path.basename(subfolder) == 'results':
        continue

    # 获取子文件夹名称
    subfolder_name = os.path.basename(subfolder)

    # 获取子文件夹中的result.txt文件路径
    result_path = os.path.join(subfolder, 'results.txt')

    # 构造目标文件名
    target_name = f'results-{subfolder_name}.txt'

    # 构造目标文件路径
    target_path = os.path.join(target_folder, target_name)

    # 复制文件到目标路径
    shutil.copyfile(result_path, target_path)