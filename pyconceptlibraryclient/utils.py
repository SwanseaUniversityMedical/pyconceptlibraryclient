import yaml
import re

def read_from_yaml_file(path: str) -> dict | None:
  '''
  Read yaml file from specified path

  Args:
    path (str): Location of yaml file
  
  Returns:
    Read in data, or None
  '''
  with open(path, 'r') as f:
    data = yaml.safe_load(f)
  return data

def write_to_yaml_file(path: str, data: dict | None) -> None:
  '''
  Writes provided data to yaml file

  Args:
    path (str): Location to save the yaml file
    data (dict): Entity definition data
  '''
  with open(path, 'w') as f:
    yaml.dump(
      data,
      f,
      default_flow_style=False,
      sort_keys=False,
    )

def try_parse_doi(publications: list) -> list:
  '''
  Tries to parse all DOIs from list of publications

  Args:
    publications (list): List of publications from entity definition file

  Returns:
    List of dicts, 'detail' key contains original publication details and 'doi' containing
    parsed DOI or None  
  '''
  pattern = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*\/(?:(?![\"&\'<>])\S)+)\b')

  output = [ ]
  for publication in publications:
    if publication is None or len(str(publication).strip()) < 1:
      continue

    doi = pattern.findall(publication)
    output.append({
      'details': publication,
      'doi': doi[0] if len(doi) > 0 else None
    })
  
  return output
