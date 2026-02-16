# test_with_different_colors.py
import sender_stand_request
import data
import copy

def test_create_order_with_different_colors():
    """
    Проверка создания заказов с разными цветами в соответствии с документацией
    Поле color: необязательный параметр, string[]
    """
    colors_to_test = [
        ["BLACK"],           # Только черный
        ["GREY"],            # Только серый
        ["BLACK", "GREY"],   # Оба цвета
        []                   # Без цвета
    ]
    
    for color in colors_to_test:
        # Создаем копию тела заказа с новым цветом
        order_body_copy = copy.deepcopy(data.order_body)
        order_body_copy["color"] = color
        
        # Создаем заказ
        response = sender_stand_request.post_new_order(order_body_copy)
        
        # Проверяем успешность создания (201 Created)
        assert response.status_code == 201, f"Ошибка для цвета {color}: код {response.status_code}"
        
        # Получаем трек-номер
        track_number = response.json().get("track")
        assert track_number is not None, f"Не получен трек для цвета {color}"
        
        # Проверяем, что заказ можно получить по треку
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200, f"Заказ с цветом {color} не найден по треку"
        
        # Проверяем, что цвет сохранился
        order_data = get_response.json()
        assert order_data["order"]["color"] == color, f"Цвет {color} не совпадает с полученным {order_data['order']['color']}"
        
        print(f"Заказ с цветом {color} успешно создан. Трек: {track_number}")