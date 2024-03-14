import pandas as pd
import subprocess
import sys

from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2

def preprocess_data(file_path):
    df_titanic = pd.read_csv(file_path)
    
    #Data Cleaning
    df_titanic = df_titanic.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    df_titanic['Age'].fillna(df_titanic['Age'].mean(), inplace=True)

    #Data Transformation

    df_titanic = pd.get_dummies(df_titanic, columns=['Sex', 'Embarked'])

    df_titanic['Age_Disc'] = df_titanic['Age']

    scaler = MinMaxScaler()
    df_titanic[['Age', 'Fare']] = scaler.fit_transform(df_titanic[['Age', 'Fare']])

    df_titanic['FamilySize'] = df_titanic['SibSp'] + df_titanic['Parch'] + 1
    
    #Data Reduction
    X = df_titanic.drop('Survived', axis=1)
    y = df_titanic['Survived']
    selector = SelectKBest(chi2, k=4)
    X_new = selector.fit_transform(X, y)

    #Data Discretization
    bins = [0, 18, 30, 50, 80]
    labels = ['Child', 'Young Adult', 'Adult', 'Elderly']
    df_titanic['AgeGroup'] = pd.cut(df_titanic['Age_Disc'], bins=bins, labels=labels)

    return df_titanic

if __name__ == "__main__":

    file_path = sys.argv[1]
    df_processed = preprocess_data(file_path)
    
    df_processed.to_csv('res_dpre.csv', index=False)
    subprocess.run(["python3", "model.py", 'res_dpre.csv'])