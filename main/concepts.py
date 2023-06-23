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

    def get_all_concepts(
        self,
        search: str = None,
        collection_ids: list = None,
        tag_ids: list = None,
        show_only_my_concepts: int = None,
        show_only_deleted_concepts: int = None,
        show_only_validated_concepts: int = None,
        brand: str = None,
        author: str = None,
        owner_username: str = None,
        do_not_show_versions: int = None,
        must_have_published_versions: int = None,
    ):
        """
        This function returns all the concepts.
        """
        path = api.Path.GET_ALL_CONCEPTS.value
        payload = {k: v for k, v in locals().items() if v is not None and k != "self"}
        response = requests.get(self.urlBuilder.get_url(path), params=payload)
        utils.check_response(response)
        return response

    def get_concept_detail(self, concept_id: int):
        """
        This function returns the concept detail based on the given concept id.
        """
        path = api.Path.GET_CONCEPT_DETAIL.value.format(concept_id=concept_id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_concept_export_codes(self, concept_id: int):
        """
        This function returns the concept export code list based on the given concept id.
        """
        path = api.Path.GET_CONCEPT_CODELIST.value.format(concept_id=concept_id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_concept_versions(self, concept_id: int):
        """
        This function returns the concept versions based on the given concept id.
        """
        path = api.Path.GET_CONCEPT_VERSIONS.value.format(concept_id=concept_id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_concept_version_detail(self, concept_id: int, version_id: int):
        """
        This function returns the concept version detail based on the given concept id and version id.
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
