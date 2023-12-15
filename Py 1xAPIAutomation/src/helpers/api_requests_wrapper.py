# To make the POST, PUT, Patch, Delete, Get
import json

import requests


# HTTP Methods - Generic Functions


def get_request(url, auth, injson):
    response = requests.get(url=url, auth=auth)
    if injson is True:
        return response.json()
    return response


def post_request(url, auth, headers, payload, injson):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if injson is True:
        return post_response.json()
    return post_response


def patch_request(url, auth, headers, payload, injson):
    patch_response_data = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if injson is True:
        return patch_response_data.json()
    return patch_response_data


def put_request(url, auth, headers, payload, injson):
    put_response_data = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if injson is True:
        return put_response_data.json()
    return put_response_data


def delete_request(url, auth, headers, payload, injson):
    delete_response_data = requests.delete(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if injson is True:
        return delete_response_data.json()
    return delete_response_data
