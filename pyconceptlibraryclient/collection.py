import api
import utils
import requests


class Collection:
    """
    This class consists of the endpoints related to the Collections.
    """

    def __init__(self, is_public: bool = True) -> None:
        self.conn = api.Connection(is_public)
        self.urlBuilder = utils.URLBuilder()

    def get_all_collections(self):
        """
        This function returns all the collections.

        Returns:
            Response (list -> json objects): A list representing all the collection present in the database.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.collections.get_all_collections()
        """
        path = api.Path.GET_ALL_COLLECTIONS.value
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_collection_by_id(self, id):
        """
        This function returns the collection info based on the given collection id.

        Parameters:
            id (int): Collection Id to retrieve a particular `collection` object
        Returns:
            Response (json object): A json object representing single collection present in the database based on passed `id`.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.collections.get_collection_by_id(1)
        """
        path = api.Path.GET_COLLECTION_BY_ID.value.format(id=id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response


def main():
    collection = Collection()
    collection.get_all_collections()
    collection.get_collection_by_id(23)


if __name__ == "__main__":
    main()
