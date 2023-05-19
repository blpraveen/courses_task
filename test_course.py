from fastapi.testclient import TestClient
from main import app
import requests
import json
from unittest.mock import patch
from fastapi import status
client = TestClient(app)

def test_courses():

    mocked_response = requests.Response()
    mocked_response.status_code = status.HTTP_200_OK

    with patch("requests.get", return_value=mocked_response) as mocked_request:
        response = client.get("/courses")

    # Expect to get the msg
    assert response.status_code == status.HTTP_200_OK


def test_course():

    mocked_response = requests.Response()
    mocked_response.status_code = status.HTTP_200_OK

    with patch("requests.get", return_value=mocked_response) as mocked_request:
        response = client.get("/course/64664f380c0ba80bae205213/")

    # Expect to get the msg
    assert response.status_code == status.HTTP_200_OK

def test_course_chapter():

    mocked_response = requests.Response()
    mocked_response.status_code = status.HTTP_200_OK

    with patch("requests.get", return_value=mocked_response) as mocked_request:
        response = client.get("/course/64664f380c0ba80bae205213/0/")

    # Expect to get the msg
    assert response.status_code == status.HTTP_200_OK



def test_course_chapters():

    mocked_response = requests.Response()
    mocked_response.status_code = status.HTTP_200_OK

    with patch("requests.get", return_value=mocked_response) as mocked_request:
        response = client.get("/course_chapter/64664f380c0ba80bae205213/")

    # Expect to get the msg
    assert response.status_code == status.HTTP_200_OK    


def test_cc_rate():

    mocked_response = requests.Response()
    mocked_response.status_code = status.HTTP_200_OK
    data = {"user_id":"64674457c92ed15950570c94","course_id":"64664f380c0ba80bae205214","chapter":1,"rate":1}
    with patch("requests.post", return_value=mocked_response) as mocked_request:
        response = client.post("/cc_rate",json='{"user_id":"64674457c92ed15950570c94","course_id":"64664f380c0ba80bae205214","chapter":1,"rate":1}')

    # Expect to get the msg
    assert response.status_code == status.HTTP_201_CREATED