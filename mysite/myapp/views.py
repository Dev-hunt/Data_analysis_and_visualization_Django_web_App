from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json

from .models import Data

# Create your views here.
def hello(request):
    if request.method == 'POST':
        print('this is post request')
        previous_data=Data.objects.all()
        previous_data.delete()
        file_name =request.FILES['file']
        df=pd.read_csv(file_name)
        json_records=df.reset_index().to_json(orient='records')
        data=[]
        data=json.loads(json_records)
        for d in data:  
            pro_pricename=d['property_name']
            pro_price=d['property_price']
            pro_rent=d['property_rent']
            pro_tax=d['property_tax']
            pro_emi=d['property_Emi']
            pro_exp=d['property_exp']
            pro_net_exp=pro_emi+pro_exp+pro_tax
            pro_net_inc=pro_rent - pro_net_exp
            dt=Data(name=pro_pricename, price=pro_price, rent=pro_rent, Emi=pro_emi, tax=pro_tax, exp=pro_exp,net_exp=pro_net_exp, net_income=pro_net_inc)
            dt.save()
        data_obj=Data.objects.all()
        context={'data_objectss':data_obj}
        return render(request,'myapp/index.html',context)
    else:
        print('thiss is get request')
    name='ashutosh'
    price=400
    movie=['rob','bob','eli','jeni']
    context={
        'names':name,
        'prices':price,
        'movies':movie
        
        }
    return render(request,'myapp/index.html',context)