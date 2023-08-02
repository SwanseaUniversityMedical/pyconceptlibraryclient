import utils, threading
from .constants import Path
from requests.auth import HTTPBasicAuth


class Connection:
    """
    This class deals with the requirements regarding the connection with the API.
    """

    def __init__(self, is_public: bool) -> None:
        self.login_ui = utils.LoginWindow(is_public)
        self.baseurl = None
        self.is_public = is_public

    def establish(self):
        self.login_ui.start()
        self.baseurl = self.login_ui.baseurl
        if not self.is_public:
            self.auth = HTTPBasicAuth(
                username=self.login_ui.user, password=self.login_ui.password
            )
        else:
            self.auth = None
        return self.baseurl, self.auth


def main():
    conn = Connection(is_public=True)
    print(conn.auth)
    print("$$$$ " + conn.baseurl)


if __name__ == "__main__":
    main()
