#!/usr/bin/env python
# coding: utf-8

# Custom Functions
import NLPfunctions
from NLPfunctions import get_encoding_type
from NLPfunctions import output_graph_combinedfreqprop


# import libraries
import os

import re, nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pandas as pd
import numpy as np

from datetime import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt

#############################################################
### import stopwords and punctuation for later use ##########
#############################################################

from nltk.corpus import stopwords

stop_words_general = list(stopwords.words('english'))
from string import punctuation

punctuation = list(punctuation)
# import custom stop words list
from Stopwords import stop_words, hypadj_stop_words

stop_words = stop_words + stop_words_general + punctuation


###################################
### creating output dirs ##########
###################################

# current directory
cwd = os.getcwd()
print("CWD is ... " + cwd)

# the folder path with the texts
folder_texts = cwd + "/Raw Txt Files/"

# folder to output graphs
folder_images = cwd + "/Figures/"
try:
    os.mkdir(folder_images)
    print(folder_images)
except:
    print("'Figures' Folder already exists.")

# folder for dataset
folder_dataset = cwd + "/Data sets/"
try:
    os.mkdir(folder_dataset)
    print(folder_dataset)
except:
    print("'Dataset' Folder already exists.")


# Type of words, this will update file names
word_type = "Hyphen_ADJ"

# create list that will hold corpus
corpus = []

# get a list of all the files in the directory, we will use this to iterate over the texts
texts = os.listdir(folder_texts)

# function to process documents
def process_document(document, i):
    try:
        text = document.read()
        text = text.replace("\n", " ")
        text = text.lower()
        text = re.sub(r'_*', '', text)

        # get file name
        file_name = i
        text_name = file_name.replace(".txt", "")

        # get year
        text_year = re.match("[\d]{4}", text_name)
        text_year = text_year.group(0)
        # print(text_year)
        # remove year from title
        text_name = re.sub(r'\d*', '', text_name)
        # print(text_name)

        # find number of words
        tokenized_text = word_tokenize(text)
        word_count = len(tokenized_text)

    except:
        print("token and lem failed")
    try:
        # create dictionary will all info
        text_dict = {
            "text_name": text_name,
            "text_year": text_year,
            "text": text,
            "text_word_count": word_count
        }
        # print(text_dict)
    # add dictionary to corpus
    except:
        print("cannot make text dict")

    corpus.append(text_dict)


# Here we can create a smaller sample of texts for debugging

# test_texts = texts[1:5]
# print(test_texts)

# create list of text names
text_names_list = []

# text num is used to track how far we are through the texts
textnum = 0

# loop through the list of texts.
for i in texts:
    try:
        from_codec = get_encoding_type(folder_texts + i)
        file = open((folder_texts + i), "r", encoding=from_codec)
        process_document(file, i)
        print(str(textnum) + " ", end="")
        textnum = textnum + 1
    except Exception as e:
        print(e)

#
# here we create the total count of words in entire corpus, we will used this later to find the overall frequency of a word in the corpus
total_corpus_word_count = 0
for i in range(len(corpus)):
    total_corpus_word_count += corpus[i]['text_word_count']
print(total_corpus_word_count)


print(len(corpus))

dataframe_dict = {}

total_hyp_adjs_list = []

text_list = []

# here we create word list which will be used to calculate percentages.
word_list = []

for i in range(len(corpus)):
    col1 = corpus[i]['text_year'] + " " + corpus[i]['text_name']
    list1 = []
    list1 = re.findall("\w+-\w+", corpus[i]['text'])
    dataframe_dict[col1] = list1

    word_list.append(list1)

    text_list.append(corpus[i]['text_year'] + corpus[i]['text_name'])

    for x in list1:
        if x not in total_hyp_adjs_list:
            if x not in hypadj_stop_words:
                total_hyp_adjs_list.append(x)
                #print(x)
        else:
            # print(x)
            pass

    corpus[i]["word_list"] = list1


all_words_dict = {}
all_words_dict["Words"] = total_hyp_adjs_list
weighted_all_words_dict = {}
weighted_all_words_dict["Words"] = total_hyp_adjs_list
word_percentage_dict = {}
word_percentage_dict["Words"] = total_hyp_adjs_list



