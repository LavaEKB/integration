from re import T
from django.shortcuts import render, get_object_or_404
from django.views import View
from integration.settings import MEDIA_ROOT
from integration.settings import BASE_DIR
from .models import ConnectSettings, BufferFood
import requests
import os

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

        # Переменные для буфера
        restaurant_bf = orgs_json[0]["id"] # id_организации
        name_bf = '' # Наименование продукта
        description_bf = '' # Описание
        price_bf = '' # Цена
        category_bf = '' # Категория
        image_bf = '' # Ссылка на картинку для буфера
        imageID = '' # Уникальное имя картинки

        # Проверяем путь к картинкам
        path = os.path.join(MEDIA_ROOT, 'upload', 'images', 'food/')
        print(path)
        if not os.path.exists(path):
            os.makedirs(path)

        for keys in prods_json.keys():
            #print(keys) # Все ключи, тип string. Пять штук
            #print(prods_json[keys]) # Три list, int, string
            if keys == 'groups' or keys == 'productCategories' or keys == 'products':
                for el in prods_json[keys]:
                    #if keys == 'groups': #  ---- Не понял, что делать с ресторанами ------
                    #    if el_key == 'id':
                    #        #print (el[el_key]) 
                    #        restaurant_bf = el[el_key]

                    if keys == 'products': 
                        for el_key in el.keys():
                            if el_key == 'name':
                                name_bf = el[el_key]
                            elif el_key == 'description':
                                description_bf = el[el_key]
                            elif el_key == 'price':
                                price_bf = el[el_key]
                            elif el_key == 'type':
                                category_bf = el[el_key]
                            elif el_key == 'images':
                                if el[el_key] != None:
                                    if len(el[el_key]) != 0: 
                                        imageID = el[el_key][0]['imageId']
                                        image_bf = requests.get(el[el_key][0]['imageUrl'])
                                        with open(path + f'{imageID}.jpg', 'wb') as img_f:
                                            img_f.write(image_bf.content) 


                        #BufferFood.objects.all().delete()

                        # Создаем запись в буфере  
                        BufferFood.objects.create(restaurant=restaurant_bf, name=name_bf, description=description_bf, price=price_bf, category=category_bf)


        #prods_json['groups'][i] - рестораны организации
        #prods_json['groups'][i]['additionalInfo'] - имя (код) ресторана на латинице, например Ресторан Френч - r_french
        #prods_json['groups'][0]['id'] - id ресторана
        #prods_json['groups'][0]['name'] - имя ресторана
        #prods_json['products'] - меню по всем ресторанам
        #prods_json['revision'] - ревизия меню
        #prods_json['uploadDate'] - дата и время загрузки ревизии


        return render(request, 'app_label_integr/bufferfood.html', context={
            'post': 'Успешно'
 
    })