import os
from shutil import copyfile


PATH = r'media/images/'
DATE_PATH = r'media/result/date/'
TIME_PATH = r'media/result/time/'
CLARITY_PATH = r'media/result/path/'
WITHOUT_GROUP_PATH = r'media/result/without/'


def sort_images(data):
    for image in data.iterrows():
        print(image[1][4], image[1][5])

        if (image[1][4] != -1):
            try:
                copyfile(image[1][0], DATE_PATH + str(image[1][4]) + "/" + image[1][0][12:])
            except IOError as io_err:
                os.makedirs(os.path.dirname(DATE_PATH + str(image[1][4]) + "/" + image[1][0][12:]))
                copyfile(image[1][0], DATE_PATH + str(image[1][4]) + "/" + image[1][0][12:])
        if (image[1][5] != -1):
            try:
                copyfile(image[1][0], TIME_PATH + str(image[1][5]) + "/" + image[1][0][12:])
            except IOError as io_err:
                os.makedirs(os.path.dirname(TIME_PATH + str(image[1][5]) + "/" + image[1][0][12:]))
                copyfile(image[1][0], TIME_PATH + str(image[1][5]) + "/" + image[1][0][12:])
        if (image[1][5] == -1 and image[1][4] == -1):
            try:
                copyfile(image[1][0], WITHOUT_GROUP_PATH + image[1][0][12:])
            except IOError as io_err:
                os.makedirs(os.path.dirname(WITHOUT_GROUP_PATH + image[1][0][12:]))
                copyfile(image[1][0], WITHOUT_GROUP_PATH + image[1][0][12:])

        if(image[1][5]==1):
            try:
                copyfile(image[[1][0], CLARITY_PATH + image[1][0][12:]])
            except IOError as io_err:
                os.makedirs(os.path.dirname(CLARITY_PATH + image[1][0][12:]))
                copyfile(image[1][0], CLARITY_PATH + image[1][0][12:])
