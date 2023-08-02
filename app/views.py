import json
from django.db import connection, reset_queries
from django.db.models import Prefetch, Sum
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Sector, Subsector, Indicator, Profile

def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func(*args, **kwargs)
        query_info = connection.queries
        print('function_name: {}'.format(func.__name__))
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return results
    return inner_func

@database_debug
def home(request):

    profile = Profile.objects.filter(name="tami").first()
    umumi_suallar = profile.data['Tehsil_merhelesi'][0]['Umumi_suallar']
    sum_of_weights = sum(question["weight"] for question in umumi_suallar)
    return HttpResponse(sum_of_weights)