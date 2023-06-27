import json


def check_response(response):
    """
    Helper function to check the response and print accordingly.
    """
    match response.status_code:
        case 200:
            print("Data Found!")
            print_response(response)
        case 201:
            print("Data Created!")
            print_response(response)
        case 404:
            print("Not found! Please Check!")
        case 403:
            print("Forbidden! This requires authentication!")
        case 500:
            print("Server Error!")

def print_response(response):
    """
    Helper function to print the response cum the json string in a formatted way.
    """
    formatted_json = json.dumps(response.json(), indent=2)
    print(formatted_json)
