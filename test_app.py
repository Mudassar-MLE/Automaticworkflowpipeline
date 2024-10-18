from app import app

def test_home():
    response = app.test.client().get("/")
    assert response.status_code==200
    assert response.data==b'FastAPI Hello world! Version 1'
