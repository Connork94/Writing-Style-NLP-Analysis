# !/usr/bin/env python
# coding: utf-8

'''
Modules to install
nltk
pandas
numpy
chardet
matplotlib
'''

# Import custom functions file
from NLPfunctions import get_encoding_type
from NLPfunctions import process_document
from NLPfunctions import output_graph_combinedfreqprop

# import libraries
import os
import nltk

nltk.download('omw-1.4')
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
from datetime import datetime
from chardet import detect
import matplotlib as mpl
import matplotlib.pyplot as plt
import pickle

#############################################################
### import stopwords and punctuation for later use ##########
#############################################################

from nltk.corpus import stopwords

stop_words_general = list(stopwords.words('english'))
from string import punctuation

punctuation = list(punctuation)
# import custom stop words list
from Stopwords import stop_words, adj_stop_words, hypadj_stop_words, blank_stop_words

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


# POS (Position of Speech) codes for filtering
list_of_codes_adj = ["JJ", "JJS", "JJR"]
list_of_codes_vrb = ["VB","VBD","VBG","VBN","VBP","VBZ"]
list_of_codes_noun = ["NN","NNS","NNP","NNPS"]

# get a list of all the files in the directory, we will use this to iterate over the texts
texts = os.listdir(folder_texts)

target_words_adj = ["awful", "pale", "supple", "dynamic", "terrific", "mighty", "foul", "red", "white", "black",
                    "crimson", "pantherish", "wolfish", "incredible", "fearful", "such", "crafty", "foolish", "scant", "fierce",
                    "horrid", "tall", "convulsive", "hot", "frantic", "big", "rigid", "hostile", "livid", "appal", "murderous",
                    "primitive", "yore", "crazy", "dark", "dead", "wild", "strange", "mad", "grim", "terrible", "white-faced"]

target_words_verb = ["fling","gaze","ask","hack","shrug","fade","answer","count","clinch","slay",
                     "shrink","slug","ruminate","writhe","haunt",
                     "demand","pull","pant","assure","grab","glimpse","shriek","stumble","howl"]

target_words_noun = ["nobody","somebody","anybody","stranger","sea","ship","pistol","sheriff","boot",
                     "saddle","ocean","fighter","round","cheek","punch","referee","uppercut","glove",
                     "coast","wharf","tide","wheel","dust"]


def analysis(word_type, list_of_codes, stop_words, target_words, folder_texts, folder_images):
    # create list that will hold corpus
    corpus = []

    # create list of text names
    text_names_list = []

    # text num is used to track how far we are through the texts
    textnum = 0

    # Here we can create a smaller sample of texts for quickly debugging the code
    test_texts = texts[1:15]

    print("Text processing count:")

    # loop through the list of texts.
    for i in texts:
        try:
            from_codec = get_encoding_type(folder_texts + i)
            file = open((folder_texts + i), "r", encoding=from_codec)
            corpus.append(process_document(file, i, list_of_codes, stop_words))
            print(str(textnum) + " ", end="")
            textnum = textnum + 1
        except Exception as e:
            print(e)

    # here we create the total count of words in entire corpus, we will used this later to find the overall frequency of a word in the corpus
    total_corpus_word_count = 0
    for i in range(len(corpus)):
        total_corpus_word_count += corpus[i]['text_word_count']

    print("")
    print("Total corpus word count:")
    print(total_corpus_word_count)

    print("Corpus length:")
    print(len(corpus))

    # here we create a dictionary that we will turn into a Pandas dataframe later
    dataframe_dict = {}

    for i in range(len(corpus)):
        col1 = corpus[i]['text_year'] + corpus[i]['text_name'] + '_word'
        col2 = corpus[i]['text_year'] + corpus[i]['text_name'] + '_word_count'
        list1 = []
        for x in corpus[i]['common_word_list_count']:
            list1.append(x[0])
        list2 = []
        for x in corpus[i]['common_word_list_count']:
            list2.append(x[1])
        dataframe_dict[col1] = list1
        dataframe_dict[col2] = list2

    # create dictinaries for output dataframes
    # three dicts: counts of words, weighted scores (which are combined with count of words dictionary), and percentage of text
    all_words_dict = {}
    weighted_all_words_dict = {}
    word_percentage_dict = {}
    list1 = []

    # Create list of all adj, if adj already in list then do not add it
    for i in range(len(corpus)):
        col1 = 'Words'
        for x in corpus[i]['word_list']:
            if x not in list1:
                list1.append(x)
            else:
                pass

        all_words_dict[col1] = list1
        weighted_all_words_dict[col1] = list1
        word_percentage_dict[col1] = list1

    print("Word list length:")
    print(len(all_words_dict['Words']))

    # create dictionary of word counts.
    for i in range(len(corpus)):
        col = (corpus[i]['text_year'] + corpus[i]['text_name'])
        list1 = []
        list_percent = []
        for x in all_words_dict['Words']:
            if x in corpus[i]['word_list']:
                items = corpus[i]['word_list']
                count = items.count(x)
                list1.append(count)
                percent = (count / corpus[i]['text_word_count'])
                list_percent.append(percent)
            else:
                list1.append(0)
                list_percent.append(0)
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
            if x in corpus[i]['word_list']:
                # weighted scores
                # if the adject appears in the 2nd half of the list of books then the number is positive
                # if it is in the first half of the books then it is negative.
                if i <= halfway:
                    weight = ((0 - halfway) + i)
                elif i > halfway:
                    weight = i - halfway
                value = (1 * weight)
                list2.append(value)
            else:
                list2.append(0)
        weighted_all_words_dict[col2] = list2

    # Output dict with frequency counts of all words with weighted score
    data2 = pd.DataFrame({key: pd.Series(value) for key, value in weighted_all_words_dict.items()})
    data2 = pd.DataFrame(data2)
    total_weighted_score = data2.sum(axis=1, numeric_only=True)

    total_freq = []

    data = pd.DataFrame({key: pd.Series(value) for key, value in all_words_dict.items()})
    data1 = pd.DataFrame(data)
    data1['row_sum'] = data1.sum(axis=1, numeric_only=True)
    total_freq = data1['row_sum']

    data1["total_weighted_score"] = total_weighted_score
    data1 = data1.sort_values(by=['total_weighted_score'], ascending=False)
    percentage_top_words = data1.Words.head(11)
    percentage_top_words = percentage_top_words.values.tolist()
    percentage_bottom_words = data1.Words.tail(11)
    percentage_bottom_words = percentage_bottom_words.values.tolist()

    # create percentile
    data1['percentile_rank'] = data1.total_weighted_score.rank(pct=True)

    file_name = folder_dataset + word_type + 's' + '_' + 'weightedscore_freq_' + datetime.now().strftime(
        "%Y%m%d-%H%M%S") + '.xlsx'
    data1.to_excel(file_name, sheet_name='sheet1', index=False)

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

    for x in target_words:
        try:
            output_graph_combinedfreqprop(x, corpus, folder_images, word_percentage_dict, text_names_list, average_freq,
                                          word_type)
        except:
            print("problem with " + str(x))
        pass

# run the analysis with adjs, verbs, and nouns
analysis("ADJ", list_of_codes_adj, adj_stop_words, target_words_adj, folder_texts, folder_images)
analysis("NOUN", list_of_codes_noun, stop_words, target_words_noun, folder_texts, folder_images)
analysis("VERB", list_of_codes_vrb, stop_words, target_words_verb, folder_texts, folder_images)