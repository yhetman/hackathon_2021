import pandas as pd
from shutil import copyfile


PATH = r'media/images/'
DATE_PATH = r'media/result/date/'
TIME_PATH = r'media/result/time/'
CLARITY_PATH = r'media/result/path/'
WITHOUT_GROUP_PATH = r'media/result/without/'

def sort_images(data):
    for image in data.iterrows():
        if (image["date"] != -1):
            copyfile(PATH+image["path"], DATE_PATH + image["date"] + "/" + image["path"])
        if (image["time"] != -1):
            copyfile(PATH+image["path"], TIME_PATH + image["time"] + "/" + image["path"])
        elif(image["date"] != -1):
            copyfile(PATH + image["path"], WITHOUT_GROUP_PATH + image["path"])

        if(image['clarity']): copyfile(PATH + image['path'], CLARITY_PATH + image["path"])
