from django.shortcuts import render
from django.http import HttpResponse


#
def index(request):
    return HttpResponse("<h1>sdfsfsdfsdf</h1>")
    # return render(request, 'demo/index.html')
