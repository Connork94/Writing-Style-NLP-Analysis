
# Introduction

This investigation attempts to identify changes in an author’s writing style and word choice over the course of their career using natural language processing. Natural language processing is a branch of computer science and linguistics concerned with how computers can process and analyze human language. The short stories of the author Robert E. Howard, which are available in the public domain and readily accessible online, were accumulated in a single dataset and analysed to identify frequently used words, and words whose usage was skewed towards either the start of end of Robert E. Howard’s career. This investigation identified several trends and changes in Robert E. Howard’s writing style which occurred as his writing style developed through his career.

## What is Natural Language Processing
In short, natural language processing (NLP) is a field combining computer science and linguistics which seeks to create methods and analyses by which a computer can read, analyse, and understand human speech and writing.
There are a variety of different computer programs in our daily lives which use NLP. For instance, the junk filter in your email service which detects junk mail uses natural language processing to identify emails which are probably spam.
## Data processing
In this analysis NLP was used to organise words into different types (e.g. adjective, noun or verb) and then remove words such as definite or indefinite articles (the, a, that etc.) These words are known as stopwords in NLP.
## Incorrectly labelled words
There are a large amount of words which cannot be organised according to their word type, such as proper nouns. Many proper nouns cannot be identified as a noun or adjective because they do not exist in a dictionary. For this reason, there is a large amount of “noise” in this dataset. This is inevitable when working which such a large dataset; there were over 11,000 adjectives identified and not feasible to manually check them all, so certain imperfections in the process must be accepted.
## Words that were removed
Many words identified were products of stylized writing in Howard's western stories.
Git, Purty, Derned, Pecooliar, Sech were all incorrectly identified as adjectives.
These words are artifacts of the point-of-view style of writing in Howard's western stories, in which Howard affected a dialect.

Other words which were in correctly identified were proper nouns (such as Cormac or O’Donnel), hyphenated words, or words with punctuation.

A full list of the words removed is available in the analysis code on GitHub.

## Processing data
Each text source was saved in the .txt format. The data from these files was read and collected into a corpus.
Each text source in the corpus was parsed into individual words, and stopwords and other unwanted words were removed. Each word was then identified as a noun, adjective, or verb and this data was stored in a dictionary using a NLP process known as part of speech tagging.
Words were then divided by the word type into separate datasets for later analysis.

# Analysing the data
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




## Notable Adjectives
### Awful
The word awful was notably favoured by Howard later in his career, although he rarely used the word in the first half of his career.

 


Looking at relative frequency, awful was used frequently in westerns and boxing stories. 
REH often used this word between 4 and 8 times in a single story, and after 1932 REH used awful in almost every story. In addition, REH used awful to describe a wide range of nouns, often abstract nouns.

•	what awful perils lurk beyond that door I cannot even guess
o	Hour of the dragon 1936
•	an awful expression of dazed surprise
o	The man on the ground 1933

Synonyms of the word awful were investigated to see identify noticeable patterns in similar words.

Table. 1 Synonyms of the word “awful”
Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
Terrific	-577	Awful	1850
Frightful	-255	Appal	686
Terrible	-205	Enormous	255
Wondrous	-65	Tremendous	171
Fantastic	-43	Marvelous	83
Grand	-25	Wonderful	25
			


The word appall (the stem of the word appalling) is also heavily skewed towards the later part of REH’s work and REH began using the word at a similar point as awful.

 

Synonyms for awful which were favoured early in REH’s career were identified. These words were terrible and terrific. 

### Terrible and terrific
Terrible and terrific were used throughout REH’s entire career, but the relative frequency of these words in each story indicates they was more frequently used within stories earlier in REH’s career. Effectively, the word was used consistently, but more frequently early in REH’s career.

 

 


Notably, the words awful, terrible, and terrific, all imply a negative connotation and could be used interchangeably, indicating a change in preference for negative adjectives over time.



### Pale and Livid
 Pale and livid were used throughout REH's career but identified as being skewed towards the end of REH's career and used in western, boxing, and fantasy stories.

 


 

The hyphenated adjective white-faced was used infrequently, but more common earlier in Howard’s career. It is possible that pale and livid replaced the use of white-faced and other adjectives.
 
### Supple
 
REH began to use the word supple frequently later in his career. Supple was often used to describe women and men in fantasy stories.

 


Looking at synonyms, lithe, slender, and limber were all skewed towards earlier, while supple was skewed towards later in the dataset.

Table 2 Synonyms of the word “supple”
Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
slender	-132	supple	928
limber	-41	lissome	91
		lithe	8


### Dynamic
Dynamic, a word frequently used to describe physical prowess, was more frequently used at the beginning of Howard's career, but usage diminished over time.
Mighty is a similar adjective, although a bit more specific, was also used early in REH’s career. 

 

### Mighty
 

Analysing the synonyms of mighty indicates that muscular, powerful or brawny, became preferred as time went by.

Table 3. Synonyms of the word “mighty”
Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
mighty	-691	muscular	602
		powerful	122
		brawny	178


## Zoomorphism
REH often compares humans to animals, a technique called zoomorphism.
The hero of the story is often compared to a panther or tiger, villains are often wolfish, ape-like, or hawk-like, and heavyweight men are bulls.
“They were wolves, but he was a tiger.”
-	Beyond the Black River
Usage of zoomorphic phrases tend to follow patterns.
Beast-like, hawk-like, and lion-like were used commonly between 1930 and 1934, but then sporadically later.
 
 
 


