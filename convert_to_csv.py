import pandas as pd

def convert_to_csv(data):
    df = pd.json_normalize(data)
    csv_data = df.to_csv(index=False)
    return csv_data
