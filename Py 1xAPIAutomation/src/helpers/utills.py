# Common Headers

def common_headers_json():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def common_headers_token():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers
