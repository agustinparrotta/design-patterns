import logging

logging.basicConfig(level="INFO")


class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query


class QueryEnhancer:
    def __init__(self, query: DictQuery):
        self.decorated = query

    def render(self):
        return self.decorated.render()


class RemoveEmpty(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v for k, v in original.items() if v}


class CaseInsensitive(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v.lower() for k, v in original.items()}


if __name__ == "__main__":
    original = DictQuery(name="John", surname="Doe", city="")
    logging.info(original.render())

    q1 = RemoveEmpty(original)
    logging.info(q1.render())

    q2 = CaseInsensitive(original)
    logging.info(q2.render())

    chain = CaseInsensitive(RemoveEmpty(original))
    logging.info(chain.render())