for i in dataframe_dict:
    # print(dataframe_dict[i])
    list1 = []
    for x in total_hyp_adjs_list:
        if x in dataframe_dict[i]:
            items = dataframe_dict[i]
            # print(items)
            count = items.count(x)
            # print(count)
            list1.append(count)
        else:
            # print("0")
            list1.append(0)
    # print(len(list))
    all_words_dict[i] = list1
    # weighted_all_words_dict[i] = list1
    word_percentage_dict[i] = list1



# create dictionary of word counts.


for i in range(len(corpus)):
    col = (corpus[i]['text_year'] + corpus[i]['text_name'])
    # print(col2)
    list1 = []
    list_percent = []
    for x in all_words_dict['Words']:
        if x in corpus[i]['word_list']:
            items = corpus[i]['word_list']
            # print(items)
            count = items.count(x)
            # print(count)
            list1.append(count)
            percent = (count / corpus[i]['text_word_count'])
            # print(percent)
            list_percent.append(percent)
            # ok that is not working
        else:
            list1.append(0)
            list_percent.append(0)
    # print(len(list))
    all_words_dict[col] = list1
    word_percentage_dict[col] = list_percent
    text_names_list.append(col)


# created weighted score, we will add this to our dataframe later.

halfway = len(corpus) / 2
print("halfway point: " + str(halfway))
for i in range(len(corpus)):
    col2 = (corpus[i]['text_year'] + corpus[i]['text_name'])
    list2 = []
    for x in weighted_all_words_dict['Words']:
        # print(x)
        if x in corpus[i]['word_list']:
            # weighted scores
            # if the adject appears in the 2nd half of the list of books then the number is positive
            # if it is in the first half of the books then it is negative.
            if i <= halfway:
                weight = ((1 - halfway) + i)
            elif i > halfway:
                weight = i - halfway
            value = (1 * weight)
            # print(value)
            list2.append(value)
        else:
            list2.append(0)
    # print(len(list))
    weighted_all_words_dict[col2] = list2
    # print(weighted_all_words_dict)


# Output dict with frequency counts of all words with weighted score

data2 = pd.DataFrame({key: pd.Series(value) for key, value in weighted_all_words_dict.items()})
data2 = pd.DataFrame(data2)
total_weighted_score = data2.sum(axis=1, numeric_only=True)
# print(total_weighted_score)

total_freq = []


data = pd.DataFrame({key: pd.Series(value) for key, value in all_words_dict.items()})
data1 = pd.DataFrame(data)
data1['row_sum'] = data1.sum(axis=1, numeric_only=True)
total_freq = data1['row_sum']
try:
    data1["total_weighted_score"] = total_weighted_score
    data1 = data1.sort_values(by=['total_weighted_score'], ascending=False)

except:
    pass

# create percentile
data1['percentile_rank'] = data1.total_weighted_score.rank(pct=True)

file_name = folder_dataset + word_type + 's' + '_' + 'weightedscore_freq_' + datetime.now().strftime(
        "%Y%m%d-%H%M%S") + '.xlsx'
try:
    data1.to_excel(file_name, sheet_name='sheet1', index=False)
except:
    print("failed to output")



# output percentage of word usage.

data = pd.DataFrame({key: pd.Series(value) for key, value in word_percentage_dict.items()})
data1 = pd.DataFrame(data)
data1["total_freq"] = total_freq
data1["average_freq"] = (data1["total_freq"] / total_corpus_word_count)
average_freq = data1["average_freq"]

file_name = folder_dataset + word_type + 's' + '_' + 'percentage_' + datetime.now().strftime(
        "%Y%m%d-%H%M%S") + '.xlsx'
data1.to_excel(file_name, sheet_name='sheet1', index=False)
print(file_name)


# target_words_early = percentage_top_words
target_words = ["brain-shattering", "rough-hewn", "lion-like", "glassy-eyed", "blood-lusting", "white-faced",
                "wide-flung", "hawk-like",
                "dark-eyed", "beak-like", "mail-clad", "blankety-blank", "soul-shaking", "blood-thirsty", "wild-eyed",
                "blue-black",
                "broad-shouldered", "white-hot", "blood-curdling", "deep-chested", "bull-like", "black-bearded",
                "white-clad", "blood-red", "hot-headed",
                "panther-like", "wolf-like", "ape-like", "beast-like", "red-stained"]

for x in target_words:
    try:
        output_graph_combinedfreqprop(x, corpus, folder_images, word_percentage_dict, text_names_list, average_freq,
                                      word_type)
    except:
        print("problem with " + str(x))
    pass

