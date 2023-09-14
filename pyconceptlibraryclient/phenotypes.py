import pandas as pd

from pyconceptlibraryclient.endpoint import Endpoint
from pyconceptlibraryclient.constants import Path
import pyconceptlibraryclient.utils as utils

PHENOTYPE_IGNORED_WRITE_FIELDS = [
  'owner', 'phenotype_id', 'phenotype_version_id',
  'created', 'updated', 'template'
]
PHENOTYPE_IGNORED_READ_FIELDS = [
  'versions', 'status', 'is_deleted', 'owner_access', 'coding_system',
  'publish_status', 'created', 'updated'
]

class Phenotypes(Endpoint):
  '''
  Queries phenotypes/ endpoints
  '''
  
  def __init__(self, *args, **kwargs) -> None:
    super(Phenotypes, self).__init__(*args, **kwargs)

  def get(self, **kwargs) -> list | None:
    '''
    Queries phenotypes/, with optional query parameters

    Keyword Args:
      search (string): Keyword search
      collections (list): IDs of collections
      tags (list): IDs of tags
      datasources (list): IDs of datasources
    
    Returns:
      Response (list): List of phenotypes matching query parameters
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = pyconceptlibraryclient.Client(is_public=False)

      >>> # Get all phenotypes
      >>> client.phenotypes.get()

      >>> # Search phenotypes
      >>> client.phenotypes.get(search='asthma', collections=19)
    '''
    url = self._build_url(Path.GET_ALL_PHENOTYPES)

    response = self._get(url, params=kwargs)
    return response

  def get_versions(self, id: str) -> list | None:
    '''
    Queries phenotypes/{id}/get-versions/

    Args:
      id (str): ID of entity to query, in format PH[\d+]
    
    Returns:
      Response (list): Version list of queried phenotype
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = pyconceptlibraryclient.Client(is_public=False)
      >>> client.phenotypes.get_versions('PH1')
    '''
    url = self._build_url(Path.GET_PHENOTYPE_VERSIONS, id=id)

    response = self._get(url)
    return response

  def get_detail(self, id: str, version_id: int | None = None) -> list | None:
    '''
    Queries phenotypes/{id}/detail/ or phenotypes/{id}/version/{version_id}/detail if 
    version_id is supplied

    Args:
      id (str): ID of entity to query, in format PH[\d+]
      version_id (int): version ID of entity
    
    Returns:
      Response (list): Details of queried phenotype
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = pyconceptlibraryclient.Client(is_public=False)

      >>> # Get detail of phenotype, PH1
      >>> client.phenotypes.get_detail('PH1')

      >>> # Get detail of version 2 of phenotype, PH1
      >>> client.phenotypes.get_detail('PH1', version_id=2)
    '''
    url = Path.GET_PHENOTYPE_DETAIL_VERSION if version_id else Path.GET_PHENOTYPE_DETAIL
    url = self._build_url(url, id=id, version_id=version_id)

    response = self._get(url)
    return response

  def get_codelist(self, id: str, version_id: int | None = None) -> list | None:
    '''
    Queries phenotypes/{id}/export/codes/ or 
    phenotypes/{id}/version/{version_id}/export/codes if version_id is supplied

    Args:
      id (str): ID of entity to query, in format PH[\d+]
      version_id (int): version ID of entity
    
    Returns:
      Response (list): Codelist of queried phenotype
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = pyconceptlibraryclient.Client(is_public=False)

      >>> # Get codelist of phenotype, PH1
      >>> client.phenotypes.get_codelist('PH1')

      >>> # Get codelist of version 2 of phenotype, PH1
      >>> client.phenotypes.get_codelist('PH1', version_id=2)
    '''
    url = Path.GET_PHENOTYPE_CODELIST_VERSION if version_id else Path.GET_PHENOTYPE_CODELIST
    url = self._build_url(url, id=id, version_id=version_id)

    response = self._get(url)
    return response  

  def save_to_file(self, path: str, id: str, version_id: int | None = None) -> None:
    '''
    Saves the YAML definition of the queried phenotype to file

    Args:
      path (str): Location to save the YAML file
      id (str): ID of entity to query, in format PH[\d+]
      version_id (int): version ID of entity
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = pyconceptlibraryclient.Client(is_public=False)

      >>> # Get codelist of phenotype, PH1
      >>> client.phenotypes.save_to_file('./path/to/file.yaml', 'PH1')

      >>> # Get codelist of version 2 of phenotype, PH1
      >>> client.phenotypes.save_to_file('./path/to/file.yaml', 'PH1', version_id=2)
    '''
    phenotype_data = self.get_detail(id=id, version_id=version_id)
    phenotype_data = self.__format_for_download(phenotype_data)

    utils.write_to_yaml_file(path, phenotype_data)
  
  def create(self, path: str) -> list | None:
    '''
    Uploads the specified phenotype definition file to the ConceptLibrary and creates
    a new phenotype

    Args:
      path (str): Location where the definition file is saved on your local machine
    
    Returns:
      Response (list): Details of the newly created phenotype
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = pyconceptlibraryclient.Client(is_public=False)
      >>> client.phenotypes.create('./path/to/file.yaml')
    '''
    data = utils.read_from_yaml_file(path)
    data = self.__format_for_upload(data)

    url = self._build_url(Path.CREATE_PHENOTYPE)
    response = self._post(url, data=data)
    response = response.get('entity')

    self.save_to_file(path, response.get('id'), version_id=response.get('version_id'))

    return response
  
  def update(self, path: str) -> list | None:
    '''
    Uses the specified phenotype definition file to update an already existing phenotype

    Args:
      path (str): Location where the definition file is saved on your local machine
    
    Returns:
      Response (list): Details of the updated phenotype
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = pyconceptlibraryclient.Client(is_public=False)
      >>> client.phenotypes.create('./path/to/file.yaml')
    '''
    data = utils.read_from_yaml_file(path)
    data = self.__format_for_upload(data, is_update=True)

    url = self._build_url(Path.UPDATE_PHENOTYPE)
    response = self._put(url, data=data)
    response = response.get('entity')

    self.save_to_file(path, response.get('id'), version_id=response.get('version_id'))

    return response

  def __format_for_upload(self, data: list | None, is_update: bool = False) -> list | None:
    '''
    
    '''
    result = {
      'data': data,
      'template': {
        'id': data['template']['id'],
        'version': data['template']['id']
      }
    }
    if is_update:
      result['entity'] = {
        'id': result['data']['phenotype_id']
      }

    if 'concept_information' in result['data'].keys():
      result['data']['concept_information'] = self.__format_concepts_for_upload(
        result['data']['concept_information']
      )

    if 'publications' in result['data'].keys():
      result['data']['publications'] = utils.try_parse_doi(result['data']['publications'])

    result['data'] = {k: v for k, v in result['data'].items() if k not in PHENOTYPE_IGNORED_WRITE_FIELDS}

    return result

  def __format_concepts_for_upload(self, data: list | None) -> list:
    '''
    
    '''
    result = []
    for concept in data:
      concept_type = concept['type']
      if concept_type == 'existing_concept':
        result.append({
          'name': concept['name'],
          'concept_id': concept['concept_id'],
          'concept_version_id': concept['concept_version_id'],
          'internal_type': concept_type
        })
        continue

      if concept_type == 'csv':
        new_concept = {
          'details': {
            'name': concept['name'],
            'coding_system': concept['coding_system'],
            'internal_type': concept['type']
          },
          'components': []
        }

        if 'concept_id' in concept and 'concept_version_id' in concept:
          new_concept |= {
            'concept_id': concept['concept_id'],
            'concept_version_id': concept['concept_version_id'],
            'is_dirty': True
          }
        else:
          new_concept['is_new'] = True
        
        new_concept['components'].append(self.__build_concept_components(concept, new_concept))

        result.append(new_concept)
        continue

    return result
  
  def __build_concept_components(self, concept: dict, new_concept: dict) -> dict:
    '''
    
    '''
    codelist = pd.read_csv(concept['filepath'])
    code_column, description_column = concept['code_column'], concept['description_column']
    has_description = description_column in codelist.columns
    
    new_component = {
      'is_new': True,
      'name': 'CODES - %s' % new_concept['details']['name'],
      'logical_type': 'INCLUDE',
      'source_type': 'FILE_IMPORT',
      'codes': []
    }
    for _, row in codelist.iterrows():
      new_component['codes'].append({
        'code': row[code_column],
        'description': '' if not has_description else row[description_column]
      })

    return new_component

  def __format_for_download(self, data: dict | None) -> list | None:
    '''
    
    '''
    result = {}
    for key, value in data[0].items():
      if not value:
        continue

      if key in PHENOTYPE_IGNORED_READ_FIELDS:
        continue

      if not isinstance(value, list) and not isinstance(value, dict):
        result[key] = value
        continue
    
      if key == 'concept_information':
        result[key] = []
        for concept in value:
          new_concept = {
            'name': concept['concept_name'],
            'type': 'existing_concept',
            'concept_id': concept['concept_id'],
            'concept_version_id': concept['concept_version_id']
          }

          result[key].append(new_concept)
        continue

      if isinstance(value, list):
        fields = {k: [v[k] for v in value] for k in value[0]}
        field_keys = fields.keys()

        if 'value' in field_keys:
          new_value = fields['value']
          if len(new_value) == 1:
            new_value = fields['value'][0]

          result[key] = new_value
          continue

        if 'doi' in field_keys:
          result[key] = fields['details']
          continue

      if isinstance(value, dict):
        field_keys = value.keys()
        if 'id' in field_keys and 'version_id' in field_keys:
          result[key] = {
            'id': value['id'],
            'version_id': value['version_id']
          }
        continue

    return result
