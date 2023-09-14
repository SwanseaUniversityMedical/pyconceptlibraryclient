from pyconceptlibraryclient.endpoint import Endpoint
from pyconceptlibraryclient.constants import Path

class Datasources(Endpoint):
  '''
  Queries datasources/ endpoints
  '''
  
  def __init__(self, *args, **kwargs) -> None:
    super(Datasources, self).__init__(*args, **kwargs)

  def get(self) -> list | None:
    '''
    Queries datasources/

    Returns:
      Response (list): A list containing all the datasources present in the database
    
    Examples:
      >>> import pyconceptlibraryclient
      >>> client = pyconceptlibraryclient.Client(is_public=False)
      >>> client.datasources.get()
    '''
    url = self._build_url(Path.GET_ALL_DATASOURCES)

    response = self._get(url)
    return response

  def get_detail(self, id: int) -> list | None:
    '''
    Queries datasources/{id}/detail/

    Parameters:
      id (int): Datasource ID
    
    Returns:
      Response (list): Details of queried datasource
    
    Examples:
        >>> import pyconceptlibraryclient
        >>> client = pyconceptlibraryclient.Client(is_public=False)
        >>> client.datasources.get_detail(1)
    '''
    url = self._build_url(Path.GET_DATASOURCE_BY_ID, id=id)

    response = self._get(url)
    return response
