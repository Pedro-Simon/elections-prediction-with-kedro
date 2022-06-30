"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def split_feature_target(df):
    '''Separates X and y (features and target) sets'''

    X = df.drop('FinalMandates', axis=1)
    y = df['FinalMandates']
    
    return X, y

def split_train_test(X, y):
    '''Split features and target into train and test sets'''
    
    X_train, X_test, y_train, y_test = train_test_split(
            X, 
            y, 
            test_size=0.3, 
            random_state=9999, 
            stratify=y
        )
        
    return X_train, X_test, y_train, y_test

def fit_model(X_train, X_test, y_train, y_test):
    """Fits RandomForestRegressor Classifier using a training dataset"""
    
    classifier = RandomForestRegressor(max_depth=10, random_state=9999)
    classifier.fit(X_train, y_train)
    
    #Predicts the test dataset to get performance measures
    y_pred = classifier.predict(X_test)
    
        # R2 Score
    r2 = float(format(r2_score(y_test, y_pred), '.5f'))
    print("\nR2 score: ", r2)
    
        #Calculate RMSE (Root Mean Square Error)
    rmse = float(format(np.sqrt(mean_squared_error(y_test, y_pred)), '.3f'))
    print("\nRMSE: ", rmse)
    
    return classifier