# 🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱
# Filename: script.py
# Author: AndrewC
# Description: Functions for our library
# DATASET: https://zzutk.github.io/SRNTT-Project-Page/
#
# dependencies: epeg
# 🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
import cv2

def parseFiles():
    p = "$HOME/dev/fall2022/664/project/data/001/"
    s = os.system(
        'ls ' + p + " >> $HOME/dev/fall2022/664/project/single_page_app/index/DATA/" + "Prototype")
    filename = "Users/andy/dev/fall2022/664/project/single_page_app/index/DATA/Prototype.txt"

    listOfFiles = []
    listOfPaths = []

    # Using readlines()
    file1 = open('./DATA/Prototype.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        listOfPaths.append(
            "/Users/andy/dev/fall2022/664/project/data/001/" + line.strip())
        listOfFiles.append(line.strip())
        print(line)

    # Begin Thumbnailer
    #listOfPaths = thumbnailer(listOfPaths)
    for i in listOfFiles:
        print(i)

    return listOfFiles

    # epeg -w 1536 -h 768 -q 50 worldmap.jpg epeg_thumb.jpg

# Thumbnailer


def thumbnailer(paths):
    for i in paths:
        image = Image.open(i)
        MAX_SIZE = (512, 512)
        image.thumbnail(MAX_SIZE)
        image.save('./PrototypeThumbnails/' +
                   i.strip("/Users/andy/dev/fall2022/664/project/data/001/"))

    return paths

def ImageMouse():
    fig, ax = plt.subplots()





    ax.set_title('Event Timeline', size=20)

    plugins.connect(fig, plugins.MousePosition(fontsize=14))
    mpld3.show()

def facialDetection(p):
    #path = "/static/data/001/" + p
    cascadePath = "/Users/andy/dev/fall2022/664/project/single_page_app/cascade.xml"

    faceCascade = cv2.CascadeClassifier("cascade.xml")

    image = cv2.imread(p)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE

    )

    print("Found {0} faces!".format(len(faces)))


if __name__ == "__main__":
    facialDetection("/Users/andy/dev/fall2022/664/project/single_page_app/static/data/001/intl-convention-204_4175471907_o.jpg")

