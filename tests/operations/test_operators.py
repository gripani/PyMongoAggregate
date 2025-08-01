from app.operations.operators.accumulator import Accumulator
from app.operations.operators.avg import Avg
from app.operations.operators.cond import Cond
from app.operations.operators.function import Function
from app.operations.operators.gt import Gt
from app.operations.operators.split import Split


def test_accumulator(code: str):

    op = Accumulator(codes=(code, code, code))
    assert op["$accumulator"]["init"].startswith("function")
    assert op["$accumulator"]["accumulateCode"].startswith("function")
    assert op["$accumulator"]["mergeCode"].startswith("function")


def test_avg():

    op = Avg("$quantity")
    assert op["$avg"] == "$quantity"


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
