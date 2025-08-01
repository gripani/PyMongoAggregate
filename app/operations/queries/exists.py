from typing import Literal

from app.operations.queries.query_operation import QueryOperation

type ExistsContentType = Literal[1]


class Exists(QueryOperation[ExistsContentType]):

    operator = "$exists"

    def __init__(self):
        super().__init__(1)
