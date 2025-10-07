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

There are only a few pairs of symmetrical pairs in the overall set and it drops new 0 if the k is increasing. These makes sense because of there are a few intermedate Tasks that appears in the most top k but these sets can only have a few top k itself so there are only a few pairs left for this kind of symmetrie. It can be sayed that the ESM-LogMe method is not symmetrical for this definition.  

### Size 
max-Size-group
![Size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/size.png)


The plots shows that the max and the large group have a high top-k symmetrie for low top-k and it drops fast for increasing k. The small and tiny group have a low symmetrie. The Groups here are only for the Target Task so the top k can be from other groups. It shows only that the choice of the target Task change how symmetrical the methode is. Becouse the sum of the percentage of the top 1 pairs is near 100 further work would investigate which pairs that are and why they behave like that. Which is intestering is that the the large group starts with a persentage that is higher than the the persentage of the overall set.

### Language 
![max-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/language.png)

The language groups have a interesting behavior because most of the languages starts at a low percentage and increase them over small k increases. Most of the languages gain a percentage that is higher than in the overall set or in the size groups. This could be an evidence that the language of the target task has an impact on how the sets are bound to each other. The language macedonian has in interessting pattern because after they drop in ther percentage they gain a recover over the 60%.


### Categorie 
![max-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/categories.png)

