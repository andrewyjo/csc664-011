import datetime
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render

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


def may(request):
    libraryForm = forms.libraryForm()
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

    for i in files:
        print(files.name)

    dates = []
    hist = []
    for i in files:
        dates.append(i.dateCreated.month)
        print(i.dateCreated.month)

    dates = sorted(Counter(dates).items())
    x, y = zip(*dates)

    print(x)
    print(y)
    # Create a random number generator with a fixed seed for reproducibility
    rng = np.random.default_rng(19680801)

    # Generate two normal distributions

    #fig, ax = plt.subplots()
    #bins = np.arange(1,14)
    #ax.hist(x, bins = bins, data=months, edgecolor="k", align='left')
    # ax.set_xticks(bins[:-1])
    #plt.plot(x,y,  marker='o', linestyle='none',)

    # We can set the number of bins with the *bins* keyword argument.

    #ax.set_title('Event Timeline', size=20)
    #plugins.connect(fig, plugins.MousePosition(fontsize=14))
    # mpld3.show()

    context = {
        'form': libraryForm,
        #    'currentLibrary': currentLibrary,
        'files': models.File.objects.all()
    }

    if 'libSelect' in request.POST:
        path = request.POST.get('path')
        name = request.POST.get('name')
        if libraryForm.is_valid():
            library = libraryForm.save()
            return render(request, "index/index.html", context)
        else:
            print(libraryForm.errors)
            return render(request, "index/index.html", context)

    if 'fdSelect' in request.POST:

        fdImg = "/Users/andy/dev/fall2022/664/project/single_page_app/static/data/001/" + \
            request.POST['fdSelect']

        numFaces = facialDetection(fdImg, request.POST['fdSelect'])
        current = models.File.objects.get(filename=request.POST['fdSelect'])
        current.faceCount = numFaces
        current.save()
        context = {
            'form': libraryForm,
            'files': models.File.objects.all(),
            'selected': models.File.objects.get(filename=request.POST['fdSelect'])
        }

        print(request.POST)
        return render(request, "index/may.html", context)

    return render(request, "index/may.html", context)


def june(request):
    libraryForm = forms.libraryForm()
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
    dates = []
    hist = []
    for i in files:
        dates.append(i.dateCreated.month)
        print(i.dateCreated.month)

    dates = sorted(Counter(dates).items())
    x, y = zip(*dates)

    print(x)
    print(y)
    # Create a random number generator with a fixed seed for reproducibility
    rng = np.random.default_rng(19680801)

    # Generate two normal distributions

    #fig, ax = plt.subplots()
    #bins = np.arange(1,14)
    #ax.hist(x, bins = bins, data=months, edgecolor="k", align='left')
    # ax.set_xticks(bins[:-1])
    #plt.plot(x,y,  marker='o', linestyle='none',)

    # We can set the number of bins with the *bins* keyword argument.

    #ax.set_title('Event Timeline', size=20)
    #plugins.connect(fig, plugins.MousePosition(fontsize=14))
    # mpld3.show()

    context = {
        'form': libraryForm,
        #    'currentLibrary': currentLibrary,
        'files': models.File.objects.all()
    }

    if 'libSelect' in request.POST:
        path = request.POST.get('path')
        name = request.POST.get('name')
        if libraryForm.is_valid():
            library = libraryForm.save()
            return render(request, "index/index.html", context)
        else:
            print(libraryForm.errors)
            return render(request, "index/index.html", context)

    if 'fdSelect' in request.POST:

        fdImg = "/Users/andy/dev/fall2022/664/project/single_page_app/static/data/001/" + \
            request.POST['fdSelect']

        numFaces = facialDetection(fdImg, request.POST['fdSelect'])
        current = models.File.objects.get(filename=request.POST['fdSelect'])
        current.faceCount = numFaces
        current.save()
        context = {
            'form': libraryForm,
            'files': models.File.objects.all(),
            'selected': models.File.objects.get(filename=request.POST['fdSelect'])
        }

        print(request.POST)
        return render(request, "index/june.html", context)

    return render(request, "index/june.html", context)


