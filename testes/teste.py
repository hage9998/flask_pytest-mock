import pytest
from create_app import create_app 
import app as application

def test_mocking_constant_a(monkeypatch):
    word = 'return_string2'
    monkeypatch.setattr(application, 'mock_here', lambda : word)
    app = create_app().test_client()
    response = app.post('/route')
    print(response)
    assert response.data.decode('utf-8') == word
