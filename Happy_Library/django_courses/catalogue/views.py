from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
# Create your views here.

# view1 - root
def index(request):
    return render(request, 'catalogue_200.html', {})
    # return HttpResponse('U r in a catalogue now') # alternative

# view2
def free(request):
    json_data = open('static/available.json')   
    data1 = json.load(json_data)                 
    data2 = json.dumps(data1)                     
    json_data.close()
    return JsonResponse(data2, safe=False)
    # return render(request, 'available.html', {}) # alternative

# view3
def on_hold(request):
    json_data = open('static/on-hold.json')   
    data1 = json.load(json_data)              
    data2 = json.dumps(data1)                   
    json_data.close()
    return JsonResponse(data2, safe=False)
    # return render(request, 'on-hold.html', {}) # alternative

# view4
def terms_output(request):
    json_data = open('static/terms.json')   
    data1 = json.load(json_data)              
    data2 = json.dumps(data1)                    
    json_data.close()
    return JsonResponse(data2, safe=False)
    # return render(request, 'terms.html', {}) # alternative
