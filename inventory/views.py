from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from inventory.models import *

def index(request):
    houses = House.objects.all()
    return render(request, 'inventory/index.html', {
        'houses': houses,
    })

def house_detail(request, id):
    try:
        house = House.objects.get(id=id)
    except House.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/house_detail.html', {
        'house': house,
    })
    return HttpResponse('<p> In house_detail view with id {0}</p>'.format(id))

def room_pic(request, id):
    try:
        roomss = Rooms.objects.filter(house_id=id)
    except Rooms.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/room_panorama.html', {
        'room': roomss[0]
    })
    return HttpResponse('<p> In house_detail view with id {0}</p>'.format(id))

def arrow_pic(request, id):
    try:
        arrow = ConnectedArrow.objects.get(id=id)
        rooms = Rooms.objects.filter(id=arrow.room_destination_id)
    except ConnectedArrow.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/room_panorama.html', {
        'room': rooms
    })

    return HttpResponse('<p> In house_detail view with id {0}</p>'.format(id))


# todo delete
def panorama(request):
    return render(request, 'inventory/panorama.html')
    return HttpResponse('<p> In house_detail view with id {0}</p>'.format(id))