from django.shortcuts import render

# Create your views here.
def indexview(request):
    return render(request,'portfolio/index.html')

def resumeview(request):
    return render(request,'portfolio/resume.html')
