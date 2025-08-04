from re import compile as re_compile

from pymongo_aggregate.operations.operators.multiply import Multiply
from pymongo_aggregate.operations.operators.regex_find import RegexFind
from pymongo_aggregate.operations.operators.sum import Sum
from pymongo_aggregate.operations.stages.count import Count
from pymongo_aggregate.operations.stages.group import Group
from pymongo_aggregate.operations.stages.match import Match
from pymongo_aggregate.operations.stages.project import Project
from pymongo_aggregate.operations.stages.unwind import Unwind


def test_count():

    op = Count("year")
    assert op["$count"] == "year"


def test_group():

    op = Group({
        "totalSaleAmount": Sum(Multiply(["field0", "field1"]))
    })
    assert op["$group"]["totalSaleAmount"]["$sum"]["$multiply"][0] == "field0"
    assert op["$group"]["totalSaleAmount"]["$sum"]["$multiply"][1] == "field1"


def test_output():

    pipeline = [
        Match({
            "experiment_name": "experiment2_proxies"
        }),
        Project({
            "proxy_id": 1,
            "input_text": 1,
            "capture_country": RegexFind(input_field="$output", pattern=re_compile(r"\*\*Country\*\*\n\s+-\s+(.*)\n"))
        }),
        Unwind(
            path="$capture_country.captures",
            include_array_index="country_index",
            preserve_null_and_empty_arrays=True
        ),
        Match({
            "country_index": 0
        }),
        Project({
            "_id": 0,
            "proxy_id": 1,
            "input_text": 1,
            "output_country": "$capture_country.captures"
        })
    ]

    for stage in pipeline:
        print(str(stage))
