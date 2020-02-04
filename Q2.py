import cv2 as cv
import matplotlib.pyplot as plt


def show(img, title):
    plt.figure()
    img = img.astype('uint8')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    plt.show()


def floyd_steinberg_with_error(img):
    h = img.shape[0]
    w = img.shape[1]
    img = img.astype('int16')
    for i in range(0, h - 1):
        for j in range(0, w - 1):
            pixel_red = img[i][j][0]
            pixel_green = img[i][j][1]
            pixel_blue = img[i][j][2]
            new_red = round(pixel_red * 3 / 255) * 255 / 3
            new_green = round(pixel_green * 3 / 255) * 255 / 3
            new_blue = round(pixel_blue * 3 / 255) * 255 / 3
            img[i][j][0] = new_red
            img[i][j][1] = new_green
            img[i][j][2] = new_blue
            error_red = pixel_red - new_red
            error_green = pixel_green - new_green
            error_blue = pixel_blue - new_blue
            img[i][j+1][0] = (img[i][j+1][0] + error_red * 7 / 16)
            img[i][j+1][1] = (img[i][j+1][1] + error_green * 7 / 16)
            img[i][j+1][2] = (img[i][j+1][2] + error_blue * 7 / 16)
            img[i+1][j-1][0] = (img[i+1][j-1][0] + error_red * 3 / 16)
            img[i+1][j-1][1] = (img[i+1][j-1][1] + error_green * 3 / 16)
            img[i+1][j-1][2] = (img[i+1][j-1][2] + error_blue * 3 / 16)
            img[i+1][j][0] = (img[i+1][j][0] + error_red * 5 / 16)
            img[i+1][j][1] = (img[i+1][j][1] + error_green * 5 / 16)
            img[i+1][j][2] = (img[i+1][j][2] + error_blue * 5 / 16)
            img[i+1][j+1][0] = (img[i+1][j+1][0] + error_red * 1 / 16)
            img[i+1][j+1][1] = (img[i+1][j+1][1] + error_green * 1 / 16)
            img[i+1][j+1][2] = (img[i+1][j+1][2] + error_blue * 1 / 16)
    img = img.astype('uint16')
    show(img, 'floyd Steinberg with error')


def floyd_steinberg_without_error(img):
    h = img.shape[0]
    w = img.shape[1]
    img = img.astype('int16')

    # new_image = np.copy(img)
    for i in range(0, h - 1):
        for j in range(0, w - 1):
            pixel_red = img[i][j][0]
            pixel_green = img[i][j][1]
            pixel_blue = img[i][j][2]
            new_red = (round(pixel_red * 3 / 255) * 255 / 3)
            new_green = (round(pixel_green * 3 / 255) * 255 / 3)
            new_blue = (round(pixel_blue * 3 / 255) * 255 / 3)
            img[i][j][0] = new_red
            img[i][j][1] = new_green
            img[i][j][2] = new_blue
    img = img.astype('uint16')
    show(img, 'floyd Steinberg without error')


if __name__ == "__main__":
    img = cv.imread('Sponge.png')
    floyd_steinberg_with_error(img)
    # floyd_steinberg_without_error(img)
