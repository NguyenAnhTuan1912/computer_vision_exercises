import cv2
import sys

# Chạy để hiểu ví dụ

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# Ngoài file này thì mình không cần, nhưng các file khác thì có.
# sys.path.append('d:/Hoctap/Computer Vision/source')
# sys.path.append('./')

from utils.myimage import MyImage

# Đường dẫn
dogs_path = "/2_dogs.jpg"

# Tạo instance của MyImage
mi = MyImage()

# Thêm ảnh
mi.add_image(dogs_path, cv2.IMREAD_GRAYSCALE)
mi.add_image(dogs_path)

# Hiển thị ảnh vừa thêm
mi.show_image("Dogs")
mi.show_image("Dogs - Gray", 0)

# Xóa ảnh
mi.remove_image(0)
mi.show_image("Dogs - Gray", 0)