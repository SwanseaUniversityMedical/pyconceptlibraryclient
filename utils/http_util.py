import json

def check_response(response):
    """
    Helper function to check the response and print accordingly.
    """
    if response.status_code == 200 or response.status_code == 201:
        print("Data Found/Created!")
    else:
        print("Error Occured! Status code: ", response.status_code)

def print_response(response):
    """
    Helper function to print the response cum the json string in a formatted way.
    """
    formatted_json = json.dumps(response.json(), indent=2)
    print(formatted_json)
