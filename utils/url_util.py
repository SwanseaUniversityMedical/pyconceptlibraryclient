class URLBuilder:
    """
    This class consists of the methods that build the url for accessing the APIs.
    """

    def __init__(self, baseurl: str) -> None:
        self.baseurl = baseurl

    def get_url(self, path: str) -> str:
        url = f"{self.baseurl}/{path}"
        print(f"Constructed URL => {url}")
        return url


def main():
    urlBuilder = URLBuilder()
    urlBuilder.get_url()


if __name__ == "__main__":
    main()
