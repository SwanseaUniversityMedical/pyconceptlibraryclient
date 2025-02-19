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
      List of dicts:
        - 'details': Original publication details.
        - 'doi': Parsed DOI or None.
        - 'primary': True if marked as [primary] in text ignores case and whitespace, otherwise False.
  '''
  pattern = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*\/(?:(?![\"&\'<>])\S)+)\b')
  primary_pattern = re.compile(r'\[\s*primary\s*\]', re.IGNORECASE)

  output = [ ]
  for publication in publications:
    if publication is None or len(str(publication).strip()) < 1:
      continue

    is_primary = bool(primary_pattern.search(publication))  # Check if marker exists
    publication_cleaned = primary_pattern.sub("", publication).strip()  # Remove marker from text
    doi = pattern.findall(publication)

    output.append({
      'details': publication_cleaned,
      'doi': doi[0] if len(doi) > 0 else None,
      'primary': is_primary
    })
  
  return output

