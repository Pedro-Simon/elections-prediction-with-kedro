"""
This is a boilerplate pipeline 'preprocessing'
generated using Kedro 0.18.1
"""
import pandas as pd

def drop_unwanted(df: pd.DataFrame):
    df = df.drop(['blankVotes', 'nullVotes', 'subscribedVoters', 'pre.blankVotes', 'pre.nullVotes', 'pre.subscribedVoters', 'pre.totalVoters', 'time'], axis=1)
    return df