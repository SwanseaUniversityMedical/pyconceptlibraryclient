import api
import utils
import requests
import yaml


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

    def save_phenotype_definition(self, id: str, dir: str = None, version_id=None):
        phenotype_data = None
        if version_id is None:
            phenotype_data = self.get_phenotype_detail(id)
        else:
            phenotype_data = self.get_phenotype_version_detail(id, version_id).json()[0]

        result = {}
        for field_name in phenotype_data:
            if field_name not in utils.constants.API_IGNORE_TEMPLATE_FIELDS:
                field_value = phenotype_data[field_name]
                if utils.should_write_field(field_value):
                    if isinstance(field_value, dict):
                        if "id" in field_value and "version_id" in field_value:
                            result[field_name] = {
                                "id": field_value["id"],
                                "version_id": field_value["version_id"],
                            }
                        else:
                            result[field_name] = field_value
                    else:
                        if field_name == "concept_information":
                            result_concepts = []
                            for concept in range(len(field_value)):
                                concept_data = {
                                    field_value[concept]["concept_name"]: {
                                        "type": "existing_concept",
                                        "concept_id": field_value[concept][
                                            "concept_id"
                                        ],
                                        "concept_version_id": field_value[concept][
                                            "concept_version_id"
                                        ],
                                    }
                                }
                                result_concepts.append(concept_data)
                            result[field_name] = result_concepts
                        elif isinstance(field_value, str | int):
                            result[field_name] = field_value
                        elif isinstance(field_value, list):
                            if len(field_value) > 1:
                                result_values = []
                                for item in range(len(field_value)):
                                    result_values.append(field_value[item]["value"])
                                result[field_name] = result_values
                            elif field_name != "publications":
                                result[field_name] = field_value[0]["value"]
                            else:
                                result[field_name] = field_value[0]

        yaml.dump(
            result,
            open(f"./assets/gen/{id}-definition-file.yaml", "w"),
            default_flow_style=False,
            sort_keys=False,
        )


def main():
    phenotype = Phenotype()
    phenotype.get_phenotypes()
    phenotype.get_phenotypes(search="Alcohol")
    phenotype.get_phenotype_detail("PH1", search="Alcohol")
    phenotype.get_phenotype_versions("PH1")
    phenotype.get_phenotype_version_detail("PH1", 3)
    phenotype.get_phenotype_code_list("PH1")
    phenotype.get_phenotype_code_list_by_version("PH1", 2)
    phenotype.save_phenotype_definition("PH1", "./assets/gen", 2)
    phenotype.save_phenotype_definition("PH2", "./assets/gen", 4)
    phenotype.save_phenotype_definition("PH3", "./assets/gen", 6)


if __name__ == "__main__":
    main()
