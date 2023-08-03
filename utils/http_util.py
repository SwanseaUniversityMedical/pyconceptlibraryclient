import json


def check_response(response):
    """
    Helper function to check the response and print accordingly.
    """
    status_code = response.status_code
    if status_code == 200:
        print("Data Found!")
        print_response(response)
    elif status_code == 201:
        print("Data Created!")
        print_response(response)
    elif status_code == 404:
        print("Not found! Please Check!")
    elif status_code == 403:
        print("Forbidden! This requires authentication!")
    elif status_code == 500:
        print("Server Error!")
    else:
        print("Unknown status code:", status_code)


def print_response(response):
    """
    Helper function to print the response cum the json string in a formatted way.
    """
    formatted_json = json.dumps(response.json(), indent=2)
    print(formatted_json)
