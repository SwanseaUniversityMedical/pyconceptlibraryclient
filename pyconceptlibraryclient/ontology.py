from pyconceptlibraryclient.endpoint import Endpoint
from pyconceptlibraryclient.constants import PATH

class Ontology(Endpoint):
  '''
  Queries ontology/ endpoints
  '''
  
  def __init__(self, *args, **kwargs) -> None:
    super(Ontology, self).__init__(*args, **kwargs)

  def get(self, **kwargs) -> list | dict | None:
    '''
    Queries ontology/node/, with optional query parameters

    NOTE:
      - See the following URL for more information on query parameters: https://conceptlibrary.saildatabank.com/api/v1/#operations-tag-ontology

      - Adding the `?exact_codes` will match the exact SNOMED code instead of fuzzy matching
        the given `codes` across all related mappings (ICD-9/10, MeSH, OPSC4, ReadCodes etc)

    Keyword Args:

      | Param         | Type     | Default            | Desc                                                             |
      |---------------|----------|--------------------|------------------------------------------------------------------|
      | search        | `string` | `NULL`             | Full-text search                                                 |
      | codes         | `list`   | `NULL`             | Either (a) SNOMED code (see below); or (b) Code ID               |
      | exact_codes   | `empty`  | `NULL`             | apply this parameter if you would like to search for exact codes |
      | type_ids      | `list`   | `NULL`             | Filter ontology type by ID                                       |
      | reference_ids | `list`   | `NULL`             | Filter ontology by Atlas reference                               |
      | page          | `number` | `1`                | Page cursor                                                      |
      | page_size     | `enum`   | `1` (_20_ results) | Page size enum, where: `1` = 20, `2` = 50 & `3` = 100 rows       |

    Returns:
      Response (dict|list):
        - If paginated: a dict of ontological nodes matching query parameters
        - If unpaginated: a list of ontological nodes matching query parameters

    Examples:
      >>> from pyconceptlibraryclient import Client
      >>> client = Client(public=False)

      >>> # Get all ontological term(s) (nodes; defaults to paginated)
      >>> client.ontology.get()

      >>> # Search ontological terms (apply '?exact_codes' parameter to search only SNOMED codes)
      >>> client.ontology.get(search='dementia', codes='281004,569.82')
    '''
    url = self._build_url(PATH.GET_ONTOLOGY_SEARCH)

    response = self._get(url, params=kwargs)
    return response

  def get_detail(self, id: int) -> dict | None:
    '''
    Queries ontology/node/{id}/

    Parameters:
      id (int): Ontology node ID

    Returns:
      Response (dict): Details of queried ontology

    Examples:
        >>> import pyconceptlibraryclient
        >>> client = Client(public=False)
        >>> client.ontology.get_detail(1)
    '''
    url = self._build_url(PATH.GET_ONTOLOGY_DETAIL, id=id)

    response = self._get(url)
    return response

  def get_groups(self) -> list | None:
    '''
    Queries ontology/; gets list of all ontological groups (types)

    Returns:
      Response (list): Details of the ontology groups

    Examples:
        >>> import pyconceptlibraryclient
        >>> client = Client(public=False)
        >>> client.ontology.get_detail(1)
    '''
    url = self._build_url(PATH.GET_ONTOLOGY_GROUPS)

    response = self._get(url)
    return response

  def get_group_detail(self, id: int) -> list | None:
    '''
    Queries ontology/type/{id}/; gets an ontology group's detail

    Parameters:
      id (int): Ontological ID

    Returns:
      Response (dict): Details of the queried ontology group

    Examples:
        >>> import pyconceptlibraryclient
        >>> client = Client(public=False)
        >>> client.ontology.get_group_detail(1)
    '''
    url = self._build_url(PATH.GET_ONTOLOGY_TYPE, id=id)

    response = self._get(url)
    return response

