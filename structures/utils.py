from django.conf import settings

from .models import Structure

def handle_uploaded_file(f):
    import json
    with open('%s/data.json' % (settings.MEDIA_ROOT), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open('%s/data.json' % (settings.MEDIA_ROOT), 'r') as data:
        json_data = json.loads(data.read())
        # Pars file and enter data into the database
        # Not sure this code belong here
        for item in json_data['data']:
            obj = Structure(region=item['Регион'],
                            country=item['Страна'],
                            value=item['Значение'])
            obj.save()

        # TODO: optimized to improve performance
