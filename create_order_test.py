# create_order_test.py
import sender_stand_request
import data

# Вспомогательная функция для создания заказа
def create_order():
    """
    Создает заказ и возвращает номер трека
    В соответствии с документацией:
    - Успешное создание: 201 Created + track
    - Тело запроса должно соответствовать документации
    """
    # Отправляем запрос на создание заказа
    response = sender_stand_request.post_new_order(data.order_body)
    
    # Проверяем, что заказ создан успешно
    assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
    
    # Получаем номер трека из ответа (в документации: { track: 124124 })
    track_number = response.json().get("track")
    assert track_number is not None, "Не удалось получить номер трека"
    
    return track_number

# Тест: создание заказа и получение данных по треку
def test_create_order_and_get_by_track():
    """
    Шаги автотеста в соответствии с документацией:
    1. Выполнить запрос на создание заказа (POST /api/v1/orders)
    2. Сохранить номер трека заказа из ответа (track)
    3. Выполнить запрос на получение заказа по треку (GET /api/v1/orders/track?t={track})
    4. Проверить, что код ответа равен 200 (успешное получение заказа)
    """
    # Шаг 1: Выполнить запрос на создание заказа
    # Шаг 2: Сохранить номер трека заказа
    track_number = create_order()
    print(f"Создан заказ с трек-номером: {track_number}")
    
    # Шаг 3: Выполнить запрос на получение заказа по треку
    response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверить, что код ответа равен 200
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    
    # Проверяем структуру ответа в соответствии с документацией
    order_data = response.json()
    assert "order" in order_data, "Ответ не содержит поле 'order'"
    
    # Проверяем, что данные заказа соответствуют созданному
    order = order_data["order"]
    assert order["firstName"] == data.order_body["firstName"]
    assert order["lastName"] == data.order_body["lastName"]
    assert order["address"] == data.order_body["address"]
    assert order["phone"] == data.order_body["phone"]
    assert order["rentTime"] == data.order_body["rentTime"]
    assert order["deliveryDate"] == data.order_body["deliveryDate"]
    assert order["comment"] == data.order_body["comment"]
    assert order["color"] == data.order_body["color"]
    
    # Проверяем наличие обязательных полей из документации
    assert "id" in order
    assert "track" in order
    assert "status" in order
    assert "cancelled" in order
    assert "finished" in order
    assert "inDelivery" in order
    assert "createdAt" in order
    assert "updatedAt" in order
    
    print(f"Тест успешно выполнен! Трек номер: {track_number}")
    print(f"Статус заказа: {order['status']}")