import pytest
import requests


def test_get():
    id = "3682"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200

    data = response_body.json()

    assert 'firstname' in data, "Incorrect first name"
    assert 'lastname' in data, "Incorrect last name"

    assert data['firstname'] == "Jay", "Incorrect Message"
    assert data['lastname'] == "Shah", "Incorrect Message"
    assert data["bookingdates"]["checkin"] == "2013-02-23", "Incorrect Message"
