from sklearn.cluster import KMeans
import subprocess
import pandas as pd
import sys
from io import StringIO
def model(titanic):
    features = titanic[['Age', 'Fare', 'Pclass']]

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(features)

    titanic['Cluster'] = kmeans.labels_

    with open("k.txt", 'w') as f:
        f.write(str(titanic['Cluster'].value_counts(sort=False)))

    return titanic

if __name__ == "__main__":
    csv_data = sys.stdin.read()
    
    df = pd.read_csv(StringIO(csv_data))

    df_titanic = model(df)
    
    csv_data = df_titanic.to_csv(index=False)

    process = subprocess.Popen(['python3', 'vis.py'], stdin=subprocess.PIPE, text=True)
    process.communicate(csv_data)