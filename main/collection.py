import api
import utils
import requests


class Collection(api.Connection):
    """
    This class consists of the endpoints related to the Collections.
    """

    def __init__(self, is_public: bool = True) -> None:
        self.conn = api.Connection(is_public)

    def get_all_collections(self):
        path = "/collections"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        return response

    def get_collection_by_id(self, id):
        path = f"/collections/{id}"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        return response


def main():
    collection = Collection()
    collection.get_all_collections()
    collection.get_collection_by_id(23)


if __name__ == "__main__":
    main()
