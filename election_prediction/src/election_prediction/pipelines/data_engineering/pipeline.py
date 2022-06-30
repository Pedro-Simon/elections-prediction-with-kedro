"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import remove_outliers, encode_label_features

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = remove_outliers,
            inputs = 'pp_election_dataset',
            outputs = 'no_outliers_election_dataset',
            name = 'remove_outliers'
        ),
        node(
            func = encode_label_features,
            inputs = 'pp_election_dataset',
            outputs = [
                'encoded_election_dateset',
                'label_encoder_party',
                'label_encoder_territory'
            ],
            name = 'encode_label_features'
        )
    ])
