import datetime
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render, redirect
from operator import attrgetter
from . import forms
from . import models
import os

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

import mpld3
from mpld3 import plugins

import cv2

from django.core import serializers

selectedLibraryFiles = []
currentEvent = 0

def sendEventJSON():
    json_serializer = serializers.get_serializer("json")()
    events = json_serializer.serialize(models.Event.objects.all().order_by('id')[:5], ensure_ascii=False)

def refEvent(request,val):
    files = models.File.objects.get(event_id = val)
    events = models.Event.objects.all()

    eventannotation = forms.emptyEventForm()
    #mainevent = models.Event.objects.get(id = 50)
    context = {
        'files': files,
        'events': events,
        'eventannotation':eventannotation,
        'selectedLibraryFiles':selectedLibraryFiles,
    }
    return render( request, 'index/test2.html', context)

def test2(request):

    files = models.File.objects.all()
    events = models.Event.objects.all()
    json_serializer = serializers.get_serializer("json")()

    eventsJSON = json_serializer.serialize(models.Event.objects.all())

    eventannotation = forms.emptyEventForm()
    #mainevent = models.Event.objects.get(id = 50)
    context = {
        'files': files,
        'events': events,
        'eventannotation':eventannotation,
        'selectedLibraryFiles':selectedLibraryFiles,
        'currentEvent':currentEvent,
        'eventsJSON': eventsJSON
    }

    if 'eventannotationbtn' in request.POST:
        eventannotation = forms.emptyEventForm(request.POST)
        #print(request.POST['name'][0])
        if eventannotation.is_valid():
            starttime1= min(selectedLibraryFiles, key=attrgetter('start_time'))
            endtime1= max(selectedLibraryFiles, key=attrgetter('end_time'))
            event = models.Event.objects.create(name=request.POST['name'],starttime=starttime1.start_time, endtime=endtime1.end_time)
            event.save()

            #event.starttime = min(selectedLibraryFiles, key=attrgetter('start_time'))
            #event.endtime = min(selectedLibraryFiles, key=attrgetter('end_time'))
            print(starttime1.start_time, " " ,endtime1.end_time)
            
            for x in selectedLibraryFiles:
                entry = models.File.objects.get(name = x.filename)
                entry.event_id = event
                entry.save()
                #print(entry.filename)
                print(x.start_time)
            

            #print(event.starttime.start_time, "|" , event.endtime)

            #print(request.POST.getlist('selectFile'))
        return render( request, 'index/test2.html', context)

    elif 'imgclickbtn' in request.POST:

        for y in models.File.objects.filter(name = request.POST['imgclickbtn']):
            selectedLibraryFiles.append(y)
            print(y.name)
        


        return render( request, 'index/test2.html', context)

    elif 'eventSelector' in request.POST:
        if request.POST['eventSelector'] != '0':
            print("hi not 57")
            files = models.File.objects.filter(event = request.POST['eventSelector'])
            json_serializer = serializers.get_serializer("json")()
            context = {
                'files': files,
                'events': events,
                'eventannotation':eventannotation,
                'selectedLibraryFiles':selectedLibraryFiles,
                'currentEvent': json_serializer.serialize(models.Event.objects.filter(id = request.POST['eventSelector'])),
                'eventsJSON': eventsJSON

            }
            #Calculating start and end time from a list of files
            #Attain a list of start dates, and find the min
            #find the max
            #These will be the threshold for events

            print(files)
            print(request.POST['eventSelector'])
            print( json_serializer.serialize(models.Event.objects.filter(id = request.POST['eventSelector'])))
            return render( request, 'index/test2.html', context)
        else:
            print("hi 57")
            #files = models.File.objects.all()
            json_serializer = serializers.get_serializer("json")()
            #events = json_serializer.serialize(models.File.objects.filter(event = request.POST['eventSelector']))
            context = {
                'files': files,
                'events': events,
                'eventannotation':eventannotation,
                'selectedLibraryFiles':selectedLibraryFiles,
                'currentEvent': json_serializer.serialize(models.Event.objects.filter(id = request.POST['eventSelector'])),
                'eventsJSON': eventsJSON

            }
            print( json_serializer.serialize(models.Event.objects.filter(id = request.POST['eventSelector'])))
            #context = {
            #    'files': files,
            #    'events': events,
            #    'eventannotation':eventannotation,
            #    'selectedLibraryFiles':selectedLibraryFiles,
            #    'currentEvent':currentEvent
            #}
            print(request.POST['eventSelector'])
            #return render( request, 'index/test2.html', context)
            return redirect(test2)


    return render( request, 'index/test2.html', context)



def timeline(request):
    context = {
        'events' : models.Event.objects.all(),
        'files' : models.File.objects.all(),
        'years' : ["2009", "2019", "2022"],
    }
    events =  models.Event.objects.filter()

    return render(request, 'index/timeline.html', context)


def spatialdata(request):
    context = {
        'events' : models.Event.objects.all(),
        'files' : models.File.objects.all(),
   }

    return render(request, 'index/dbeaver.html')



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
    events = models.Event.objects.all()
    #mainevent = models.Event.objects.get(id = 50)
    context = {
        'files': files,
        'events': events,
        #'mainevent': mainevent
    }

    return render(request, "index/index.html", context)

def newEvent(request):
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

    years = ["2022", "2019", "2009"]


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

