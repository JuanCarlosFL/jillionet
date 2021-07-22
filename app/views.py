
from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, 'inicio.html', {})



#def orderbook(request):

#    return render(request, 'orderbook.html', {})




def jillfarm(request):
    return HttpResponse("jillfarm")


def jillp2(request):
    return HttpResponse(p2venta)



#


