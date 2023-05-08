from app.models import *
import pandas as pd

def run():
    data = pd.read_csv('KPI tracking - Weights Data.csv')
    sector_list = data['Sector'].unique()

    for sector in sector_list:
        s = Sector.objects.create(sector_name=sector)
        s.save()