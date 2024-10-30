import cv2
import numpy as np

def nothing(x):
    pass

def criminisi(image, mask):
    # 使用Criminisi算法（OpenCV的实现）进行图像修复
    filled_image = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    return filled_image

# 加载图像
image_path = '4.jpg'
image = cv2.imread(image_path)

# 确保图像已成功加载
if image is None:
    print("错误：未找到图像。")
else:
    # 以灰度模式读取图像
    img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 创建一个窗口用于调整阈值
    cv2.namedWindow('Thresholding')
    cv2.createTrackbar('Thresh', 'Thresholding', 145, 255, nothing)

    # 初始化阈值
    thresh = cv2.getTrackbarPos('Thresh', 'Thresholding')

    while True:
        # 获取当前的阈值
        thresh = cv2.getTrackbarPos('Thresh', 'Thresholding')

        # 阈值操作，将像素值 >= thresh 的设为 255，其余设为 0
        ret, mask = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
        
        # 使用Criminisi算法修复图像
        fixed_image = criminisi(image, mask)
        
        # 显示图像
        cv2.imshow('原始图像', image)
        cv2.imshow('修复后的图像', fixed_image)
        
        key = cv2.waitKey(1) & 0xFF
        
        # 如果按下 'q' 键，则退出循环
        if key == ord('q'):
            break
        # 如果按下 '+' 键，则增加阈值
        elif key == ord('='):
            thresh = min(thresh + 1, 255)
            cv2.setTrackbarPos('Thresh', 'Thresholding', thresh)
        # 如果按下 '-' 键，则减少阈值
        elif key == ord('-'):
            thresh = max(thresh - 1, 0)
            cv2.setTrackbarPos('Thresh', 'Thresholding', thresh)

    # 清理资源
    cv2.destroyAllWindows()