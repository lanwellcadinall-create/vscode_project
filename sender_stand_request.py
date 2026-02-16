# sender_stand_request.py
import requests
import configuration
import data

# Функция для создания нового заказа
def post_new_order(body):
    """
    Отправляет POST-запрос на создание нового заказа
    Возвращает полный ответ от сервера
    """
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Функция для получения заказа по треку
def get_order_by_track(track_number):
    """
    Отправляет GET-запрос на получение заказа по номеру трека
    track_number: номер трека заказа
    Возвращает полный ответ от сервера
    """
    return requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track_number},
                        headers=data.headers)