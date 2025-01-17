import json
import csv
from datetime import datetime

import san
from pandas import DataFrame

san.ApiConfig.api_key = "API_SAN_KEY"

metrics = [
    "price_usd",
    "volume_usd",
    "daily_active_addresses"
]

start_date = "2023-01-01"
end_date = datetime.now().strftime("%Y-%m-%d")
data_set = DataFrame()

for metric in metrics:
    data = san.get(
        metric,
        slug="bitcoin",
        from_date=start_date,
        to_date=end_date,
        interval="1d"
    )
    if data_set.empty:
        data_set = data
    else:
        data_set = data_set.merge(data, left_index=True, right_index=True, suffixes=('_left', '_right'))


data_set["date"] = data_set.index
data_set = data_set[["date"] + [col for col in data_set.columns if col != "date"]]
data_set.columns = ["date","price", "volume", "daily_active_addresses"]

DataFrame.to_json(data_set, 'bitcoin_data_extended.json', orient='records')

DataFrame.to_csv(data_set, 'bitcoin_data_extended.csv', sep=";", index=False)
