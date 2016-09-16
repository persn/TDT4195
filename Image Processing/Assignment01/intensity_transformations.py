import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def negative(image):
    return 255 - image

def gamma(image, c, gamma):
    imagelog = image.astype(np.float32)
    imagelog /= 255
    imagelog = c * (imagelog ** gamma)

    return imagelog

# Load color image
image = misc.imread('../images/1/5.1.10-aerial.tiff', mode = 'L')
#image = misc.imread('../images/1/5.2.09-aerial.tiff', mode = 'L')

# Apply intensity transformation to image
image = negative(image)
#image = gamma(image, 1, 5)

# Show image
plt.figure()
plt.imshow(image, cmap=plt.cm.gray)
plt.show()
