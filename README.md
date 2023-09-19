# pyconceptlibraryclient
An implementation of the API client for the Concept Library in Python.

The Concept Library is a system for storing, managing, sharing, and documenting clinical code lists in health research. More information can be found here: https://conceptlibrary.saildatabank.com/.

## Documentation
https://swanseauniversitymedical.github.io/pyconceptlibraryclient/

## Installation
This package can be easily installed using pip. In your terminal, run the following command:
```
pip install git+https://github.com/SwanseaUniversityMedical/pyconceptlibraryclient.git@v1.0.0
```

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
client = Client(username='my-username', password='password)
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
  url=DOMAINS.DEMO
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
# Search phenotypes
search_results = client.phenotypes.get(
  search='asthma',
  collections=19
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
# Search concepts
search_results = client.concepts.get(
  search='asthma',
  collections=19
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