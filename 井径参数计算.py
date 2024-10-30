import cv2
import numpy as np

# 输入的值 x
x = float(input("请输入一个值 x: "))

# 读取图片
img = cv2.imread('Otsu_Thresholding.jpg', 0)

# 获取原始图像的尺寸
original_height, original_width = img.shape

# 设置新的宽度为 x * π
new_width = int(x * np.pi*2.54*6)

# 根据新的宽度计算新的高度，保持宽高比
ratio = original_width / original_height
new_height = int(new_width / ratio)

# 调整图像尺寸
resized_img = cv2.resize(img, (new_width, new_height))

# 设置阈值，将像素值小于该阈值的部分视为黑色
threshold_value = 127

# 应用阈值处理
ret, threshold_img = cv2.threshold(resized_img, threshold_value, 255, cv2.THRESH_BINARY_INV)

# 找到所有轮廓
contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 初始化变量用于累计黑色区域的面积和周长
total_area = 0
total_perimeter = 0

# 遍历所有轮廓，找到黑色区域的轮廓
for i, contour in enumerate(contours):
    # 计算面积和周长
    area = cv2.contourArea(contour)/36
    perimeter = cv2.arcLength(contour, True)/6

    # 如果面积大于某个阈值（例如10），则认为是黑色区域
    if area > 0:
        total_area += area
        total_perimeter += perimeter
        print(f"黑色区域{i+1}: 面积={area}, 周长={perimeter}")


print(f"孔隙总面积：{total_area}，总周长：{total_perimeter}")

# 显示处理后的图片
cv2.imshow("Threshold Image", threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()