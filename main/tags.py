import api
import utils
import requests


class Tags:
    """
    This class consists of the endpoints related to the Tags.
    """

    def __init__(self, is_public: bool = True) -> None:
        self.conn = api.Connection(is_public)
        self.urlBuilder = utils.URLBuilder()

    def get_all_tags(self):
        """
        This function returns all the tags.
        """
        path = api.Path.GET_ALL_TAGS.value
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response

    def get_tag_info(self, id: int):
        """
        This function returns the tag info based on the given tag id.
        """
        path = api.Path.GET_TAG_BY_ID.value.format(id=id)
        response = requests.get(self.urlBuilder.get_url(path))
        utils.check_response(response)
        return response


def main():
    tag = Tags()
    tag.get_all_tags()
    tag.get_tag_info(3)


if __name__ == "__main__":
    main()
