from app.handlers.routes import configure_routes
from flask import Flask


def test_predict_response():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 200
    assert response.json == 0 or response.json == 1
