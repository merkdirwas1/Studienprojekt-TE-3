# Studienprojekt-TE-3

## Table of Contents
1. [Example](##Which impact has the Task size on the LogMe Score)
2. [Example2](#example2)
3. [Third Example](#third-example)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)


A class is defined by a specific feature of the Tasks as, language, Size, Task Domain. If Tasks are sharing a feature they are part of the same group. 

**Definition: Size classes**
To investigate the impact of the size on the LogMe Score I defined 4 groups of sizes. 

| **Name** | **Datapoint Range**    | **Size**  |
|----------|------------------------|-----------|
| Max      | 7.5k to 10k Datapoints | 562 Tasks |
| large    | 5k to 7.5k Datapoints  | 101 Tasks |
| small    | 2.5 to 5k Datapoints   | 134 Tasks |
| Tiny     | up to 2.5k Datapoints  | 575 Tasks |

# TODO: simmetrie erklären
# todo: top k symmetrie erklären 







## Which impact has the Task size on the LogMe Score
TODO: what did you do to answer the question
![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/newplot(8).png)


The Figure Shows the Range of the LogMe scores where a Task of one size group is the intermediate task and a Task of an other group is the target Task. It shows that there are only small differences if the intermediate Task group is changed and only if the Target Task is another group the range is changing. It also shows that the most values are under 0 and it shifts to left if the target Task get smaller. It also shows that if the Target task is an tiny one the range of the LogMe scores goes up to 1300+.

TODO: what did you do to answer the question


![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/spread-gr%C3%B6%C3%9Fe.png)

This Figure shows the spread of the LogME score in correlation with the size of a task. It shows that the plot converges at 0 and if the size is getting smaller the range of  possible logMe scores is getting larger. So larger tasks have a smaller spread than smaller ones.  This Figure is filtered because some of the Tasks produces LogMe scores over 100 so they compress so it is bad to read. 

## Which Tasks are often in the Top k intermediate Tasks?
I want to investigate the top k intermediate tasks over all task to examine if there are specific tasks that occur more often then other. For better plots I only show Task which occur more then 300 times in the top k.

### Top 10 top-k

![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%2010.png)

As the Fig. shows there are a few tasks which appear often in the Top 10 intermediate Tasks. There are 2 Tasks that occur more then 500 times which means that over 36% of all target task it could be a good intermediate task.

All of the 6 Tasks are in the max size class.
If we look into the Task categories we see that the most intermediate datasets come from the text-classification categorie  and there are just two other categories 

| **text-classification** | **multiple-choice** | **token-classification** |
|-------------------------|---------------------|--------------------------|
| 6                       | 2                   | 1                        |

With a look into the languages we see that 4 of the datasets are in english. One is in chinese and one in gujarati.
### Top 25 top-k

![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%2025.png)
In the top 25 the trend continues and many more intermediate task occur often in the top 25 of all inter tasks. 
The distribution of the sizes can be seen in the table: 
| **text-classification** | **multiple-choice** | **token-classification** |
|-------------------------|---------------------|--------------------------|
| 6                       | 2                   | 1                        |

Like in the top 10 the most Tasks are in the text-classification categorie or in multiple-choice or in token classification.
| **text-classification** | **multiple-choice** | **token-classification** | **question-answering** | **zero-shot-classification** | **text-generation** | **translation** |
|-------------------------|---------------------|--------------------------|------------------------|------------------------------|---------------------|-----------------|
| 16                      | 5                   | 4                        | 2                      | 1                            | 1                   | 1               |

In the languages 9 Tasks are in english and the rest are singleton in one language. 

### Top 50 top-k
![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%2050.png)

In the top 50 the trend continues again and it shows that there are a few dataset that occur very often in the top 50. the first 2 top 50 Tasks occur over 50%.
The distribution of the sizes can be seen in the table: 

| **max** | **large** | **small** | **tiny** |
|---------|-----------|-----------|----------|
| 27      | 2         | 2         | 3        |

The trend of the 10 and 25 top k continues in the top 50 and the most tasks are text-classification follow up by multiple-choise and token classification.

| text-classification | multiple-choice | token-classification | question-answering | text2text-generation | text-generation | translation | zero-shot-classification | text-retrieval | fill-mask |
|---------------------|-----------------|----------------------|--------------------|----------------------|-----------------|-------------|--------------------------|----------------|-----------|
| 34                  | 9               | 7                    | 4                  | 3                    | 2               | 1           | 1                        | 1              | 1         |

In the languages it is the same and 21 of the Tasks are in english while the other languages are only once or twice. 

### Top 100 top-k

![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%20100.png)


In the top 100 it shows that the dataset claritylab_utcd_out-of-domain is in the top 100 of over 0.69% of all target Tasks. All four plots shows that the top k intermediate tasks are only a few tasks that could be good intermediate tasks. This could be a characteristic of this intermediate task or a weakness of the LogMe-ESM method.

The distribution of the sizes can be seen in the table: 

| **max** | **large** | **small** | **tiny** |
|---------|-----------|-----------|----------|
| 44      | 3         | 10        | 32       |

It shows that it is more likely that the best intermediate task is a max set because the percentage share of the max Tasks is larger than the percentage share of max Tasks over all tasks.

If we look into the categories of the top 100 then it shows that the best Tasks are in multiple-choice, token-classification and question-answering. That the amount of text-classification Tasks is so high is because the most tasks are in text-classification too. 

| **text-classification** | **multiple-choice** | **token-classification** | **question-answering** | **text2text-generation** | **text-retrieval** | **zero-shot-classification** | **text-generation** | **translation** | **fill-mask** | **sentence-similarity** | **None** |
|-------------------------|---------------------|--------------------------|------------------------|--------------------------|--------------------|------------------------------|---------------------|-----------------|---------------|-------------------------|----------|
| 87                      | 16                  | 20                       | 17                     | 6                        | 5                  | 4                            | 4                   | 2               | 1             | 1                       | 1        |

## top k symetrie

### max-Size-Class
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/max%2020.png)
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/max%20100.png)
### large-Size-Class
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/large%2020.png)
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Large%20100.png)
### small-Size-Class
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/small%2020.png)
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/small%20100.png)
### tiny-Size-Class
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/tiny%2020.png)
![size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/tiny%20100.png)
