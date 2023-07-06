import api
import utils
import requests
import yaml, json


class Phenotype:
    """
    This class consists of the endpoints related to the Phenotypes.
    """

    def __init__(self, is_public: bool = True) -> None:
        self.conn = api.Connection(is_public)
        self.urlBuilder = utils.URLBuilder()

    def get_phenotypes(self, **kwargs):
        """
        This function returns all the phenotypes.

        Optional Parameters:

        search: str,
        collection_ids: list,
        tag_ids: list,
        selected_phenotype_types: list,
        show_only_my_phenotypes: int,
        show_only_deleted_phenotypes: int,
        show_only_validated_phenotypes: int,
        brand: str,
        author: str,
        owner_username: str,
        do_not_show_versions: int,
        must_have_published_versions: int,
        """
        path = api.Path.GET_ALL_PHENOTYPES.value
        payload = {k: v for k, v in kwargs.items() if v is not None}
        response = requests.get(self.urlBuilder.get_url(path), params=payload)
        utils.check_response(response)
        return response

    def get_phenotype_detail(self, **kwargs):
        """
        This function returns the phenotype detail based on the given phenotype id.

        Optional Parameters:

        id: str,
        search: str,
        collection_ids: list,
        tag_ids: list,
        selected_phenotype_types: list,
        show_only_my_phenotypes: int,
        show_only_deleted_phenotypes: int,
        show_only_validated_phenotypes: int,
        brand: str,
        author: str,
        owner_username: str,
        do_not_show_versions: int,
        must_have_published_versions: int
        """
        path = api.Path.GET_PHENOTYPE_DETAIL.value.format(id=id)
        payload = {k: v for k, v in kwargs.items() if v is not None}
        response = requests.get(self.urlBuilder.get_url(path), params=payload)
        utils.check_response(response)
        return response

    def get_phenotype_versions(self, id: str):
        """
        This function returns all the phenotype versions.
        """
        path = api.Path.GET_PHENOTYPE_VERSIONS.value.format(id=id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_phenotype_version_detail(self, id: str, version_id: int):
        """
        This function returns the phenotype version detail based on the given phenotype id and the version id.
        """
        path = api.Path.GET_PHENOTYPE_VERSION_DETAIL.value.format(
            id=id, version_id=version_id
        )
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_phenotype_code_list(self, id: str):
        """
        This function returns the codes list based on the given phenotype id.
        """
        path = api.Path.GET_PHENOTYPE_CODELIST.value.format(id=id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_phenotype_code_list_by_version(self, id: str, version_id: int):
        """
        This function returns the codes list based on the given phenotype id.
        """
        path = api.Path.GET_PHENOTYPE_VERSION_CODELIST.value.format(
            id=id, version_id=version_id
        )
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
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

    def create_phenotype(self, data):
        """
        This function creates a phenotype defined in the form of json which is passed as an argument
        """
        path = api.Path.CREATE_PHENOTYPE.value
        response = requests.post(
            self.urlBuilder.get_url(path),
            auth=self.conn.auth,
            data=json.dumps(data),
        )
        utils.check_response(response)
        return response

    def update_phenotype(self, data):
        """
        This function creates a phenotype defined in the form of json which is passed as an argument
        """
        path = api.Path.UPDATE_PHENOTYPE.value
        response = requests.put(
            self.urlBuilder.get_url(path),
            auth=self.conn.auth,
            data=json.dumps(data),
        )
        utils.check_response(response)
        return response

    def upload_phenotype(
        self, is_update: bool, dir: str = "./assets/definition_file_create.yaml"
    ):
        """
        This function creates/updates a phenotype defined in the form of json which is passed as an argument depending upon
        the parameter 'is_update' that is passed. If it is True, then we hit the update_phenotype endpoint otherwise, we hit
        the create_endpoint endpoint.
        """
        data = utils.yaml_to_json(dir)
        if data:
            modified_data = utils.format_phenotype(data, is_update)
            if is_update:
                to_be_updated_phenotype = json.loads(
                    utils.insert_empty_fields(modified_data)
                )
                to_be_updated_phenotype = modified_data
                if to_be_updated_phenotype["data"]["template"]:
                    template_data = utils.format_template(to_be_updated_phenotype)
                    del to_be_updated_phenotype["data"]["template"]
                    to_be_updated_phenotype["template"] = template_data
                else:
                    raise ValueError("Template id and version are missing")
                if to_be_updated_phenotype["data"]["concept_information"]:
                    to_be_updated_phenotype["data"][
                        "concept_information"
                    ] = utils.format_concept(
                        to_be_updated_phenotype["data"]["concept_information"]
                    )
                response = self.update_phenotype(to_be_updated_phenotype)
                phenotype_response_json = response.json()
                result = {
                    "data": json.loads(data)["data"],
                    "entity": [{"id": phenotype_response_json["entity"]["id"]}],
                }
                yaml.dump(
                    result,
                    open(
                        utils.constants.PATH_FOR_STORING_FILE_AFTER_UPDATE_PHENOTYPE
                        + f"{phenotype_response_json['entity']['id']}-definition-output-file.yaml",
                        "w",
                    ),
                    default_flow_style=False,
                    sort_keys=False,
                )
                yaml.dump(
                    result,
                    open("./assets/definition_file_update.yaml", "w"),
                    default_flow_style=False,
                    sort_keys=False,
                )
            else:
                new_phenotype = json.loads(utils.insert_empty_fields(modified_data))
                new_phenotype = {"data": modified_data}
                if new_phenotype["data"]["template"]:
                    template_data = utils.format_template(new_phenotype)
                    del new_phenotype["data"]["template"]
                    new_phenotype["template"] = template_data
                else:
                    raise ValueError("Template id and version are missing")
                if new_phenotype["data"]["concept_information"]:
                    new_phenotype["data"]["concept_information"] = utils.format_concept(
                        new_phenotype["data"]["concept_information"]
                    )
                response = self.create_phenotype(new_phenotype)
                phenotype_response_json = response.json()
                result = {"data": json.loads(data), "response": phenotype_response_json}
                yaml.dump(
                    result,
                    open(
                        utils.constants.PATH_FOR_STORING_FILE_AFTER_CREATE_PHENOTYPE
                        + f"{phenotype_response_json['entity']['id']}-definition-output-file.yaml",
                        "w",
                    ),
                    default_flow_style=False,
                    sort_keys=False,
                )
            return result
        else:
            raise ValueError(
                "File is invalid, please check the file location and filetype (supports .yaml files only)"
            )


def main():
    phenotype = Phenotype(is_public=False)
    # phenotype.get_phenotypes()
    # phenotype.get_phenotypes(search="Alcohol")
    # phenotype.get_phenotype_detail("PH1", search="Alcohol")
    # phenotype.get_phenotype_versions("PH1")
    # phenotype.get_phenotype_version_detail("PH1", 3)
    # phenotype.get_phenotype_code_list("PH1")
    # phenotype.get_phenotype_code_list_by_version("PH1", 2)
    # phenotype.save_phenotype_definition("PH1", "./assets/gen", 2)
    # phenotype.save_phenotype_definition("PH2", "./assets/gen", 4)
    # phenotype.save_phenotype_definition("PH3", "./assets/gen", 6)
    phenotype.upload_phenotype(is_update=False)


if __name__ == "__main__":
    main()
