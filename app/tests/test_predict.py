from app.handlers.routes import configure_routes
from flask import Flask


def test_predict_respond():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'
    student = {'age': 18, 'health': 5, 'absences':0}

    response = client.get(url, json= student)

    assert response.status_code == 200
    assert response.json == 0 or response.json == 1
