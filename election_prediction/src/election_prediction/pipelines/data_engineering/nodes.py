"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import LabelEncoder

def remove_outliers(df):
    #Calculate zscore for each row and column
    z = np.abs(stats.zscore(df.drop(['territoryName', 'Party'], axis=1)))
    
    #Remove rows with outliers
    return df[(z < 3).all(axis=1)]

def encode_label_features(df):
    #Creating and fitting label encoder for Party
    label_encoder_party = LabelEncoder()
    label_encoder_party = label_encoder_party.fit(df['Party'])
    df['Party'] = label_encoder_party.transform(df['Party'])

    #Creating and fitting label encoder for Territory
    label_encoder_territory = LabelEncoder()
    label_encoder_territory = label_encoder_territory.fit(df['territoryName'])
    df['territoryName'] = label_encoder_territory.transform(df['territoryName'])

    return df, label_encoder_party, label_encoder_territory