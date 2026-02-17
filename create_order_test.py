# create_order_test.py
import sender_stand_request
import data

# Вспомогательная функция (не тест, поэтому без test_)
def create_order():
    """
    Создает заказ и возвращает номер трека
    """
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
    track_number = response.json().get("track")
    assert track_number is not None, "Не удалось получить номер трека"
    return track_number

# ТЕСТОВАЯ ФУНКЦИЯ (обязательно с префиксом test_)
def test_create_order_and_get_by_track():
    """
    Тест: создание заказа и получение данных по треку
    """
    # Шаг 1: Создание заказа
    track_number = create_order()
    print(f"Создан заказ с трек-номером: {track_number}")
    
    # Шаг 2: Получение заказа по треку
    response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 3: Проверка кода ответа
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    
    # Проверка структуры ответа
    order_data = response.json()
    assert "order" in order_data, "Ответ не содержит поле 'order'"
    
    print(f"Тест успешно выполнен! Трек номер: {track_number}")