The categories shows the same behavior like the groups. Some of them starting with a percentage around 50-60% but they drop fast at increasing k and most of the categories dont recover ofer 20% which is slighty abouve the overall set but near them. 

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
# todo
|    | **name**                           | **text-classification** | **text2text-generation** | **translation**    | **text-generation** | **token-classification** | **multiple-choice** | **question-answering** | **table-question-answering** | **zero-shot-classification** | **summarization**  | **feature-extraction** | **text-retrieval** | **fill-mask**      | **sentence-similarity** | **image-classification** | **image-segmentation** | **image-to-image** | **image-to-text**  | **object-detection** | **zero-shot-image-classification** | **other**          | **None**           |
|----|------------------------------------|-------------------------|--------------------------|--------------------|---------------------|--------------------------|---------------------|------------------------|------------------------------|------------------------------|--------------------|------------------------|--------------------|--------------------|-------------------------|--------------------------|------------------------|--------------------|--------------------|----------------------|------------------------------------|--------------------|--------------------|
| 0  | **text-classification**            | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |
| 1  | **text2text-generation**           | 17.5893384254499        | 16.771912747480478       | 14.969783667153944 | 16.771912747480478  | 16.771912747480478       | 15.953190026199508  | 16.771912747480478     | 16.771912747480478           | 16.771912747480478           | 16.821412981253882 | 16.821412981253882     | 14.040844689194566 | 16.691512295021006 | 15.552007006489685      | 16.821412981253882       | 16.821412981253882     | 16.821412981253882 | 16.821412981253882 | 16.821412981253882   | 16.821412981253882                 | 14.775850097935201 | 17.5893384254499   |
| 2  | **translation**                    | 2.6663417326031085      | 2.6660883537822135       | 2.6659382572982264 | 2.6660883537822135  | 2.6660522800272695       | 2.666130931542699   | 2.6661039509015945     | 2.665547089617256            | 2.666055769123703            | 2.6658822194833967 | 2.6659003205357505     | 2.6659723248109293 | 2.6658923506023484 | 2.665931236483393       | 2.6659003205357505       | 2.6658679392849227     | 2.6658679392849227 | 2.6659003205357505 | 2.6658679392849227   | 2.6658679392849227                 | 2.66588605034165   | 2.6663417326031085 |
| 3  | **text-generation**                | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |
| 4  | **token-classification**           | 155.56826129780893      | 153.98529399645264       | 146.0832544602141  | 153.98529399645264  | 153.98529399645264       | 150.88463676137474  | 153.98529399645264     | 153.98529399645264           | 153.98529399645264           | 155.56826129780893 | 155.56826129780893     | 152.3200401723516  | 152.09037504570395 | 153.88250286434817      | 155.56826129780893       | 155.56826129780893     | 155.56826129780893 | 155.56826129780893 | 155.56826129780893   | 155.56826129780893                 | 151.71709906480004 | 155.56826129780893 |
| 5  | **multiple-choice**                | 82.14736598995016       | 81.69991120661031        | 77.78857592847622  | 81.69991120661031   | 81.69991120661031        | 80.01919609625796   | 81.69991120661031      | 81.69991120661031            | 81.8107939103744             | 81.69991120661031  | 81.69991120661031      | 78.1276625453205   | 79.26274698979653  | 80.47224712350973       | 80.54187980869656        | 80.54187980869656      | 80.54187980869656  | 80.54187980869656  | 80.54187980869656    | 80.54187980869656                  | 80.20126868643935  | 82.14736598995016  |
| 6  | **question-answering**             | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |
| 7  | **table-question-answering**       | 1.3225504381601345      | 1.3166172431468306       | 1.3153743370946702 | 1.3198812126378756  | 1.319062385972064        | 1.319062385972064   | 1.3198812126378756     | 1.3110976318460805           | 1.3198812126378756           | 1.3138242080013738 | 1.313691619378273      | 1.3190380321191375 | 1.314408427667287  | 1.313691619378273       | 1.313691619378273        | 1.3135352015536808     | 1.3135352015536808 | 1.313691619378273  | 1.3135352015536808   | 1.3135352015536808                 | 1.312195956769821  | 1.3225504381601345 |
| 8  | **zero-shot-classification**       | 46.5023290500327        | 41.15355742199045        | 39.45219420055928  | 41.15355742199045   | 41.15355742199045        | 41.491174407347344  | 41.491174407347344     | 41.15355742199045            | 41.15355742199045            | 41.15355742199045  | 41.15355742199045      | 39.01497193720055  | 39.77558344278706  | 39.440035895830206      | 39.40758973652369        | 39.40758973652369      | 39.40758973652369  | 39.40758973652369  | 39.40758973652369    | 39.40758973652369                  | 39.19018997933996  | 46.5023290500327   |
| 9  | **summarization**                  | 104.31862849212017      | 101.65048372229249       | 99.47817317741409  | 103.9934189579141   | 104.18472070448853       | 101.63984655142477  | 101.65048372229249     | 101.65048372229249           | 102.25441789017344           | 104.19879468840448 | 104.19879468840448     | 104.18472070448853 | 103.9934189579141  | 99.89870007446244       | 104.19879468840448       | 104.19879468840448     | 104.19879468840448 | 104.19879468840448 | 104.19879468840448   | 104.19879468840448                 | 102.74739084198599 | 104.31862849212017 |
| 10 | **feature-extraction**             | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 11 | **text-retrieval**                 | 36.10433566589214       | 34.87767471902576        | 34.87767471902576  | 35.12567778917545   | 34.777742827505485       | 34.697830296195626  | 34.777742827505485     | 34.777742827505485           | 34.777742827505485           | 35.61607068635006  | 35.61607068635006      | 34.23990182693673  | 35.000096321934045 | 34.22903603107557       | 35.61607068635006        | 35.61607068635006      | 35.61607068635006  | 35.61607068635006  | 35.61607068635006    | 35.61607068635006                  | 35.088447857802805 | 36.10433566589214  |
| 12 | **fill-mask**                      | 155.56826129780893      | 153.98529399645264       | 146.0832544602141  | 153.98529399645264  | 153.98529399645264       | 150.88463676137474  | 153.98529399645264     | 153.98529399645264           | 153.98529399645264           | 155.56826129780893 | 155.56826129780893     | 152.3200401723516  | 152.09037504570395 | 153.88250286434817      | 155.56826129780893       | 155.56826129780893     | 155.56826129780893 | 155.56826129780893 | 155.56826129780893   | 155.56826129780893                 | 151.71709906480004 | 155.56826129780893 |
| 13 | **sentence-similarity**            | 39.93129670815432       | 39.28344238266383        | 39.45219420055928  | 39.77558344278706   | 39.332761030673225       | 39.786513365401426  | 39.2699839141043       | 38.3143869562798             | 39.507515889596135           | 39.45219420055928  | 39.40758973652369      | 39.01497193720055  | 39.77558344278706  | 39.23578778596472       | 39.40758973652369        | 39.40758973652369      | 39.40758973652369  | 39.40758973652369  | 39.40758973652369    | 39.40758973652369                  | 39.19018997933996  | 39.93129670815432  |
| 14 | **image-classification**           | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 15 | **image-segmentation**             | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 16 | **image-to-image**                 | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 17 | **image-to-text**                  | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 18 | **object-detection**               | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 19 | **zero-shot-image-classification** | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 20 | **other**                          | 21.239857506160618      | 20.569422066551923       | 20.342286222109305 | 21.03688019066529   | 20.70350114753004        | 20.463975674905367  | 20.569422066551923     | 20.569422066551923           | 20.569422066551923           | 21.00810385066473  | 21.00810385066473      | 19.834200619024816 | 21.03688019066529  | 20.3157490668739        | 21.00810385066473        | 21.00810385066473      | 21.00810385066473  | 21.00810385066473  | 21.00810385066473    | 21.00810385066473                  | 20.26681043977138  | 21.239857506160618 |
| 21 | **None**                           | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |

