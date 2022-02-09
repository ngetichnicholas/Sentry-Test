from django.shortcuts import render
from django.http import HttpResponse
from .tasks import my_first_task

# Create your views here.
def index(request):
    return render(request,'index.html')

def my_task_test(request):
    my_first_task.delay(10)
    return HttpResponse('response done')

