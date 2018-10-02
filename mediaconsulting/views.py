from django.shortcuts import render

# Create your views here.
def mediaconsulting(request):
    return render (request, 'mediaconsulting/consulting.html')
