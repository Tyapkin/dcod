from .utils import get_regions

def regions_processor(request):
    return {'REGIONS': get_regions(request)}
