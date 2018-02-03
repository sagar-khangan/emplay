# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.IntegerField()
    account_child_account = models.IntegerField()
    potential = models.CharField(max_length=2)
    pipeline = models.CharField(max_length=2)
    stage =  models.CharField(max_length=4)

    def __str__(self):
        return (str(self.account_id)+" : "+str(self.account_child_account))

class Account_Risk(models.Model):
    account_id = models.IntegerField()
    account_name = models.CharField(max_length=250)
    customer_name = models.CharField(max_length=250)
    account_risk = models.TextField()

    def __str__(self):
        return str(self.account_id)


