from pyconceptlibraryclient.endpoint import Endpoint
from pyconceptlibraryclient.constants import Path

class Templates(Endpoint):
  '''
  Queries templates/ endpoints
  '''
  
  def __init__(self, *args, **kwargs) -> None:
    super(Templates, self).__init__(*args, **kwargs)

  def get(self) -> list | None:
    '''
    Queries templates/

    Returns:
      Response (list): A list containing all the templates present in the database
    
    Examples:
      >>> import pyconceptlibraryclient
      >>> client = pyconceptlibraryclient.Client(is_public=False)
      >>> client.templates.get()
    '''
    url = self._build_url(Path.GET_ALL_TEMPLATES)

    response = self._get(url)
    return response

  def get_versions(self, id: int) -> list | None:
    '''
    Queries templates/{id}/get-versions/

    Parameters:
      id (int): Template ID
    
    Returns:
      Response (list): Version list of queried template
    
    Examples:
        >>> import pyconceptlibraryclient
        >>> client = pyconceptlibraryclient.Client(is_public=False)
        >>> client.templates.get_versions(1)
    '''
    url = self._build_url(Path.GET_TEMPLATE_VERSIONS, id=id)

    response = self._get(url)
    return response

  def get_detail(self, id: int, version_id: int | None = None) -> list | None:
    '''
    Queries templates/{id}/detail/ or templates/{id}/versions/{version_id}/detail/ if
    version_id is supplied

    Parameters:
      id (int): Template ID
      version_id (int): Version ID
    
    Returns:
      Response (list): Details of queried template
    
    Examples:
        >>> import pyconceptlibraryclient
        >>> client = pyconceptlibraryclient.Client(is_public=False)

        >>> # Get detail of a template
        >>> client.templates.get_detail(1)
        
        >>> # Get detail of a template with specific version
        >>> client.templates.get_detail(1, version_id=1)
    '''
    url = Path.GET_TEMPLATE_DETAIL_VERSION if version_id else Path.GET_TEMPLATE_DETAIL
    url = self._build_url(url, id=id, version_id=version_id)

    response = self._get(url)
    return response
