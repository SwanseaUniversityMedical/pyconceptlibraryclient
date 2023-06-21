from dotenv import dotenv_values


class URLBuilder:
    """
    This class consists of the methods that build the url for accessing the APIs.
    """

    def __init__(self) -> None:
        self.config = dotenv_values(".env")
        self.baseurl = self.config["BASEURL"]

    def get_url(self, path: str) -> str:
        url = f"{self.baseurl}/{path}"
        print(f"Constructed URL => {url}")
        return url


def main():
    urlBuilder = URLBuilder()
    urlBuilder.get_url()


if __name__ == "__main__":
    main()
