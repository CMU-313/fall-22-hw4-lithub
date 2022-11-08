from app.handlers.routes import configure_routes
from flask import Flask


def test_predict_response():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/get-decision'
    score = {"score" : 17}

    response = client.get(url, json= score)

    assert response.status_code == 200
    assert response.json == 0 or response.json == 1

def test_predict_response():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/get-decision'
    score = {"score" : "type mismatch!"}

    response = client.get(url, json= score)

    assert response.status_code == 400
    assert response.get_data() == b"invalid score"

def test_predict_response():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/get-decision'
    score = {"score" : -10}

    response = client.get(url, json= score)

    assert response.status_code == 400
    assert response.get_data() == b"score must be number from 0 to 20"