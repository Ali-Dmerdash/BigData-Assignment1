import pandas as pd
import subprocess
import sys
from io import StringIO

def generate_insight(df):

    with open("eda-in-1.txt", 'w') as f:
        f.write("Missing Values in Each Column:\n" + str(df.isnull().sum()))

    with open("eda-in-2.txt", 'w') as f:
        f.write("Duplicated Rows:\n" + str(df[df.duplicated()]))

    with open("eda-in-3.txt", 'w') as f:
        f.write("Unique values in 'Age' Column:\n" + str(df['Age'].unique()))

if __name__ == "__main__":
    csv_data = sys.stdin.read()
    
    df = pd.read_csv(StringIO(csv_data))
    generate_insight(df)

    csv_data = df.to_csv(index=False)
    process = subprocess.Popen(['python3', 'dpre.py'], stdin=subprocess.PIPE, text=True)
    process.communicate(csv_data)