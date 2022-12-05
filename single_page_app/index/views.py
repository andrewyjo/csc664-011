import datetime
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render, redirect

from . import forms
from . import models
import os

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

import mpld3
from mpld3 import plugins

import cv2




# create a function
def facialDetection(p, filename):
    #path = "/static/data/001/" + p
    cascadePath = "/Users/andy/dev/fall2022/664/project/single_page_app/cascade.xml"

    faceCascade = cv2.CascadeClassifier("cascade.xml")

    image = cv2.imread(p)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE

    )

    print("Found {0} faces!".format(len(faces)))
    numFaces = len(faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite(os.path.join(
        "/Users/andy/dev/fall2022/664/project/single_page_app/static/fd/001/", filename), image)

    return numFaces


def index(request):
    #currentLibrary = models.Library.objects.get(id=1)

    #os.system('ls ../data/001/ >> filelist.txt')

    # Init Library Files
    # for i,j in zip(open('filelist.txt') ,open('datelist.txt')):
    #   x = "/Users/andy/dev/fall2022/664/project/single_page_app/static/data/001/" + i
    #   #os.system(x)
    #   #exiftool -d "%Y-%m-%d %H:%M:%S" venice-beach-2022_52095619642_o.jpg | grep 'Create Date' | head -1 | awk '{print $4,$5,$6}'

    #   #SAVING NEW FILES TO DB
    #   blob = models.File(filename=i.rstrip(), path=x.rstrip() , dateCreated=j.rstrip())
    #   blob.save()
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
              "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN"]

    files = models.File.objects.all()
    context = {
        'files': files
    }

    return render(request, "index/index.html", context)

def bubbles(request):
    #currentLibrary = models.Library.objects.get(id=1)

    #os.system('ls ../data/001/ >> filelist.txt')

    # Init Library Files
    # for i,j in zip(open('filelist.txt') ,open('datelist.txt')):
    #   x = "/Users/andy/dev/fall2022/664/project/single_page_app/static/data/001/" + i
    #   #os.system(x)
    #   #exiftool -d "%Y-%m-%d %H:%M:%S" venice-beach-2022_52095619642_o.jpg | grep 'Create Date' | head -1 | awk '{print $4,$5,$6}'

    #   #SAVING NEW FILES TO DB
    #   blob = models.File(filename=i.rstrip(), path=x.rstrip() , dateCreated=j.rstrip())
    #   blob.save()
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
              "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN"]

    files = models.File.objects.all()
    selectedFiles = []

    emptyEventForm = forms.emptyEventForm()

    selectedFiles = request.POST.getlist('selectFile')

    if request.method == 'POST':
        emptyEventForm = forms.emptyEventForm(request.POST)
        if emptyEventForm.is_valid():
            event = emptyEventForm.save()
            print(event.id)
            for x in request.POST.getlist('selectFile'):
                entry = models.File.objects.get(id = x)
                entry.event = event
                entry.save()
            print(request.POST.getlist('selectFile'))

            context = {
                'event' : models.Event.objects.get(id = event.id),
                #'files' : models.File.objects.all(event = event)
            }
            return redirect(index)

            #return render(request, "index/eventViewer.html", context)





    #if request.method == 'POST':




    context = {
        'files': files,
        'months': months,
        'emptyEventForm':emptyEventForm
    }

    return render(request, "index/test.html", context)

