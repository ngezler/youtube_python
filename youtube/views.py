from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from .forms import LoginForm
# Create your views here.
class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        variableA = 'some text here'
        return render(request,self.template_name, {'variableA': variableA})

#login form
class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request,self.template_name, {'form': form})

    def post(self, request):
        Print("hello this is Post")
        return HttpResponse("This is ilogin view Post request.")

#class for uploading videos
class new_video(View):
    template_name = 'new_video.html'
    def get(self, request):
        variableA = 'Upload a new video'
        return render(request,self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse("This is index view Post request.")