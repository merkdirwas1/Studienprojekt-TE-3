# Studienprojekt-TE-3

## Table of Contents
1. [Methods](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#methods)
2. [Which impact has the Task size on the LogMe Score](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-impact-has-the-task-size-on-the-logme-score)
3. [Which Tasks are often in the Top k intermediate Tasks?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#which-tasks-are-often-in-the-top-k-intermediate-tasks)
4. [How symmetrical in order of top-k symmetrie are the Groups?](https://github.com/merkdirwas1/Studienprojekt-TE-3/tree/main?tab=readme-ov-file#top-k-symetrie)
5. [How symmetrical in order of distance symmetrie are the groups?]


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

### Size 
max-Size-group
![max-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/max%20100.png)
large-Size-group
![large-Size-group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/Large%20100.png)
small-Size-group
![small-Size-group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/small%20100.png)
tiny-Size-group
![tiny-Size-Group](https://github.com/merkdirwas1/Studienprojekt-TE-3/blob/main/images/tiny%20100.png)

The plots shows that the max and the large group have a high top-k symmetrie for low top-k and it drops fast for increasing k. The small and tiny group have a low symmetrie. The Groups here are only for the Target Task so the top k can be from other groups. It shows only that the choice of the target Task change how symmetrical the methode is. Becouse the sum of the percentage of the top 1 pairs is near 100 further work would investigate which pairs that are and why they behave like that.

### Language 
TODO
### Categorie 
TODO




## How symmetrical in order of distance symmetrie are the groups?

im allgemeinen
Im allgemeinen liegt die Verteilung an starken Paaren bei um die 8.6% und bei schwachen Paaren bei um die 18.8%. Was die Frage  mit "unlikely" beantwortet.

### How symmetrical are the sizes?
Alle kombinationen von Größenklassen haben einen gesteigerten Anteil an symetrischen Paaren, mit ausnahme von (tiny, A); (A, tiny) Paaren. Diese sind seltener symetrisch im vergleich zur Gesammtverteilung. Scheinbar sind größere Datensets öfter symetrisch zueinander als kleine Sets es sind.
#todo: table einfügen

strong
|           | **max**       | **large**     | **small**     | **tiny**      |
|-----------|---------------|---------------|---------------|---------------|
| **max**   |  0,1226995294 |               |               |               |
| **large** |  0,1156464313 |  0,1260159196 |               |               |
| **small** |  0,1335600095 |  0,1269251656 |  0,1491718992 |               |
| **tiny**  | 0,04804200749 | 0,04935797056 | 0,05801542937 | 0,01948834243 |

Ratio gesammt 0,08603666537

|           | **max**      | **large**    | **small**    | **tiny**      |
|-----------|--------------|--------------|--------------|---------------|
| **max**   | 0,2518830856 |              |              |               |
| **large** | 0,2774701549 | 0,3089233347 |              |               |
| **small** | 0,2811447811 | 0,3007277072 | 0,2978660479 |               |
| **tiny**  | 0,1087885101 | 0,1214531788 | 0,1212529829 | 0,05382325845 |

Ratio gesammt
0,1884581279


### How symmetrical are languages?
Die meisten Sprachenklassen sind zu 13-20% start und zu 10-30% schwach symetrisch. Wie bei der transitivität habe sind die Werte wieder im verhältnis zu der maximal möglichen Anzahl an Paaren in dieser Sprachklasse, wobei ich hier (A,A) Paare schon ausschließe. Sprachen zeigen zudem ein erhöhtes vorkommen ans starken/ schwachen Paaren im vergleich zur Gesammtverteilung über alle Klassen hinweg.
#todo: table einfügen


### How symmetrical are categories?
Im Allgemeinen sind Kategorien nicht symmetrisch da der größte starke symetriewiert bei 30% liegt und das bei einer sehr kleinen Kategorie
Die hälfte der Kategorien zeigt allerdings ein erhöhten anteil an stark symmetrischen paaren im vergleich zum gesammt set sodass davon auszugehen ist dass die wahrscheinlichkeit für symetrische paare in einer kategorie steigen kann. die andere hälfte ist allerdings leicht unterdurchschnittlich. Gerade die Kategorien text-generation und question-answering sind dahingehend stark unterdurchschnittlich
#todo: table einfügen



