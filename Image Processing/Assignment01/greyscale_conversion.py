import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

# Convert color image to greyscale by average
#
# grey pixel = (R + G + B) / 3
def average(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i,j]
            r = np.uint16(pixel[0])
            g = np.uint16(pixel[1])
            b = np.uint16(pixel[2])

            grey = (r + g + b) // 3

            image[i,j] = grey

# Convert color image to greyscale by weighted average
#
# grey pixel = 0.2126 * R + 0.7152 * G + 0.0722 * B
def weighted_average(image):
    red_weight = 0.2126
    green_weight = 0.7152
    blue_weight = 0.0722

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i,j]
            r = np.uint16(pixel[0])
            g = np.uint16(pixel[1])
            b = np.uint16(pixel[2])

            grey = np.uint8((red_weight * r) + (green_weight * g) + (blue_weight * b))

            image[i,j] = grey

# Load color image
image = misc.imread('../images/1/4.1.07-jelly-beans.tiff')
#image = misc.imread('../images/1/4.2.06-lake.tiff')

# Convert image to greyscale
average(image)
#weighted_average(image)

# Show image
plt.figure()
plt.imshow(image)
plt.show()
