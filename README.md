# Robert-E-Howard-NLP-analysis


## Quick Start
Download the files and open in the IDE of your choice.

You will need to extract the RAR file with the texts into the project directory.

The file Analysis Function Hyphenated Adj.py is a variation of the normal Analysis Function code. Hyphenated adjectives required a slightly different approach to process.

find an R Shiny dashboard with data loaded here:
https://connork.shinyapps.io/REHShinyFinal/



#Introduction

This investigation attempts to identify changes in an author’s writing style and word choice over the course of their career using natural language processing. Natural language processing is a branch of computer science and linguistics concerned with how computers can process and analyze human language. The short stories of the author Robert E. Howard, which are available in the public domain and readily accessible online, were accumulated in a single dataset and analysed to identify frequently used words, and words whose usage was skewed towards either the start of end of Robert E. Howard’s career. This investigation identified several trends and changes in Robert E. Howard’s writing style which occurred as his writing style developed through his career.

##What is Natural Language Processing
In short, natural language processing (NLP) is a field combining computer science and linguistics which seeks to create methods and analyses by which a computer can read, analyse, and understand human speech and writing.
There are a variety of different computer programs in our daily lives which use NLP. For instance, the junk filter in your email service which detects junk mail uses natural language processing to identify emails which are probably spam.
##Data processing
In this analysis NLP was used to organise words into different types (e.g. adjective, noun or verb) and then remove words such as definite or indefinite articles (the, a, that etc.) These words are known as stopwords in NLP.
##Incorrectly labelled words
There are a large amount of words which cannot be organised according to their word type, such as proper nouns. Many proper nouns cannot be identified as a noun or adjective because they do not exist in a dictionary. For this reason, there is a large amount of “noise” in this dataset. This is inevitable when working which such a large dataset; there were over 11,000 adjectives identified and not feasible to manually check them all, so certain imperfections in the process must be accepted.
##Words that were removed
Many words identified were products of stylized writing in Howard's western stories.
Git, Purty, Derned, Pecooliar, Sech were all incorrectly identified as adjectives.
These words are artifacts of the point-of-view style of writing in Howard's western stories, in which Howard affected a dialect.

Other words which were in correctly identified were proper nouns (such as Cormac or O’Donnel), hyphenated words, or words with punctuation.

A full list of the words removed is available in the analysis code on GitHub.

##Processing data
Each text source was saved in the .txt format. The data from these files was read and collected into a corpus.
Each text source in the corpus was parsed into individual words, and stopwords and other unwanted words were removed. Each word was then identified as a noun, adjective, or verb and this data was stored in a dictionary using a NLP process known as part of speech tagging.
Words were then divided by the word type into separate datasets for later analysis.

##Analysing the data
To analyse the data, the words were identified which are more skewed towards the start or end of the dataset. This revealed the broad changes in the words used by REH over time. Synonyms were identified and grouped together. Groups of synonyms which had both words that were used at the start of REH’s career and words which were used at the end, indicating a change in the preference for a particular type of word over time were identified as being significant and analysed.

A brief review of the most commonly used adjectives in REH’s stories allows for analysis of REH’s choice of words at a basic level. 
Among the most common adjectives are, of course, common adjectives which any author would use. Adjectives like big, small etc.

Word	Frequency
black	2620
other	1859
great	1856
old	1810
long	1324
last	1227
more	1146
white	1091
dead	1082
red	994
big	990
own	983
first	977
open	883
few	882
many	855
wild	801
good	793
dark	686
human	677
such	672
strange	671
high	668
full	646
right	621
little	602
hard	576

Looking at the lesser used but still common adjectives, aspects of REH’s style become identifiable.
Among the most commonly used adjectives are the colours Black, Red, and White. These colours are used as adjectives in the majority of stories and are often featured in the story titles.
In addition, other highly provocative adjectives are identifiable as characteristic of REH’s writing style.
•	Dark
•	Dead
•	Wild
•	Strange
•	Mad
•	Grim


Calculating a word’s usage longitudinally to identify changes in word preference
Apart from the simply frequency words in the texts, how REH’s preference for particular words changed over time is of interest.

To identify words, whose usage increased or decreased over time, a weighted score for each adjective was created to identify words, the usage of which, was skewed towards the beginning or end of Howard's career.

Words with either a large negative or large positive weighted scores are words that REH favoured more at either the start or end of his career respectively.
Using the word remarkable as an example, the weighted score is 356.5, indicating that the word was used more frequently at the end of Howard's career.

A score is close to zero indicates that the adjective was either not used frequently or was used consistently through Howard's career. It indicates a lack of change in preference by the author and is of little interest for the purpose of analysis.




##Notable Adjectives
The word awful was notably favoured by Howard later in his career, although he rarely used the word in the first half of his career.

