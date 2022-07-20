import os
from PIL import Image
 
 
input_file = "./222.jpg"
output_file = "./output.jpg"

im = Image.open(input_file)
size = os.path.getsize(input_file) / 1024
w, h = im.size

# 压缩图片
while size > 100:
    w, h = round(w * 0.9), round(h * 0.9)
    im = im.resize((w, h), Image.ANTIALIAS)
    im.save(output_file)
    size = os.path.getsize(output_file) / 1024

# 修改分辨率
im.save(output_file, dpi=(400, 720))
