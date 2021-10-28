from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        pass

class About(View):
    def get(self, request):
        return render(request, 'about.html')