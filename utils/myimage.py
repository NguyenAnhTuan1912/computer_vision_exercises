import cv2
import numpy as np

from enum import Enum
from typing import Type, Union

# Module này dùng để thực hiện các công việc lên ảnh.
# Sẽ được cập nhật thêm.

__root__ = "data"

class MyImage:
  """
  MyImage
  ===
  
  Dùng để tạo ra một đối tượng để thực hiện các thao tác trên ảnh. Object này
  sẽ giữ một hay nhiều tấm ảnh trong nó, để tiện cho việc mình có thể dùng lại sau.
  
  >>> mi = MyImage(root_path) ## root mặc định là "/data".
  >>> ## Thêm một tấm ảnh vào cuối.
  >>> mi.add_image(path, cv2.COLOR_GRAY2BGR)
  >>> ## Thêm một tấm ảnh nữa vào cuối.
  >>> mi.add_image(path)
  >>> ## Hiển thị ảnh ở cuối danh sách.
  >>> mi.show_image()
  
  """
  
  
  def __init__(self, root: str = __root__):
    self.root = root
    self.images = []
  
  
  
  # GET IAMGE WITH cv2
  def __get_image_cv2(
    self,
    path: str,
    color: int = None
  ) -> cv2.typing.MatLike | None:
    """
    Private
    Phương thức này dùng cv2 dể đọc một file ảnh bằng cv2.
    
    - param path: đường dẫn tới ảnh cần lấy, đường dẫn phải là `/path` mới hợp lệ.
    - param color: màu cho ảnh. Lấy từ cv2.
    """
    try:
      if color == None:
        return cv2.imread(self.root + path)
      return cv2.imread(self.root + path, color)
      
    except Exception as e:
      print(str(e))
  
  
  
  # GET IMAGE IN LIST
  def __get_image_in_list(
    self,
    at: int = None
  ):
    """
    Private
    Phương thức này dùng để lấy một ảnh đã được thêm ở trong list
    - param at: vị trí của ảnh muốn lấy.
    """
    if at == None:
       at = len(self.images) - 1
    return self.images[at]
  
  
  
  ## GET BLUE IMAGE IN LIST
  def __get_blur_image(
    self,
    x: int = 3,
    ddepth: int = -1,
    at: int = None
  ):
    """
    Private
    Phương thức này dùng để lấy ra ảnh mờ.
    
    - param x: độ mờ, tạm hiểu là thế :3
    - param ddepth: độ sâu.
    - param at: vị trí ảnh trong list muốn làm mờ.
    """
    try:
      kernel = np.ones((x, x), np.float32) / (x * x * 1.0)
      
      # Lấy ảnh
      img = self.__get_image_in_list(at)
      
      # Trả về ảnh mờ
      return cv2.filter2D(img, ddepth, kernel)
    except Exception as e:
      print(str(e))
      
      
      
  # GET CANNY
  def __get_canny(
    self,
    at: int = None,
    dx: cv2.UMat = 10,
    dy: cv2.UMat = 10
  ):
    """
    Phương thức này sẽ trả về một canny. Sẽ được cập nhập thêm.
    
    - param at: Vị trí ảnh muốn show.
    - param dx:
    - param dy:
    """
    try:
      # Chuyển ảnh về GRAYSCALE và hiển thị cạnh.
      gray_img = self.convert_color(cv2.COLOR_RGB2GRAY, at)
      
      # Trả về canny
      return cv2.Canny(gray_img, dx, dy)
    except Exception as e:
      print(str(e))
      
      
      
  # CONVERT IMAGE
  def convert_color(
    self,
    color: int,
    at: int = None
  ):
    """
    Phương thức này dùng để chuyển một ảnh sang màu khác.
    
    - param color: màu muốn convert.
    - param at: Vị trí ảnh muốn convert.
    """
    try:
      # Lấy ảnh
      img = self.__get_image_in_list(at)
      
      # Chuyển ảnh về GRAYSCALE và hiển thị cạnh.
      converted_img = cv2.cvtColor(img, color)
      
      # Trả về canny
      return converted_img
    except Exception as e:
      print(str(e))
    
  
  
  
  # ADD IMAGEs
  def add_image(
    self,
    path: str,
    color: int = None
  ):
    """
    Phương thức này dùng để thêm một ảnh vào trong danh sách.
    
    - param path: đường dẫn tới ảnh ở thư mục data.
    - param color: màu cho ảnh.
    """
    try:
      self.images.append(self.__get_image_cv2(path, color))
    except Exception as e:
      print(str(e))
      
      

  # REMOVE IMAGE
  def remove_image(
    self,
    at: int = None
  ):
    """
    Dùng phương thức này để remove một ảnh ra khỏi list. Nếu như không có at
    thì sẽ tự động xóa ảnh cuối danh sách. Ngược lại, nếu có thì xóa tại at.
    
    - param at: vị trí ảnh cần xóa.
    """
    try:
      if at == None:
        at = len(self.images) - 1
      return self.images.pop(at)
    except Exception as e:
      print(str(e))
    
    
    
  # SHOW IMAGE
  def show_image(
    self,
    title: str = None,
    at: int = None,
    color = None
  ):
    """
    Phương thức này dùng cv2 để hiển thị một ảnh. Nếu như không có at thì nó sẽ
    tự động hiện ảnh được thêm cuối cùng
    
    - param title: title cho cửa số hiện ảnh.
    - param at: hiển thị một ảnh ở một vị trí nào đó.
    - param color: màu muốn hiển thị. Lưu ý những ảnh từ đầu không phải ở màu gốc!
    
    @example
    >>> mi.show_image("Hello")
    >>> mi.show_image("Hello", 1)
    """
    try:
      # Nếu như không có title, thì cho nó một thông số tự động.
      if title == None:
        title = "My image"
      
      img = self.__get_image_in_list(at)
      
      # Nếu như có color
      if color != None:
        img = self.convert_color(color, at)
        
      cv2.imshow(title, img)
      cv2.waitKey(0)
    except Exception as e:
      print(str(e))
      
      
      
  def show_edge_canny(
    self,
    title: str = None,
    at: int = None,
    dx: cv2.UMat = 10,
    dy: cv2.UMat = 10
  ):
    """
    Phương thức này sẽ detect cạnh với cv2.Canny. Sẽ được cập nhập thêm.
    
    - param title: Tiêu đề cho window.
    - param at: Vị trí ảnh muốn show.
    - param dx:
    - param dy:
    """
    try:
      if title == None:
        title = "Edges detection with Canny"
      
      # Lấy canny
      canny = self.__get_canny(at, dx, dy)
      
      # Show
      cv2.imshow(title, canny)
      cv2.waitKey(0)
    except Exception as e:
      print(str(e))
      
      

  # SHOW BLUR
  def show_blur(
    self,
    title: str = None,
    x: int = 3,
    ddepth: int = -1,
    at: int = None
  ):
    """
    Phương thức này sẽ detect cạnh với cv2.Canny. Sẽ được cập nhập thêm.
    
    - param title: tiêu đề cho window.
    - param x: độ mờ, tạm hiểu là thế :3
    - param ddepth: độ sâu.
    - param at: vị trí ảnh trong list muốn làm mờ.
    """
    try:
      if title == None:
        title = "Blur image {}x{}".format(x, x)
      
      # Chuyển ảnh về GRAYSCALE và hiển thị cạnh.
      blur = self.__get_blur_image(x, ddepth, at)
      
      # Show
      cv2.imshow(title, blur)
      cv2.waitKey(0)
    except Exception as e:
      print(str(e))