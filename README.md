# Studienprojekt-TE-3

## Table of Contents
1. [Methods](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#methods)
2. [Which impact has the Task size on the LogMe Score](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-impact-has-the-task-size-on-the-logme-score)
3. [Which Tasks are often in the Top k intermediate Tasks?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-tasks-are-often-in-the-top-k-intermediate-tasks)
4. [How symmetrical in order of top-k symmetrie are the Groups?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#top-k-symetrie)
5. [How symmetrical in order of distance symmetrie are the groups?](https://github.com/merkdirwas1/Studienprojekt-TE-3?tab=readme-ov-file#how-symmetrical-in-order-of-distance-symmetrie-are-the-groups)


## Methods

**Definition class:**<br>
A class is defined by a specific feature of the Tasks as, language, Size, Task Domain. If Tasks are sharing a feature they are part of the same group. 

**Definition Size groups:**<br>
To investigate the impact of the size on the LogMe Score I defined 4 groups of sizes. 

| **Name** | **Datapoint Range**    | **Size**  |
|----------|------------------------|-----------|
| Max      | 7.5k to 10k Datapoints | 562 Tasks |
| large    | 5k to 7.5k Datapoints  | 101 Tasks |
| small    | 2.5 to 5k Datapoints   | 134 Tasks |
| Tiny     | up to 2.5k Datapoints  | 575 Tasks |

To investigate the impact of Task to each other I defined two kinds of symmetrie. The first one is top-k symmetrie an the second one is distance symmetrie.

**Definition top-k symmetrie:**<br>
If Task A is a top-k intermediate Task of Task B and if Task B is a top-k intermediate Task of Taks A, then the both are symmetrical.

**Definition distance symmetrie:**<br>
If the distance of the LogMe score of Task A and Taks B is lower or equal of 0.1 then the Task A and B are strong symmetrical. If this distance is smaller or equal then 0.5 they are weak symmetrical.

## Which impact has the Task size on the LogMe Score
To anwser this question I looked into the plots of LogMe scores in the different size groups to investigate if there are indicators of how the size affect the Score.
![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/newplot(8).png)


The Figure Shows the Range of the LogMe scores where a Task of one size group is the intermediate task and a Task of an other group is the target Task. It shows that there are only small differences if the intermediate Task group is changed. Only if the Target Task is another group the range is changing. It also shows that the most values are under 0 and it shifts to left if the target Task get smaller. It also shows that if the Target task is an tiny one the range of the LogMe scores goes up to 1300+.

To investigate even further I want to look at the spread of the LogMe score. The spread is defined as the max-min LogMe scores for each Target Task. To investigate of the size of the Target Task have an impact to the Scores I Plot this in correlation with the size of a task.
![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/spread-gr%C3%B6%C3%9Fe.png)

It shows that the plot converges at 0 and if the size is getting smaller the range of  possible logMe scores is getting larger. So larger tasks have a smaller spread than smaller ones.  This Figure is filtered because some of the Tasks produces LogMe scores over 100 so they compress so it is bad to read. 

So it looks like the Size have an Impact on the LogMe Score. It defines how the spread is and how the range of LogMe scores will be. 

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


## How symmetrical in order of top-k symmetrie are the Groups?
I want to investigate if this method is symmetrical and if are the groups of the different classes more likely symmetrical? For the size groups I ploted the percentage of symetrical pairs for increasing top-k. For the other two classes there are only tables because they have too much group with to less Tasks per group to plot each of them. 

![generel](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/topksimgeneral.png)
# TODO: auswertung

### Size 
max-Size-group
![Size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/size.png)


The plots shows that the max and the large group have a high top-k symmetrie for low top-k and it drops fast for increasing k. The small and tiny group have a low symmetrie. The Groups here are only for the Target Task so the top k can be from other groups. It shows only that the choice of the target Task change how symmetrical the methode is. Becouse the sum of the percentage of the top 1 pairs is near 100 further work would investigate which pairs that are and why they behave like that.

# TODO: auswertung generel einfügen

### Language 
![max-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/language.png)
### Categorie 
![max-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/categories.png)


## How symmetrical in order of distance symmetrie are the groups?

In order to answer this question I first calculated the ratio of strong and weak pairs. For the strong pairs the ratio is 8.6% over all Tasks and for the weak pairs it is 18.8% over all Tasks. So in general this method isn't symmetrical in order of definition. Next I wanted to know if the classes shows a higher ratio, which could mean that the classes have an impact on how good two task suit each other. I dont calculate if (A,A) pairs are symmetrical.

### How symmetrical are the sizes?
For the size groups I calculated a table for the strong and the weak pairs. it shows the ratio of the symmetrical pairs, with the column stands for that the intermedate Task is in this group size and the row stands for the target task size group. 

**strong pair ratio:**
|           | **max** | **large** | **small** | **tiny** |
|-----------|---------|-----------|-----------|----------|
| **max**   |   10,02 |           |           |          |
| **large** |    6,48 |      5,07 |           |          |
| **small** |     7,2 |      4,96 |      6,48 |          |
| **tiny**  |    9,35 |      6,65 |      6,66 |     9,27 |

It shows that max-max; max-tiny and tiny-tiny have slightly higher symmetrical pairs bit it is also unlikely that 2 Task in this group are symmetrical. Max-tiny and tiny-tiny are still near to the overall ratio so it could be random that they have this score.


**weak pair ratio:**
|           | **max** | **large** | **small** | **tiny** |
|-----------|---------|-----------|-----------|----------|
| **max**   |   20,58 |           |           |          |
| **large** |   13,58 |       8,5 |           |          |
| **small** |   18,77 |     12,61 |     17,42 |          |
| **tiny**  |   20,17 |     12,71 |     18,45 |    19,69 |

for the weak pairs it is the same like for the strong pairs. 


### How symmetrical are languages?
The results of my calculation for the languages can be found in the table below. It also shows how large each language group is.
| **Name**   | **group size** | **strong ratio** | **weak ratio** |
|------------|----------------|------------------|----------------|
| english    |            719 |             4,57 |          14,15 |
| russian    |             33 |             8,33 |          10,04 |
| greek      |              7 |             9,52 |           4,76 |
| polish     |             25 |             9,67 |             29 |
| german     |             17 |            10,29 |          40,44 |
| tamil      |              9 |            11,11 |          30,56 |
| french     |             33 |            11,74 |          18,56 |
| none       |             12 |            12,12 |           19,7 |
| turkish    |             11 |            12,73 |          34,55 |
| swedish    |             33 |            12,88 |          10,61 |
| romanian   |              6 |            13,33 |             40 |
| portuguese |             26 |            14,15 |          23,69 |
| indonesian |              7 |            14,29 |          33,33 |
| malayalam  |              7 |            14,29 |          19,05 |
| spanish    |             18 |            14,38 |          40,52 |
| slovanian  |              9 |            16,67 |          27,78 |
| japanese   |             25 |            17,67 |          41,33 |
| marathi    |              6 |               20 |              0 |
| tagalog    |              6 |               20 |          46,67 |
| urdu       |              6 |               20 |          33,33 |
| chinese    |             34 |            21,39 |          23,53 |
| hindi      |             13 |            23,08 |          16,67 |
| danish     |             20 |            24,21 |          23,16 |
| arabic     |             15 |            24,76 |          45,71 |
| bengali    |              8 |               25 |          32,14 |
| gujarati   |              7 |            28,57 |          19,05 |
| italian    |              7 |            28,57 |           4,76 |
| telegu     |              7 |            28,57 |           4,76 |
| norwegian  |             18 |            30,07 |           7,84 |
| kannada    |              7 |            33,33 |          14,29 |
| bulgarian  |              6 |               40 |          33,33 |
| korean     |             23 |            40,71 |          15,81 |

The table shows that there are many groups which higher strong symmetrie and higher weak simmetrie, which shows that languages have a slightly impact on how the LogMe score behave. Though the most of the language Groups have a small size so it lacks of evidence that this is a general behavior. 

### How symmetrical are categories?
The results of my calculation for the categories can be found in the table below. It also shows how large each categorie group is.
| **Name**                       | **group size** | **strong ratio** | **weak ratio** |
|--------------------------------|----------------|------------------|----------------|
| text-generation                |            174 |             0,75 |           2,37 |
| question-answering             |            294 |             1,42 |           2,55 |
| other                          |              9 |             2,78 |          11,11 |
| text2text-generation           |             48 |             2,93 |           7,36 |
| fill-mask                      |             26 |             4,31 |          19,69 |
| zero-shot-classification       |             37 |             5,71 |          10,96 |
| multiple-choice                |            146 |             6,13 |            8,9 |
| token-classification           |            138 |             7,45 |          15,37 |
| sentence-similarity            |             37 |             8,41 |          27,48 |
| summarization                  |            133 |            12,12 |          25,55 |
| translation                    |              8 |            17,86 |          17,86 |
| feature-extraction             |            104 |            18,28 |          33,08 |
| image-classification           |             94 |            19,01 |          30,04 |
| image-to-text                  |             94 |            19,01 |          30,04 |
| image-segmentation             |             93 |            19,28 |          29,43 |
| image-to-image                 |             93 |            19,28 |          29,43 |
| object-detection               |             93 |            19,28 |          29,43 |
| zero-shot-image-classification |             93 |            19,28 |          29,43 |
| text-retrieval                 |             15 |            26,67 |           18,1 |
| table-question-answering       |              9 |            30,56 |          47,22 |

Other than the language groups the categorie groups have a size large enough to give more evidence. The table shows that half of the categories have an higher strong and weak ratio than the overall set. Which means that the categories have an larger impact on the behavior of the LogMe score than language. This method is stil not symmetrical in order of my definition.

