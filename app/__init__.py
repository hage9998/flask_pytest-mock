from flask import Flask, request
from app.return_string import test_return


def mock_here():
    response = test_return().get_string()
    return response

def create_app():
    app = Flask(__name__)
    app.add_url_rule('/route', None, mock_here, methods=['POST'])
    return app