|    | **name**                           | **text-classification** | **text2text-generation** | **translation**    | **text-generation** | **token-classification** | **multiple-choice** | **question-answering** | **table-question-answering** | **zero-shot-classification** | **summarization**  | **feature-extraction** | **text-retrieval** | **fill-mask**      | **sentence-similarity** | **image-classification** | **image-segmentation** | **image-to-image** | **image-to-text**  | **object-detection** | **zero-shot-image-classification** | **other**          | **None**           |
|----|------------------------------------|-------------------------|--------------------------|--------------------|---------------------|--------------------------|---------------------|------------------------|------------------------------|------------------------------|--------------------|------------------------|--------------------|--------------------|-------------------------|--------------------------|------------------------|--------------------|--------------------|----------------------|------------------------------------|--------------------|--------------------|
| 0  | **text-classification**            | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |
| 1  | **text2text-generation**           | 17.5893384254499        | 16.771912747480478       | 14.969783667153944 | 16.771912747480478  | 16.771912747480478       | 15.953190026199508  | 16.771912747480478     | 16.771912747480478           | 16.771912747480478           | 16.821412981253882 | 16.821412981253882     | 14.040844689194566 | 16.691512295021006 | 15.552007006489685      | 16.821412981253882       | 16.821412981253882     | 16.821412981253882 | 16.821412981253882 | 16.821412981253882   | 16.821412981253882                 | 14.775850097935201 | 17.5893384254499   |
| 2  | **translation**                    | 2.6663417326031085      | 2.6660883537822135       | 2.6659382572982264 | 2.6660883537822135  | 2.6660522800272695       | 2.666130931542699   | 2.6661039509015945     | 2.665547089617256            | 2.666055769123703            | 2.6658822194833967 | 2.6659003205357505     | 2.6659723248109293 | 2.6658923506023484 | 2.665931236483393       | 2.6659003205357505       | 2.6658679392849227     | 2.6658679392849227 | 2.6659003205357505 | 2.6658679392849227   | 2.6658679392849227                 | 2.66588605034165   | 2.6663417326031085 |
| 3  | **text-generation**                | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |
| 4  | **token-classification**           | 155.56826129780893      | 153.98529399645264       | 146.0832544602141  | 153.98529399645264  | 153.98529399645264       | 150.88463676137474  | 153.98529399645264     | 153.98529399645264           | 153.98529399645264           | 155.56826129780893 | 155.56826129780893     | 152.3200401723516  | 152.09037504570395 | 153.88250286434817      | 155.56826129780893       | 155.56826129780893     | 155.56826129780893 | 155.56826129780893 | 155.56826129780893   | 155.56826129780893                 | 151.71709906480004 | 155.56826129780893 |
| 5  | **multiple-choice**                | 82.14736598995016       | 81.69991120661031        | 77.78857592847622  | 81.69991120661031   | 81.69991120661031        | 80.01919609625796   | 81.69991120661031      | 81.69991120661031            | 81.8107939103744             | 81.69991120661031  | 81.69991120661031      | 78.1276625453205   | 79.26274698979653  | 80.47224712350973       | 80.54187980869656        | 80.54187980869656      | 80.54187980869656  | 80.54187980869656  | 80.54187980869656    | 80.54187980869656                  | 80.20126868643935  | 82.14736598995016  |
| 6  | **question-answering**             | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |
| 7  | **table-question-answering**       | 1.3225504381601345      | 1.3166172431468306       | 1.3153743370946702 | 1.3198812126378756  | 1.319062385972064        | 1.319062385972064   | 1.3198812126378756     | 1.3110976318460805           | 1.3198812126378756           | 1.3138242080013738 | 1.313691619378273      | 1.3190380321191375 | 1.314408427667287  | 1.313691619378273       | 1.313691619378273        | 1.3135352015536808     | 1.3135352015536808 | 1.313691619378273  | 1.3135352015536808   | 1.3135352015536808                 | 1.312195956769821  | 1.3225504381601345 |
| 8  | **zero-shot-classification**       | 46.5023290500327        | 41.15355742199045        | 39.45219420055928  | 41.15355742199045   | 41.15355742199045        | 41.491174407347344  | 41.491174407347344     | 41.15355742199045            | 41.15355742199045            | 41.15355742199045  | 41.15355742199045      | 39.01497193720055  | 39.77558344278706  | 39.440035895830206      | 39.40758973652369        | 39.40758973652369      | 39.40758973652369  | 39.40758973652369  | 39.40758973652369    | 39.40758973652369                  | 39.19018997933996  | 46.5023290500327   |
| 9  | **summarization**                  | 104.31862849212017      | 101.65048372229249       | 99.47817317741409  | 103.9934189579141   | 104.18472070448853       | 101.63984655142477  | 101.65048372229249     | 101.65048372229249           | 102.25441789017344           | 104.19879468840448 | 104.19879468840448     | 104.18472070448853 | 103.9934189579141  | 99.89870007446244       | 104.19879468840448       | 104.19879468840448     | 104.19879468840448 | 104.19879468840448 | 104.19879468840448   | 104.19879468840448                 | 102.74739084198599 | 104.31862849212017 |
| 10 | **feature-extraction**             | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 11 | **text-retrieval**                 | 36.10433566589214       | 34.87767471902576        | 34.87767471902576  | 35.12567778917545   | 34.777742827505485       | 34.697830296195626  | 34.777742827505485     | 34.777742827505485           | 34.777742827505485           | 35.61607068635006  | 35.61607068635006      | 34.23990182693673  | 35.000096321934045 | 34.22903603107557       | 35.61607068635006        | 35.61607068635006      | 35.61607068635006  | 35.61607068635006  | 35.61607068635006    | 35.61607068635006                  | 35.088447857802805 | 36.10433566589214  |
| 12 | **fill-mask**                      | 155.56826129780893      | 153.98529399645264       | 146.0832544602141  | 153.98529399645264  | 153.98529399645264       | 150.88463676137474  | 153.98529399645264     | 153.98529399645264           | 153.98529399645264           | 155.56826129780893 | 155.56826129780893     | 152.3200401723516  | 152.09037504570395 | 153.88250286434817      | 155.56826129780893       | 155.56826129780893     | 155.56826129780893 | 155.56826129780893 | 155.56826129780893   | 155.56826129780893                 | 151.71709906480004 | 155.56826129780893 |
| 13 | **sentence-similarity**            | 39.93129670815432       | 39.28344238266383        | 39.45219420055928  | 39.77558344278706   | 39.332761030673225       | 39.786513365401426  | 39.2699839141043       | 38.3143869562798             | 39.507515889596135           | 39.45219420055928  | 39.40758973652369      | 39.01497193720055  | 39.77558344278706  | 39.23578778596472       | 39.40758973652369        | 39.40758973652369      | 39.40758973652369  | 39.40758973652369  | 39.40758973652369    | 39.40758973652369                  | 39.19018997933996  | 39.93129670815432  |
| 14 | **image-classification**           | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 15 | **image-segmentation**             | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 16 | **image-to-image**                 | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 17 | **image-to-text**                  | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 18 | **object-detection**               | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 19 | **zero-shot-image-classification** | 7.983071541656673       | 7.980764017785885        | 7.978497997248855  | 7.980764017785885   | 7.980866262177747        | 7.980870645993219   | 7.981234194656936      | 7.974292049993282            | 7.982960389912294            | 7.981145947491793  | 7.981145947491793      | 7.980298835519095  | 7.979260845305322  | 7.980631307789051       | 7.981145947491793        | 7.981145947491793      | 7.981145947491793  | 7.981145947491793  | 7.981145947491793    | 7.981145947491793                  | 7.979868099111081  | 7.983071541656673  |
| 20 | **other**                          | 21.239857506160618      | 20.569422066551923       | 20.342286222109305 | 21.03688019066529   | 20.70350114753004        | 20.463975674905367  | 20.569422066551923     | 20.569422066551923           | 20.569422066551923           | 21.00810385066473  | 21.00810385066473      | 19.834200619024816 | 21.03688019066529  | 20.3157490668739        | 21.00810385066473        | 21.00810385066473      | 21.00810385066473  | 21.00810385066473  | 21.00810385066473    | 21.00810385066473                  | 20.26681043977138  | 21.239857506160618 |
| 21 | **None**                           | 1802.1060874757104      | 1644.0291182315673       | 1553.0737591674292 | 1644.0291182315673  | 1644.0291182315673       | 1642.4704975474506  | 1644.0291182315673     | 1638.4869759750413           | 1638.4869759750413           | 1719.9070821682271 | 1719.9070821682271     | 1581.313035413542  | 1596.3541718218758 | 1630.4183669976164      | 1719.9070821682271       | 1719.9070821682271     | 1719.9070821682271 | 1719.9070821682271 | 1719.9070821682271   | 1719.9070821682271                 | 1601.3371829163139 | 1802.1060874757104 |


