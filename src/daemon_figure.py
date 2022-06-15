import os
from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import imageio

# import resources

dpi = 72
# fig = plt.figure(1, figsize=(1175 / dpi, 1280 / dpi), dpi=dpi, frameon=False)
# ax = fig.add_axes([0, 0, 1, 1])
# img = mpimg.imread("image.jpg")
# img2 = img.copy()
# img2[:, :, 0] = img2[:, :, 1] = img2[:, :, 2] = (
#     0.6 * img[:, :, 0] + 0.3 * img[:, :, 1] + 0.1 * img[:, :, 2]
# )
# ax2 = fig.add_axes([0.5, 0.5, 0.5, 0.5], frameon=False)
# ax2.imshow(img2, aspect="equal")
# print(img.shape, img)
# # jaye ax.plot
# imgplot = ax.imshow(img)
# fig.savefig("plot.pdf")

# y = np.random.randint(30, 40, size=(40))
# y = np.linspace(0, np.pi * 2, 50)
y = np.linspace(0, (3.14) * 2, 50)

print(np.sin(y))
filenames = []
# for i in y:
for i in y:
    # plot the line chart
    # plt.plot(y[:i])
    # plt.ylim(20, 50)
    fig = plt.figure(1, figsize=(1175 / dpi, 1280 / dpi), dpi=dpi, frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    img = mpimg.imread("../resources/image.jpg")
    imgplot = ax.imshow(img)

    img2 = img.copy()
    img2[:, :, 0] = img2[:, :, 1] = img2[:, :, 2] = (
        0.6 * img[:, :, 0] + 0.3 * img[:, :, 1] + 0.1 * img[:, :, 2]
    )
    ax2 = fig.add_axes([0.5, 0.5, 0.5, 0.5], frameon=False)
    ax2.imshow(img2, aspect="equal")

    ax3 = fig.add_axes([0, 0, 1, 0.5], frame_on=False)
    ax3.plot(y + i, np.sin(y + i))

    # create file name and append it to a list
    filename = f"{i}.png"
    filenames.append(filename)

    # save frame
    plt.savefig(filename)
    plt.close()
# build gif
with imageio.get_writer("mygif.gif", mode="I") as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove files
for filename in set(filenames):
    os.remove(filename)
