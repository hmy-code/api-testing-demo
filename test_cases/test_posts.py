import requests
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import BASE_URL
def test_get_post_success():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

#逆向测试
def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404

#数据交互测试
def test_create_new_post():
    payload = {"title": "test", "body": "hello", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "test"
@pytest.mark.parametrize("post_id",[1,2,3])
def test_get_multiple_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"]==post_id
