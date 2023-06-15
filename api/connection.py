from dotenv import dotenv_values


class Connection:
    """
    This class deals with the requirements regarding the connection with the API.
    """

    def __init__(self, is_public: bool) -> None:
        self.config = dotenv_values(".env")
        self.baseurl = self.config["BASEURL"]
        if is_public is False:
            self.user = self.config["USER"]
            self.password = self.config["PASSWORD"]
