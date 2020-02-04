import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def show_with_plot(img, title):
    plt.figure()
    if 'gray' in title:
        plt.imshow(img, cmap='gray')
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    plt.show()


def part_a(img):
    return np.dot(img[..., :3], [0.299, 0.587, 0.114])


def part_b(img):
    # img = part_a(img)
    img[np.where(img >= 127)] = 255
    img[np.where(img < 127)] = 0
    return img


if __name__ == "__main__":
    img = cv.imread('Sponge.png')
    # print(img.shape)
    show_with_plot(img, 'Original')

    img = part_a(img)
    # print(img.shape)
    show_with_plot(img, '8bit gray scale')

    img = part_b(img)
    show_with_plot(img, '2bit gray scale')
