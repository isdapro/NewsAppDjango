from django.shortcuts import get_object_or_404,render
from eventregistry import *
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import datetime
from django.utils import timezone
from newsapi import NewsApiClient
from django.shortcuts import redirect
from users.models import Tasks
from django.urls import reverse
from pycountry_convert import *
from predicthq import Client
import time

# Create your views here.
def home(request):
    '''
    The code for EventRegistry
    er = EventRegistry(apiKey = settings.NEWS_APP_KEY)
    q = QueryArticlesIter(dateStart = datetime.datetime.now() + datetime.timedelta(days=-30), sourceGroupUri = "general/ERtop50")
    #q = GetTrendingConcepts(source = "news", count = 10)
    #q.setRequestedResult(RequestEventsInfo(count=20, sortBy="date"))
    titl=[]
    desc=[]
    loc=[]
    dat=[]
    for event in q.execQuery(er, sortBy = "date",maxItems=20, returnInfo = ReturnInfo(articleInfo=ArticleInfoFlags(location=True))):
        titl.append(event)
        #desc.append(event['summary'])
        loc.append(event['location']['label'])
        #dat.append(event['date'])
    #res = er.execQuery(q)

    mylist = zip(titl,desc,loc,dat)

    return HttpResponse(titl)
    '''
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    newsapi = NewsApiClient (api_key = settings.NEWS_API_KEY)
    topheadlines = newsapi.get_top_headlines(sources='abc-news,al-jazeera-english,associated-press,business-insider,cnn,bbc-news',page_size=15)

    articles = topheadlines['articles']

    titl=[]
    desc=[]
    img=[]

    for art in articles:
        titl.append(art['title'])
        desc.append(art['description'])
        img.append(art['urlToImage'])

    mylist = zip(titl,desc,img)

    return render(request, 'home.html', {'mylist':mylist})

    #return render(request, 'home.html')


def search(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    search_val = request.POST.get("search")
    #print(request.POST)
    newsapi = NewsApiClient (api_key = settings.NEWS_API_KEY)
    search_articles = newsapi.get_everything(q=search_val, page_size=100, from_param = datetime.datetime.now() + timezone.timedelta(days=-30))['articles']

    phq = Client(access_token=settings.EVENT_API_KEY)
    titl2=[]
    desc2=[]
    date=[]
    for ev in phq.events.search(q=search_val, limit=100, relevance="rank"):
        titl2.append(ev.title[:500])
        desc2.append(ev.description[:500]) if (ev.description) else desc2.append(ev.description)

        dateTime = ev.start.strftime("%Y-%m-%d %H:%M:%S")
        date.append(dateTime[:11])


    titl=[]
    desc=[]
    #img=[]

    for art in search_articles:
        titl.append(art['title'][:500])
        desc.append(art['description'][:1000]) if (art['description']) else desc.append(art['description'])
        #img.append(art['urlToImage'])

    mylist = zip(titl,desc)
    mylist2 = zip(titl2,desc2,date)

    return render(request, 'News/search.html', {'mylist':mylist,'mylist2':mylist2})

    #return render(request, 'News/search.html')
def addtask(request):
    currentuser = request.user
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    Tasks.objects.create(user=currentuser, task_title=title, task_desc=desc)

    return HttpResponseRedirect(reverse('mytasks'))

def removetask(request):
    currentuser = request.user
    object_id = request.POST.get("primary")
    Tasks.objects.filter(user=currentuser, pk=object_id).delete()

    return HttpResponseRedirect(reverse('mytasks'))


def myloc(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    currentuser = request.user
    loc_temp = currentuser.location
    loc=country_name_to_country_alpha2(loc_temp).lower()
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    search_articles = newsapi.get_top_headlines(country=loc, page_size = 100)['articles']

    titl2=[]
    desc2=[]
    date=[]


    phq = Client(access_token=settings.EVENT_API_KEY)
    for ev in phq.events.search(country=loc, limit=50, relevance = "rank"):
        titl2.append(ev.title[:500])
        desc2.append(ev.description[:500]) if (ev.description) else desc2.append(ev.description)

        dateTime = ev.start.strftime("%Y-%m-%d %H:%M:%S")
        date.append(dateTime[:11])



    titl=[]
    desc=[]
    #img =[]

    for art in search_articles:
        titl.append(art['title'][:500])
        desc.append(art['description'][:1000]) if (art['description']) else desc.append(art['description'])
        #img.append(art['urlToImage'])


    mylist = zip(titl,desc)
    mylist2 = zip(titl2,desc2,date)

    return render(request, 'News/myloc.html', {'mylist':mylist, 'mylist2':mylist2})

def mytasks(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request,'News/mytasks.html')
