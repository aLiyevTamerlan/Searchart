from django.db import connection
from django.db import reset_queries
from app.models import Sector

def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func()
        query_info = connection.queries
        print('function_name: {}'.format(func.__name__))
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return results
    return inner_func
@database_debug
def run():
    sectors = Sector.objects.prefetch_related('sub_sectors__indicators').filter(slug="social")
    print([sector.sector_name for sector in sectors])
    return [sector for sector in sectors]