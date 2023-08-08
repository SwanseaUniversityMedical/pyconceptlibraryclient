import api
import utils
import requests


class Templates:
    """
    This class consists of the endpoints related to the Templates.
    """

    def __init__(self, url, auth) -> None:
        self.urlBuilder = utils.URLBuilder(url)
        self.auth = auth

    def get_all_templates(self):
        """
        This function returns all the templates.

        Returns:
            Response (list -> json objects): A list representing all the templates present in the database.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.templates.get_all_templates()
        """
        path = api.Path.GET_ALL_TEMPLATES.value
        response = requests.get(self.urlBuilder.get_url(path), auth=self.auth)
        utils.check_response(response)
        return response

    def get_template_detail(self, id: int):
        """
        This function returns the template info based on the given template id.

        Parameters:
            id (int): Template Id to retrieve a particular `template` object
        Returns:
            Response (json object): A json object representing single template present in the database based on passed `id`.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.templates.get_template_detail(1)
        """
        path = api.Path.GET_TEMPLATE_DETAIL.value.format(id=id)
        response = requests.get(self.urlBuilder.get_url(path), auth=self.auth)
        utils.check_response(response)
        return response

    def get_template_version_detail(self, id: int, version_id: int):
        """
        This function returns the template-version info based on the given template id and version id.

        Parameters:
            id (int): Template Id to retrieve a particular `template` object.
            version_id (int): Version Id to retrieve a particular `template_version` object.
        Returns:
            Response (json object): A json object representing single template with version information present in the database based on passed `id` and `version_id`.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.templates.get_template_version_detail(1, 2)
        """
        path = api.Path.GET_TEMPLATE_VERSION_DETAIL.value.format(
            id=id, version_id=version_id
        )
        response = requests.get(self.urlBuilder.get_url(path), auth=self.auth)
        utils.check_response(response)
        return response

    def get_template_versions(self, id: int):
        """
        This function returns the template-version list based on the given template id.

        Parameters:
            id (int): Template Id to retrieve a particular `template` object.
        Returns:
            Response (list -> json object): A list representing all the template versions present in the database.
        Examples:
            >>> import pyconceptlibraryclient
            >>> client = pyconceptlibraryclient.Client(is_public=False)
            >>> client.templates.get_template_versions(1)
        """
        path = api.Path.GET_TEMPLATE_VERSIONS.value.format(id=id)
        response = requests.get(self.urlBuilder.get_url(path), auth=self.auth)
        utils.check_response(response)
        return response
