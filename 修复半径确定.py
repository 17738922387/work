import cv2
import numpy as np

def criminisi(image, mask, radius):
    # 使用Criminisi算法（OpenCV的实现）进行图像修复
    filled_image = cv2.inpaint(image, mask, radius, cv2.INPAINT_TELEA)
    return filled_image

def update_radius(val):
    global radius, fixed_image
    radius = val
    fixed_image = criminisi(image, mask, radius)
    cv2.imshow('修复后的图像', fixed_image)

# 加载图像
image = cv2.imread('1.png')

# 确保图像已成功加载
if image is None:
    print("错误：未找到图像。")
else:
    # 以灰度模式读取图像
    img_gray = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)

    # 阈值操作，将像素值 >= 140 的设为 255，其余设为 0
    ret, mask = cv2.threshold(img_gray, 165, 255, cv2.THRESH_BINARY)

    # 初始化修复半径
    radius = 3

    # 使用Criminisi算法修复图像
    fixed_image = criminisi(image, mask, radius)

    # 创建一个窗口并绑定滑动条
    cv2.namedWindow('修复后的图像')
    cv2.createTrackbar('修复半径', '修复后的图像', radius, 20, update_radius)  # 最大值设为100

    # 显示原始图像和修复后的图像
    cv2.imshow('原始图像', image)
    cv2.imshow('修复后的图像', fixed_image)

    # 保存修复后的图像
    cv2.imwrite('fixed_image.jpg', fixed_image)

    # 等待按键后关闭所有窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()