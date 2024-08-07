from django.http import HttpResponse
import os
import pandas as pd
from database.models import Main


def parse_view(request):
    filename = ''
    for i in os.listdir(os.getcwd() + '/DIGIS'):
        if i.endswith('.xls') or i.endswith('.xlsx'):
            filename = i
            break
    file = pd.read_excel(os.getcwd() + '/DIGIS/' + filename)

    trash = Main.objects.filter(provider='DIGIS')
    for el in trash:
        el.delete()


    for row in file.itertuples():
        if not pd.isna(getattr(row, '_11')) and type(getattr(row, '_11')) != str:
            print(row, '\n')
            num = getattr(row, '_1') if not pd.isna(getattr(row, '_1')) else None
            name_provider = getattr(row, '_3') if not pd.isna(getattr(row, '_3')) else None
            provider = 'Digis'
            cost = getattr(row, '_11')
            article = getattr(row, '_5') if not pd.isna(getattr(row, '_5')) else None
            link = getattr(row, '_8') if not pd.isna(getattr(row, '_8')) else None
            Main.objects.create(num=num, name_provider=name_provider, provider=provider, cost=cost, article=article, link=link)

    return HttpResponse('OK')
