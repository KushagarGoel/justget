from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import mainform

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('Username')
            messages.success(request, f'New account created {username}')
            login(request, user)
            messages.info(request, f'Logged in as {username}')
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')

    form = UserCreationForm
    return render(request, 'main/register.html', context={"form": form})


def request_logout(request):
    logout(request)
    messages.info(request, f"Logout successful")
    return redirect("main:homepage")

def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,"Successfully logged in")
                return redirect("main:homepage")
            else:
                messages.info(request, "Either username or password is not correct")
        else:
            messages.info(request, "Data is not valid")

    form = AuthenticationForm
    return render(request,
                  "main/login.html",
                  {"form":form})


def show_account(request):
    return render(request=request, template_name='main/account.html')

class inpu(TemplateView):
    template = "main/home.html"

    def get(self, request):
        form = mainform()
        return render(request,
                      "main/home.html",
                      {"form": form,
                       })

    def post(self, request):
        form = mainform(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.error(request, f'Form saved')
                form = mainform()
                return redirect('main:homepage')
            except:
                messages.error(request, f'Please Login first')
                return redirect('main:register')
        else:
            messages.error(request, f'Please fill correct data')

        form = mainform()
        return render(request, "main/home.html",{'form': form} )

def show_it(request):
    return render(request,
                  "main/inp.html",
                  {'post': Post.objects.all})