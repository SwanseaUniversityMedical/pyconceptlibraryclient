from pyconceptlibraryclient.endpoint import Endpoint
from pyconceptlibraryclient.constants import Path

class Collections(Endpoint):
  '''
  Queries collections/ endpoints
  '''
  
  def __init__(self, *args, **kwargs) -> None:
    super(Collections, self).__init__(*args, **kwargs)

  def get(self) -> list | None:
    '''
    Queries collections/

    Returns:
      Response (list): A list containing all the collections present in the database
    
    Examples:
      >>> import pyconceptlibraryclient
      >>> client = pyconceptlibraryclient.Client(is_public=False)
      >>> client.collections.get()
    '''
    url = self._build_url(Path.GET_ALL_COLLECTIONS)

    response = self._get(url)
    return response

  def get_detail(self, id: int) -> list | None:
    '''
    Queries collections/{id}/detail/

    Parameters:
      id (int): Collection ID
    
    Returns:
      Response (list): Details of queried collection
    
    Examples:
        >>> import pyconceptlibraryclient
        >>> client = pyconceptlibraryclient.Client(is_public=False)
        >>> client.collections.get_detail(1)
    '''
    url = self._build_url(Path.GET_COLLECTION_BY_ID, id=id)

    response = self._get(url)
    return response
