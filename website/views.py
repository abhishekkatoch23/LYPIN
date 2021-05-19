from django.shortcuts import render, HttpResponse

# Create your views here.


def about(request):
    return HttpResponse("this is aboutpage")

def index(request):
    return render(request, 'index.html', {})

def cbse(request):
    return render(request, 'cbse.html', {})

def icse(request):
    return render(request, 'icse.html', {})    

def cbseclass10(request):
    return render(request, 'cbse-class10.html', {})  

def icseclass10(request):
    return render(request, 'icse-class10.html', {})        

def cbseclass12(request):
    return render(request, 'cbse-class12.html', {})     

def icseclass12(request):
    return render(request, 'icse-class12.html', {})

def pu(request):
    return render(request, 'pu.html', {})

def ba(request):
    return render(request, 'ba.html', {})

def ba1(request):
    return render(request, 'ba1.html', {})