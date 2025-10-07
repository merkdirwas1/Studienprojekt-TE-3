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
