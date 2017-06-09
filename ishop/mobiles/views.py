# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from models import Mobile


bought_mobiles = []


def get_total():
    total = 0
    for p in bought_mobiles:
        total += get_object_or_404(Mobile, pk=p).price
    return total


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login/")

    mobiles = Mobile.objects.order_by('-manufacturer')[:5]
    total = get_total()

    return render(request, 'mobiles/index.html', {'mobiles': mobiles, 'total': total})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/xo4y/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def detail(request, mobile_id):
    mobile = get_object_or_404(Mobile, pk=mobile_id)
    return render(request, 'mobiles/detail.html', {'mobile': mobile, 'total': get_total()})


def card(request):
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