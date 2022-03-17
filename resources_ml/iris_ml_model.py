import pandas as pd
import numpy as np

# importing iris dataset and loading onto a pandas dataframe
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])


# adding another columns called as target_name using map funciton
def target_name(target):
    target_named = None
    if target == 0:
        target_named = 'setosa'
    elif target == 1:
        target_named =  'versicolor'
    else:
        target_named = 'virginica'
    return target_named

df['target_name'] = df.target.map(lambda x: target_name(x))


# shuffeling the dataset
df = df.sample(frac = 1)

# dropping the target variable
df.drop('target', axis = 1, inplace = True)

# changing target_name to dtype as category
df.target_name = df.target_name.astype('category')

# making a train-test split
train = df[:120]
test = df[120:]

# creating the features and targets for train and test datasets
train_X = train.drop('target_name', axis = 1)
train_Y = train['target_name']

test_X = test.drop('target_name', axis = 1)
test_Y = test['target_name']

# importing the ml classification models from sklearn library
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


# calling the log and rf model objects
log_model = LogisticRegression()
rf_model = RandomForestClassifier()

# importing the accuracy metrics from sklearn
from sklearn.metrics import accuracy_score

# fitting the log model and getting the accuracy score
log_model.fit(train_X, train_Y)
test_pred = log_model.predict(test_X)
score_log = accuracy_score(test_Y, test_pred)
print(score_log)


# fitting the RandomForestClassifier model and getting the accuracy score
rf_model.fit(train_X, train_Y)
test_pred_rf = rf_model.predict(test_X)
score_rf = accuracy_score(test_Y, test_pred_rf)
print(score_rf)

# dumping the models on pickle files
import pickle
pickle.dump(log_model,open("iris_ml_model.sav", "wb"))
pickle.dump(rf_model, open("iris_rf_model.sav", "wb"))


# Fin