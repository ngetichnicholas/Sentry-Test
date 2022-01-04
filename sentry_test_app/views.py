from django.shortcuts import render

# Create your views here.
def index(request):
    x=45
    y=0
    product = x/y
    print(product)
    return render(request,'indext.html')
