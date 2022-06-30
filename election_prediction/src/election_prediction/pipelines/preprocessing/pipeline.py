"""
This is a boilerplate pipeline 'preprocessing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import drop_unwanted

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = drop_unwanted,
            inputs = "raw_election_dataset",
            outputs = "pp_election_dataset",
            name = "drop_unwanted"
        )
    ])
