from django.shortcuts import render
from django.views.generic.base import View, HttpResponse

# Create your views here.
class index(View):
    template_name = 'index.html'
    def get(self, request):
        variableA = 'some text here'
        return render(request,self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse("This is index view Post request.")




#class for uploading videos
class new_video(View):
    template_name = 'new_video.html'
    def get(self, request):
        variableA = 'Upload a new video'
        return render(request,self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse("This is index view Post request.")