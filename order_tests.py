# Шашин Семён, 19-я когорта — Финальный проект. Инженер по тестированию плюс

import request
import data

# функция получения номера трека созданного заказа
# и возвращает значение словаря в виде строки (словарь: ключ - значение)
def create_order():
    body = data.user_body.copy()
    track = request.post_new_order(body)
    return str(track.json()['track'])

def positive_assert():
    track = create_order()
    #print(track)
    parametrs = data.get_parametrs.copy()
    #print(parametrs)
    parametrs["t"] = track
   #print(parametrs)
    response = request.get_info_order(parametrs)
    assert response.status_code == 200

def test_run():
    positive_assert()
