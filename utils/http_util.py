def check_response(response):
    """
    Helper function to check the response and print accordingly.
    """
    if response.status_code == 200 or response.status_code == 201:
        print("Data Found/Created!")
    else:
        print("Error Occured! Status code: ", response.status_code)
