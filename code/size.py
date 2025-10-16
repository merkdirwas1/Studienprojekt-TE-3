import sqlite3
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def get_size_group(size):
    # return size group of given size
    if size > 7500:
        return "max"
    elif size > 5000:
        return "large"
    elif size > 2500:
        return "small"
    else:
        return "tiny"

def size_gesamt(con):
    # shows how many tasks are in the size classes

    cursor = con.cursor()
    cursor.execute("SELECT size FROM Metadata")
    size_data = cursor.fetchall()
    cursor.execute(" SELECT COUNT(size) FROM Metadata WHERE cast(size as decimal)>7500;")
    res_max = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(size) FROM Metadata WHERE cast(size as decimal)>5000 AND cast(size as decimal)<=7500;")
    res_large = cursor.fetchall()[0][0]
    cursor.execute( "SELECT COUNT(size) FROM Metadata WHERE cast(size as decimal)<=5000 AND cast(size as decimal)>2500;")
    res_small = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(size) FROM Metadata WHERE cast(size as decimal)<=2500;")
    res_tiny = cursor.fetchall()[0][0]

    result_dict_size = {}
    result_dict_size["max"] = res_max
    result_dict_size["large"] = res_large
    result_dict_size["small"] = res_small
    result_dict_size["tiny"] = res_tiny

    return result_dict_size


def werte_verteilung_size(con, filter= True):
    # creates an figure with 4x4 sub plots. each plot shows an size group pair with left is intermediate and bottom is target
    # 
    cursor = con.cursor()
    cursor.execute("SELECT Name, size FROM Metadata")
    res = cursor.fetchall()

    result_dict_size = {}
    result_dict_size["max"] = []
    result_dict_size["large"] = []
    result_dict_size["small"] = []
    result_dict_size["tiny"] = []

    for name, size in res:
        size_group = get_size_group(int(size))
        result_dict_size[size_group].append(name)


    result_dict_values = {}
    result_dict_values["max"] = {}
    result_dict_values["large"] = {}
    result_dict_values["small"] = {}
    result_dict_values["tiny"] = {}


    for size_class in result_dict_size:
        result_dict_values[size_class]["max-" + size_class] = []
        result_dict_values[size_class]["large-" + size_class] = []
        result_dict_values[size_class]["small-" + size_class] = []
        result_dict_values[size_class]["tiny-" + size_class] = []



        for name in result_dict_size[size_class]:
            # tiny

            cursor.execute("SELECT score FROM " + name + " WHERE cast(size as decimal)<=2500;")
            res = cursor.fetchall()
            for datapoint in res:
                result_dict_values[size_class]["tiny-" + size_class].append(float(datapoint[0]))

            #small
            cursor.execute("SELECT score FROM " + name + " WHERE cast(size as decimal)<=5000 AND cast(size as decimal)>2500;")
            res = cursor.fetchall()
            for datapoint in res:
                result_dict_values[size_class]["small-" + size_class].append(float(datapoint[0]))

            #large
            cursor.execute("SELECT score FROM " + name + " WHERE cast(size as decimal)>5000 AND cast(size as decimal)<=7500;")
            res = cursor.fetchall()
            for datapoint in res:
                result_dict_values[size_class]["large-" + size_class].append(float(datapoint[0]))

            # max
            cursor.execute("SELECT score FROM " + name + " WHERE cast(size as decimal)>7500;")
            res = cursor.fetchall()
            for datapoint in res:
                result_dict_values[size_class]["max-" + size_class].append(float(datapoint[0]))

    fig = make_subplots(rows=4, cols=4, start_cell="bottom-left")

    i,j= 1,1
    for target_size in result_dict_values:
        i = 1
        for intermediate_size in result_dict_values[target_size]:
            fig.add_trace(go.Histogram(
                x=result_dict_values[target_size][intermediate_size],
                histnorm='percent',
                name=intermediate_size,  # name used in legend and hover labels
                xaxis="x1",
                opacity=0.75,
                showlegend=True

            ),row=i, col=j)
            fig.update_xaxes(title_text=intermediate_size, row=i, col=j)
            i +=1
        j +=1


    fig.update_layout(
        title_text='LogMe Verteilung in Prozenten',  # title of plot
        yaxis_title_text='Anteil in %',  # yaxis label
        bargap=0.2,  # gap between bars of adjacent location coordinates
        bargroupgap=0.1,# gap between bars of the same location coordinates
        showlegend= False
    )

    fig.show()