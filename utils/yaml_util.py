import yaml


def should_write_field(value):
    if value == [] or value == "":
        return False
    else:
        return True


def write_to_yaml_file(file_location, data):
    with open(file_location, "w") as file:
        yaml.dump(data, file)
