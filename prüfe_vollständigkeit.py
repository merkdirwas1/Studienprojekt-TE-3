import csv
import os
import numpy as np
import pandas as pd

name_data = []
query_helper = []
query_helper2 = []
with open("help_scores", "r") as data_file:
    reader = csv.reader(data_file)
    data = list(reader)

for point in data:
    query_helper.append((point[0], point[1]))
    point[0] = point[0].replace("/", "_")
    point[0] = point[0] + "_" + point[1]
    name_data.append(point[0])

del name_data[0]
del query_helper[0]
comp = len(name_data)

# name column


right = []

for filename in os.listdir("../../data"):
    if filename[:-9] in name_data:
        right.append(filename)
        index = name_data.index(filename[:-9])
        del query_helper[index]
        del name_data[index]
    else:
        continue


with open("help_scores", "r") as data_file:
    reader = csv.reader(data_file)
    data = list(reader)
    with open('query_new', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\t',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for point in data:
            if (point[0],point[1]) in query_helper:
                    spamwriter.writerow(point)

