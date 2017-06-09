# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from django.shortcuts import get_object_or_404, render
from models import Mobile


bought_mobiles = [1, 2]


def get_total():
    total = 0
    for p in bought_mobiles:
        total += get_object_or_404(Mobile, pk=p).price
    return total


def index(request):
    mobiles = Mobile.objects.order_by('-manufacturer')[:5]
    total = get_total()

    return render(request, 'mobiles/index.html', {'mobiles': mobiles, 'total': total})


def detail(request, mobile_id):
    mobile = get_object_or_404(Mobile, pk=mobile_id)
    return render(request, 'mobiles/detail.html', {'mobile': mobile, 'total': get_total()})


def card(request):
    # poll = get_object_or_404(Poll, pk=poll_id)
    mobiles = []

    for mobile_id in bought_mobiles:
        mobiles.append(get_object_or_404(Mobile, pk=mobile_id))

    return render(request, 'mobiles/card.html',
                  {'mobiles': mobiles, 'mobiles_id': bought_mobiles, 'total': get_total()})


def buy(request, mobile_id):
    bought_mobiles.append(mobile_id)

    mobile = get_object_or_404(Mobile, pk=mobile_id)

    return render(request, 'mobiles/buy.html', {'mobile': mobile, 'total': get_total()})


def remove(request, mobile_id):
    bought_mobiles.remove(int(mobile_id))

    return render(request, 'mobiles/remove.html', {'mobile_id': mobile_id, 'total': get_total()})