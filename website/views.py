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
    
def ba2(request):
    return render(request, 'ba2.html', {})

def ba3(request):
    return render(request, 'ba3.html', {})

def ba4(request):
    return render(request, 'ba4.html', {})

def ba5(request):
    return render(request, 'ba5.html', {})

def ba6(request):
    return render(request, 'ba6.html', {})

def bcom(request):
    return render(request, 'bcom.html', {})

def bcom1(request):
    return render(request, 'bcom1.html', {})

def bcom2(request):
    return render(request, 'bcom2.html', {})

def bcom3(request):
    return render(request, 'bcom3.html', {})

def bcom4(request):
    return render(request, 'bcom4.html', {})

def bcom5(request):
    return render(request, 'bcom5.html', {})

def bcom6(request):
    return render(request, 'bcom6.html', {})
