import api
import utils
import requests


class Tags:
    """
    This class consists of the endpoints related to the Tags.
    """

    def __init__(self, is_public: bool = True) -> None:
        self.conn = api.Connection(is_public)

    def get_all_tags(self):
        """
        This function returns all the tags.
        """
        path = "/tags"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        utils.print_response(response)
        return response

    def get_tag_info(self, id: int):
        """
        This function returns the tag info based on the given tag id.
        """
        path = f"/tags/{id}"
        response = requests.get(self.conn.baseurl + path)
        utils.check_response(response)
        utils.print_response(response)
        return response


def main():
    tag = Tags()
    tag.get_all_tags()
    tag.get_tag_info(3)


if __name__ == "__main__":
    main()
