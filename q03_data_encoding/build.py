# %load q03_data_encoding/build.py
from greyatomlib.multivariate_regression_project.q01_load_data.build import load_data
from greyatomlib.multivariate_regression_project.q02_data_split.build import split_dataset
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
df = load_data('data/student-mat.csv')
 
x_train, x_test, y_train, y_test =  split_dataset(df)

# Write your code below
def label_encode(X,X_test):
    X=X.apply(LabelEncoder().fit_transform)
    X_test=x_test.apply(LabelEncoder().fit_transform)
    return X,X_test



