from django.shortcuts import render



# Create your views here.


def index(req):
    return render(req, 'template/pages/index.html')


def about(req):
    return render(req, 'template/pages/about.html')
