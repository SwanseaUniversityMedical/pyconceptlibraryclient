import utils
from .constants import Path
from requests.auth import HTTPBasicAuth


class Connection:
    """
    This class deals with the requirements regarding the connection with the API.
    """

    def __init__(self, is_public: bool) -> None:
        # Show the user a GUI asking for his/her user credentials
        if is_public is False:
            login_ui = utils.LoginWindow()

            # Create the main tkinter window
            window = login_ui.create_window()

            # Create labels and entry fields for username and password
            picked_url = login_ui.get_url_dropdown_field(
                window, url_values=[Path.BASEURL_LOCAL.value, Path.BASEURL_PROD.value]
            )
            login_ui.get_username_field(window)
            login_ui.get_password_field(window)

            # Create the login button and provide function to call once it is pressed.
            login_ui.get_login_button(window)

            # Start the main tkinter event loop
            window.mainloop()

            self.baseurl = picked_url.get().strip()
            self.auth = HTTPBasicAuth(
                username=login_ui.user, password=login_ui.password
            )
        else:
            login_ui = utils.LoginWindow()
            window = login_ui.create_window()
            picked_url = login_ui.get_url_dropdown_field(
                window, url_values=[Path.BASEURL_LOCAL.value, Path.BASEURL_PROD.value]
            )
            # Create the login button and provide function to call once it is pressed.
            login_ui.get_connect_button(window)

            # Start the main tkinter event loop
            window.mainloop()
            self.baseurl = picked_url.get().strip()
            self.auth = None
