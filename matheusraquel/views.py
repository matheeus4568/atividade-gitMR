from django.shortcuts import render

# Create your views here.
def raquel(request):
    return render(request, "raquel.html")

def matheus(request):
    return render(request, "matheus.html")