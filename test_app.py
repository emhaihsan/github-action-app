from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, World!'

def test_greet():
    response = app.test_client().get('/greet/John')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, John!'

def test_unknown_route():
    response = app.test_client().get('/unknown')
    assert response.status_code == 404

def test_greet_no_name():
    response = app.test_client().get('/greet')
    assert response.status_code == 404