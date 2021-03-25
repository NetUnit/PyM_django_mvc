from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.

# view1
def clock(request):
    dt.datetime.now()
    return render(request, 'clock.html', {})
    # return HttpResponse('[418]: I\'m a teapot' ) # alternative

# view2
def index1(request):

    return render(request, 'library_418.html', {})
    # return HttpResponse('[418]: I\'m a teapot') # alternative 

### http://127.0.0.1:8000/ - ip