import sqlite3
import pandas as pd
def symmetrie(dataframe, group_size):
    # calculate the symmetrie of pairs in order of distance in a given group
    arr = dataframe.to_numpy()
    cnt = 0
    schwach = 0
    nicht = 0
    stark = 0
    pairs = {}
    pairs["stark"] =  []
    pairs["schwach"] = []

    for j in range(group_size):
        for i in range(1+j,group_size):
            a = float(arr[j][i])
            b = float(arr[i][j])
            result = abs(a-b)
            cnt += 1
            # result abs(a-b) / (a*a + b*b)
            if result<= 0.1:
                stark += 1
                pairs["stark"].append((j,i))
            elif result<= 0.5:
                schwach += 1
                pairs["schwach"].append((j, i))
            else:
                nicht += 1


    return (stark, schwach, nicht, cnt, pairs)


def overall_sym(con):
    # calculate the symmetrie in order of distance over all sets
    dataframe = pd.read_sql('SELECT * FROM array_complete', con)
    del dataframe["index"]
    del dataframe["name"]
    werte = symmetrie(dataframe, 1372)
    return werte
