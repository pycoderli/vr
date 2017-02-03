from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from inventory.models import Item
from inventory.models import Rooms

def index(request):
    items = Item.objects.all()
    return render(request, 'inventory/index.html', {
        'items': items,
    })

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
    return HttpResponse('<p> In item_detail view with id {0}</p>'.format(id))

def image_link(request, id):
    try:
        roomss = Rooms.objects.filter(item_id=id)
    except Rooms.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/room_panorama.html', {
        'room': roomss[0]
    })
    return HttpResponse('<p> In item_detail view with id {0}</p>'.format(id))


# todo delete
def panorama(request):
    return render(request, 'inventory/panorama.html')
    return HttpResponse('<p> In item_detail view with id {0}</p>'.format(id))