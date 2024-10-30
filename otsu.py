import cv2
import numpy as np
from skimage import io, filters
import matplotlib.pyplot as plt

# 读取图像
image_path = 'fixed_image.jpg'  # 替换为您的实际图像路径
image = io.imread(image_path, as_gray=True)

# Otsu阈值分割
otsu_threshold = filters.threshold_otsu(image)
binary_otsu = image > otsu_threshold

# 将布尔类型的二值化图像转换为uint8类型
binary_otsu = binary_otsu.astype(np.uint8) * 255

# 输出Otsu阈值分割结果
plt.figure(figsize=(10, 5))

# 显示原始图像
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# 显示二值化图像
plt.subplot(1, 2, 2)
plt.imshow(binary_otsu, cmap='gray')  # 注意这里直接使用转换后的binary_otsu
plt.title('Otsu Thresholding')
plt.axis('off')

# 保存二值化图像
cv2.imwrite('otsu.png', binary_otsu)  # 更改文件扩展名为.png或其他支持的格式

# 等待按键后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.show()