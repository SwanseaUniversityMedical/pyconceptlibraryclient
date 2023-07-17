import api
import utils
import requests


class Concepts:
    """
    This class consists of the endpoints related to the Concepts.
    """

    def __init__(self, is_public: bool = True) -> None:
        self.conn = api.Connection(is_public)
        self.urlBuilder = utils.URLBuilder()

    def get_all_concepts(self, **kwargs):
        """
        This function returns all the concepts.

        Keyword Args:
            search (string): Optional,
            collection_ids (list): Optional,
            tag_ids (list): Optional,
            show_only_my_concepts (int): Optional,
            show_only_deleted_concepts (int): Optional,
            show_only_validated_concepts (int): Optional,
            brand (string): Optional,
            author (string): Optional,
            owner_username (string): Optional,
            do_not_show_versions (int): Optional,
            must_have_published_versions (int): Optional
        Returns:
            Response (list -> json objects): A list representing all the concepts present in the database.
        Example:
            >>> import pyconceptlibraryclient
            >>> client = Client(is_public=False)
            >>> client.concepts.get_all_concepts()
        """
        path = api.Path.GET_ALL_CONCEPTS.value
        payload = {k: v for k, v in kwargs.items() if v is not None}
        response = requests.get(self.urlBuilder.get_url(path), params=payload)
        utils.check_response(response)
        return response

    def get_concept_detail(self, concept_id: int):
        """
        This function returns the concept detail based on the given concept id.

        Parameters:
            concept_id (int): Concept Id to retrieve a particular `concept` object
        Returns:
            Response (json object): A json object representing a single concept present in the database based on passed `id`.
        Example:
            >>> import pyconceptlibraryclient
            >>> client = Client(is_public=False)
            >>> client.concepts.get_concept_detail(concept_id=1)
        """
        path = api.Path.GET_CONCEPT_DETAIL.value.format(concept_id=concept_id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_concept_export_codes(self, concept_id: int):
        """
        This function returns the concept export code list based on the given concept id.

        Parameters:
            concept_id (int): Concept Id to retrieve a particular `concept_export_code` object
        Returns:
            Response (json object): A json object representing a single concept export code present in the database based on passed `id`.
        Example:
            >>> import pyconceptlibraryclient
            >>> client = Client(is_public=False)
            >>> client.concepts.get_concept_export_codes(concept_id=1)
        """
        path = api.Path.GET_CONCEPT_CODELIST.value.format(concept_id=concept_id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_concept_versions(self, concept_id: int):
        """
        This function returns the concept versions based on the given concept id.

        Parameters:
            concept_id(int): Concept Id to retrieve a particular `concept_version` object
        Returns:
            Response (json object): A json object representing a single concept version present in the database based on passed `id`.
        Example:
            >>> import pyconceptlibraryclient
            >>> client = Client(is_public=False)
            >>> client.concepts.get_concept_versions(concept_id=1)
        """
        path = api.Path.GET_CONCEPT_VERSIONS.value.format(concept_id=concept_id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_concept_version_detail(self, concept_id: int, version_id: int):
        """
        This function returns the concept version detail based on the given concept id and version id.

        Parameters:
            concept_id(int): Concept Id to retrieve a particular `concept_version_detail` object
            version_id(int): Version Id to retrieve a particular `concept_version_detail` object
        Returns:
            Response (json object): A json object representing a single concept version detail present in the database based on passed `id`.
        Example:
            >>> import pyconceptlibraryclient
            >>> client = Client(is_public=False)
            >>> client.concepts.get_concept_version_detail(concept_id=1, version_id=1)
        """
        path = api.Path.GET_CONCEPT_VERSION_DETAIL.value.format(
            concept_id=concept_id, version_id=version_id
        )
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_concept_version_export_codes(self, concept_id: int, version_id: int):
        """
        This function returns the concept version export codes based on the given concept id and version id.

        Parameters:
            concept_id(int): Concept Id to retrieve a particular `concept_version_export_code` object
            version_id(int): Version Id to retrieve a particular `concept_version_export_code` object
        Returns:
            Response (json object): A json object representing a single concept_version_export_code present in the database based on passed `id`.
        Example:
            >>> import pyconceptlibraryclient
            >>> client = Client(is_public=False)
            >>> client.concepts.get_concept_version_detail(concept_id=1, version_id=1)
        """
        path = api.Path.GET_CONCEPT_VERSION_CODELIST.value.format(
            concept_id=concept_id, version_id=version_id
        )
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response


def main():
    concept = Concepts()
    concept.get_all_concepts(search="Alcohol")
    concept.get_all_concepts(brand="HDRUK", collection_ids=[20, 23])
    concept.get_concept_detail(714)
    concept.get_concept_export_codes(714)
    concept.get_concept_versions(714)
    concept.get_concept_version_detail(714, 8627)
    concept.get_concept_version_export_codes(714, 8627)


if __name__ == "__main__":
    main()
