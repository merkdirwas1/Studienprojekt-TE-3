import itertools
import networkx as nx
import csv

import numpy

from relationen import *
from size import *
import numpy as np
import pandas as pd
from warnings import simplefilter
import plotly.express as px
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)



def in_class_dist_sim(con, identifikator="language",group="korean", min_group_size = 15, filter=0):
    cursor = con.cursor()
    res = cursor.execute("SELECT Name FROM Metadata WHERE " + identifikator + " LIKE '%" + group + "%' AND cast(size as decimal)>=" + str(filter) + ";")
    names = res.fetchall()
    group_size = len(names)
    if group_size >= min_group_size:
        Name_list = list(itertools.chain(*names))
        data_dict = {}
        data_stats = {}
        for name in Name_list:
            res_data = cursor.execute("SELECT * FROM " + name)
            data_dict[name] = res_data.fetchall()
            res_stats = cursor.execute("SELECT * FROM Statistics WHERE Name='"+name+"'")
            data_stats[name] = res_stats.fetchall()

        prozent, _ = top_k(con,data_dict,group,group_size)

    return prozent


def werte_verteilung(con, filter= True):
    # shows distribution of LogME values over all Tasks
    dataframe = pd.read_sql('SELECT * FROM array_complete', con)
    del dataframe["index"]
    del dataframe["name"]

    data = dataframe.values.reshape(-1,).tolist()
    data = [float(x) for x in data]
    if filter == True:
        data = [x for x in data if x <= 20 and x >= -20]
    data.sort()
    fig = px.histogram(data)
    fig.show()

def tabelle(con, identifikator="language",group_size_filter = 15, dataset_size_filter=100, func="max"):
    # calculates tables with left is intermediate and top is target task
    # for all Tasks of an class and a given function who decide which LogMe score is chosen
    # func = min, max, mean
    cursor = con.cursor()
    res = cursor.execute(
        "SELECT " + identifikator + " FROM Metadata WHERE cast(size as decimal)>=" + str(dataset_size_filter) + ";")
    data = res.fetchall()
    klassen = {}

    for data_tuple in data:
        for classes in data_tuple:
            if identifikator == "categorie":
                classes = classes.replace(" ", "").split(",")
            else:
                classes = classes.split(",")
            for klasse in classes:
                klassen[klasse] = []
    del_klassen = []
    for klasse in klassen:
        res = cursor.execute(
            "SELECT Name FROM Metadata WHERE " + identifikator + " LIKE '%" + klasse + "%' AND cast(size as decimal)>=" + str(
                dataset_size_filter) + ";")

        data = res.fetchall()
        group_size = len(data)

        if group_size >= group_size_filter:
            for dataset in data:
                klassen[klasse].append(dataset[0])
        else:
            del_klassen.append(klasse)

    for klasse in del_klassen:
        del klassen[klasse]

    klassen_list = list(klassen.keys())
    tabelle_gesammt = pd.DataFrame({'name': klassen_list})
    klassen_anzahl = len(klassen_list)
    for klassen_name in klassen_list:
        tmp = [None for _ in range(klassen_anzahl)]
        tabelle_gesammt[klassen_name] = tmp
        tabelle_gesammt = tabelle_gesammt.copy()

    for i in range(0, klassen_anzahl):
        target_klass = tabelle_gesammt["name"][i]
        target = klassen[target_klass]
        for j in range(1, klassen_anzahl + 1):
            intermediate_klass = tabelle_gesammt.columns[j]

            data = []

            for dataset in target:
                res = cursor.execute(
                    "SELECT score FROM " + dataset + " WHERE " + identifikator + " LIKE '%" + intermediate_klass + "%'")
                res_data = res.fetchall()
                if res_data:
                    data.append(res_data[0])
            data_tmp = []
            for data_tuple in data:
                data_tmp.append(float(data_tuple[0]))

            arr = np.array(data_tmp)

            if func == "max":
                tabelle_gesammt.loc[i, intermediate_klass] = arr.max()
            if func == "mean":
                tabelle_gesammt.loc[i, intermediate_klass] = arr.mean()
            if func == "min":
                tabelle_gesammt.loc[i, intermediate_klass] = arr.min()
    return tabelle_gesammt

def create_graph(tabelle_gesammt):
    del tabelle_gesammt["text-classification"]
    tabelle_gesammt = tabelle_gesammt.drop(0)

    G = nx.Graph()
    names = []
    for name in tabelle_gesammt['name']:
        G.add_node(name)
        names.append(name)


    weight = np.zeros((len(tabelle_gesammt['name']), len(tabelle_gesammt['name'])))
    cut_off = int(len(tabelle_gesammt['name']) * 0.3)
    del tabelle_gesammt["name"]
    arr = tabelle_gesammt.to_numpy()
    for iter in range(0, len(arr)):
        for cnt in range(iter+1, len(arr)):
            weight[iter, cnt] = arr[iter, cnt]
            weight[cnt, iter] = arr[cnt,iter]
            G.add_edge(names[iter], names[cnt], weight=float(weight[iter, cnt]))


    for i in range(cut_off):
        min_weight_edge = []
        for u in G.nodes():
            try:
                min_weight_edge.append(min(G.edges(u), key=lambda x: G.get_edge_data(x[0], x[1])["weight"]))
            except:
                continue



        for u,v in min_weight_edge:
            try:
                G.remove_edge(u,v)
            except:
                continue


    #pos=nx.spring_layout(G, threshold=0.00001,scale=2, weight="weight")
    pos=nx.forceatlas2_layout(G, weight="weight")
    nx.draw(G,pos)

    node_x = []
    node_y = []
    cnt = 0
    for node in pos:
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        cnt += 1


    fig = go.Figure()

    # Add edges to the figure
    for u, v, data in G.edges(data=True):
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='rgb(210,210,210)', width=1),))

    # Add nodes to the figure
    for node in G.nodes():
        x, y = pos[node]
        if not node:
            node = "None"
        fig.add_trace(go.Scatter(x=[x], y=[y],mode="markers+text", marker=dict(size=10),text=node,))
    # Show the figure
    fig.update_traces(textfont_size=10,textposition="top center")

    fig.show()
