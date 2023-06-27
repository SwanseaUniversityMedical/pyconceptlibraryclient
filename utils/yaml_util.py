from .constants import API_IGNORE_TEMPLATE_FIELDS, API_IGNORE_WRITE_FIELDS
import yaml, json


def should_write_field(value):
    if value == [] or value == "":
        return False
    else:
        return True


def write_to_yaml_file(file_location, data):
    yaml.dump(
        data,
        file_location,
        default_flow_style=False,
        sort_keys=False,
    )


def format_template(my_json: json):
    return {
        "id": my_json["data"]["template"][0]["id"],
        "version": my_json["data"]["template"][1]["version_id"],
    }


def format_phenotype(data, is_update: bool = False):
    my_json = json.loads(data)
    if is_update:
        my_json["entity"] = {"id": ""}
        my_json["entity"]["id"] = my_json["phenotype_id"]
        for field in API_IGNORE_WRITE_FIELDS:
            if is_update:
                del my_json[field]
    return my_json


def format_concept(concept_data: list):
    result = []
    for item in range(len(concept_data)):
        concept = concept_data[item]
        new_concept = {}
        for concept_name, concept_info in concept.items():
            new_concept.update({"name": concept_name})
            for params in concept_info:
                # For type
                if "type" in params.keys():
                    match params["type"]:
                        case "existing_concept":
                            new_concept.update({"internal_type": params["type"]})
                        case other:
                            new_concept.update(
                                {
                                    "details": {
                                        "coding_system": params["coding_system"],
                                    },
                                    "internal_type": params["type"],
                                }
                            )
                    continue
                # For concept_id
                elif "concept_id" in params.keys():
                    new_concept.update({"concept_id": params["concept_id"]})
                    continue

                # For concept_version_id
                elif "concept_history_id" in params.keys():
                    new_concept.update(
                        {"concept_version_id": params["concept_history_id"]}
                    )
                    continue
                else:
                    new_concept.update({"is_new": True})
                    continue

                # TODO : Logic for Csv and Inline to be added later
            result.append(new_concept)
    return result


def insert_empty_fields(my_json, is_update: bool = False):
    for field in API_IGNORE_TEMPLATE_FIELDS:
        if is_update:
            my_json["data"][field] = None
        else:
            my_json[field] = None
    return json.dumps(my_json, indent=2)


def yaml_to_json(dir: str):
    with open(dir, "r") as yaml_file:
        json_data = yaml.safe_load(yaml_file)
    return json.dumps(json_data)
