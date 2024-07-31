# Шашин Семён, 19-я когорта — Финальный проект. Инженер по тестированию плюс

import Conf
import requests
import data

# Определение функции для отправки POST-запроса на создание заказа
def post_new_order(body):
    return requests.post(Conf.URL_SERVICE + Conf.CREATE_USER_ORDER,
                         json=body,
                         headers=data.headers)

def get_info_order(track):
    return requests.get(Conf.URL_SERVICE + Conf.ORDER_INFO,
                        params=track)
