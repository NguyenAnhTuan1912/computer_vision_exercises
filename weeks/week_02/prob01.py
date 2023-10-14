import cv2
import sys

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# sys.path.append('d:/Hoctap/Computer Vision/source')
sys.path.append('./')

from utils.myimage import MyImage

# Đường dẫn
dogs_path = "/2_dogs.jpg"
buildings_path = "/buildings.jpg"

# Tạo instance của MyImage
mi = MyImage()

# Thêm ảnh
mi.add_image(dogs_path)
mi.add_image(buildings_path)

# Kết quả
# 1. Ảnh gốc
mi.show_image(title="Original")

# 2. Show ảnh xám
mi.show_image(title="Gray", color=cv2.COLOR_RGB2GRAY)

# 3. Làm mờ ảnh
mi.show_blur(title="Blur", x=10)

# 4. Phát hiện cạnh
mi.show_edge_canny(title="Edge detection", dx=100, dy=200)