# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    data = pd.read_csv("GBvideos.csv")
    for i, row in data.iterrows():
        old_s = row['trending_date'].replace(".", "/")
        old_s = datetime.strptime(old_s, '%Y/%d/%m')
        data.set_value(i, 'trending_date', old_s)
    print(data['trending_date'])
