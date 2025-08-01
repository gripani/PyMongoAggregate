from typing import Any

from app.operations.queries.query_operation import QueryOperation


class Equals(QueryOperation[Any]):

    operator = "$eq"
