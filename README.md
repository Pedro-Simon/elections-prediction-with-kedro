# elections-prediction-with-kedro
This repository contains a machine learning model to predict portuguese elections results using Kedro.
The information about the dataset used in this project can be found [here](https://archive.ics.uci.edu/ml/datasets/Real-time+Election+Results%3A+Portugal+2019).

## Getting started

### Clone repository
To run this project at your local machine, it's first necessary to clone this repository.

### Install requirements
The requirements file is located in path ./election_prediction/src/requirements.txt.
If using pip, run the command pip install -r ./path/to/requirements.txt (changing the correct path)

### Getting the dataset
It´s not necessary to download the dataset from anywhere. The raw data is located inside the ./election_prediction/data/01_raw folder.

### Running Kedro
Now that you've installed Kedro, simply run the command <b>kedro run</b> to execute all pipelines.
By default, this project is configured to run all the pipelines with kedro run command.
If you want to run a specific pipeline, use <b>kedro run --pipeline [PIPELINE_NAME]</b>.

List of all pipelines names:
- <b>pp</b> - pipeline of pre-processing of data, where the data is cleaned.
- <b>de</b> - pipeline of feature engineering (data engineering), where new columns are created.
- <b>ds</b> - pipeline of data science, where the dataset is splited and model is fitted.

## About Kedro

Kedro is a Data Science tool that helps MLOps processes turning data transformation and prediction modelling into a pipeline. With Kedro, the collaborative workflow between the Data Scientist and Data Engineer is enhanced.

To learn more about kedro, check the [Documentation](https://kedro.readthedocs.io/en/stable/).