def july(request):
    libraryForm = forms.libraryForm()
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
    dates = []
    hist = []
    for i in files:
        dates.append(i.dateCreated.month)
        print(i.dateCreated.month)

    dates = sorted(Counter(dates).items())
    x, y = zip(*dates)

    print(x)
    print(y)
    # Create a random number generator with a fixed seed for reproducibility
    rng = np.random.default_rng(19680801)

    # Generate two normal distributions

    #fig, ax = plt.subplots()
    #bins = np.arange(1,14)
    #ax.hist(x, bins = bins, data=months, edgecolor="k", align='left')
    # ax.set_xticks(bins[:-1])
    #plt.plot(x,y,  marker='o', linestyle='none',)

    # We can set the number of bins with the *bins* keyword argument.

    #ax.set_title('Event Timeline', size=20)
    #plugins.connect(fig, plugins.MousePosition(fontsize=14))
    # mpld3.show()

    context = {
        'form': libraryForm,
        #    'currentLibrary': currentLibrary,
        'files': models.File.objects.all()
    }

    if 'libSelect' in request.POST:
        path = request.POST.get('path')
        name = request.POST.get('name')
        if libraryForm.is_valid():
            library = libraryForm.save()
            return render(request, "index/july.html", context)
        else:
            print(libraryForm.errors)
            return render(request, "index/july.html", context)

    if 'fdSelect' in request.POST:

        fdImg = "/Users/andy/dev/fall2022/664/project/single_page_app/static/data/001/" + \
            request.POST['fdSelect']

        numFaces = facialDetection(fdImg, request.POST['fdSelect'])
        current = models.File.objects.get(filename=request.POST['fdSelect'])
        current.faceCount = numFaces
        current.save()
        context = {
            'form': libraryForm,
            'files': models.File.objects.all(),
            'selected': models.File.objects.get(filename=request.POST['fdSelect'])
        }

        print(request.POST)
        return render(request, "index/july.html", context)

    return render(request, "index/july.html", context)


def november(request):
    libraryForm = forms.libraryForm()
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
    dates = []
    hist = []
    for i in files:
        dates.append(i.dateCreated.month)
        print(i.dateCreated.month)

    dates = sorted(Counter(dates).items())
    x, y = zip(*dates)

    print(x)
    print(y)
    # Create a random number generator with a fixed seed for reproducibility
    rng = np.random.default_rng(19680801)

    # Generate two normal distributions

    #fig, ax = plt.subplots()
    #bins = np.arange(1,14)
    #ax.hist(x, bins = bins, data=months, edgecolor="k", align='left')
    # ax.set_xticks(bins[:-1])
    #plt.plot(x,y,  marker='o', linestyle='none',)

    # We can set the number of bins with the *bins* keyword argument.

    #ax.set_title('Event Timeline', size=20)
    #plugins.connect(fig, plugins.MousePosition(fontsize=14))
    # mpld3.show()

    context = {
        'form': libraryForm,
        #    'currentLibrary': currentLibrary,
        'files': models.File.objects.all()
    }

    if 'libSelect' in request.POST:
        path = request.POST.get('path')
        name = request.POST.get('name')
        if libraryForm.is_valid():
            library = libraryForm.save()
            return render(request, "index/november.html", context)
        else:
            print(libraryForm.errors)
            return render(request, "index/november.html", context)

    if 'fdSelect' in request.POST:

        fdImg = "/Users/andy/dev/fall2022/664/project/single_page_app/static/data/001/" + \
            request.POST['fdSelect']

        numFaces = facialDetection(fdImg, request.POST['fdSelect'])
        current = models.File.objects.get(filename=request.POST['fdSelect'])
        current.faceCount = numFaces
        current.save()
        context = {
            'form': libraryForm,
            'files': models.File.objects.all(),
            'selected': models.File.objects.get(filename=request.POST['fdSelect'])
        }

        print(request.POST)
        return render(request, "index/november.html", context)

    return render(request, "index/november.html", context)
