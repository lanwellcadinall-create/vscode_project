# configuration.py

# Базовый URL API Яндекс.Самокат (замените {id} на актуальный ID вашего стенда)
URL_SERVICE = "https://{id}.serverhub.praktikum-services.ru"

# Пути к эндпоинтам API
CREATE_ORDER_PATH = "/api/v1/orders"              # Создание заказа
GET_ORDER_BY_TRACK_PATH = "/api/v1/orders/track"  # Получение заказа по треку