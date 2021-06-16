import pandas as pd
import csv
import os

# arr = os.listdir()
# path=arr[3]

# files_path = [os.path.abspath(x) for x in os.listdir()]
# print(files_path[3])
# print(path)

# files = open()

# with open('crawl_pilih.txt', 'r', encoding='utf-8') as f:
    # data = f.read()
# print(data)
# # print(len(f))
# f.close()

# file=[ i for i in enumerate(data)]
# for i,j in data:
#     file.append(''+f)

# print(file)

# data = []
# # # path = "crawl_pilih.txt"
# files = [f for f in os.listdir(files_path[3]) if os.path.isfile(f)]
# # # # files = [f for f in os.listdir(path) if os.path.isfile(f)]
# for f in files:
#   with open (f, "r") as myfile:
    # data.append(myfile.read())
#
# df = pd.DataFrame(data, columns=['username','tweets'])
# for i in range(108):
#     df = df.append({'id':i}, ignore_index=True)
# df =
# print(df)


# index =
df = pd.read_csv("crawl_pilih2.csv",  delimiter=";", header=None, quoting=csv.QUOTE_NONE, encoding='utf-8')
df.columns = ["username", "tweets"]
print(df.head(8))
# df = pd.read_csv("crawl_pilih.csv", index=False ,delimiter=";")
# df = pd.read_csv("data.csv", index_col=0 ,delimiter=",")

# df = pd.read_csv("crawl_pilih.csv", index_col=0 ,sep=";")
# print(df.head(7))


# # saving xlsx file
# GFG = pd.ExcelWriter('crawl_pilih_label2.xlsx')
GFG = pd.ExcelWriter('crawl_pilih_label3.xlsx')
df.to_excel(GFG)
GFG.save()
# df.to_excel('./crawl_pilih_plusplus.xlsx')
# df.to_excel(GFG, index = False)
#
