from re import compile as re_compile

from pymongo_aggregate.operations.operators.regex_find import RegexFind
from pymongo_aggregate.pipeline import PipelineBuilder


def test_pipeline_builder():
    print()

    pipeline_builder = (
        PipelineBuilder()
        .match({"experiment_name": "experiment2_proxies"})
        .project({
            "proxy_id": 1,
            "input_text": 1,
            "capture_country": RegexFind(input_field="$output", pattern=re_compile(r"\*\*Country\*\*\n\s+-\s+(.*)\n"))
        })
        .unwind(
            path="$capture_country.captures",
            include_array_index="country_index",
            preserve_null_and_empty_arrays=True
        )
        .match({"country_index": 0})
        .project({
            "_id": 0,
            "proxy_id": 1,
            "input_text": 1,
            "output_country": "$capture_country.captures"
        })
        .build()
    )
    pipeline = pipeline_builder.pipeline

    for stage in pipeline:
        print(str(stage))
