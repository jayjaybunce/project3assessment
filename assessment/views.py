from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import WishItem
# Create your views here.

def homepage(request):
    wishitems = WishItem.objects.all()
    context = {
        'wishitems' : wishitems,
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        wishitem = WishItem(content=request.POST['content'])
        wishitem.save()
        return redirect('homepage')



    return render(request, 'add.html')


def delete(request, item_id):
    item = WishItem.objects.get(id=item_id)
    item.delete()
    return redirect('homepage')