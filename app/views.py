from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_Topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic insertion is completed')




def insert_Webpage(request):
    t_n=input('enter the topic name')
    n=input('enter the name')
    u=input('enter the url')
    TO=Topic.objects.get_or_create(topic_name=t_n)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('web page insertion completed')







def insert_Accessrecords(request):
    t_n=input('enter the topic name')
    w_n=input('enter the webname')
    a=input('enter the author')
    d=input('enter the date')
    u=input('enter the url')
    TO=Topic.objects.get_or_create(topic_name=t_n)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=w_n,url=u)[0]
    WO.save()
    AO=Accessrecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    AO.save()
    return HttpResponse('accessrecords insertion copmpleted')