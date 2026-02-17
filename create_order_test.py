# create_order_test.py
import sender_stand_request
import data

# Вспомогательная функция 
def create_order():
    """
    Создает заказ и возвращает полный ответ от сервера
    (без проверок! только действие)
    """
    # Отправляем запрос на создание заказа
    response = sender_stand_request.post_new_order(data.order_body)
    return response

# Тест: создание заказа и получение данных по треку
def test_create_order_and_get_by_track():
    """
    Шаги автотеста:
    1. Выполнить запрос на создание заказа
    2. Сохранить номер трека заказа
    3. Выполнить запрос на получение заказа по треку
    4. Проверить, что код ответа равен 200
    """
    # Шаг 1: Выполнить запрос на создание заказа
    create_response = create_order()
    
    # Проверяем, что заказ создан успешно
    assert create_response.status_code == 201, f"Ожидался код 201, получен {create_response.status_code}"
    
    # Шаг 2: Сохранить номер трека заказа
    response_data = create_response.json()
    track_number = response_data.get("track")
    assert track_number is not None, "Не удалось получить номер трека"
    print(f"Создан заказ с трек-номером: {track_number}")
    
    # Шаг 3: Выполнить запрос на получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверить, что код ответа равен 200
    assert get_response.status_code == 200, f"Ожидался код 200, получен {get_response.status_code}"
    
    # Дополнительные проверки данных заказа
    order_data = get_response.json()
    assert "order" in order_data, "Ответ не содержит поле 'order'"
    
    order = order_data["order"]
    assert order["firstName"] == data.order_body["firstName"]
    assert order["lastName"] == data.order_body["lastName"]
    assert order["address"] == data.order_body["address"]
    assert order["phone"] == data.order_body["phone"]
    assert order["rentTime"] == data.order_body["rentTime"]
    assert order["deliveryDate"] == data.order_body["deliveryDate"]
    assert order["comment"] == data.order_body["comment"]
    assert order["color"] == data.order_body["color"]
    
    print(f"Тест успешно выполнен! Трек номер: {track_number}")