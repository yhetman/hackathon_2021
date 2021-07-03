import pandas as pd
from shutil import copyfile


PATH = "app/media/input/"
DATE_PATH = "/media/output/date/"
TIME_PATH = "/media/output/time/"
CLARITY_PATH = "/media/output/path/"
WITHOUT_GROUP_PATH = "/media/output/without/"

def sort_images(data: pd.DataFrame):
    for image in data.iterrows():
        if (image["date"] != -1):
            copyfile(PATH+image["path"], DATE_PATH + image["date"] + "/" + image["path"])
        if (image["time"] != -1):
            copyfile(PATH+image["path"], TIME_PATH + image["time"] + "/" + image["path"])
        elif(image["date"] != -1):
            copyfile(PATH + image["path"], WITHOUT_GROUP_PATH + image["path"])

        if(image["clarity"]): copyfile(PATH + image["path"], CLARITY_PATH + image["path"])
