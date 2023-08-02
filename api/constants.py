from enum import Enum


class Path(Enum):
    """
    This class consits of the specific path resource or endpoint on the server that we want to access.
    """

    # Main URL
    BASEURL_LOCAL = "http://localhost:8000/api/v1"
    BASEURL_PROD = "<Add Prod URL>"  # TODO Add this later

    # Concepts
    GET_ALL_CONCEPTS = "concepts"
    GET_CONCEPT_DETAIL = "concepts/C{concept_id}/detail"
    GET_CONCEPT_CODELIST = "concepts/C{concept_id}/export/codes"
    GET_CONCEPT_VERSIONS = "concepts/C{concept_id}/get-versions"
    GET_CONCEPT_VERSION_DETAIL = "concepts/C{concept_id}/version/{version_id}/detail"
    GET_CONCEPT_VERSION_CODELIST = (
        "concepts/C{concept_id}/version/{version_id}/export/codes"
    )

    # Collection
    GET_ALL_COLLECTIONS = "collections"
    GET_COLLECTION_BY_ID = "collections/{id}/detail"

    # Tags
    GET_ALL_TAGS = "tags"
    GET_TAG_BY_ID = "tags/{id}/detail"

    # Phenotype
    GET_ALL_PHENOTYPES = "phenotypes"
    GET_PHENOTYPE_DETAIL = "phenotypes/{id}/detail"
    GET_PHENOTYPE_VERSIONS = "phenotypes/{id}/get-versions"
    GET_PHENOTYPE_VERSION_DETAIL = "phenotypes/{id}/version/{version_id}/detail"
    GET_PHENOTYPE_FIELD = "phenotypes/{id}/export/{field}"
    GET_PHENOTYPE_VERSION_FIELD = "phenotypes/{id}/version/{version_id}/export/{field}"
    CREATE_PHENOTYPE = "phenotypes/create/"
    UPDATE_PHENOTYPE = "phenotypes/update/"
