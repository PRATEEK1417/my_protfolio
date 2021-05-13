from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request,'index.html',{})


def photography(request):
    return render(request, "photography.html", {})

def resume(request):
    return render(request,"resume.html",{})
