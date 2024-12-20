from pyconceptlibraryclient.endpoint import Endpoint
from pyconceptlibraryclient.constants import PATH

class Concepts(Endpoint):
  '''
  Queries concepts/ endpoints
  '''
  
  def __init__(self, *args, **kwargs) -> None:
    super(Concepts, self).__init__(*args, **kwargs)

  def get(self, **kwargs) -> dict | list | None:
    '''
    Queries concepts/, with optional query parameters

    NOTE:
      - See the following URL for more information on query parameters: https://conceptlibrary.saildatabank.com/api/v1/#operations-tag-concepts

    Keyword Args:
      search (string): Keyword search
      collections (list): IDs of collections
      tags (list): IDs of tags
      datasources (list): IDs of datasources

    Response (dict|list):
      - If paginated: a dict of concepts matching query parameters
      - If unpaginated: a list of concepts matching query parameters
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = Client(public=False)

      >>> # Get all concepts (defaults to paginated)
      >>> client.concepts.get()

      >>> # [NOTE: not recommended!] Get unpaginated list of concepts
      >>> client.concepts.get(no_pagination=True)

      >>> # Search concepts
      >>> client.concepts.get(search='asthma', collections=19)
    '''
    url = self._build_url(PATH.GET_ALL_CONCEPTS)

    response = self._get(url, params=kwargs)
    return response

  def get_versions(self, id: str) -> list | None:
    '''
    Queries concepts/{id}/get-versions/

    Args:
      id (str): ID of entity to query, in format C[\d+]
    
    Returns:
      Response (list): Version list of queried concept

    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = Client(public=False)
      >>> client.concepts.get_versions('PH1')
    '''
    url = self._build_url(PATH.GET_CONCEPT_VERSIONS, id=id)

    response = self._get(url)
    return response

  def get_detail(self, id: str, version_id: int | None = None) -> list | None:
    '''
    Queries concepts/{id}/detail/ or concepts/{id}/version/{version_id}/detail if 
    version_id is supplied

    Args:
      id (str): ID of entity to query, in format C[\d+]
      version_id (int): version ID of entity
    
    Returns:
      Response (list): Details of queried concept
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = Client(public=False)

      >>> # Get detail of phenotype, PH1
      >>> client.concepts.get_detail('PH1')

      >>> # Get detail of version 2 of phenotype, PH1
      >>> client.concepts.get_detail('PH1', version_id=2)
    '''
    url = PATH.GET_CONCEPT_DETAIL if version_id else PATH.GET_CONCEPT_DETAIL
    url = self._build_url(url, id=id, version_id=version_id)

    response = self._get(url)
    return response

  def get_codelist(self, id: str, version_id: int | None = None) -> list | None:
    '''
    Queries concepts/{id}/export/codes/ or 
    concepts/{id}/version/{version_id}/export/codes if version_id is supplied

    Args:
      id (str): ID of entity to query, in format C[\d+]
      version_id (int): version ID of entity
    
    Returns:
      Response (list): Codelist of queried concept
    
    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = Client(public=False)

      >>> # Get codelist of phenotype, PH1
      >>> client.concepts.get_codelist('PH1')

      >>> # Get codelist of version 2 of phenotype, PH1
      >>> client.concepts.get_codelist('PH1', version_id=2)
    '''
    url = PATH.GET_CONCEPT_CODELIST if version_id else PATH.GET_CONCEPT_CODELIST
    url = self._build_url(url, id=id, version_id=version_id)

    response = self._get(url)
    return response  
