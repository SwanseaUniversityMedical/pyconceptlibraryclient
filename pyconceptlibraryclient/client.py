import api
from pyconceptlibraryclient.phenotypes import Phenotype
from pyconceptlibraryclient.collection import Collection
from pyconceptlibraryclient.concepts import Concepts
from pyconceptlibraryclient.tags import Tags
from pyconceptlibraryclient.datasources import DataSources


class Client(api.Connection):
    def __init__(self, is_public: bool) -> None:
        super().__init__(is_public)
        self.is_public = is_public
        self.baseurl, self.auth = super().establish()

    @property
    def phenotypes(self) -> Phenotype:
        """
        Entrypoint for Phenotypes through the client instance
        """
        if not getattr(self, "_phenotypes", None):
            setattr(self, "_phenotypes", Phenotype(url=self.baseurl, auth=self.auth))
        return getattr(self, "_phenotypes")

    @property
    def tags(self) -> Tags:
        """
        Entrypoint for Tags through the client instance
        """
        if not getattr(self, "_tags", None):
            setattr(self, "_tags", Tags(url=self.baseurl, auth=self.auth))
        return getattr(self, "_tags")

    @property
    def collections(self) -> Collection:
        """
        Entrypoint for Collections through the client instance
        """
        if not getattr(self, "_collections", None):
            setattr(self, "_collections", Collection(url=self.baseurl, auth=self.auth))
        return getattr(self, "_collections")

    @property
    def concepts(self) -> Concepts:
        """
        Entrypoint for Concepts through the client instance
        """
        if not getattr(self, "_concepts", None):
            setattr(
                self,
                "_concepts",
                Concepts(url=self.baseurl, auth=self.auth),
            )
        return getattr(self, "_concepts")

    @property
    def datasources(self) -> DataSources:
        """
        Entrypoint for DataSources through the client instance
        """
        if not getattr(self, "_datasources", None):
            setattr(
                self,
                "_datasources",
                DataSources(url=self.baseurl, auth=self.auth),
            )
        return getattr(self, "_datasources")


def main():
    client = Client(is_public=False)
    # client.phenotypes.get_phenotypes()
    # client.collections.get_all_collections()
    # client.concepts.get_all_concepts()
    # client.tags.get_all_tags()
    # client.datasources.get_all()
    # client.datasources.get_one_detail(1)


if __name__ == "__main__":
    main()
