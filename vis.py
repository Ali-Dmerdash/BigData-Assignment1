import matplotlib.pyplot as plt
import sys
import pandas as pd
from io import StringIO

def create_visualization(titanic):
    plt.scatter(titanic['Age'], titanic['Fare'], c=titanic['Cluster'])
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('K-means Clustering of Titanic Passengers')
    plt.savefig('vis.png')

if __name__ == "__main__":
    csv_data = sys.stdin.read()
    
    titanic = pd.read_csv(StringIO(csv_data))
    create_visualization(titanic)