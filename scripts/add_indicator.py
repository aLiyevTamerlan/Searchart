import pandas as pd
from app.models import Indicator, Subsector

def run():
    data = pd.read_csv('KPI tracking - Weights Data.csv')
    content_data = pd.read_csv('KPI tracking - KPIs from theglobaleconomy.csv')[['Description', 'Indicator']]
    subsectors = data['Subsector']
    indecators = data['Indicator']
    
    # for index in range(len(subsectors)):
    #     if subsectors[index] != "Other":

    #         subsector = Subsector.objects.get(subsector_name=subsectors[index])
    #         indecator = Indicator.objects.create(indicator_name=indecators[index], sub_sector=subsector)
    #         indecator.save()

    for indecator in range(len(content_data['Indicator'])):
        content_data['Indicator'][indecator] = content_data['Indicator'][indecator].replace(",","")

    for indecator in data['Indicator']:
        
        for content in range(len(content_data)):
            if content_data['Indicator'][content] == indecator and indecator != "Other":
                ind = Indicator.objects.get(indicator_name=indecator)
                ind.content=content_data['Description'][content]
                ind.save()

    
