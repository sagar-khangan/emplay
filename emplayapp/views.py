# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db.models import Count
from .models import *


def index(request):

    # count unique child accounts
    child_account_count = len(Account.objects.values('account_child_account').annotate(child_count=Count('account_child_account',distinct=True)))

    # account accounts with stage Won
    won_count = len(Account.objects.filter(stage="Won"))

    # count distinct account with pipeline = HP
    count_pipeline = Account.objects.filter(pipeline="HP").values('pipeline').annotate(
                     n=Count('account_id', distinct=True))

    # count distinct account with potential = HP
    count_potential = Account.objects.filter(potential="HP").values('potential').annotate(
                      n=Count('account_id',distinct =True))

    # account risk data
    account_risk_data = [{"account_name":i.account_name,"customer_name":i.customer_name,"risk":i.account_risk.split("@")} for i in  Account_Risk.objects.all()]

    queries = {"child_account_count": child_account_count,
               "won_count": won_count, "count_pipeline": count_pipeline[0]['n'], "count_potential":count_potential[0]['n']}

    return render(request, 'index.html', {'queries':queries,'account_risk_data':account_risk_data})
