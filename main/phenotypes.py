import api
import utils
import requests


class Phenotype:
    """
    This class consists of the endpoints related to the Phenotypes.
    """

    def __init__(self, is_public: bool = True) -> None:
        self.conn = api.Connection(is_public)

    def get_phenotypes(
        self,
        search: str = None,
        collection_ids: list = None,
        tag_ids: list = None,
        selected_phenotype_types: list = None,
        show_only_my_phenotypes: int = None,
        show_only_deleted_phenotypes: int = None,
        show_only_validated_phenotypes: int = None,
        brand: str = None,
        author: str = None,
        owner_username: str = None,
        do_not_show_versions: int = None,
        must_have_published_versions: int = None,
    ):
        """
        This function returns all the phenotypes.
        """
        path = "/phenotypes"
        payload = {k: v for k, v in locals().items() if v is not None and k != "self"}
        response = requests.get(self.conn.baseurl + path, params=payload)
        utils.check_response(response)
        utils.print_response(response)
        return response

    def get_phenotype_detail(
        self,
        id: str,
        search: str = None,
        collection_ids: list = None,
        tag_ids: list = None,
        selected_phenotype_types: list = None,
        show_only_my_phenotypes: int = None,
        show_only_deleted_phenotypes: int = None,
        show_only_validated_phenotypes: int = None,
        brand: str = None,
        author: str = None,
        owner_username: str = None,
        do_not_show_versions: int = None,
        must_have_published_versions: int = None,
    ):
        """
        This function returns the phenotype detail based on the given phenotype id.
        """
        path = f"/phenotypes/{id}/detail"
        payload = {k: v for k, v in locals().items() if v is not None and k != "self"}
        response = requests.get(self.conn.baseurl + path, params=payload)
        utils.check_response(response)
        utils.print_response(response)
        return response

    def get_phenotype_versions(self, id: str):
        """
        This function returns all the phenotype versions.
        """
        path = f"/phenotypes/{id}/get-versions"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        utils.print_response(response)
        return response

    def get_phenotype_version_detail(self, id: str, version_id: int):
        """
        This function returns the phenotype version detail based on the given phenotype id and the version id.
        """
        path = f"/phenotypes/{id}/version/{version_id}/detail"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        utils.print_response(response)
        return response

    def get_phenotype_code_list(self, id: str):
        """
        This function returns the codes list based on the given phenotype id.
        """
        path = f"/phenotypes/{id}/export/codes"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        utils.print_response(response)
        return response

    def get_phenotype_code_list(self, id: str):
        """
        This function returns the codes list based on the given phenotype id.
        """
        path = f"/phenotypes/{id}/export/codes"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        utils.print_response(response)
        return response

    def get_phenotype_code_list_by_version(self, id: str, version_id: int):
        """
        This function returns the codes list based on the given phenotype id.
        """
        path = f"/phenotypes/{id}/version/{version_id}/export/codes/"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        utils.print_response(response)
        return response


def main():
    phenotype = Phenotype()
    phenotype.get_phenotypes()
    phenotype.get_phenotypes(search="Alcohol")
    phenotype.get_phenotype_detail("PH1", search="Alcohol")
    phenotype.get_phenotype_versions("PH1")
    phenotype.get_phenotype_version_detail("PH1", 3)
    phenotype.get_phenotype_code_list("PH1")
    phenotype.get_phenotype_code_list_by_version("PH1", 2)


if __name__ == "__main__":
    main()
