import pandas as pd

class DatasetManager:
    def load_csv(self, path):
        return pd.read_csv(path)

    def save_csv(self, df, path):
        df.to_csv(path, index=False)

    def describe(self, df):
        return df.describe()
