from requests.auth import HTTPBasicAuth
import getpass

from pyconceptlibraryclient.templates import Templates
from pyconceptlibraryclient.phenotypes import Phenotypes
from pyconceptlibraryclient.concepts import Concepts
from pyconceptlibraryclient.collections import Collections
from pyconceptlibraryclient.tags import Tags
from pyconceptlibraryclient.datasources import Datasources
import pyconceptlibraryclient.constants as constants

class Client():
  '''
  This package acts as a client for the ConceptLibrary API

  # Examples:
  
  ## Authentication
  ### Public API
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(is_public=True)
  ```

  ### Authenticated API (terminal requests credentials)
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(is_public=False)
  ```

  ### Authenticated API (providing credentials)
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(username='my-username', password='my-password')
  ```

  ## Providing a different URL
  ### Using built-in domains
  ``` python
  from pyconceptlibraryclient import Client, Domains
  client = Client(is_public=False, url=Domains.HDRUK)
  ```
  
  ### Using a custom URL
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(is_public=False, url='my-custom-url')
  ```
  '''

  def __init__(
      self, 
      username: str = None,
      password: str = None,
      is_public: bool = False,
      url: constants.Domains | str = constants.DEFAULT_URL
    ) -> None:
    if isinstance(url, constants.Domains):
      url = url.value
    self.url = url or input('Connection URL: ')
    self.url = self.url if self.url[-1] == '/' else self.url + '/'

    if is_public:
      return

    username = username or input('Username: ')
    password = password or getpass.getpass('Password: ')

    self._auth = HTTPBasicAuth(
      username=username,
      password=password
    )

  @property
  def templates(self) -> Templates:
    '''
      Entrypoint for templates through the client instance
    '''
    if not getattr(self, '__templates', None):
      setattr(self, '__templates', Templates(self.url, self._auth))
    return getattr(self, '__templates')

  @property
  def phenotypes(self) -> Phenotypes:
    '''
      Entrypoint for phenotypes through the client instance
    '''
    if not getattr(self, '__phenotypes', None):
      setattr(self, '__phenotypes', Phenotypes(self.url, self._auth))
    return getattr(self, '__phenotypes')

  @property
  def concepts(self) -> Concepts:
    '''
      Entrypoint for concepts through the client instance
    '''
    if not getattr(self, '__concepts', None):
      setattr(self, '__concepts', Concepts(self.url, self._auth))
    return getattr(self, '__concepts')

  @property
  def collections(self) -> Collections:
    '''
      Entrypoint for collections through the client instance
    '''
    if not getattr(self, '__collections', None):
      setattr(self, '__collections', Collections(self.url, self._auth))
    return getattr(self, '__collections')

  @property
  def tags(self) -> Tags:
    '''
      Entrypoint for tags through the client instance
    '''
    if not getattr(self, '__tags', None):
      setattr(self, '__tags', Tags(self.url, self._auth))
    return getattr(self, '__tags')

  @property
  def datasources(self) -> Datasources:
    '''
      Entrypoint for datasources through the client instance
    '''
    if not getattr(self, '__datasources', None):
      setattr(self, '__datasources', Datasources(self.url, self._auth))
    return getattr(self, '__datasources')
