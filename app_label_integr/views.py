from re import T
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ConnectSettings
import requests

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'app_label_integr/index.html'
        )

class CheckConnectionView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(ConnectSettings, app_connections='Iiko')

        err = 0 # Флаг ошибки

        # Получаем токен
        params_login = {
            "user_id": post.user_id,
            "user_secret": post.user_secret
            }
        try:
            token = requests.get(post.url_token, params=params_login)
        except ConnectionError:
            print("ConnectionError")
            err = 1

        if err == 0 and token.status_code == 200:
            token_json = token.json()

        with open('t_file.txt', 'w', encoding='utf-8') as t_f:
            print(token_json, file=t_f) 

        return render(request, 'app_label_integr/checkconnection.html', context={
            'post': token_json
    })     

class BufferFoodView(View):
    def get(self, request, *args, **kwargs):
        with open('t_file.txt', encoding='utf-8') as t_f:
             token = t_f.read().strip()
        
        # Список организаций
        params_orgs = {"access_token": token} 
        orgs = requests.get("https://iiko.biz:9900/api/0/organization/list", params_orgs)
        orgs_json = orgs.json()

        # Список блюд первой организации
        params_prods = {
            "access_token": token,
            "revision": "0",
            } 
        prods = requests.get(f'https://iiko.biz:9900/api/0/nomenclature/{orgs_json[0]["id"]}', params_prods)
        prods_json = prods.json()

        #id_rest = prods_json['groups'][0]['id']
        #for prods in prods_json:
        #    if 

#"['groups'][0]['id']": "24e02f41-c240-4bdc-8a8a-b76580ae10c5"

        #prods_json['groups'][i] - рестораны организации
        #prods_json['groups'][i]['additionalInfo'] - имя (код) ресторана на латинице, например Ресторан Френч - r_french
        #prods_json['groups'][0]['id'] - id ресторана
        #prods_json['groups'][0]['name'] - имя ресторана
        #prods_json['products'] - меню по всем ресторанам
        #prods_json['revision'] - ревизия меню
        #prods_json['uploadDate'] - дата и время загрузки ревизии


        return render(request, 'app_label_integr/bufferfood.html', context={
            'post': prods_json['products']
    })