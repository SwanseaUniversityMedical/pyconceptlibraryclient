# pyconceptlibraryclient
An implementation of the API client for the Concept Library in Python.

The Concept Library is a system for storing, managing, sharing, and documenting clinical code lists in health research. More information can be found here: https://conceptlibrary.saildatabank.com/.

## Documentation
https://swanseauniversitymedical.github.io/pyconceptlibraryclient/

## Installation
This package can be installed using pip. In your terminal, run the following command:
```
pip install git+https://github.com/SwanseaUniversityMedical/pyconceptlibraryclient.git@v1.0.0
```

### Inside the SAIL gateway / offline install

SAIL users or users requiring offline installation of the package can:
1. Download the [latest release](https://github.com/SwanseaUniversityMedical/pyconceptlibraryclient/releases)
2. Install the package using pip, e.g. `pip install /path/to/file/pyconceptlibraryclient-1.0.1.tar.gz`

# Using the package
The package provides a function to connect to the Concept Library API and multiple functions to send requests to the API's endpoints.

## Creating an API connection

```python
from pyconceptlibraryclient import Client

# Non-authenticated API
client = Client(public=True)

# Authenticated API (terminal requests credentials)
client = Client(public=False)

# Authenticated API (user providing credentials)
client = Client(username='my-username', password='password')
```

The `url` parameter can be used to specify a different version of the ConceptLibrary API
``` python
from pyconceptlibraryclient import Client, DOMAINS

# Using common domains stored in pyconceptlibrary.DOMAINS
## SAIL (conceptlibrary.saildatabank.com/)
client = Client(
  public=True,
  url=DOMAINS.SAIL
)

## HDRUK (phenotypes.healthdatagateway.org/)
client = Client(
  public=True,
  url=DOMAINS.HDRUK
)

## ADP (conceptlibrary.saildatabank.com/ADP/)
client = Client(
  public=True,
  url=DOMAINS.ADP
)

## Gateway (conceptlibrary.serp.ac.uk/)
client = Client(
  public=True,
  url=DOMAINS.GATEWAY
)

## Demo site (conceptlibrary.demo-dev.saildatabank.com/)
client = Client(
  public=True,
  url=DOMAINS.DEMO
)

# Custom URL
client = Client(
  public=True,
  url='my-custom-url.com/'
)
```

## Making API requests
The following functions can be used to retrieve the various types of data stored in the Concept Library. For each function, more information visit the documentation pages, [here](https://swanseauniversitymedical.github.io/pyconceptlibraryclient/client/) or [here](https://conceptlibrary.saildatabank.com/api/v1/)

### Templates
``` python
# Get all templates
template_list = client.templates.get()

# Get the version history of a template
template_versions = client.templates.get_versions(1)

# Get the template detail
template_detail = client.templates.get_detail(1)

# Get a specific version of the template
template_list = client.templates.get_detail(1, version_id=1)
```

### Phenotypes

#### Querying
``` python
# Search phenotypes (defaults to paginated)
search_results = client.phenotypes.get(
  search='asthma',
  collections=19
)

page = search_results.get('page')
page_size = search_results.get('page_size')
total_pages = search_results.get('total_pages')
search_data = search_results.get('data')

# Iterate over search result pages
next_page = client.phenotypes.get(
  page=page + 1,
  search='asthma',
  collections=19
)

# [NOTE: not recommended!] Search unpaginated list of phenotypes
search_results = client.phenotypes.get(
  search='asthma',
  collections=19,
  no_pagination=True
)

# Search phenotypes
phenotype_versions = client.phenotypes.get_versions('PH1')

# Search phenotypes
phenotype_detail = client.phenotypes.get_detail('PH1')

# Search phenotypes
phenotype_detail = client.phenotypes.get_detail('PH1', version_id=2)

# Search phenotypes
phenotype_codelist = client.phenotypes.get_codelist('PH1')

# Search phenotypes
phenotype_codelist = client.phenotypes.get_codelist('PH1', version_id=2)
```

#### Downloading a definition file
``` python
# Downloading a phenotype's definition file
client.phenotypes.save_definition_file('./path/to/file.yaml', 'PH1')

# Downloading a specific version of a phenotype's definition file
client.phenotypes.save_definition_file('./path/to/file.yaml', 'PH1', version_id=2)
```

#### Creating/Updating
``` python
# Create a phenotype from a definition file
client.phenotypes.create('./path/to/file.yaml')

# Update a phenotype from a definition file
client.phenotypes.update('./path/to/file.yaml')
```

### Concepts
``` python
# Search concepts (defaults to paginated)
search_results = client.concepts.get(
  search='asthma',
  collections=19
)

page = search_results.get('page')
page_size = search_results.get('page_size')
total_pages = search_results.get('total_pages')
search_data = search_results.get('data')

# Iterate over search result pages
next_page = client.concepts.get(
  page=page + 1,
  search='asthma',
  collections=19
)

# [NOTE: not recommended!] Search unpaginated list of concepts
search_results = client.concepts.get(
  search='asthma',
  collections=19,
  no_pagination=True
)

# Search concepts
concept_versions = client.concepts.get_versions('C714')

# Search concepts
concept_detail = client.concepts.get_detail('C714')

# Search concepts
concept_detail = client.concepts.get_detail('C714', version_id=2567)

# Search concepts
concept_codelist = client.concepts.get_codelist('C714')

# Search concepts
concept_codelist = client.concepts.get_codelist('C714', version_id=2567)
```

### Collections
``` python
# Get all collections
collection_list = client.collections.get()

# Get the collection detail
collection_detail = client.collections.get_detail(18)
```

### Tags
``` python
# Get all tags
tag_list = client.tags.get()

# Get the tag detail
tag_detail = client.tags.get_detail(1)
```

### Datasources
``` python
# Get all datasources
datasource_list = client.datasources.get()

# Get the datasource detail
datasource_detail = client.datasources.get_detail(1)
```

### Ontology
``` python
# Get paginated list of ontological term(s) (nodes; paginated by default)
search_results = client.ontology.get()

page = search_results.get('page')
page_size = search_results.get('page_size')
total_pages = search_results.get('total_pages')
search_data = search_results.get('data')

# Iterate over search result pages
next_page = client.ontology.get(
  page=page + 1,
  search='asthma',
  collections=19
)

# [NOTE: not recommended!] Get unpaginated list of ontological term(s)
search_results = client.ontology.get(no_pagination=TRUE)

# Search ontological term(s) (paginated by default, apply `no_pagination=T` if required)
# [!] See the following for more information on parameters:
#     https://conceptlibrary.saildatabank.com/api/v1/#operations-tag-ontology
#
search_results = client.ontology.get(
  # Searches across names, descriptions & synonyms
  search='dementia',

  # Search by snomed codes (or ICD9/10, OPSC4, ReadCode2/3 etc)
  #  - Note: this will fuzzy match across all code mappings;
  #          apply the `exact_codes=T` parameter if you want exact matches
  codes='281004'
)

# Get a specific ontology node by ID
ontology_node = client.ontology.get_detail(1)

# Get all ontology groups available
ontology_groups = client.ontology.get_groups()

# Get the ontology group's detail
clin_speciality_list = client.ontology.get_group_detail(1)
```
