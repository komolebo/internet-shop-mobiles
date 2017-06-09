# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal

from django.db import models


# class Poll(models.Model):
# question = models.CharField(max_length=200)
# pub_date = models.DateTimeField('date published')
#
#     def __unicode__(self):
#         return self.question
#
#
# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __unicode__(self):
#         return self.choice_text


class Mobile(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=50)
    trunk = models.CharField(max_length=50)
    features = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=4, default=Decimal('0.0000'))

    def __unicode__(self):
        return self.name


class User:
    def __init__(self, user_id, mobile_ids=[]):
        self.user_id = user_id
        self.mobile_ids = mobile_ids
