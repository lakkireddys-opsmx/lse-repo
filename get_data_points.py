import sys
import pandas as pd
import random

def get_data_points(file_path):
    df = pd.read_csv(file_path)
    total_rows = len(df)
    start_index = random.randint(0, total_rows - 10)
    data_points = df.iloc[start_index:start_index + 10]
    return data_points

if __name__ == "__main__":
    input_file = sys.argv[1]
    data_points = get_data_points(input_file)
    data_points.to_csv(sys.stdout, index=False)

