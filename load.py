import pandas as pd
import sys
import subprocess


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <path_to_dataset>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    df = pd.read_csv(file_path)

    csv_data = df.to_csv(index=False)
    process = subprocess.Popen(['python3', 'eda.py'], stdin=subprocess.PIPE, text=True)
    process.communicate(csv_data)
