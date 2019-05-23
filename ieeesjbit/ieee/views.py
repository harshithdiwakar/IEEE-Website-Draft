from .models import Members, General, News,Announcement, Events
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.template import loader
from django.views.decorators.http import require_POST
from .forms import Post


def index(request):
    general = General.objects.all()
    index_template = loader.get_template('ieee/index.html')
    index_content = {'general': general,}
    return HttpResponse(index_template.render(index_content,request))


def committee(request):
    members = Members.objects.all()
    general = General.objects.all()
    member_template = loader.get_template('ieee/committee.html')
    member_content = {
        'members': members,
        'general': general,
    }
    return HttpResponse(member_template.render(member_content,request))


def news(request):
    news = News.objects.all()
    announce = Announcement.objects.all()
    news_template = loader.get_template('ieee/news.html')
    news_content = {
        'news': news,
        'announce': announce,
    }
    return HttpResponse(news_template.render(news_content,request))


def form(request):
    if request.method == 'POST':
        register = Registration(request.POST)

        if register.is_valid():
            text = form.cleaned_data['name', 'event_name', 'college', 'phone_number', 'email',]
            return HttpResponseRedirect('/ieee/')

    else:
        register = Registration()

    form_template = loader.get_template('ieee/form.html')
    form_content = {'register': register }
    return HttpResponse(form_template.render(form_content, request))

def events(request):
    event = Events.objects.all()
    general = General.objects.all()
    event_template = loader.get_template('ieee/events.html')
    event_content = {
        'event': event,
        'general':general,
    }
    return HttpResponse(event_template.render(event_content,request))

def about(request):
    return render(request,'ieee/about.html')

def excom(request):
    return render(request,'ieee/excom.html')

def gallery(request):
    return render(request,'ieee/gallery.html')

#def posts(request):
#    return render(request, 'ieee/posts.html')


def posts(request):
    post_form = Post()

    if post_form.is_valid():
        post_form.save()

    posts_content = {
        'form': post_form,
    }
    return render(request,'ieee/posts.html', posts_content)