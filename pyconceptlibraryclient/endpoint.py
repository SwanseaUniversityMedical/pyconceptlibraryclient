from requests.auth import HTTPBasicAuth
import requests
import json

import pyconceptlibraryclient.constants as constants

class Endpoint:
  '''
  Base class that describes an endpoint and defines shared behaviour
  '''

  def __init__(self, url: str, auth: HTTPBasicAuth = None) -> None:
    self._url = url
    self._auth = auth

  def _get(self, url: str, params: dict = None) -> list | None:
    '''
    Makes get request to supplied URL, with authentication and params if supplied

    Args:
      url (str): Url to make request to
      params (dict): params to query
    
    Returns:
      Loaded data, or None after checking response
    '''
    response = requests.get(
      url, 
      params=params,
      auth=self._auth
    )
    
    return self.__check_response(response)
  
  def _post(self, url: str, data: dict = None) -> list | None:
    '''
    Makes post request to supplied URL, with authentication and data if supplied

    Args:
      url (str): Url to make request to
      data (dict): Data to send
    
    Returns:
      Loaded data, or None after checking response
    '''
    response = requests.post(
      url,
      data=json.dumps(data),
      auth=self._auth
    )
    
    return self.__check_response(response)
  
  def _put(self, url: str, data: dict = None) -> list | None:
    '''
    Makes put request to supplied URL, with authentication and data if supplied

    Args:
      url (str): Url to make request to
      data (dict): Data to send
    
    Returns:
      Loaded data, or None after checking response
    '''
    response = requests.put(
      url,
      data=json.dumps(data),
      auth=self._auth
    )
    
    return self.__check_response(response)

  def _build_url(self, url: str, **kwargs) -> str:
    '''
    Builds URL based on connection URL, api path and formatted endpoint

    Args:
      url (str): Endpoint to format

    Returns:
      Formatted URL
    '''
    return self._url + constants.API_PATH + url.format(**kwargs)

  def __check_response(self, response: requests.Response) -> list | dict | None:
    '''
    Checks response of request, returns loaded response if successful otherwise raises error

    Args:
      Response (requests.Response): Request's response object

    Returns:
      Result if successful, otherwise None and raises error
    '''
    if response.status_code in constants.SUCCESS_STATUS_CODES:
      try:
        result = json.loads(response.text)
      except Exception as err:
        raise err
      else:
        return result

    try:
      error_response = json.loads(response.text)

      message, detail, errors = error_response.get('message'), error_response.get('detail'), error_response.get('errors')
      if message or detail or errors:
        raise RuntimeError(
          'Response {status_code}: {message} > {errors}'.format(
            status_code = response.status_code, 
            message = error_response.get('message') or error_response.get('detail'),
            errors = error_response.get('errors')
          )
        )
    except RuntimeError as err:
      raise err
    except Exception as err:
      raise err
