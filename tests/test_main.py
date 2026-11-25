import pytest
from src.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Пример существующего теста (из методички)
def test_get_existed_user(client):
    """Тест на получение существующего пользователя"""
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Alice'

# --- Реализуем остальные тесты, которые требовались в методичке ---

def test_get_non_existent_user(client):
    """Тест на получение несуществующего пользователя (ожидаем 404)"""
    response = client.get('/users/999')
    assert response.status_code == 404
    assert "error" in response.json

def test_health_check(client):
    """Тест эндпоинта проверки работоспособности"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

def test_invalid_route(client):
    """Тест несуществующего маршрута (ожидаем 404)"""
    response = client.get('/invalid-route')
    assert response.status_code == 404