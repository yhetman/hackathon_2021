# Duplicate  search with MSE
#not finished

import skimage.measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import shutil
import imghdr


IMAGE_PATH = r'./../../../media/images/'
DATE_PATH = r'./../../../media/result/date/'
LOCATION_PATH = r'./../../../media/result/location/'
WITHOUT_GROUP_PATH = r'./../../../media/result/without/'
DUPLICATES_PATH = r"./../../../media/result/duplicates/"


def compare_images():
    res = []

    if not os.path.exists(DUPLICATES_PATH):
        os.mkdir(DUPLICATES_PATH)

    for folder in [DATE_PATH, LOCATION_PATH, WITHOUT_GROUP_PATH]:
        duplicates = compare_group_images(folder)
        for path in duplicates:
            shutil.move(path, DUPLICATES_PATH)



def compare_group_images(directory, show_imgs=True, similarity="high", compression=50):
    """
    directory (str).........folder to search for duplicate/similar images
    show_imgs (bool)........True = shows the duplicate/similar images found in output
                            False = doesn't show found images
    similarity (str)........"high" = searches for duplicate images, more precise
                            "low" = finds similar images
    compression (int).......recommended not to change default value
                            compression in px (height x width) of the images before being compared
                            the higher the compression i.e. the higher the pixel size, the more computational ressources and time required
    """
    # list where the found duplicate/similar images are stored
    duplicates = []
    lower_res = []

    imgs_matrix = create_imgs_matrix(directory, compression)

    # search for similar images
    if similarity == "low":
        ref = 1000
    # search for 1:1 duplicate images
    else:
        ref = 200

    main_img = 0
    compared_img = 1
    nrows, ncols = compression, compression
    srow_A = 0
    erow_A = nrows
    srow_B = erow_A
    erow_B = srow_B + nrows

    while erow_B <= imgs_matrix.shape[0]:
        while compared_img < (len(image_files)):
            # select two images from imgs_matrix
            imgA = imgs_matrix[srow_A: erow_A,  # rows
                   0: ncols]  # columns
            imgB = imgs_matrix[srow_B: erow_B,  # rows
                   0: ncols]  # columns
            # compare the images
            rotations = 0
            while image_files[main_img] not in duplicates and rotations <= 3:
                if rotations != 0:
                    imgB = rotate_img(imgB)
                err = mse(imgA, imgB)
                if err < ref:
                    if show_imgs == True:
                        show_img_figs(imgA, imgB, err)
                        show_file_info(compared_img, main_img)
                    add_to_list(image_files[main_img], duplicates)
                    check_img_quality(directory, image_files[main_img], image_files[compared_img], lower_res)
                rotations += 1
            srow_B += nrows
            erow_B += nrows
            compared_img += 1

        srow_A += nrows
        erow_A += nrows
        srow_B = erow_A
        erow_B = srow_B + nrows
        main_img += 1
        compared_img = main_img + 1

    msg = "\n***\n DONE: found " + str(len(duplicates)) + " duplicate image pairs in " + str(
        len(image_files)) + " total images.\n The following files have lower resolution:"
    print(msg)
    return set(lower_res)


# Function that searches the folder for image files, converts them to a matrix
def create_imgs_matrix(directory, compression):
    global image_files
    image_files = []
    # create list of all files in directory
    folder_files = [filename for filename in os.listdir(directory)]

    # create images matrix
    counter = 0
    for filename in folder_files:
        if not os.path.isdir(directory + filename) and imghdr.what(directory + filename):
            img = cv2.imdecode(np.fromfile(directory + filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            if type(img) == np.ndarray:
                img = img[..., 0:3]
                img = cv2.resize(img, dsize=(compression, compression), interpolation=cv2.INTER_CUBIC)
                if counter == 0:
                    imgs_matrix = img
                    image_files.append(filename)
                    counter += 1
                else:
                    imgs_matrix = np.concatenate((imgs_matrix, img))
                    image_files.append(filename)
    return imgs_matrix


# Function that calulates the mean squared error (mse) between two image matrices
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


# Function that plots two compared image files and their mse
def show_img_figs(imageA, imageB, err):
    fig = plt.figure()
    plt.suptitle("MSE: %.2f" % (err))
    # plot first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # plot second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()


# Function for rotating an image matrix by a 90 degree angle
def rotate_img(image):
    image = np.rot90(image, k=1, axes=(0, 1))
    return image


# Function for printing filename info of plotted image files
def show_file_info(compared_img, main_img):
    print("Duplicate file: " + image_files[main_img] + " and " + image_files[compared_img])


# Function for appending items to a list
def add_to_list(filename, list):
    list.append(filename)


# Function for checking the quality of compared images, appends the lower quality image to the list
def check_img_quality(directory, imageA, imageB, list):
    size_imgA = os.stat(directory + imageA).st_size
    size_imgB = os.stat(directory + imageB).st_size
    if size_imgA > size_imgB:
        add_to_list(imageB, list)
    else:
        add_to_list(imageA, list)

if __name__ == "__main__":
    compare_images()