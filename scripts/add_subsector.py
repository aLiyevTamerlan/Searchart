from app.models import *
import pandas as pd

def run():
    
    data = pd.read_csv('KPI tracking - Weights Data.csv')
    l = []
    sector_list = data[['Sector', 'Subsector']]
    subsectors = data['Subsector']
    sectors = data['Sector']
    print(sector_list['Subsector'])
    for sub in range(len(subsectors)):

        if sector_list['Subsector'][sub] not in l:
            l.append(sector_list['Subsector'][sub])
            if sectors[sub] != "Other":
                sector = Sector.objects.get(sector_name=sectors[sub])
                subsector = Subsector.objects.create(subsector_name=sector_list['Subsector'][sub],sector=sector)
                subsector.save()