import utils, threading
from .constants import Path
from requests.auth import HTTPBasicAuth


class Connection:
    """
    This class deals with the requirements regarding the connection with the API.
    """

    def __init__(self, is_public: bool) -> None:
        login_ui = utils.LoginWindow(is_public)
        self.baseurl = login_ui.baseurl
        if not is_public:
            self.auth = HTTPBasicAuth(
                username=login_ui.user, password=login_ui.password
            )
        else:
            self.auth = None


def main():
    conn = Connection(is_public=False)
    print(conn.auth)
    print(conn.baseurl)


if __name__ == "__main__":
    main()
