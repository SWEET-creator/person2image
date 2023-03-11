import cv2
import numpy as np
 
height = 200
width = 300
img = np.zeros((height, width, 3), np.uint8)

# 例えば，データは1~5の数値とする
data = [1,2,3,1,2,3,4,4,5,1]

# 変換をする関数
def convert(data):
  return

color = convert(data)

color = [200, 10, 10]
for w in range(0, width):
  img[:, w] = color

cv2.imwrite('color_img.jpg', img)