from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test

# Create your views here.
def index(request):
    return render(request,'index.html')

def my_task_test(request):
    test.delay(10)
    return HttpResponse('response done')

