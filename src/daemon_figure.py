import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import imageio

# import resources

dpi = 72
fig = plt.figure(1, figsize=(1175 / dpi, 1280 / dpi), dpi=dpi, frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
img = mpimg.imread("image.jpg")
img2 = img.copy()
img2[:, :, 0] = img2[:, :, 1] = img2[:, :, 2] = (
    0.6 * img[:, :, 0] + 0.3 * img[:, :, 1] + 0.1 * img[:, :, 2]
)
ax2 = fig.add_axes([0.5, 0.5, 0.5, 0.5], frameon=False)
ax2.imshow(img2, aspect="equal")
print(img.shape, img)
# jaye ax.plot
imgplot = ax.imshow(img)
fig.savefig("plot.pdf")
