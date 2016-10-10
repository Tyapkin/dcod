from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from chartit import DataPool, Chart
from .forms import UploadJsonForm
from .utils import handle_uploaded_file
from .models import Structure

def index(request):
    pk = request.COOKIES.get('current_region')

    structuredata = DataPool(
        series=[{
            'options': {
                'source': Structure.objects.filter(region__id=int(pk))
            },
            'terms': [
                'region',
                'country',
                'value'
            ]
        }]
    )

    chart = Chart(
        datasource=structuredata,
        series_options=[{
            'options': {
                'type': 'column',
                'dataLabels': {
                    'enabled': 'true',
                    'rotation': '-90',
                    'color': '#FFFFFF',
                    'align': 'center',
                    'format': '{point.y:.1f}'
                },
            },
            'terms': {
                'country': ['value'],
            },
        }],
        chart_options={
            'title': {
                'text': 'Values by Country'
            },
        }
    )

    return render_to_response('structures/index.html', {'objects': chart},
                              context_instance=RequestContext(request))

def form_upload(request):
    form = UploadJsonForm(request.POST, request.FILES or None)

    if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        return HttpResponseRedirect(reverse('success'))
    else:
        form = UploadJsonForm()
    return render_to_response('structures/upload_form.html', {'form': form},
                              context_instance=RequestContext(request))

def success(request):
    return HttpResponseRedirect(reverse('upload'))
