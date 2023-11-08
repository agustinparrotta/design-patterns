import logging

logging.basicConfig(level="INFO")


class UsernameLookup:
    """Class to adapt."""

    def search(self, user_namespace):
        logging.info("looking for %s", user_namespace)


class UserSource(UsernameLookup):
    "Option 1. Adapted class. Client will use fetch method."

    def fetch(self, user_id, username):
        user_namespace = self._adapt_arguments(user_id, username)
        return self.search(user_namespace)

    @staticmethod
    def _adapt_arguments(user_id, username):
        return f"{user_id}:{username}"


class UserSourceComp:
    def __init__(self, username_lookup: UsernameLookup) -> None:
        self.username_lookup = username_lookup

    def fetch(self, user_id, username):
        user_namespace = self._adapt_arguments(user_id, username)
        return self.username_lookup.search(user_namespace)

    @staticmethod
    def _adapt_arguments(user_id, username):
        return f"{user_id}:{username}"


if __name__ == "__main__":
    logging.info("Option 1")
    source = UserSource()
    source.fetch("123", "JohnDoe")

    logging.info("Option 2")
    source = UserSourceComp(UsernameLookup())
    source.fetch("123", "JohnDoe")
