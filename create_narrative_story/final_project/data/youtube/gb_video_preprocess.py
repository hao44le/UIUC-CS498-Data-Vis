# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime, date

if __name__ == '__main__':
    data = pd.read_csv("GBvideos.csv")
    data['trending_weekday'] = ""
    for i, row in data.iterrows():
        [year, day, month] = row['trending_date'].split(".")
        year = int("20"+year)
        month = int(month)
        day = int(day)
        d = datetime(year, month, day)
        data.set_value(i, 'trending_weekday', month)

    data.to_csv("GBvideos_post.csv")

