from django.conf import settings
from .models import Structure, Region

def handle_uploaded_file(f):
    import json

    with open('%s/data.json' % (settings.MEDIA_ROOT), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open('%s/data.json' % (settings.MEDIA_ROOT), 'r') as data:
        json_data = json.loads(data.read())
        # Pars file and enter data into the database
        # Not sure this code belong here
        regions = []

        for item in json_data['data']:
            if item['Регион'] not in regions:
                regions.append(item['Регион'])

        for region in regions:
            Region(title=region).save()

        for item in json_data['data']:
            r = Region.objects.get(title=item['Регион'])
            Structure(region=r,
                      country=item['Страна'],
                      value=item['Значение']).save()

        # TODO: optimized to improve performance

def get_regions(request):
    """
    Returns list of existing regions
    """
    cur_region = get_current_region(request)

    regions = []
    for region in Region.objects.all().order_by('title'):
        regions.append({
            'id': region.id,
            'region': region.title,
            'selected': cur_region and cur_region.id == region.id and True or False
        })
    return regions

def get_current_region(request):
    """
    Returns currently selected group or None
    """

    # We remember selected region in a cookie
    id = request.COOKIES.get('current_region')

    if id:
        try:
            region = Region.objects.get(pk=str(id))
        except Region.DoesNotExist:
            return None
        else:
            return region
    else:
        return None
