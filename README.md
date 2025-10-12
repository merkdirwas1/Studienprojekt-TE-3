# Studienprojekt-TE-3

## Table of Contents
1. [Methods](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#methods)
2. [Which impact has the Task size on the LogMe Score](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-impact-has-the-task-size-on-the-logme-score)
3. [Which Tasks are often in the Top k intermediate Tasks?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-tasks-are-often-in-the-top-k-intermediate-tasks)
4. [How symmetrical in order of top-k symmetrie are the Groups?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#top-k-symetrie)
5. [How symmetrical in order of distance symmetrie are the groups?](https://github.com/merkdirwas1/Studienprojekt-TE-3?tab=readme-ov-file#how-symmetrical-in-order-of-distance-symmetrie-are-the-groups)
6. [Are the mean / minimum / maximum in a class different from the values out of the group?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#are-the-mean--minimum--maximum-in-a-class-different-from-the-values-out-of-the-group)


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

# Are the mean / minimum / maximum in a class different from the values out of the group?
In order to investigate if my chosen classes show an evidence of how the Tasks are bound together I calculatet the max, min and mean value of all Task in a group and of all task out of the group. If there is an evidence that the group bound task together it should e shown in these values. 
## Languages
Because there are many lanugages with only a few Task I filtered all languages which dont have min. 15 task in it. The high values of english comes from the very small tasks, which have only 2 or 6 data point. 

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

The Data shows that there are no large differences between the in group maximum and the out group maximun beside in the english and the swedish group. The most Tasks are on english bit dont has to say that it is a genereal behavior because of that the tiny sets show a large spread in the LogMe values. The same behavior is shown by the mean over all in and out group values. By the minimum values it is even stronger an the values a nearer to each other. So the languages dont give a evidence if two task are bound together or if a Taks of the same language give a better intermedate task than a taks of an other language.

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

For the categories it is exactly the same behavior than for the languages. The in group values are near to the out group values an the by the most categories the differences are very small so that it dont produce any evidence that the tasks of the same categories are a better intermedate dataset than tasks from other groups 


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

Also for the size groups it is the same behavior like the other two classes. There are no large differences between the groups in order of that in the groups there is evidence that ingroups intermediate Task are better for the transfer learning than out of the groups. What is interesting is that the max group has by far the lowest LogMe score then the other groups.  


# Top k Inclas
categories
| **Name**                       | **Top k Inclass**   |
|--------------------------------|---------------------|
| translation                    | 0.125               |
| text-generation                | 0.1313888888888889  |
| token-classification           | 0.15850604720549843 |
| multiple-choice                | 0.16607169054721502 |
| question-answering             | 0.20659591836734695 |
| table-question-answering       | 0.2962962962962963  |
| zero-shot-classification       | 0.08984660336011688 |
| summarization                  | 0.04780801209372638 |
| feature-extraction             | 0.04058801775147929 |
| text-retrieval                 | 0.24444444444444444 |
| fill-mask                      | 0.032               |
| sentence-similarity            | 0.04382761139517896 |
| text2text-generation           | 0.12                |
| image-classification           | 0.03531009506564056 |
| image-segmentation             | 0.0345704705746329  |
| image-to-image                 | 0.0345704705746329  |
| image-to-text                  | 0.03531009506564056 |
| object-detection               | 0.0345704705746329  |
| zero-shot-image-classification | 0.0345704705746329  |
| other                          | 0.0                 |

language todo

size todo
