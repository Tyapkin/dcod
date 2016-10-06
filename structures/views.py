from django.shortcuts import render

def index(request):
    return render(request, 'structures/index.html', {})

def form_download(request):
    return render(request, 'structures/load_form.html', {})
