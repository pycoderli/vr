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
        rooms = Room.objects.filter(house_id=id)
        next_room = ConnectedArrow.objects.filter(room_id=id)
        next_destination_id = next_room[0].room_destination_id
    except Room.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/room_panorama.html', {
        'room': rooms[0],
        'next_destination_id' : next_destination_id
    })
    return HttpResponse('<p> In house_detail view with id {0}</p>'.format(id))

def arrow_pic(request, id):
    try:
        arrow = ConnectedArrow.objects.get(id=id)
        rooms = Room.objects.filter(id=arrow.room_destination_id)
        next_room = ConnectedArrow.objects.filter(room_id=id)
        next_destination_id = next_room[0].room_destination_id
    except ConnectedArrow.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/room_panorama.html', {
        'room': rooms[0],
        'next_destination_id' : next_destination_id
    })

    return HttpResponse('<p> In house_detail view with id {0}</p>'.format(id))


# todo delete
def panorama(request):
    return render(request, 'inventory/panorama.html')
    return HttpResponse('<p> In house_detail view with id {0}</p>'.format(id))