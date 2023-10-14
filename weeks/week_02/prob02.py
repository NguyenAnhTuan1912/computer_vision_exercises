# Nhận diện khuôn mặt
import cv2
import sys

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# sys.path.append('d:/Hoctap/Computer Vision/source')
sys.path.append('./')

from utils.myimage import MyImage

# Đường dẫn
people_path = "/people.jpg"

# Tạo instance của MyImage
mi = MyImage()

# Thêm ảnh
mi.add_image(people_path)

# Kết quả
# 1. Hiển thị ở ảnh tĩnh
# mi.detect_face_cc(scaleFactor=1.6, minNeighbors=2)

# 2. Trong video
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    
    # Dùng detect_face_cc để vẽ các kết quả nhận diện khuôn mặt.
    mi.detect_face_cc(
      img=frame,
      scaleFactor=1.5,
      minNeighbors=2,
      canWait=False
    )
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()