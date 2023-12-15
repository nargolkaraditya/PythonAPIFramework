from src.constants.api_contsants import APIConstants
from src.helpers.api_requests_wrapper import post_request,put_request,patch_request
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.utills import common_headers_json,common_headers_token
import pytest


class TestCreateBooking(object):

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, headers=common_headers_json(),
                                payload=payload_create_token(), injson=False)
        print(response)
        verify_http_status_code(response, expect_data=200)
        print(response.json())
        token = response.json()["token"]
        print(token)
        verify_response_key_should_not_be_none(token)
        return token

    @pytest.fixture()
    def create_booking(self):
        response = put_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                payload=payload_create_booking(), injson=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, expect_data=200)
        return bookingid

    def test_update_booking(self, create_token, create_booking): # Token/Basic Auth and booking id needed from create booking
        bookingid = create_booking
        put_url = APIConstants.url_create_booking() + "/"+ str(bookingid)
        response = post_request(url=put_url, auth=None, headers=common_headers_token(),
                            payload=payload_create_booking(), injson=False)
        print(response)

    def test_delete_booking(self,create_token, create_booking):  # Token/Basic Auth and booking id needed from create booking
        bookingid = create_booking
        delete_url = APIConstants.url_create_booking() + "/"+ str(bookingid)
        response = post_request(url=delete_url, auth=None, headers=common_headers_token(),
                                payload=None, injson=False)
        print(response)
