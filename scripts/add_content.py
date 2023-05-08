
import pandas as pd, re

from app.models import Indicator, Subsector

def run():
    content_data = pd.read_csv('KPI tracking - KPIs from theglobaleconomy.csv')[['Description', 'Indicator']]
    data = pd.read_csv('KPI tracking - Weights Data.csv')


    for indecator in range(len(content_data['Indicator'])):
        content_data['Indicator'][indecator] = content_data['Indicator'][indecator].replace(",","")

    for indecator in data['Indicator']:
        
        for content in range(len(content_data)):
            if content_data['Indicator'][content] == indecator and indecator != "Other":
                ind = Indicator.objects.get(name=indecator)
                ind.content=content_data['Description'][content]
                ind.save()
                

    

    

    