import re
import requests
from bs4 import BeautifulSoup

import pandas as pd
import csv
from datetime import datetime
from datetime import datetime


url = "http://www.nairaland.com"
raw_html = requests.get(url)
raw_data = raw_html.text
soup_data = BeautifulSoup(raw_data, "lxml")
print(soup_data("td"))
for data in soup_data("td"):
    print (data.text)
member_found = None

re_match = "[\w]+\([\d]+\)"
for data in soup_data("td"):
    data_found = re.findall(re_match, data.text)
    
    if data_found:
        member_found = data_found
    print(member_found)

member_found_replaced = [x.replace(")", "") for x in member_found]
print(member_found_replaced)

for y in member_found_replaced:
    member_cleaned = y.split("(")
    print(member_cleaned)

    
member_cleaned={}
for y in member_found_replaced:
 temp_data = y.split("(")
 member_cleaned[temp_data[0]] = int(temp_data[1])
print(member_cleaned)
columns_name = ["Username", "Age"]
df = pd.DataFrame(list(member_cleaned.items()), columns = columns_name )
print(df)
todays_date = datetime.now().date()
df["Date"] = todays_date
print(df)
csv_name = todays_date.strftime("%Y%m%d")

df.to_csv(csv_name + ".csv")
