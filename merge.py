import csv

dataset_1=[]
dataset_2=[]

with open("final.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_1.appenda(row)

with open("new_data.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

header_1=dataset_1[0]
star_data_1=dataset_1[1:]

header_2=dataset_2[0]
star_data_2=dataset_2[1:]

headers=header_1+header_2
star_data=[]

for index, data_row in enumerate(star_data_1):
    star_data.append(star_data_1[index]+star_data_2[index])

with open("finalData.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)