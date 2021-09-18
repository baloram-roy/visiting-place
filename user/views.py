from user.models import Profile
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                # return render(request, 'place/place_list.html')
                return redirect('place-list')
        else:
            print('Username:{} and Password {}'.format(username,password))
            return HttpResponse('invlid login details')
    else:       
        return render(request,'user/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'Your account has been created {username}')
            return redirect('place-list')

    else:
        form = RegisterForm()
    return render(request,'user/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user-login')

def profile_view(request):
    return render(request, 'user/profile.html')




