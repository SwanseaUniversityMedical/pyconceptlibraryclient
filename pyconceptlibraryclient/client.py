from requests.auth import HTTPBasicAuth
import getpass

from pyconceptlibraryclient.templates import Templates
from pyconceptlibraryclient.phenotypes import Phenotypes
from pyconceptlibraryclient.concepts import Concepts
from pyconceptlibraryclient.collections import Collections
from pyconceptlibraryclient.tags import Tags
from pyconceptlibraryclient.datasources import Datasources
from pyconceptlibraryclient.ontology import Ontology
import pyconceptlibraryclient.constants as constants

class Client():
  '''
  This package acts as a client for the ConceptLibrary API

  # Examples:
  
  ## Authentication
  ### Public API
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(public=True)
  ```

  ### Authenticated API (terminal requests credentials)
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(public=False)
  ```

  ### Authenticated API (providing credentials)
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(username='my-username', password='my-password')
  ```

  ## Providing a different URL
  ### Using built-in domains
  ``` python
  from pyconceptlibraryclient import Client, DOMAINS
  client = Client(public=False, url=DOMAINS.HDRUK)
  ```
  
  ### Using a custom URL
  ``` python
  from pyconceptlibraryclient import Client
  client = Client(public=False, url='my-custom-url')
  ```
  '''

  def __init__(
      self, 
      username: str = None,
      password: str = None,
      public: bool = False,
      url: constants.DOMAINS | str = constants.DEFAULT_URL
    ) -> None:
    if isinstance(url, constants.DOMAINS):
      url = url.value
    self.url = url or input('Connection URL: ')
    self.url = self.url if self.url[-1] == '/' else self.url + '/'

    if public:
      self.__auth = None
      return

    username = username or input('Username: ')
    password = password or getpass.getpass('Password: ')

    self.__auth = HTTPBasicAuth(
      username=username,
      password=password
    )

  @property
  def templates(self) -> Templates:
    '''
      Entrypoint for templates through the client instance
    '''
    if not getattr(self, '__templates', None):
      setattr(self, '__templates', Templates(self.url, self.__auth))
    return getattr(self, '__templates')

  @property
  def phenotypes(self) -> Phenotypes:
    '''
      Entrypoint for phenotypes through the client instance
    '''
    if not getattr(self, '__phenotypes', None):
      setattr(self, '__phenotypes', Phenotypes(self.url, self.__auth))
    return getattr(self, '__phenotypes')

  @property
  def concepts(self) -> Concepts:
    '''
      Entrypoint for concepts through the client instance
    '''
    if not getattr(self, '__concepts', None):
      setattr(self, '__concepts', Concepts(self.url, self.__auth))
    return getattr(self, '__concepts')

  @property
  def collections(self) -> Collections:
    '''
      Entrypoint for collections through the client instance
    '''
    if not getattr(self, '__collections', None):
      setattr(self, '__collections', Collections(self.url, self.__auth))
    return getattr(self, '__collections')

  @property
  def tags(self) -> Tags:
    '''
      Entrypoint for tags through the client instance
    '''
    if not getattr(self, '__tags', None):
      setattr(self, '__tags', Tags(self.url, self.__auth))
    return getattr(self, '__tags')

  @property
  def datasources(self) -> Datasources:
    '''
      Entrypoint for datasources through the client instance
    '''
    if not getattr(self, '__datasources', None):
      setattr(self, '__datasources', Datasources(self.url, self.__auth))
    return getattr(self, '__datasources')

  @property
  def ontology(self) -> Ontology:
    '''
      Entrypoint for ontology through the client instance
    '''
    if not getattr(self, '__ontology', None):
      setattr(self, '__ontology', Ontology(self.url, self.__auth))
    return getattr(self, '__ontology')
