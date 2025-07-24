import cv2 as cv
import numpy as np

img = cv.imread('l01-shadding-correction/tungsten_filament_shaded.tif').astype(np.float32)
shade = cv.imread('l01-shadding-correction/tungsten_sensor_shading.tif').astype(np.float32)

# The images have the same size, so resizing is not necessary

# Remove 0's from shade
shade[shade == 0] = 1e-5

result = img / shade

normalized = np.clip(result * 255.0, 0, 255).astype(np.uint8)

cv.imwrite('l01-shadding-correction/result.tif', normalized)
