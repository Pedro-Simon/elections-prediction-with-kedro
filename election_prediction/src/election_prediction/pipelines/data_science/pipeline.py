"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_feature_target, split_train_test, fit_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = split_feature_target,
            inputs = 'encoded_election_dateset',
            outputs = ['X', 'y'],
            name = 'split_feature_target'
        ),
        node(
            func = split_train_test,
            inputs = ['X', 'y'],
            outputs = ['X_train', 'X_test', 'y_train','y_test'],
            name = 'split_train_test'
        ),
        node(
            func = fit_model,
            inputs = ['X_train', 'X_test', 'y_train','y_test'],
            outputs = 'classifier',
            name = 'fit_model'
        )
    ])
