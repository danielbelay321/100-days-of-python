
import csv

# rep_name  ="[name]"
# with open("invited_names.txt") as names:
#     names = names.readlines()
#
#
#
# for name in names:
#     name = name.strip()
#     with open("starting_letters.txt") as starting:
#         letter = starting.read()
#         new_letter = letter.replace(rep_name,name).strip()
#         print(new_letter)
#         with open(f"{name.strip()}.txt","w") as lettering:
#             lettering.write(new_letter)


import pandas as pd

data_dict = {
    "name": ["daniel", "abebe", "samuel"],
    "score": [90, 98, 90]
}

datas = pd.DataFrame(data_dict)
datas.to_csv(r"D:\003 weather-data.csv", index=False)
print(datas)