Ape-like was also used frequently between 1928 and 1930 but then abandoned until after 1934, when it was seldom used.
 












## Colours
Another of REH’s favourite descriptive techniques is the use of vivid colours.
“A SHUDDERING, white-faced dawn crept over the black hills to shiver above the red shambles that had been the village of Bogonda”.
•	Wings in the Night
Black was one of the most common adjectives used in Howards stories.
 

The colour red was mentioned in almost every story. 
 
Some hyphenated adjectives which used red such as blood-red or red-stained were used sporadically after 1933, but rarely before. This is consistent with Howard’s used of hyphenated adjectives; Howard invents a hyphenated adjective, uses it for a period of time, before eventually abandoning it.
Blood-red
 
### Red-stained
 
### Crimson
Crimson was less common but also frequently used and spread across Howards entire career.
 

## Hyphenated Adjectives
A notable aspect of early 20th century fiction was the use of hyphenated adjectives.
This style lost favor later in the century, giving way to less florid descriptions.
Howard did indulge in hyphenated adjectives, and some of his most vivid descriptions are such phrases.
Interestingly, Howard often uses a particular hyphenated combination for a period of time, and thereafter abandons it.
A good example being “glass-eyed”, which Howard used 7 times between 1930 and 1932 but only twice after that period and never before 1932. Howards seems to find a new hyphenated adjective or phrase that he likes, then uses this for several stories until it becomes stale and moves on to other descriptions.
 

### blood thirsty, and blood curdling
When examining the use of blood-thirsty and blood-curdling an interesting pattern emerges. Both adjectives appear to be used during specific periods of time, if not in the same stories, in stories written immediately before or after.

 

 


Here a notable characteristic of Howard’s writing style can be seen, that of finding a description which he enjoys using, employing this description, followed by the eventually abandonment of the description after he has used it for a period.
Verbs
Even from his early career, Howard’s action scenes stood out as exceptional. Howard’s use of verbs is crucial to these scenes and examining verbs shows some the most distinct changes in his writing style over time.
Early verbs
The use of fling changed drastically over time. Not only was the word used in more stories early in Howard’s career but also used more frequently within those stories.
 
Examining synonyms of fling shows a variety of other verbs such as toss, whirl, and pass became preferred later in REH’s career.

Table 4 Synonyms of the word “fling”
Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
fling	-1052	whirl	692
		pass	442
		dispose	363
		discard	343
		toss	221



### Jump

Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
Leap	-508	Jump	1471
Bound	-186		
Spring	-135		


### Slug (Slugging)
Verbs describing boxing or fisticuffs were common in the late 1920s and early 1930s in REH’s work. These words were preferred mainly in short stories about boxing, which were popular in pulp magazines at the time.
 The verbs slug, punch and smash are notable examples.
 


Analysing synonyms of slug shows that less specific verbs came to replace the boxing-based verbs after 1930.
Synonyms of the word “slug”
Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
slug	-355	hit	1422
punch	-258	strike	244
smash	-232	belt	98






 
### Hack
 

Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
hack	-436	cut	530
rend	-149	rip	530
		tear	463


### Slay
 

Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
slay	-373	murder	651

### Gaze
Gaze was used more frequently in 1920’s but the proportional usage remained even over the course of Howard’s career.
 


## Other verbs
Many verbs were favoured later or early in REH’s but no identifiable shifts in preference for these verbs was identified in the related synonyms.

### Stumble
 

### Shriek
Words like shriek, howl, yell, and scream were preferred later in REH’s career. It is unclear why this shift occurred, but it may relate to a change in the genre, in which REH was writing.
 


Early in Career	Later in Career
Word	Weighted Score	Word	Weighted Score
		howl	1138
		shriek	1047
		yell	949
		holler	931
		squall	567
		scream	454
		Roar	360
		cry	314
		shrill	238
		Wail	186
		screech	53

 

### Glimpse
 

### Assure
 

### Pant (Panting)
 

### Pull
Although a basic verb, “Pull” increased in frequency towards the end of Howard’s career.
 

### Demand
 



### Grab
 


## Noun usage
The genre of story that Howard was writing is the decisive factor determining whether Howard used a particular noun. Howard wrote in several different genres through his careers, according to trends in the magazine market, wherein he sold his writing.
Nouns such as ‘pistol’, ‘boot’, ‘wheel’, ‘dust’, and ‘saddle’, are all words that are heavily skewed towards late career usage. This is hardly surprising as Howard wrote and sold many western stories later in his career after he had realized the potential of this market.
 
 

 

Words used early in Howard’s career and not later tend to be nautical themed.
‘Sea’, ‘ship’, ‘ocean’, ‘tide’, ‘wharf’, and ‘coast’ are notable examples.

Sea, Ship, Ocean, Tide, Wharf, and Coast
 
 
 
 
 
 

Themes relating to boxing also are used more frequently early in Howard’s career.
‘Fighter’, ‘round’, ‘cheek’, ‘punch’, ‘glove’, ’forehead’, ‘referee’, and ‘uppercut’ are observable.

Interesting examples of words which may indicate either stylistic changes in writing or simply change in theme are “nobody”, “anybody”, and “somebody”, which were used more frequently later.
 
 
 
It’s easy to imagine these words being used in the context of a western story, which is more modern, but more difficult to see them being used in fantasy or historical fiction. Despite these, these words were not used in many of the early stories in a contemporary setting, such as Skull-Face.

