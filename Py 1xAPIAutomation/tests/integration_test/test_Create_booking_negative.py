from src.constants.api_contsants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utills import common_headers_json
import pytest


class TestCreateBooking(object):


    @pytest.mark.negative
    def test_create_booking_tc1(self):
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                payload={}, injson=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, expect_data=500)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
            response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                    payload={"firstname": "admin"}, injson=False)
            print(response)
            bookingid = response.json()["bookingid"]
            print(bookingid)
            verify_response_key_should_not_be_none(response.json()["bookingid"])
            verify_http_status_code(response, expect_data=500)

    @pytest.mark.negative
    def test_create_booking_tc3(self):
                response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                        payload=None, injson=False)
                print(response)
                bookingid = response.json()["bookingid"]
                print(bookingid)
                verify_response_key_should_not_be_none(response.json()["bookingid"])
                verify_http_status_code(response, expect_data=400)

    @pytest.mark.negative
    def test_create_booking_tc4(self):
                response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                        payload="This is a Text", injson=False)
                print(response)
                bookingid = response.json()["bookingid"]
                print(bookingid)
                verify_response_key_should_not_be_none(response.json()["bookingid"])
                verify_http_status_code(response, expect_data=500)
