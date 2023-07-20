import api
from pyconceptlibraryclient.phenotypes import Phenotype
from pyconceptlibraryclient.collection import Collection
from pyconceptlibraryclient.concepts import Concepts
from pyconceptlibraryclient.tags import Tags


class Client(api.Connection):
    def __init__(self, is_public: bool) -> None:
        super().__init__(is_public)
        self.is_public = is_public

    @property
    def phenotypes(self) -> Phenotype:
        """
        Entrypoint for Phenotypes through the client instance
        """
        if not getattr(self, "_phenotypes", None):
            setattr(self, "_phenotypes", Phenotype(self.is_public))
        return getattr(self, "_phenotypes")

    @property
    def tags(self) -> Tags:
        """
        Entrypoint for Tags through the client instance
        """
        if not getattr(self, "_tags", None):
            setattr(self, "_tags", Tags(self.is_public))
        return getattr(self, "_tags")

    @property
    def collections(self) -> Collection:
        """
        Entrypoint for Collections through the client instance
        """
        if not getattr(self, "_collections", None):
            setattr(self, "_collections", Collection(self.is_public))
        return getattr(self, "_collections")

    @property
    def concepts(self) -> Concepts:
        """
        Entrypoint for Concepts through the client instance
        """
        if not getattr(self, "_concepts", None):
            print(self.is_public)
            setattr(self, "_concepts", Concepts(self.is_public))
        return getattr(self, "_concepts")


def main():
    client = Client(is_public=False)
    # client.phenotypes.get_phenotypes()
    # client.collections.get_all_collections()
    # client.concepts.get_all_concepts()


if __name__ == "__main__":
    main()
