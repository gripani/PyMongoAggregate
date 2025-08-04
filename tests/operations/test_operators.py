from pymongo_aggregate.operations.operators.accumulator import Accumulator
from pymongo_aggregate.operations.operators.avg import Avg
from pymongo_aggregate.operations.operators.cond import Cond
from pymongo_aggregate.operations.operators.function import Function
from pymongo_aggregate.operations.operators.gt import Gt
from pymongo_aggregate.operations.operators.size import Size
from pymongo_aggregate.operations.operators.split import Split


def test_accumulator(code: str):

    op = Accumulator(codes=(code, code, code))
    assert op["$accumulator"]["init"].startswith("function")
    assert op["$accumulator"]["accumulateCode"].startswith("function")
    assert op["$accumulator"]["mergeCode"].startswith("function")


def test_avg():

    op = Avg("$quantity")
    assert op["$avg"] == "$quantity"


def test_size():
    op = Size("$quantity")
    assert op["$size"] == "$quantity"


def test_function(code):

    op = Function(
        code=code,
        args=[]
    )
    assert op["$function"]["body"].startswith("function")
    assert len(op["$function"]["args"]) == 0


def test_split():

    op = Split(field="field", delimiter=",")
    assert op["$split"][0] == "field"
    assert op["$split"][1] == ','


def test_cond(a, b):

    op = Cond(
        if_expr=Gt("field", a),
        then_case=b,
        else_case=0
    )
    assert op["$cond"]["if"]["$gt"][0] == "field"
    assert op["$cond"]["if"]["$gt"][1] == a
    assert op["$cond"]["then"] == b
