import pandas as pd
import glob

csv_files = glob.glob("data/daily_sales_data_*.csv")
dfs = [pd.read_csv(file) for file in csv_files]
all_data = pd.concat(dfs, ignore_index=True)

pink_data = all_data[all_data["product"] == "pink morsel"]

pink_data["price"] = pink_data["price"].str.replace('$', '', regex=False).astype(float)
pink_data["sales"] = pink_data["price"] * pink_data["quantity"]

processed_data = pink_data[["sales", "date", "region"]]

processed_data.to_csv("data/processed_sales_data.csv", index=False)
