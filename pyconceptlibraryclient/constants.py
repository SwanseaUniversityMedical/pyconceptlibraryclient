from enum import Enum

API_VERSION = '1'
API_PATH = 'api/v%s/' % API_VERSION

SUCCESS_STATUS_CODES = [200, 201]

class PATH(str, Enum):
  '''
  Library endpoints
  '''

  # Templates
  GET_ALL_TEMPLATES = 'templates'
  GET_TEMPLATE_VERSIONS = 'templates/{id}/get-versions/'
  GET_TEMPLATE_DETAIL = 'templates/{id}/detail/'
  GET_TEMPLATE_DETAIL_VERSION = 'templates/{id}/version/{version_id}/detail/'

  # Phenotypes
  GET_ALL_PHENOTYPES = 'phenotypes'
  GET_PHENOTYPE_VERSIONS = 'phenotypes/{id}/get-versions'
  GET_PHENOTYPE_DETAIL = 'phenotypes/{id}/detail'
  GET_PHENOTYPE_DETAIL_VERSION = 'phenotypes/{id}/version/{version_id}/detail'
  GET_PHENOTYPE_CODELIST = 'phenotypes/{id}/export/codes'
  GET_PHENOTYPE_CODELIST_VERSION = 'phenotypes/{id}/version/{version_id}/export/codes'
  CREATE_PHENOTYPE = 'phenotypes/create/'
  UPDATE_PHENOTYPE = 'phenotypes/update/'

  # Concepts
  GET_ALL_CONCEPTS = 'concepts'
  GET_CONCEPT_VERSIONS = 'concepts/{id}/get-versions'
  GET_CONCEPT_DETAIL = 'concepts/{id}/detail'
  GET_CONCEPT_DETAIL_VERSION = 'concepts/{id}/version/{version_id}/detail'
  GET_CONCEPT_CODELIST = 'concepts/{id}/export/codes'
  GET_CONCEPT_CODELIST_VERSION = 'concepts/{id}/version/{version_id}/export/codes'

  # Collections
  GET_ALL_COLLECTIONS = 'collections'
  GET_COLLECTION_BY_ID = 'collections/{id}/detail'

  # Tags
  GET_ALL_TAGS = 'tags'
  GET_TAG_BY_ID = 'tags/{id}/detail'

  # Datasources
  GET_ALL_DATASOURCES = 'data-sources'
  GET_DATASOURCE_BY_ID = 'data-sources/{id}/detail'

  # Ontology
  GET_ONTOLOGY_GROUPS = 'ontology/'
  GET_ONTOLOGY_TYPE   = 'ontology/type/{id}/'
  GET_ONTOLOGY_SEARCH = 'ontology/node/'
  GET_ONTOLOGY_DETAIL = 'ontology/node/{id}/'

class DOMAINS(str, Enum):
  '''
  List of common ConceptLibrary domains:
   - SAIL: https://conceptlibrary.saildatabank.com/
   - HDRUK: https://phenotypes.healthdatagateway.org/
   - ADP: https://conceptlibrary.saildatabank.com/ADP/
   - GATEWAY: http://conceptlibrary.serp.ac.uk/
   - DEMO: https://conceptlibrary.demo-dev.saildatabank.com/
   - LOCAL: http://127.0.0.1:8000/
  '''
  SAIL = 'https://conceptlibrary.saildatabank.com/',
  HDRUK = 'https://phenotypes.healthdatagateway.org/',
  ADP = 'https://conceptlibrary.saildatabank.com/ADP/',
  GATEWAY = 'http://conceptlibrary.serp.ac.uk/',
  DEMO = 'https://conceptlibrary.demo-dev.saildatabank.com/',
  LOCAL = 'http://127.0.0.1:8000/'

DEFAULT_URL = DOMAINS.SAIL
