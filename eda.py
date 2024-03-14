import pandas as pd
import subprocess
import sys

def generate_insight(file_path):

    with open("eda-in-1.txt", 'w') as f:
        f.write("Missing Values in Each Column:\n" + str(df.isnull().sum()))

    with open("eda-in-2.txt", 'w') as f:
        f.write("Duplicated Rows:\n" + str(df[df.duplicated()]))

    with open("eda-in-3.txt", 'w') as f:
        f.write("Unique values in 'Age' Column:\n" + str(df['Age'].unique()))

if __name__ == "__main__":
    file_path = sys.argv[1]
    df = pd.read_csv(file_path)
    
    generate_insight(file_path)    
    subprocess.run(["python3", "dpre.py", file_path])