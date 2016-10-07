from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import UploadJsonForm
from .utils import handle_uploaded_file
from .models import Structure

def index(request):
    qs = Structure.objects.all()
    return render(request, 'structures/index.html', {'objects': qs})

def form_upload(request):
    form = UploadJsonForm(request.POST, request.FILES or None)

    if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        return HttpResponseRedirect(reverse('success'))
    else:
        form = UploadJsonForm()
    return render(request, 'structures/upload_form.html', {'form': form})

def success(request):
    return HttpResponseRedirect(reverse('upload'))
