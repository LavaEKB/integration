import requests

err = 0 # Флаг ошибки

# Получаем токен
params_login = {
    "user_id": "demoDelivery",
    "user_secret": "PI1yFaKFCGvvJKi"
    }
try:
    token = requests.get("https://iiko.biz:9900/api/0/auth/access_token", params=params_login)
except ConnectionError:
    print("ConnectionError")
    err = 1

if err == 0 and token.status_code == 200:
    token_json = token.json()

    #print(token_json)

    # Список организаций
    params_orgs = {"access_token": token_json} 
    orgs = requests.get("https://iiko.biz:9900/api/0/organization/list", params_orgs)
    orgs_json = orgs.json()

    #print(orgs_json[0]["id"])

    # Список блюд первой организации
    params_prods = {
        "access_token": token_json,
        "revision": "0"
        } 
    prods = requests.get(f'https://iiko.biz:9900/api/0/nomenclature/{orgs_json[0]["id"]}', params_prods)
    prods_json = prods.json()

    #print(prods_json)

    # Добавляем заказ с составным модификатором и новым покупателем
    params_order =  {
        "access_token": token_json,
        "requestTimeout": "00%3A"
        } 
    data_order = {
            "organization": "e464c693-4a57-11e5-80c1-d8d385655247",
            "customer": {
                "id": "",
                "name": "API_user",
                "phone": "+78008887700"
            },
            "order": {
                "id": "",
                "date": "2022-05-15 16:37:00",
                "phone": "+79998887766",
                "isSelfService": "false",
                "items":[
                    {
                    "id": "d73ad3e6-2858-483b-ac51-ff8296e6c093",
                    "name": "Товар с групповыми модификаторами",
                    "amount": 1,
                    "code": "00080",
                    "sum": 999,
                    "modifiers": [
                            {
                            "id": "b2d1e92d-4188-4e9a-8baf-0e19b0ac0853",
                            "name": "мод из группы1",
                            "amount": 1,
                            "groupId": "0c390a0b-b074-44e4-b324-32cf6c78755c",
                            "groupName": "групповые модификаторы"
                            }
                        ]
                    }
                ],
            "address": {
                "city": "Екатеринбург",
                "street": "ул.Стахановская",
                "home": "1",
                "apartment": "1",
                "comment": "Доставить горячим"
                }
            }
        }

    order = requests.post('https://iiko.biz:9900/api/0/orders/add', params=params_order,json=data_order)
    order_json = order.json()

    #print(order_json)


    # Список городов и улиц для первой организации
    params_streets = {"access_token": token_json, "organization" : orgs_json[0]["id"]} 
    streets = requests.get("https://iiko.biz:9900/api/0/cities/cities", params_streets)
    streets_json = streets.json()

    #with open('streets.txt', 'w', encoding='utf-8') as streets_file:
        #print(streets_json, file=streets_file)    

    # Первый город
    print(streets_json[0]["city"]["name"])
    

else:
    print('Ошибка получения токена.')