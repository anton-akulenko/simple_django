from django.views.generic import ListView
from django.shortcuts import render

from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})