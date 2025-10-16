import sqlite3
import plotly.graph_objects as go
import networkx as nx
import pandas as pd
import numpy as np
from size import *
import copy

import plotly.express as px

def top_k_sim(con, k,topkdict):
    cur = con.cursor()

    # for name_b in name_a look if name_a in name_b
    for name in topkdict:
        cur.execute("SELECT Name FROM " + name)
        res = cur.fetchmany(k)
        for names in res:
            topkdict[name].append(names[0])
    names = topkdict.keys()
    cnt = 0
    for name_a in topkdict:
        for name_b in topkdict[name_a]:
            cur.execute("SELECT Name FROM " + name_b)
            res = cur.fetchmany(k)
            for names in res:
                if name_a == names[0]:
                    cnt += 1
    return cnt/(len(topkdict)*k)

con = sqlite3.connect("Studienprojekt.db")

def create_fig_topk(con, dclass):
    cursor = con.cursor()
    res = cursor.execute("SELECT categorie FROM Metadata")
    data = res.fetchall()
    categorie_array = []

    for touple in data:
        for categories in touple:
            categories = categories.replace(" ", "").split(",")
            for categorie in categories:
                if categorie not in categorie_array:
                    categorie_array.append(categorie)

    queries = {}
    results = {}
    for categorie in categorie_array:
        queries[categorie] = "SELECT Name FROM Metadata  WHERE "+dclass+" LIKE '%" + categorie + "%';"
        results[categorie] = []

    for query in queries:

        cursor.execute(queries[query])
        res = cursor.fetchall()
        topkdict = {}
        for name in res:
            topkdict[name[0]] = []


        for k in range(1,100):
            print(k)
            topkdictcopy = copy.deepcopy(topkdict)
            i = top_k_sim(con, k,topkdictcopy)
            results[query].append(i)


    df = pd.DataFrame.from_dict(results)
    fig = px.line(df)
    fig.update_layout(xaxis_title="top k", yaxis_title="Anteil in %",title="Anteil Symmetrischer Paare in %")
    fig.show()


def create_fig_size(con):
    cursor = con.cursor()

    queries = {
        "max": "SELECT Name FROM Metadata  WHERE cast(size as decimal)==10000;",
        "large": "SELECT Name FROM Metadata  WHERE cast(size as decimal)>5000 AND cast(size as decimal)<10000;",
        "small": "SELECT Name FROM Metadata  WHERE cast(size as decimal)<=5000 AND cast(size as decimal)>1000;",
        "tiny": "SELECT Name FROM Metadata  WHERE cast(size as decimal)<=1000;"
    }
    results = {
        "max": [],
        "large": [],
        "small": [],
        "tiny": []
    }
    for query in queries:

        cursor.execute(queries[query])
        res = cursor.fetchall()
        topkdict = {}
        for name in res:
            topkdict[name[0]] = []

        for k in range(1, 100):
            print(k)
            topkdictcopy = copy.deepcopy(topkdict)
            i = top_k_sim(con, k, topkdictcopy)
            results[query].append(i)

    df = pd.DataFrame.from_dict(results)
    fig = px.line(df)
    fig.update_layout(xaxis_title="top k", yaxis_title="Anteil in %", title="Anteil Symmetrischer Paare in %")
    fig.show()

def top_k_all_data(con,k=50,threshold= 300):
    # shows the top k Intermediate Tasks over all Task
    # threshold: filters all Task with lower occurrence then the threshold
    cursor = con.cursor()
    result_dict_size = {}
    result_dict_size["max"] = 0
    result_dict_size["large"] = 0
    result_dict_size["small"] = 0
    result_dict_size["tiny"] = 0

    tmp_dict = {}

    cursor.execute("SELECT Name FROM Metadata")
    names = cursor.fetchall()

    # select all top k
    for name in names:
        cursor.execute("SELECT Name FROM " + name[0])
        res_data = cursor.fetchall()
        for cnt in range(0, k):
            if res_data[cnt][0] not in tmp_dict:
                tmp_dict[res_data[cnt][0]] = 1
            else:
                tmp_dict[res_data[cnt][0]] += 1

    # sort
    tmp_dict = {k: v for k, v in sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True)}

    # filter
    topk = {}
    for name in tmp_dict:
        if tmp_dict[name] >= threshold:
            topk[name] = tmp_dict[name]

    # generate plot
    data = pd.DataFrame(topk, index=[1])
    data= data.transpose()
    fig = px.bar(data)
    fig.update_layout(
        title_text='Top k Intermediate Tasks over all Tasks',  # title of plot
        yaxis_title_text='occurrence',  # yaxis label
        showlegend= False
    )
    fig.show()

    # investigate the dataset sizes of the top k
    for name in topk:
        cursor.execute("SELECT size FROM Metadata WHERE Name='" + name + "'")
        res_data = cursor.fetchall()

        size_group = get_size_group(int(res_data[0][0]))
        result_dict_size[size_group] += 1

    # investiage the domains
    result_dict_categorie = {}
    for name in topk:
        cursor.execute("SELECT categorie FROM Metadata WHERE Name='" + name + "'")
        res_data = cursor.fetchall()
        categories = res_data[0][0].replace(" ", "").split(",")
        for categorie in categories:
            if categorie not in result_dict_categorie:
                result_dict_categorie[categorie] = 1
            else:
                result_dict_categorie[categorie] += 1


    # investigate the languanges
    result_dict_language = {}
    for name in topk:
        cursor.execute("SELECT language FROM Metadata WHERE Name='" + name + "'")
        res_data = cursor.fetchall()
        languages = res_data[0][0].replace(" ", "").split(",")
        for language in languages:
            if language not in result_dict_language:
                result_dict_language[language] = 1
            else:
                result_dict_language[language] += 1


    #return result_dict_size, result_dict_categorie, result_dict_language
    return result_dict_language


def top_k(cursor,data_dict,group, k=50):
    # calculate the top 50 symmetrie in a given group
    result_dict_size = {}
    result_dict_size["max"] = 0
    result_dict_size["large"] = 0
    result_dict_size["small"] = 0
    result_dict_size["tiny"] = 0


    result_dict = {}
    for datapoint in data_dict:
        for cnt in range(0, k):
            group_data = data_dict[datapoint][cnt][2]
            #print(group_data)
            if group in group_data:
                group_data = group

                res = cursor.execute("SELECT size FROM Metadata WHERE Name='" + data_dict[datapoint][cnt][0] + "'")
                size_data = res.fetchone()
                size_group = get_size_group(int(size_data[0]))
                result_dict_size[size_group] += 1


            if group_data not in result_dict:
                result_dict[group_data] = 1
            else:
                result_dict[group_data] += 1
    try:
        amount = result_dict[group]
    except:
        amount = 0
    total = sum(value for value in result_dict.values())
    return amount/total, result_dict_size

