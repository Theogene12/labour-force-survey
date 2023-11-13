from django.shortcuts import render

def home(request):
    context={}
    return render(request,"myApp/home.html", context)

def home(request):
    return render(request, "home.html", {})

def hom(request):
    return render(request, "hom.html", {})

def nyarugenge(request):
    return render(request, "nyarugenge.html", {})

def dashboard(request):
    return render(request, "dashboard.html", {})
def Gasabo(request):
    
    return render(request, "Gasabo.html", {})
def kicukiro(request):
    
    return render(request, "kicukiro.html", {})
def test(request):
    
    return render(request, "test.xlsx", {})
