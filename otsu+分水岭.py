import cv2
import numpy as np
from skimage import morphology

# 读取图像并转换为灰度图像
img = cv2.imread('fixed_image.jpg', cv2.IMREAD_GRAYSCALE)

# 使用Otsu二值化
_, binary_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 应用形态学开运算
binary_otsu = morphology.binary_opening(binary_otsu, selem=morphology.disk(3))
import numpy as np
from scipy import ndimage
from skimage import morphology
binary_otsu = morphology.binary_opening(binary_otsu, selem=morphology.disk(3))
from skimage import io, filters, segmentation, color, exposure
from scipy.ndimage import distance_transform_edt
from skimage.feature import peak_local_max
import matplotlib.pyplot as plt
from skimage.morphology import disk, binary_opening
# 读取图像
image_path = 'fixed_image.jpg'  # 替换为您的实际图像路径
image = io.imread(image_path, as_gray=True)

# Otsu阈值分割
otsu_threshold = filters.threshold_otsu(image)
binary_otsu = image > otsu_threshold

# 对二值图像进行形态学操作以去除噪声（可选）
binary_otsu = binary_otsu.astype(np.uint8)
binary_otsu = morphology.binary_opening(binary_otsu, selem=morphology.disk(3)) # type: ignore

# 分水岭算法分割
distance = ndimage.distance_transform_edt(binary_otsu)
local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=binary_otsu) # type: ignore
markers = ndimage.label(local_maxi)[0]
labels_ws = segmentation.watershed(-distance, markers, mask=binary_otsu)

# 将分割结果转换为彩色图像以方便可视化
colored_labels = color.label2rgb(labels_ws, bg_label=0)
# Otsu阈值分割
otsu_threshold = filters.threshold_otsu(colored_labels)
binary_otsu = image > otsu_threshold

# 对二值图像进行形态学操作以去除噪声（可选）
binary_otsu = binary_otsu.astype(np.uint8)
binary_otsu = morphology.binary_opening(binary_otsu, selem=morphology.disk(3)) # type: ignore

# 显示原始图像、Otsu二值化结果以及分水岭分割结果
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(binary_otsu, cmap='gray')
ax[1].set_title('Otsu Thresholding')
ax[2].imshow(colored_labels)
ax[2].set_title('Watershed Segmentation')

cv2.imwrite('Otsu_Thresholding.jpg', (binary_otsu * 255).astype(np.uint8))
plt.tight_layout()
plt.show()