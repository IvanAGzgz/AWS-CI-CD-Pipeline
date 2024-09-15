from app import app

def test_home():
    respone=app.test_client().get("/")

    assert respone.status_code==200
    assert respone.data==b"Hello World!"