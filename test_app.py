import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello' in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_info(client):
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app'] == 'test-QX'
# 添加新的测试用例
def test_hello_content(client):
    """测试首页返回内容"""
    response = client.get('/')
    assert b'CI/CD' in response.data

def test_health_message(client):
    """测试健康检查消息"""
    response = client.get('/health')
    data = response.get_json()
    assert data['message'] == 'OK'

def test_info_version(client):
    """测试版本信息"""
    response = client.get('/api/info')
    data = response.get_json()
    assert data['version'] == '1.0.0'

def test_404_page(client):
    """测试不存在的页面"""
    response = client.get('/not-exist')
    assert response.status_code == 404
