from src.constants.api_contsants import BASE_url, APIConstants, base_url


def test_crud():
    print(BASE_url)


url_class = APIConstants.base_url()
print(url_class)

url_direct_func = base_url()
print(url_direct_func)
