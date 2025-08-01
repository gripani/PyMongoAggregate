"""sum operator module"""
from app.const import COMMON_STAGES
from app.operations.operators.op_operation import OpOperation


class Sum(OpOperation[str | list[str] | OpOperation]):

    """$sum (aggregation)

    Calculates and returns the collective sum of numeric values. $sum ignores non-numeric values.
    """

    operator = "$sum"

    @staticmethod
    def stages_availability() -> tuple[str, ...]:
        """returns the available stages in which this operator can be defined"""
        return COMMON_STAGES
