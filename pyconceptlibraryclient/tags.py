from pyconceptlibraryclient.endpoint import Endpoint
from pyconceptlibraryclient.constants import Path

class Tags(Endpoint):
  '''
  Queries tags/ endpoints
  '''
  
  def __init__(self, *args, **kwargs) -> None:
    super(Tags, self).__init__(*args, **kwargs)

  def get(self) -> list | None:
    '''
    Queries tags/

    Returns:
      Response (list): A list containing all the tags present in the database
    
    Examples:
      >>> import pyconceptlibraryclient
      >>> client = Client(is_public=False)
      >>> client.tags.get()
    '''
    url = self._build_url(Path.GET_ALL_TAGS)

    response = self._get(url)
    return response

  def get_detail(self, id: int) -> list | None:
    '''
    Queries tags/{id}/detail/

    Parameters:
      id (int): Tag ID
    
    Returns:
      Response (list): Details of queried tags
    
    Examples:
        >>> import pyconceptlibraryclient
        >>> client = Client(is_public=False)
        >>> client.tags.get_detail(1)
    '''
    url = self._build_url(Path.GET_TAG_BY_ID, id=id)

    response = self._get(url)
    return response
