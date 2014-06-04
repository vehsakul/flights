from django.shortcuts import render
from models import Airport, Route
from forms import *
import json
from django.http import HttpRequest, HttpResponse

# Create your views here.


def airport_location(request):
    form = AirportForm()
    return render(request, 'airport_location.html', {'form': form})


def airport_autocomplete(request):
    if request.method == 'GET':
        form = AirportForm(request.GET, empty_permitted=True)
        if form.is_valid():
            res_set = Airport.objects.filter(name__icontains=form.cleaned_data['name'],
                                             country__icontains=form.cleaned_data['country'],
                                             city__icontains=form.cleaned_data['city']).order_by('name')
            extract_from_airport = lambda air: dict(
                id=air.id,
                country=air.country,
                city=air.city,
                name=air.name,
                lat=air.lat,
                lon=air.lon,
            )
            airports = json.dumps([extract_from_airport(air) for air in res_set[:10]], indent=2)
            return HttpResponse(content=airports,
                                content_type='text/json')
        else:
            print form.errors
    return HttpResponse(status=400)


