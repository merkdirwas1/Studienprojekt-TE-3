# Studienprojekt-TE-3

## Table of Contents
1. [Reproducibility]()
2. [Methods](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#methods)
3. [Which impact has the Task size on the LogMe Score?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-impact-has-the-task-size-on-the-logme-score)
4. [Which Tasks are often in the Top k intermediate Tasks?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-tasks-are-often-in-the-top-k-intermediate-tasks)
5. [How symmetrical in order of top-k symmetrie are the Groups?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#top-k-symetrie)
6. [How often do tasks from the same group appear in the top 50 of a group task? ](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#how-often-do-tasks-from-the-same-group-appear-in-the-top-50-of-a-group-task)
7. [How symmetrical in order of distance symmetrie are the groups?](https://github.com/merkdirwas1/Studienprojekt-TE-3?tab=readme-ov-file#how-symmetrical-in-order-of-distance-symmetrie-are-the-groups)
8. [Are the mean / minimum / maximum in a class different from the values out of the group?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#are-the-mean--minimum--maximum-in-a-class-different-from-the-values-out-of-the-group)

## Reproducibility
1. Calculate the LogMe Scores for each dataset. For that use the calculate_LogME.py which need the dataset_call csv. Alternatively use Data1-3 for the database creation.
2. After calculating all LogMe scores use the prüfe_vollständigkeit.py script to check for complettness or to get a new list of queries. The script need the help_scores for that.
3. The data are needed to create the database. To create the database the create_database.py script has 4 functions.<br>
  3.1. The first is the create_meta_table() to create a table which holds Name, size, language, categorie, size_group as information <br>
  3.2. After that run the create_datatables() function to create a table for each Task which use the meta_table to hold Name, score, language, categorie, size, size_group for each intermediate task for each task. <br>
  3.3. The function create_matrix() create a table which holds a 2d matrix which all scores. left is the intermediate taks and top is the target task. <br>
4. There are a variety of function to calculate / plot the result of the project.<br>
  4.1 For the first plot of the question "Which impact has the Task size on the LogMe Score?" the function werte_verteilung_size() is used <br>
  4.2. For the second plot TODO is used <br>
  4.3 For the plots and tables of the question Which Tasks are often in the Top k intermediate Tasks? the top_k_all_data() is used <br>
  4.4 For the symmetrie in order of top-k the functions create_fig_topk and create_fig_size <br>
  4.5 for the symmetrie in order of distance the function overall_sym and in_class_dist_sim for the groups  is used <br>
  4.6 for the tables of the mean / min / max different the table tabelle is used <br>


## Methods

**Definition class:**<br>
A class is defined by a specific feature of the tasks, such as the language used, the size of the task or the task domain. If tasks share a feature, they are part of the same group. 

**Definition Size groups:**<br>
To investigate the impact of size on LogMe scores, I defined four size groups. 

| **Name** | **Datapoint Range**    | **Size**  |
|----------|------------------------|-----------|
| Max      | 7.5k to 10k Datapoints | 562 Tasks |
| large    | 5k to 7.5k Datapoints  | 101 Tasks |
| small    | 2.5 to 5k Datapoints   | 134 Tasks |
| Tiny     | up to 2.5k Datapoints  | 575 Tasks |

In order to investigate the impact of tasks on each other, I defined two types of symmetry. The first is a top-k symmetry and the second is a distance symmetry. 

**Definition top-k symmetrie:**<br>
If Task A is a top-k intermediate task of Task B, and Task B is a top-k intermediate task of Task A, then they are both symmetrical.

**Definition distance symmetrie:**<br>
If the LogMe score distance between Task A and Task B is 0.1 or lower, then Task A and Task B are strongly symmetrical. If this distance is smaller than or equal to 0.5, they are weakly symmetrical.

## Which impact has the Task size on the LogMe Score?
To answer this question, I examined the LogMe scores in different size groups to see if there were any indicators of how size affects the score.
![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/newplot(8).png)

The figure illustrates the range of LogMe scores at which one task from one size group is the intermediate task and one task from another group is the target task. The findings indicate that when the intermediate task group is altered, there is only a marginal difference in the results. The range is subject to alteration in instances where the target task belongs to a different group. Furthermore, the data indicates that the majority of values are below 0, with a concomitant shift to the left as the target task becomes more modest in scope. Furthermore, it has been demonstrated that in the case of a relatively modest target task, the range of LogMe scores is shown to increase to a value in excess of 1300.

In order to conduct a more thorough investigation, it is necessary to examine the distribution of LogMe scores. This is defined as the maximum minus the minimum LogMe score for each target task. In order to ascertain whether the magnitude of the target task exerts an influence on the scores, a correlation is plotted between the size of the task and the scores.
![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/spread-gr%C3%B6%C3%9Fe.png)

It shows that the plot converges at 0, and that the range of possible logMe scores increases as the size decreases. Therefore, larger tasks have a smaller spread than smaller ones.  This figure has been filtered because some tasks produce LogMe scores over 100, which causes compression and makes it difficult to read.

So it looks like size has an impact on the LogMe score. It determines the spread and range of LogMe scores.

## Which Tasks are often in the Top k intermediate Tasks?
I want to investigate the top k intermediate tasks across all tasks to see if there are any that occur more frequently than others. To improve the quality of the plots, I only show tasks that have occurred more than 300 times in the top k.

### Top 10 top-k

![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%2010.png)

As Fig. shows, a few tasks appear frequently among the top 10 intermediate tasks. Two tasks occur more than 500 times, meaning that they could be a good intermediate task for over 36% of all target tasks.

All six tasks are in the maximum size class.
Looking at the task categories, we see that the intermediate datasets mostly come from the text classification category, with just two other categories. 

| **text-classification** | **multiple-choice** | **token-classification** |
|-------------------------|---------------------|--------------------------|
| 6                       | 2                   | 1                        |

Looking at the languages, we see that four of the datasets are in English. One is in Chinese and one is in Gujarati.

### Top 25 top-k

![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%2025.png)
The trend continues in the top 25, with many more intermediate tasks occurring, often in the top 25 of all intermediate tasks. 
The size distribution can be seen in the table below: 
| **text-classification** | **multiple-choice** | **token-classification** |
|-------------------------|---------------------|--------------------------|
| 6                       | 2                   | 1                        |

Like in the top 10 the most Tasks are in the text-classification categorie or in multiple-choice or in token classification.
| **text-classification** | **multiple-choice** | **token-classification** | **question-answering** | **zero-shot-classification** | **text-generation** | **translation** |
|-------------------------|---------------------|--------------------------|------------------------|------------------------------|---------------------|-----------------|
| 16                      | 5                   | 4                        | 2                      | 1                            | 1                   | 1               |

Nine of the tasks are in English, while the rest are in a single language. 

### Top 50 top-k
![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%2050.png)

The trend continues in the top 50, showing that a few datasets occur very frequently. The first two top 50 tasks occur over 50% of the time.
The size distribution can be seen in the table. 

| **max** | **large** | **small** | **tiny** |
|---------|-----------|-----------|----------|
| 27      | 2         | 2         | 3        |

The trend continues in the top 50, showing that a few datasets occur very frequently. The first two top 50 tasks occur over 50% of the time.
The size distribution can be seen in the table. 

| text-classification | multiple-choice | token-classification | question-answering | text2text-generation | text-generation | translation | zero-shot-classification | text-retrieval | fill-mask |
|---------------------|-----------------|----------------------|--------------------|----------------------|-----------------|-------------|--------------------------|----------------|-----------|
| 34                  | 9               | 7                    | 4                  | 3                    | 2               | 1           | 1                        | 1              | 1         |

In the languages it is the same and 21 of the Tasks are in english while the other languages are only once or twice. 

### Top 100 top-k

![SIZE](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Top%20100.png)

The top 100 shows that the claritylab_utcd_out-of-domain dataset is in the top 100 for over 0.69% of all target tasks, indicating its significant presence in the dataset. As illustrated by all four plots, only a limited number of tasks could be considered suitable intermediate tasks for the top k. This observation may be indicative of a inherent characteristic of these intermediate tasks, or alternatively, it could be perceived as a deficiency within the LogMe-ESM method.

The distribution of the sizes can be seen in the table: 

| **max** | **large** | **small** | **tiny** |
|---------|-----------|-----------|----------|
| 44      | 3         | 10        | 32       |

This finding indicates that the optimal intermediate task is more likely to be a maximum set, as the percentage share of maximum tasks is greater than the percentage of maximum tasks over all tasks.
Looking at the top 100 categories shows that the best tasks are multiple-choice, token classification and question answering. The high number of text-classification tasks is because most tasks are in text-classification.

| **text-classification** | **multiple-choice** | **token-classification** | **question-answering** | **text2text-generation** | **text-retrieval** | **zero-shot-classification** | **text-generation** | **translation** | **fill-mask** | **sentence-similarity** | **None** |
|-------------------------|---------------------|--------------------------|------------------------|--------------------------|--------------------|------------------------------|---------------------|-----------------|---------------|-------------------------|----------|
| 87                      | 16                  | 20                       | 17                     | 6                        | 5                  | 4                            | 4                   | 2               | 1             | 1                       | 1        |


## How symmetrical in order of top-k symmetrie are the Groups?
I want to investigate whether this method is symmetrical, and whether groups of different classes are more likely to be symmetrical. For the size groups, the percentage of symmetrical pairs was plotted for an increasing top-k. For the remaining two classes, the utilisation of tables is imperative due to the disproportionate number of groups and the subsequent limited number of tasks assigned to each group.

![generel](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/topksimgeneral.png)

There are only a few pairs of symmetrical sets in the overall set, and a new 0 is introduced if k increases. This phenomenon can be explained by the presence of several intermediate tasks within the top k, which themselves only contain a limited number of top k elements. Consequently, this results in a reduced number of pairs available for this type of symmetry. It can be argued that the ESM-LogMe method is not symmetrical according to this definition.

### Size 
max-Size-group
![Size](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/size.png)

The plot demonstrates that the maximum and large groups exhibit a high top-k symmetry for low top-k, which experiences a rapid decline as k increases. It is evident that both small and tiny groups exhibit a low degree of symmetry. The groups in question are exclusively for the target task, and thus the top k can be derived from other groups. This demonstrates that the selection of target task has a significant impact on the symmetry of the method. It is evident that the sum of the percentage of the top 1 pairs approaches 100. Consequently, further research is necessary to ascertain the specific pairs responsible for this phenomenon and to explore the underlying reasons for their behaviour. It is noteworthy that the initial percentage of the large group is higher than the percentage of the overall set.

### Language 
![max-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/language.png)

The language groups exhibit interesting behaviour, as most languages start at a low percentage and increase in small increments. Most languages gain a higher percentage than in the overall set or size groups. This could suggest that the target language has an impact on how the sets are bound to each other. Macedonian is an interesting case because, after dropping below 60%, it recovers to above 60%.

### Categorie 
![max-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/categories.png)

The categories show the same behaviour as the groups. Some of them start with a percentage of around 50–60%, but this drops quickly as k increases, with most of the categories failing to recover above 20%, which is slightly above the overall set, but close to it.

## How often do tasks from the same group appear in the top 50 of a group task? 
In my top K symmetry research, I don't have the restriction that if A is in the top K of B and B is in the top K of A, that A and B are in the same group. Now, I want to investigate how many of the top K of an group are from the same group. For that, I chose an K of 50.

### categories
| **Name**                       | **Top k Inclass** | **group size** | **group size / total size** |
|--------------------------------|-------------------|----------------|-------------------------------|
| translation                    | 12.5%             | 8              | 0.05%                         |
| text-generation                | 13.13%            | 174            | 12%                          |
| token-classification           | 15.85%            | 138            | 10%                          |
| multiple-choice                | 16.60%            | 146            | 10%                          |
| question-answering             | 20.65%            | 294            | 21%                          |
| table-question-answering       | 29.62%            | 9              | 0.6%                         |
| zero-shot-classification       | 8.98%             | 37             | 0.2%                         |
| summarization                  | 4.78%             | 133            | 9.6%                         |
| feature-extraction             | 4.05%             | 104            | 7.5%                         |
| text-retrieval                 | 24.44%            | 15             | 1%                           |
| fill-mask                      | 3.2%              | 26             | 1%                           |
| sentence-similarity            | 4.38%             | 37             | 2%                           |
| text2text-generation           | 0.12%             | 48             | 3%                           |
| image-classification           | 3.53%             | 94             | 6%                           |
| image-segmentation             | 3.45%             | 93             | 6.7%                         |
| image-to-image                 | 3.45%             | 93             | 6.7%                         |
| image-to-text                  | 3.53%             | 94             | 6.8%                         |
| object-detection               | 3.45%             | 93             | 6.7%                         |
| zero-shot-image-classification | 3.45%             | 93             | 6.7%                         |
| other                          | 0%                | 9              | 0.6%                         |

Some of the categories, like token-classification or multiple-choice, show a higher accuracy of tasks of the same group than their accuracy in the dataset, which is an evidence that these groups have an impact on the LogMe score. The most categories don't show these and many categories, like the Image-X groups, have a lower acuracy of intermediate tasks of the same group. So, there is no clear answer if the category has an impact on the ESM-LogMe score.


### language
To calculate the table, I filtered all languages under 15 tasks for better proof of evidence.
| **Name**   | **Top k Inclass** | **group size** | **group size / total size** |
|------------|-------------------|----------------|-----------------------------|
| english    | 58.67%            | 719            | 52.5%                       |
| arabic     | 6.79%             | 15             | 1%                          |
| french     | 7.16%             | 33             | 2.4%                        |
| danish     | 4.33%             | 20             | 1.4%                        |
| norwegian  | 0.07%             | 18             | 1.3%                        |
| swedish    | 3.26%             | 33             | 2.4%                        |
| chinese    | 12.34%            | 34             | 2.4%                        |
| german     | 9.72%             | 17             | 1.3%                        |
| spanish    | 5.03%             | 18             | 1.3%                        |
| japanese   | 3.04%             | 25             | 1.8%                        |
| korean     | 5.67%             | 23             | 1.6%                        |
| polish     | 7.68%             | 25             | 1.8%                        |
| portuguese | 5.32%             | 26             | 1.8%                        |
| russian    | 6.77%             | 33             | 2.4%                        |

Contrary to the categories, near all languages have a higher accuracy of tasks of the same group in the top 50 than their accuracy in the total dataset. That can be an evidence that these groups bind more together. But all groups except English have a small group size. 

### size
| **Name** | **Inclass** | **group size** | **group size / total size** |
|----------|-------------|----------------|-----------------------------|
| max      | 18%         | 562            | 40.9%                       |
| large    | 2%          | 101            | 7.3%                        |
| small    | 6%          | 134            | 9.4%                        |
| tiny     | 51%         | 575            | 41.9%                       |

In the size groups, max, large and small are lower than their occurrence in the dataset. The tiny group has a higher percentage. What is interesting is that in the top k 50 symmetries this group has the lowest amount of symmetrical pairs, but in these they have the highest. 


## How symmetrical in order of distance symmetrie are the groups?

To answer this question, I first calculated the ratio of strong and weak pairs. For strong pairs, the ratio is 8.6% across all tasks, whereas for weak pairs, it is 18.8%. Therefore, in general, this method is not symmetrical in terms of its definition. Next, I wanted to know if the classes showed a higher ratio, which could mean that the classes impact how well two tasks suit each other. I did not calculate whether (A, A) pairs were symmetrical.

### How symmetrical are the sizes?
I calculated a table for the size groups of strong and weak pairs. It shows the ratio of symmetrical pairs, with the columns representing the intermediate task size group and the rows representing the target task size group.

**strong pair ratio:**
|           | **max** | **large** | **small** | **tiny** |
|-----------|---------|-----------|-----------|----------|
| **max**   |   10,02 |           |           |          |
| **large** |    6,48 |      5,07 |           |          |
| **small** |     7,2 |      4,96 |      6,48 |          |
| **tiny**  |    9,35 |      6,65 |      6,66 |     9,27 |

It shows that Max-Max, Max-Tiny and Tiny-Tiny have slightly higher symmetrical pairs, but it is also unlikely that two tasks in this group are symmetrical. However, max-tiny and tiny-tiny are still close to the overall ratio, so this score could be random.


**weak pair ratio:**
|           | **max** | **large** | **small** | **tiny** |
|-----------|---------|-----------|-----------|----------|
| **max**   |   20,58 |           |           |          |
| **large** |   13,58 |       8,5 |           |          |
| **small** |   18,77 |     12,61 |     17,42 |          |
| **tiny**  |   20,17 |     12,71 |     18,45 |    19,69 |

for the weak pairs it is the same like for the strong pairs. 


### How symmetrical are languages?
The results of my calculations for the languages are shown in the table below. The table also shows the size of each language group.

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

The table shows that many groups have strong and weak symmetries, which suggests that languages have a slight impact on how the LogMe score behaves. However, most of the language groups are small, so there is a lack of evidence that this is a general behaviour. 

### How symmetrical are categories?
The results of my calculations for each category can be found in the table below. The table also shows the size of each category group.
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

Other than the language groups, the category groups are large enough to provide more evidence. The table shows that half of the categories have a higher strong-to-weak ratio than the overall set. This means that the categories have a larger impact on LogMe behaviour than language. However, this method is still not symmetrical according to my definition.

# Are the mean / minimum / maximum in a class different from the values out of the group?
To investigate whether my chosen classes show evidence of how the tasks are bound together, I calculated the maximum, minimum and mean values of all tasks in a group and of all tasks outside the group. If the groups are bound together, this should be reflected in these values. 

## Languages
As there are many languages with only a few tasks, I filtered out all languages with fewer than 15 tasks. The high values for English come from the very small tasks, which have only two or six data points. 

Language max
| **Name**   | **In group**        | **Out group**       |
|------------|--------------------|--------------------|
| english    | 1735.0313230254735 | 1624.1109686892019 |
| french     | 2.7615756614129974 | 2.7588487293546673 |
| danish     | 6.8460222981089    | 8.107664050384923  |
| arabic     | 1.5847829481510214 | 1.5863573839200442 |
| chinese    | 6.574687684561337  | 6.569653592392724  |
| french     | 39.77558344278706  | 39.24549235894605  |
| german     | 2.7615756614129974 | 2.7588487293546673 |
| japanese   | 2.1345875282330806 | 2.1349547185376667 |
| korean     | 2.3609181691204606 | 2.413036884309162  |
| norwegian  | 6.930154713572541  | 7.537314275363754  |
| polish     | 5.738192587351391  | 5.59202088647841   |
| portuguese | 3.558472830793034  | 3.5571303816158757 |
| russian    | 79.81252453641478  | 80.38830716071169  |
| spanish    | 4.6010936912531495 | 3.718795019651674  |
| swedish    | 39.425049074065804 | 36.03396909324652  |

Language mean
| **Name**   | **Inclass**          | **Outclass**         |
|------------|----------------------|----------------------|
| english    | 93.35852942322366    | 82.05229532710565    |
| french     | 0.52265407638516     | 0.5204308185338292   |
| danish     | 0.38852841461776266  | 0.4372223925907785   |
| arabic     | -0.30615877642476386 | -0.30827563271218617 |
| chinese    | 0.1721208729576099   | 0.1624114748587041   |
| french     | 1.9372417966996045   | 1.902868418657351    |
| german     | 0.22540081689853833  | 0.22273434874289527  |
| japanese   | -0.1233224663100758  | -0.1244533354877197  |
| korean     | -0.27395667017222747 | -0.27334715443970253 |
| norwegian  | 0.4251097618194247   | 0.4297386644156368   |
| polish     | 0.6196449714316207   | 0.5972913979727744   |
| portuguese | 0.3950698519392807   | 0.3936295317344332   |
| russian    | 11.57229005895875    | 11.392958705128681   |
| spanish    | 0.344799767329328    | 0.31574797309036945  |
| swedish    | 4.023945756283439    | 3.940464393940656    |


Language min
| **Name**   | **Inclass**         | **Outclass**        |
|------------|---------------------|---------------------|
| english    | -15.28944784638076  | -15.296238763185718 |
| french     | -0.7010022024478596 | -0.7012139925753781 |
| danish     | -0.7161296724074233 | -0.7180640141685253 |
| arabic     | -0.6650838397733436 | -0.667692338596599  |
| chinese    | -0.7264153174723449 | -0.7267058340214115 |
| french     | -0.7113503529712969 | -0.7122693843865596 |
| german     | -0.7046732650650498 | -0.7054997199616516 |
| japanese   | -0.6947136191216362 | -0.6962705408191199 |
| korean     | -0.7024392594096739 | -0.7043843740693424 |
| norwegian  | -0.7235297756063368 | -0.7240433917000201 |
| polish     | -0.5944517329973472 | -0.6025486446817426 |
| portuguese | -0.6372739218639126 | -0.6387441400988584 |
| russian    | -0.7246318350808925 | -0.7253432519229753 |
| spanish    | -0.7026658191829092 | -0.7050762147546915 |
| swedish    | -0.7178182515087663 | -0.7189209661286434 |

The data indicates that there are no significant differences between the in-group and out-group maximums, with the exception of the English and Swedish groups. While the majority of tasks are conducted in English, this does not necessarily imply a universal tendency. The limited sample sizes indicate considerable variation in the LogMe values. The mean of all in-group and out-group values exhibits equivalent behaviour. The minimum values demonstrate an even more pronounced trend, with the values exhibiting greater proximity. Consequently, the languages provide no evidence to indicate whether two tasks are bound together or whether a task of the same language provides a superior intermediate task in comparison to a task of a different language.

## Categories

Categories max
| **Name**                       | **Inclass**         | **Outclass**       |
|--------------------------------|---------------------|--------------------|
| text-classification            | 1802.1060874757104  | 1679.2512369724063 |
| text2text-generation           | 16.771912747480478  | 16.55799101660633  |
| text-generation                | 1644.0291182315673  | 1681.3231263101025 |
| token-classification           | 153.98529399645264  | 154.42547544175702 |
| multiple-choice                | 80.01919609625796   | 80.89832721475253  |
| question-answering             | 1644.0291182315673  | 1681.3231263101025 |
| zero-shot-classification       | 41.15355742199045   | 40.58403498056704  |
| summarization                  | 104.19879468840448  | 103.36237662331776 |
| feature-extraction             | 7.981145947491793   | 7.981102570060276  |
| text-retrieval                 | 34.23990182693673   | 35.252732046859734 |
| fill-mask                      | 152.09037504570395  | 154.5369412623893  |
| sentence-similarity            | 39.23578778596472   | 39.46958673350547  |
| image-classification           | 7.981145947491793   | 7.981102570060276  |
| image-segmentation             | 7.981145947491793   | 7.981102570060276  |
| image-to-image                 | 7.981145947491793   | 7.981102570060276  |
| image-to-text                  | 7.981145947491793   | 7.981102570060276  |
| object-detection               | 7.981145947491793   | 7.981102570060276  |
| zero-shot-image-classification | 7.981145947491793   | 7.981102570060276  |
| None                           | 1802.1060874757104  | 1672.0244810604472 |

Categories mean
| **Name**                       | **Inclass**        | **Outclass**       |
|--------------------------------|--------------------|--------------------|
| text-classification            | 51.59119291285194  | 47.708272788347905 |
| text2text-generation           | 5.081956908284033  | 5.126554434085802  |
| text-generation                | 294.1472541949229  | 295.6455334698621  |
| token-classification           | 3.8944280194494634 | 3.877359990390994  |
| multiple-choice                | 9.229611905399887  | 9.356569019838862  |
| question-answering             | 215.34245059160386 | 214.94017582129234 |
| zero-shot-classification       | 5.8795954971133035 | 5.908662089502606  |
| summarization                  | 2.7464223754710577 | 2.7211863811758117 |
| feature-extraction             | 0.6854612602494801 | 0.6862207612999085 |
| text-retrieval                 | 2.1193182260929158 | 2.184217319464152  |
| fill-mask                      | 6.585356992002224  | 6.638463693570109  |
| sentence-similarity            | 4.907537967839183  | 4.970064054678972  |
| image-classification           | 0.6910701941063404 | 0.6921251808160463 |
| image-segmentation             | 0.6930017710689304 | 0.6941053568147919 |
| image-to-image                 | 0.6930017710689304 | 0.6941053568147919 |
| image-to-text                  | 0.6910701941063404 | 0.6921251808160463 |
| object-detection               | 0.6930017710689304 | 0.6941053568147919 |
| zero-shot-image-classification | 0.6930017710689304 | 0.6941053568147919 |
| None                           | 51.68392398458587  | 47.58802976069973  |

Categories min
| **Name**                       | **Inclass**          | **Outclass**        |
|--------------------------------|----------------------|---------------------|
| text-classification            | -15.280406535565998  | -15.289197121522388 |
| text2text-generation           | -3.6592097471189544  | -3.472918152381215  |
| text-generation                | -3.5270129252985427  | -3.4806944360177097 |
| token-classification           | -3.566504093398874   | -3.4783714261294545 |
| multiple-choice                | -0.7265930012375048  | -0.7267950559997317 |
| question-answering             | -3.6115640481504516  | -3.475720840555833  |
| zero-shot-classification       | -0.7253149361844886  | -0.7256534874145115 |
| summarization                  | -0.6427657833232789  | -0.64439334046602   |
| feature-extraction             | -0.6165538231539536  | -0.616478711970118  |
| text-retrieval                 | -0.7114117260087753  | -0.7142583009317199 |
| fill-mask                      | -0.6356351957764386  | -0.6403313705350285 |
| sentence-similarity            | -0.6427657833232789  | -0.6443933404660201 |
| image-classification           | -0.6165538231539536  | -0.616478711970118  |
| image-segmentation             | -0.6165538231539536  | -0.616478711970118  |
| image-to-image                 | -0.6165538231539536  | -0.616478711970118  |
| image-to-text                  | -0.6165538231539536  | -0.616478711970118  |
| object-detection               | -0.6165538231539536  | -0.616478711970118  |
| zero-shot-image-classification | -0.6165538231539536  | -0.616478711970118  |
| None                           | -15.280406535565998  | -15.28971421481394  |

The behaviour for the categories is exactly the same as for the languages. The in-group values are close to the out-group values, and in most categories, the differences are so small that they do not provide evidence that tasks from the same categories are a better intermediate dataset than tasks from other groups. 

## Size group 
Size group max
| **Name** | **Inclass**        | Outclass           |
|----------|--------------------|--------------------|
| max      | 9.379093280187472  | 9.370476408234943  |
| large    | 5.174757984908695  | 5.172931789996076  |
| small    | 6.079290820484999  | 6.076872832822961  |
| tiny     | 1802.1060874757104 | 1671.6596575151411 |

Size group mean
| **Name** | **Inclass**          | Outclass             |
|----------|----------------------|----------------------|
| max      | 0.14748967044692704  | 0.14533471484362878  |
| large    | 0.09234750205971215  | 0.09350551200151314  |
| small    | 0.017601843815750584 | 0.018859761867356495 |
| tiny     | 122.14065318251944   | 108.87527700467786   |

Size group min
| **Name** | **Inclass**         | Outclass            |
|----------|---------------------|---------------------|
| max      | -15.280406535565998 | -15.293673498195245 |
| large    | -0.7268702199719896 | -0.7253801837325383 |
| small    | -0.7266595729063818 | -0.7267329031219479 |
| tiny     | -3.566504093398874  | -3.442566581869449  |

The same behaviour is observed for the size groups as for the other two classes. There are no significant differences between the groups, and there is evidence that intermediate tasks within groups are better for transfer learning than tasks outside of groups. Interestingly, the max group has by far the lowest LogMe score compared to the other groups.  
