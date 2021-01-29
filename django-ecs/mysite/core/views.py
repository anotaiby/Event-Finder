from .forms import NameForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.templatetags.static import static
from django.template import loader
from .models import Event
import datetime


def home(request):
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def delete(request, event_id):
    if request.user.is_authenticated:
        username = request.user.username

    instance = Event.objects.get(id=event_id)
    if(instance and instance.username == username):
        title = instance.title
        instance.delete()
        return render(request, 'home.html', {'msg': 'Deleted event {}'.format(title)})
    else:
        return render(request, 'home.html', {'msg': 'You are not authorised to delete event {}'.format(instance.title)})


def detail(request, event_id):
    q = Event.objects.get(pk=event_id)
    img_url = q.image
    return render(request, 'detail.html', {'e': q})


@login_required
def edit(request, event_id):
    
    username = request.user.username
    instance = Event.objects.get(id=event_id)
    if(instance and instance.username == username):    
        q = Event.objects.get(pk=event_id)
        if request.method == 'POST':
            form = NameForm(request.POST,  request.FILES)
            if form.is_valid():
                q.title = form.cleaned_data.get('title')
                q.desc = form.cleaned_data.get('desc')
                q.venue = form.cleaned_data.get('venue')
                q.image = form.cleaned_data.get('image')
                q.contact = form.cleaned_data.get('contact')
                q.time = form.cleaned_data.get('time')
                q.save()

                return redirect('/' + str(event_id))
            # else
                # return HttpResponse('You are looking at event {} {}.<br> {} <img src="{}"> '.format(event_id, q.title, q.desc, img_url))

        else:
            form = NameForm(initial={'title': q.title,
                                    'desc': q.desc, 'venue': q.venue,
                                    'image': q.image,
                                    'contact':q.contact,
                                    'time': q.time})
        return render(request, 'add.html', {'form': form, 'data': {'id': event_id, 'url': str(event_id) + '/edit'}})
    else:
        return render(request, 'home.html', {'msg': 'You are not authorised to edit event {}'.format(instance.title)})

def index(request):
    latest_event_list = Event.objects.order_by('-time')[:25]
    template = loader.get_template('index.html')
    context = {
        'latest_event_list': latest_event_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def add(request):
    if request.method == 'POST':
        form = NameForm(request.POST,  request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            venue = form.cleaned_data.get('venue')
            image = form.cleaned_data.get('image')
            time = form.cleaned_data.get('time')
            contact = form.cleaned_data.get('contact')
            username = request.user.username
            store_corporate = Event(
                title=title,
                desc=desc,
                venue=venue,
                image=image,
                time=time,
                contact=contact,
                username=username)
            store_corporate.save()
            return render(request, 'home.html', {'msg': 'Added event {}'.format(title)})
    else:
        form = NameForm(initial={'time': datetime.date.today()})
    return render(request, 'add.html', {'form': form, 'data': {'url': 'add'}})
