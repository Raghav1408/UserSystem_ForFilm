from django.shortcuts import render, HttpResponse,Http404
from .models import User
from .forms import UserForm
from django.views.generic import FormView


def home(request):
    form = UserForm()
    return render(request, 'UserSystem_ForFilm/index.html', {'form': form})


def goto(request):
    opt_id = request.POST['opt']
    email=request.POST['email']
    Pass = request.POST['password']
    form = UserForm(request.POST)
    if opt_id=='1':
        new_user = User.object.create_user(email,password=Pass,is_crew=True)
        return render(request,'UserSystem_ForFilm/Crew.html', {'form' : form})
    if opt_id=='2':
        new_user = User.object.create_user(email, password=Pass, is_talent=True)
        return render(request, 'UserSystem_ForFilm/Talent.html', {'form' : form})
    if opt_id == '3':
        new_user = User.object.create_user(email, password=Pass, is_producer=True)
        return render(request, 'UserSystem_ForFilm/Service Provider.html', {'form' : form})
    if opt_id== '4':
        new_user = User.object.create_user(email, password=Pass, is_service_provider=True)
        return render(request, 'UserSystem_ForFilm/Producer.html', {'form' : form})
# Create your views here.
