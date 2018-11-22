from django.shortcuts import render

def editing(request):
    return render(request, 'videoediting/editing.html')

def reason(request):
    return render(request, 'videoediting/reason.html')

def consq(request):
    return render(request, 'videoediting/consq.html')

def onemoment(request):
    return render(request, 'videoediting/onemoment.html')

def camera(request):
    return render(request, 'videoediting/camera.html')
