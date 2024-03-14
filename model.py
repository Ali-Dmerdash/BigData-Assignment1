from sklearn.cluster import KMeans
import subprocess
import pandas as pd
import sys

def model(file_path):
    titanic = pd.read_csv(file_path)

    features = titanic[['Age', 'Fare', 'Pclass']]

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(features)

    titanic['Cluster'] = kmeans.labels_

    with open("k.txt", 'w') as f:
        f.write(str(titanic['Cluster'].value_counts(sort=False)))

    return titanic

if __name__ == "__main__":
    
    file_path = sys.argv[1]
    df_titanic = model(file_path)

    csv_data = df_titanic.to_csv(index=False)

    # subprocess.run(["python3", "vis.py"], input=csv_data, text=True, encoding='utf-8')

    process = subprocess.Popen(['python3', 'vis.py'], stdin=subprocess.PIPE, text=True)
    process.communicate(csv_data)