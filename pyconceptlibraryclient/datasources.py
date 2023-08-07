import api
import utils
import requests


class DataSources:
    """
    This class consists of the endpoints related to the Data Sources.
    """

    def __init__(self, url, auth) -> None:
        self.urlBuilder = utils.URLBuilder(url)
        self.auth = auth

    def get_all(self):
        """
        This function returns all the datasources.

        Returns:
            Response (list -> json objects): A list representing all the datasources present in the database.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.datasources.get_all()
        """
        path = api.Path.GET_ALL_DATASOURCES.value
        response = requests.get(self.urlBuilder.get_url(path), auth=self.auth)
        utils.check_response(response)
        return response

    def get_one_detail(self, id: int):
        """
        This function returns the datasource info based on the given datasource id.

        Parameters:
            id (int): Datasource Id to retrieve a particular `datasource` object
        Returns:
            Response (json object): A json object representing single datasource present in the database based on passed `id`.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.datasources.get_one_detail(1)
        """
        path = api.Path.GET_DATASOURCE_BY_ID.value.format(id=id)
        response = requests.get(self.urlBuilder.get_url(path), auth=self.auth)
        utils.check_response(response)
        return response
