from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth


class Connection:
    """
    This class deals with the requirements regarding the connection with the API.
    """

    def __init__(self, is_public: bool) -> None:
        self.config = dotenv_values(".env")
        self.baseurl = self.config["BASEURL"].strip()
        if is_public is False:
            self.user = self.config["USER"].strip()
            self.password = self.config["PASSWORD"].strip()
            self.auth = HTTPBasicAuth(username=self.user, password=self.password)
