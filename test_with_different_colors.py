# test_with_different_colors.py
import sender_stand_request
import data
import copy

def test_create_order_with_different_colors():
    """
    Проверка создания заказов с разными цветами
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
        create_response = sender_stand_request.post_new_order(order_body_copy)
        
        # Проверяем успешность создания
        assert create_response.status_code == 201, f"Ошибка для цвета {color}: код {create_response.status_code}"
        
        # Получаем трек-номер
        create_data = create_response.json()
        track_number = create_data.get("track")
        assert track_number is not None, f"Не получен трек для цвета {color}"
        
        # Получаем заказ по треку
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200, f"Заказ с цветом {color} не найден по треку"
        
        # Проверяем, что цвет сохранился
        get_data = get_response.json()
        assert get_data["order"]["color"] == color, f"Цвет {color} не совпадает с полученным {get_data['order']['color']}"
        
        print(f"Заказ с цветом {color} успешно создан. Трек: {track_number}")