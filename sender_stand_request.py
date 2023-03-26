import configuration
import requests
import data


def post_new_order(order_body):  # объявляем функцию на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,   # подставялем полный url
                         json=order_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


def get_order(order_id):  # функция на получение трека заказа
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH,  # подставялем полный url
                        params={"t": order_id})   # уточняем параметр


def check_order_create():  # объявляем функцию на проверку полученных данных
    order_body = data.order_body.copy()  # уточняем, что тело заказа напрямую скопировано из файла дата
    order_response = post_new_order(order_body)  # В переменную order_response сохраняется результат запроса на создание заказа
    order_id = order_response.json()["track"]  #  то же самое для трека заказа

    get_order_response = get_order(order_id)

    assert order_response.status_code == 201  #  проверка успешного вернувшегося кода 201
    assert get_order_response.status_code == 200  #  проверка успешного вернувшегося кода 200

def test_create_order_success_response():  #  тест на создание заказа и успешное получение его по треку с ответом 200
    check_order_create()