|    | **name**       | **english**        | **french**         | **danish**         | **arabic**         | **chinese**        | **french**         | **german**         | **japanese**       | **korean**         | **norwegian**      | **polish**         | **portuguese**     | **russian**        | **spanish**        | **swedish**        |
|----|----------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| 0  | **english**    | 1735.0313230254735 | 1638.4869759750413 | 1602.0324807026443 | 1554.7643410703977 | 1643.8676970609038 | 1646.4341313891905 | 1638.4869759750413 | 1558.8920745280661 | 1574.7921593894544 | 1680.2024278326103 | 1608.4696543704708 | 1631.6362876426774 | 1620.1580457089726 | 1609.4050842445727 | 1729.9252257587864 |
| 1  | **french**     | 2.7628120061326187 | 2.7615756614129974 | 2.757664750259334  | 2.7585472954045107 | 2.761368505579404  | 2.7615756614129974 | 2.7615756614129974 | 2.757203608253881  | 2.7543568208547438 | 2.7589747661044615 | 2.758633470246984  | 2.7601491927108976 | 2.7598178759875784 | 2.7571247105983363 | 2.758041162784542  |
| 2  | **danish**     | 8.667288395887594  | 8.032710773739774  | 6.8460222981089    | 7.355532241902658  | 9.325812375709388  | 8.032710773739774  | 8.032710773739774  | 7.437251782992875  | 7.929114164918669  | 7.924380635923676  | 8.692248323470004  | 8.42089173537302   | 8.505721975124642  | 8.032710773739774  | 7.677836324629937  |
| 3  | **arabic**     | 1.592620067181387  | 1.5857336909799056 | 1.5844193529977302 | 1.5847829481510214 | 1.5893925051254576 | 1.5857336909799056 | 1.587866661201072  | 1.585689084912875  | 1.5840985542107968 | 1.5855217236169643 | 1.5862789287553078 | 1.586900480860694  | 1.590396922529873  | 1.5857336909799056 | 1.5848807038100907 |
| 4  | **chinese**    | 6.664087336881646  | 6.638030437583273  | 6.537914599366077  | 6.557208871816717  | 6.574687684561337  | 6.638030437583273  | 6.638030437583273  | 6.525123596983927  | 6.60456972849532   | 6.512882778265399  | 6.542208553334181  | 6.555994785167398  | 6.5049113019281215 | 6.638030437583273  | 6.512560735415176  |
| 5  | **french**     | 39.93129670815432  | 39.77558344278706  | 39.151621921655234 | 39.028261916541254 | 39.199188506340576 | 39.77558344278706  | 39.77558344278706  | 38.98112384323271  | 37.97457066882462  | 39.37673296697443  | 39.29368118596313  | 39.67883052731346  | 39.38072256394352  | 39.09519214710424  | 39.48030753283139  |
| 6  | **german**     | 2.7628120061326187 | 2.7615756614129974 | 2.757664750259334  | 2.7585472954045107 | 2.761368505579404  | 2.7615756614129974 | 2.7615756614129974 | 2.757203608253881  | 2.7543568208547438 | 2.7589747661044615 | 2.758633470246984  | 2.7601491927108976 | 2.7598178759875784 | 2.7571247105983363 | 2.758041162784542  |
| 7  | **japanese**   | 2.1365081083006725 | 2.1349349635610912 | 2.1345860299092654 | 2.1344336371120787 | 2.1367054433693444 | 2.1349349635610912 | 2.135516082711097  | 2.1345875282330806 | 2.1344790626851085 | 2.1345360055326488 | 2.134244306235946  | 2.134811721636822  | 2.1358555233905006 | 2.1349349635610912 | 2.1344386377235827 |
| 8  | **korean**     | 3.0061566308468395 | 2.4531723329968615 | 1.8557822047897847 | 2.571360492460612  | 2.8099347547722435 | 2.4531723329968615 | 2.257319322693837  | 1.6499900850381128 | 2.3609181691204606 | 2.581998106581623  | 3.771395351301546  | 1.9517382082609642 | 2.679147277515562  | 2.219194036032551  | 2.1152749905785475 |
| 9  | **norwegian**  | 8.869915727847955  | 7.6911509969296015 | 6.866673794718082  | 7.212486195795854  | 8.745619674628125  | 7.6911509969296015 | 7.6911509969296015 | 7.255575795215861  | 7.391073387467777  | 6.930154713572541  | 8.109409559821279  | 7.058653649975061  | 7.461519164115454  | 7.6911509969296015 | 7.119470370272911  |
| 10 | **polish**     | 5.881568506100097  | 5.649782098827879  | 5.6673539722821795 | 5.463783087850102  | 5.6841987708832615 | 5.649782098827879  | 5.649782098827879  | 5.431268759227643  | 5.448136066205046  | 5.693677468197806  | 5.738192587351391  | 5.535813453856044  | 5.583054159169187  | 5.538631396112617  | 5.7010080939518115 |
| 11 | **portuguese** | 3.626699888956971  | 3.5437696105650893 | 3.5427401122407485 | 3.5111773107350435 | 3.5816225199011065 | 3.600054800518968  | 3.571725353825171  | 3.5206355877869746 | 3.5201415257890445 | 3.5992968294609398 | 3.523575559849688  | 3.558472830793034  | 3.55125626886294   | 3.5587547500445407 | 3.617944731426125  |
| 12 | **russian**    | 81.69991120661031  | 78.56564660477868  | 82.14736598995016  | 80.58488313844704  | 80.81410154038198  | 81.02886330978018  | 80.21306731793135  | 79.87131681766454  | 79.41166383256828  | 81.00442598793211  | 79.36339557802981  | 80.49745421115621  | 79.81252453641478  | 80.36445021350235  | 81.18135854712943  |
| 13 | **spanish**    | 7.315874910799548  | 4.6010936912531495 | 1.8498441169196287 | 3.1088713772273473 | 4.017284449803233  | 4.6010936912531495 | 4.6010936912531495 | 3.9648580171510246 | 3.3516953691741653 | 3.2356995555783135 | 4.641064056630746  | 2.519759022442826  | 4.735074175194162  | 4.6010936912531495 | 3.116904041590864  |
| 14 | **swedish**    | 39.52113648703541  | 36.315419760964026 | 36.062893607926924 | 34.703034553303894 | 37.6109523256773   | 36.94876375176252  | 36.66667506042218  | 34.92791868191664  | 33.71731222874354  | 38.29993447275022  | 34.47430263655879  | 36.47473735160362  | 36.16020892695575  | 36.07944485361935  | 39.425049074065804 |

