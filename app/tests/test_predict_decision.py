from app.handlers.routes import configure_routes
from flask import Flask


def test_predict_response():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
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

def test_predict_response_no_reason():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision/decision'
    student = {"studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_reason():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": 1,
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"invalid reason"

def test_predict_response_no_studytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_studytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": "what is that",
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"invalid study time"

def test_predict_response_outofbound_studytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 10,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"study time must be integer from 1 to 4"

def test_predict_response_no_activities():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_activities():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "a lot",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"invalid activities"

def test_predict_response_no_absences():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_absences():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences": 0.1,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"invalid absences"

def test_predict_response_no_higher():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_higher():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "sure", 
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"invalid higher"

def test_predict_response_no_traveltime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_traveltime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 10,
               "failures": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"travel time must be integer from 1 to 4"

def test_predict_response_no_failures():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_failures():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": -1,
               "Dalc": 5,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"failures must be integer from 1 to 4"

def test_predict_response_no_Dalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_Dalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": "as much as possible", 
               "Walc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"Dalc must be integer from 1 to 5"

def test_predict_response_no_Walc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"missing required arguments"

def test_predict_response_invalid_Walc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    student = {"reason": "reputation",
               "studytime": 4,
               "activities": "yes",
               "absences":92,
               "higher": "no",
               "traveltime": 4,
               "failures": 4,
               "Dalc": 5,
               "Walc": "very low"}

    response = client.get(url, json= student)

    assert response.status_code == 400
    assert response.get_data() == b"Walc must be integer from 1 to 5"