from django.shortcuts import render
from django.http import Http404

from inventory.models import Item;

def index(request):
	items = Item.objects.exclude(amount=0);
	#render(request, <view file>, <dictionary query set>)
	return render(request, "inventory/index.html", {
		"items": items,
		});

def item_detail(request, id):
	#if item id doesnt exist raise an error with Http404 object
	try:
		item = Item.objects.get(id=id);
	except Item.DoesNotExist:
		raise Http404("th is item does not exist");
	return render(request, "inventory/item_detail.html", {
		"item": item,
		})