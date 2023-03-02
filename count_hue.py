from PIL import Image
import colorsys
import os
import numpy as np

# 定义一个函数用于将 RGB 转换为 Hue
def hue_from_rgb(rgb):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    return h * 360

# 指定图像文件夹的路径
folder_path = "/path/to/folder"

# 获取所有 png 格式的文件名
files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

# 遍历文件夹中的每个文件
for file in files:
    # 构建完整路径
    file_path = os.path.join(folder_path, file)

    # 加载图像
    image = Image.open(file_path)

    # 获取图像的像素数据
    pixels = image.load()

    # 提取图像的 hue 值，并将结果保存为一个矩阵
    hue_matrix = np.zeros((image.height, image.width))
    for x in range(image.width):
        for y in range(image.height):
            hue = hue_from_rgb(pixels[x, y])
            hue_matrix[y, x] = hue

    # 将矩阵写入同名的 txt 文件中
    output_file_path = os.path.splitext(file_path)[0] + ".txt"
    with open(output_file_path, "w") as f:
        np.savetxt(f, hue_matrix, delimiter=",", fmt="%d")