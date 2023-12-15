import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/3156")
    print(response_body.status_code)
    print(response_body.json())
    if response_body.status_code == 200:
        print("TC#1 - Get request is successful")
    else:
        print("TC$1 - Get booking is not successful")


if __name__ == '__main__':
    main()
