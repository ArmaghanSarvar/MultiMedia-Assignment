from matplotlib import pyplot as plt
import cv2 as cv
from Pixel import Pixel
import operator
import numpy as np

image = cv.imread('Sponge.png')


def show(img, title):
    plt.figure()
    img = img.astype('uint8')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    plt.show()


def part_a():
    channels = cv.split(image)
    colors = ("b", "g", "r")
    plt.figure()

    for (chan, color) in zip(channels, colors):
        # histogram for each channel
        hist = cv.calcHist([chan], [0], None, [256], [0, 256])
        # plot the histogram
        plt.plot(hist, color=color)
        plt.title(color + " Histogram")
        plt.xlim([0, 256])
        plt.show()


def print_pixlist(pixels_list):
    for i in range(0, len(pixels_list) - 1):
        print(pixels_list[i].value)


def show_final(list_pix):
    new_img = np.zeros((h, w, 3))
    for pixel in list_pix:
            new_img[pixel.x][pixel.y][0] = mapping_colors[pixel.value][0]
            new_img[pixel.x][pixel.y][1] = mapping_colors[pixel.value][1]
            new_img[pixel.x][pixel.y][2] = mapping_colors[pixel.value][2]
    show(new_img, 'Final')


pixels_list = []
h, w = image.shape[0:2]
for i in range(0, h):
    for j in range(0, w):
        pixels_list.append(Pixel(image[i][j][0], image[i][j][1], image[i][j][2], i, j))


def median_cut(pixels_list, bit_number):
    global mapping_colors
    if bit_number == 8:
        red_sum = 0
        green_sum = 0
        blue_sum = 0
        for i in range(0, len(pixels_list)):
            red_sum += pixels_list[i].red
            green_sum += pixels_list[i].green
            blue_sum += pixels_list[i].blue
        red_avg = red_sum/len(pixels_list)
        green_avg = green_sum/len(pixels_list)
        blue_avg = blue_sum/len(pixels_list)
        mapping_colors[pixels_list[0].value].append((red_avg))
        mapping_colors[pixels_list[0].value].append((green_avg))
        mapping_colors[pixels_list[0].value].append((blue_avg))
        return
    if bit_number % 3 == 0:
        pixels_list.sort(key=operator.attrgetter('red'))
    elif bit_number % 3 == 1:
         pixels_list.sort(key=operator.attrgetter('green'))
    elif bit_number % 3 == 2:
        pixels_list.sort(key=operator.attrgetter('blue'))
    for i in range(0, len(pixels_list)):
        if i < len(pixels_list) // 2:
            pixels_list[i].value = pixels_list[i].value * 2
        else:
            pixels_list[i].value = pixels_list[i].value * 2 + 1
    median_cut(pixels_list[0:len(pixels_list)//2], bit_number + 1)
    median_cut(pixels_list[len(pixels_list)//2:len(pixels_list)], bit_number + 1)


mapping_colors = [[]]
for i in range(0, 256):
    mapping_colors.append([])

median_cut(pixels_list, 0)
print(mapping_colors)
show_final(pixels_list)
