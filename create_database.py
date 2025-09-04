import itertools
import sqlite3
import csv
import os
from time import sleep
import numpy as np
from huggingface_hub import HfApi
import pandas as pd
from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
"""pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)"""


def create_statistics():
    con = sqlite3.connect("Studienprojekt.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS statistics")
    cur.execute("CREATE TABLE statistics(Name, min, max, mean, median, spread)")

    res = cur.execute("SELECT Name FROM Metadata")
    names = res.fetchall()
    Name_list = list(itertools.chain(*names))
    for name in Name_list:
        res = cur.execute("SELECT * FROM " + name)
        data = res.fetchall()
        arr = np.zeros(len(names)+1)
        for cnt in range(len(data)):
            arr[cnt] = data[cnt][1]

        params = (name, arr.min(), arr.max(),arr.mean(), np.median(arr), arr.max() - arr.min())
        cur.execute("INSERT INTO statistics VALUES (?,?,?,?,?,?)", params)
    con.commit()


def create_datatables():
    con = sqlite3.connect("Studienprojekt.db")
    cur = con.cursor()

    for filename in os.listdir("data"):
        table_name = filename[:-9]
        table_name = table_name.replace("-", "_")
        table_name = table_name.replace(".", "_")
        cur.execute("DROP TABLE IF EXISTS "+table_name)
        cur.execute("CREATE TABLE " + table_name + "(Name, score, language, categorie, size)")
        with open("data\\" + filename, 'r') as file :
           data_reader = csv.reader(file)
           data = list(data_reader)
           del data[0]
           for point in data:
               name = point[0].replace("/", "_")
               name = name + "_" + point[1]
               name = name.replace("-", "_")
               name = name.replace(".", "_")

               res = cur.execute("SELECT * FROM Metadata WHERE Name='"+name+"'")
               row = res.fetchall()
               if row == []:
                   continue
               params = (name, point[-1], row[0][-2], row[0][-1], row[0][-3])
               cur.execute("INSERT INTO "+table_name+" VALUES (?,?,?,?, ?)", params)


           con.commit()






def create_meta_table():
    api = HfApi()
    con = sqlite3.connect("Studienprojekt.db")
    cur = con.cursor()

    #cur.execute("CREATE TABLE IF NOT EXISTS  Metadata(Name, size, language, categorie)")
    cur.execute("DROP TABLE IF EXISTS Metadata")
    cur.execute("CREATE TABLE Metadata(Name, size, language, categorie)")
    with open("/archiv/datasets_names", "r") as f:
        categorie_data = {}
        reader = csv.reader(f, delimiter="\t")
        for line in reader:
            categories = []
            sleep(1)
            try:
                card_data = api.list_datasets(search=line[0])
                data = list(card_data)[0].tags

                for categorie in data:
                    if "task_categories" in categorie:
                        wordEndIndex = categorie.index("task_categories") + len("task_categories")
                        cat = categorie[wordEndIndex + 1:]
                        categories.append(cat)
                categorie_data[line[0]] = categories
            except:
                print(line[0])

    with open("dataset_calls.csv", "r") as f:
        delimiter = ', '
        reader = csv.reader(f, delimiter="\t")
        for line in reader:
            subset = None if line[5] == 'None' else line[5]
            categories = categorie_data[line[0]]

            if subset is not None:
                name = line[0] + "_" + subset
                name = name.replace("/", "_")
            else:
                name = line[0]
                name = name.replace("/", "_")
            name = name.replace("-", "_")
            name = name.replace(".", "_")
            params = (name, line[6],line[-1].lower().strip(), delimiter.join(categories))
            cur.execute("INSERT INTO Metadata VALUES (?,?,?,?)", params)

    con.commit()



def create_matrix():

    con = sqlite3.connect("Studienprojekt.db")
    cur = con.cursor()
    res = cur.execute("SELECT Name FROM Metadata")
    names = res.fetchall()
    size = len(names)
    Name_list = list(itertools.chain(*names))
    data_dict = {}
    data_stats = {}
    for name in Name_list:
        res_data = cur.execute("SELECT * FROM " + name)
        data_dict[name] = res_data.fetchall()
        res_stats = cur.execute("SELECT * FROM Statistics WHERE Name='"+name+"'")
        data_stats[name] = res_stats.fetchall()
    array_complete = pd.DataFrame({'name': Name_list})
    cnt = 0
    for name in Name_list:
        print(cnt)
        cnt += 1
        tmp = [0 for i in range(size)]
        for datapoint in data_dict[name]:
            if datapoint[0] in Name_list:
                idx = array_complete.index[array_complete['name'] == datapoint[0]].tolist()[0]
                tmp[idx] = datapoint[1]
        array_complete[name] = tmp
    array_complete.to_sql(name="array_complete", con = con)


