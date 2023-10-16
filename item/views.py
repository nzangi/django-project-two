from django.shortcuts import render,get_list_or_404

from .models import Item

# Create your views here.
def detail(request,pk):
    item = get_list_or_404(Item,pk)
    return render(request,'item/detail.html',{
        'item': item
    })