|    | **name**       | **english**         | **french**          | **danish**          | **arabic**          | **chinese**         | **french**          | **german**          | **japanese**        | **korean**          | **norwegian**       | **polish**          | **portuguese**      | **russian**         | **spanish**         | **swedish**         |
|----|----------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 0  | **english**    | -15.28944784638076  | -15.294464205812343 | -15.296549033977968 | -15.305978383697179 | -15.280406535565998 | -15.287895396888905 | -15.294464205812343 | -15.297410047065513 | -15.304897155843522 | -15.301426852172169 | -15.30385512783194  | -15.29950406814272  | -15.286767484210024 | -15.294310643729544 | -15.299413543849921 |
| 1  | **french**     | -0.6992834845998055 | -0.7010022024478596 | -0.7019307678601165 | -0.7019826281994637 | -0.7012624309627963 | -0.7010022024478596 | -0.699411777728409  | -0.7016505816390219 | -0.7016667767022806 | -0.7009022237432163 | -0.7016001237584251 | -0.7016891911706341 | -0.7000230510892843 | -0.7013546743359961 | -0.701305473842412  |
| 2  | **danish**     | -0.7182549771628457 | -0.7224354805353419 | -0.7161296724074233 | -0.720678636269886  | -0.716526774216311  | -0.7180341904428423 | -0.720202879676541  | -0.7192421359071398 | -0.7161585866671056 | -0.7162402179794765 | -0.7171963053588487 | -0.7171894103309222 | -0.7176351054952195 | -0.7179428103741166 | -0.7153496509370785 |
| 3  | **arabic**     | -0.6614457843480523 | -0.6709345562755846 | -0.6682118065716637 | -0.6650838397733436 | -0.6666522403946131 | -0.6689739926183713 | -0.6661309461763874 | -0.6680715780066224 | -0.6708701742837992 | -0.6670100013321922 | -0.6707998342647334 | -0.6657209946213667 | -0.664791286798912  | -0.6661689148930039 | -0.6656640755185395 |
| 4  | **chinese**    | -0.7263253815237231 | -0.7265276306934259 | -0.7267550788876223 | -0.7266744479138975 | -0.7264153174723449 | -0.7265276306934259 | -0.7265276306934259 | -0.7269427150069174 | -0.7273590614623819 | -0.7267146654694427 | -0.7267221902032083 | -0.7264941147288366 | -0.7265572912888881 | -0.7267157503786889 | -0.7266576348581888 |
| 5  | **french**     | -0.710292841189797  | -0.712472676662622  | -0.7128241459553457 | -0.7125670700892923 | -0.7116034953255219 | -0.7113503529712969 | -0.7108186282938045 | -0.7126972819689654 | -0.7119699373725756 | -0.7127361565509096 | -0.7130945910078454 | -0.7124427969913067 | -0.7120314312588062 | -0.7118060313676859 | -0.712437754180594  |
| 6  | **german**     | -0.703587731879585  | -0.7052558609992676 | -0.7059435171323557 | -0.7062316149699128 | -0.7052887037528901 | -0.7052558609992676 | -0.7046732650650498 | -0.7051797942535489 | -0.7059197494277466 | -0.7060242855619956 | -0.7054499394441348 | -0.7056335729649543 | -0.7043033490083712 | -0.7051505427009072 | -0.705859568286118  |
| 7  | **japanese**   | -0.695715949292784  | -0.6968178607425701 | -0.6970563639212256 | -0.6965509271673918 | -0.6952341659237424 | -0.6961028548206434 | -0.695293166829063  | -0.6947136191216362 | -0.6955168951172304 | -0.6961297953306711 | -0.6968803262335974 | -0.6971754051827834 | -0.6966119623641043 | -0.695870372345667  | -0.6962769346698676 |
| 8  | **korean**     | -0.7032379722941433 | -0.7050953579592256 | -0.705316951933701  | -0.7053571579421383 | -0.7034109361549967 | -0.7030339988958509 | -0.7028233523967029 | -0.704084878309158  | -0.7024392594096739 | -0.7051681466252707 | -0.7056119877499936 | -0.705110475132474  | -0.7040334831750998 | -0.7030100210985655 | -0.7049401155282731 |
| 9  | **norwegian**  | -0.7229848319439599 | -0.7259571433621739 | -0.7224851862218591 | -0.7248264717038528 | -0.7236089001341346 | -0.7231272845565508 | -0.7250824419950943 | -0.7236789116377211 | -0.7228838929897927 | -0.7235297756063368 | -0.724000450706759  | -0.7242670837908481 | -0.7244503988568473 | -0.7243966605999771 | -0.7237992655446484 |
| 10 | **polish**     | -0.5936595857813813 | -0.6066675444421126 | -0.6037842432815598 | -0.6057396494756544 | -0.6023153361765299 | -0.6007487172308541 | -0.6023219135570705 | -0.605217899533055  | -0.6026168280931721 | -0.6008578954671661 | -0.5944517329973472 | -0.5997070524401501 | -0.602761113669402  | -0.6005143056498884 | -0.5998798818460402 |
| 11 | **portuguese** | -0.63725649534967   | -0.639010072575788  | -0.6388005441396251 | -0.6394254083416778 | -0.6389359423148572 | -0.639010072575788  | -0.6379435667024589 | -0.63876994100327   | -0.6386727525310072 | -0.6380245058689514 | -0.6393154909852562 | -0.6372739218639126 | -0.6388033075615754 | -0.6387818465043466 | -0.6381803701805566 |
| 12 | **russian**    | -0.724997746833581  | -0.7260520180261555 | -0.7256542289732185 | -0.7257593125191322 | -0.7250977910761869 | -0.7251971925977343 | -0.7248988627710182 | -0.725689535905615  | -0.7261420754528833 | -0.7259920182760065 | -0.7241061844623147 | -0.7251126514970812 | -0.7246318350808925 | -0.7246932430601071 | -0.7250671603812257 |
| 13 | **spanish**    | -0.7029850187873523 | -0.7057112528674556 | -0.7054977266463813 | -0.7062829467448595 | -0.704280931018054  | -0.7024261126256717 | -0.7028837456140385 | -0.7051390343758784 | -0.7043176512293334 | -0.7058016978081392 | -0.7060284976958364 | -0.7059943767339596 | -0.7056958266119746 | -0.7026658191829092 | -0.7059309918394067 |
| 14 | **swedish**    | -0.7113984177000529 | -0.7199734281851626 | -0.7202527991143097 | -0.7202136859795817 | -0.7195656027490247 | -0.7199734281851626 | -0.7185301863374405 | -0.7135494853287604 | -0.7195120372763494 | -0.7196003520296307 | -0.719630159610825  | -0.7189978336630315 | -0.7159388769549775 | -0.7202346842581074 | -0.7178182515087663 |

