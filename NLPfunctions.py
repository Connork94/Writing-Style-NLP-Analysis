## get parts of speech

import nltk
from nltk.corpus import wordnet
from collections import Counter

# This function finds and returns the most likely part of speech for a particular word
def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synsets(word)

    pos_counts = Counter()
    pos_counts["n"] = len([item for item in probable_part_of_speech if item.pos() == "n"])
    pos_counts["v"] = len([item for item in probable_part_of_speech if item.pos() == "v"])
    pos_counts["a"] = len([item for item in probable_part_of_speech if item.pos() == "a"])
    pos_counts["r"] = len([item for item in probable_part_of_speech if item.pos() == "r"])

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    return most_likely_part_of_speech


## tokenize and lemmatize

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def tokenize_lemmatize_word(text):
    lemmatizer = WordNetLemmatizer()
    tokenized_string = word_tokenize(text)
    lemmatized_pos = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized_string]
    return lemmatized_pos


from chardet import detect


# finds and returns the type of encoding of a text file
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']


import re


# function to process documents
def process_document(document, i, list_of_codes, stop_words):
    # load document and remove unwanted characters
    text = document.read()
    text = text.replace("\n", " ")
    text = text.replace("—", " ")
    text = text.replace(".", " ")
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

    # Tokenize text
    # find number of words
    tokenized_text = word_tokenize(text)
    # print(tokenized_text)
    word_count = len(tokenized_text)
    total_corpus_word_count = word_count

    # create dictionary which will hold all info
    text_dict = {
        "text_name": text_name,
        "text_year": text_year,
        "text": text,
        "text_word_count": word_count
    }

    # Lemmatize words
    lemmatized_words = tokenize_lemmatize_word(text)
    # POS tag words
    pos_tags_new = nltk.pos_tag(lemmatized_words)

    word_list = []



    # Here we can change the types of words we are looking for...
    for token in pos_tags_new:
        if token[1] in list_of_codes:
            if token[0] not in stop_words:
                # print(token[0])
                word_list.append(token[0])
    # add common adjectives to dictionary
    text_dict["word_list"] = word_list

    # Create bag of words
    bag_of_words = Counter(word_list)
    bag_of_words = bag_of_words.most_common()
    bag_of_words_common = []
    for word in bag_of_words:
        if word[1] > 1:
            bag_of_words_common.append(word)

    # add common adjectives with counts to dictionary
    text_dict["common_word_list_count"] = bag_of_words_common

    # remove complete text. We do not need this data in the dict any more
    try:
        text_dict.pop("text")
    except:
        print('text already popped')
    return(text_dict)

import matplotlib as mpl
import matplotlib.pyplot as plt

# create a function to output matplotlib frequency chart of a specific word
def output_graph_combinedfreqprop(word, corpus, folder_images, word_percentage_dict, text_names_list, average_freq, word_type):
    # plot freq line
    x_axis = []
    y_axis = []
    list1 = []
    for i in range(len(corpus)):
        name = (corpus[i]['text_year'] + " " + corpus[i]['text_name'])
        x_axis.append(name)
        if word in corpus[i]['word_list']:
            items = corpus[i]['word_list']
            # print(items)
            count = items.count(word)
            # print(count)
            list1.append(count)
        else:
            list1.append(0)
        # print(len(list))
        y_axis = list1

    # create vars for percentage line
    y_axis2 = []
    list2 = []
    ref_line = []
    for i in range(len(word_percentage_dict['Words'])):
        if word_percentage_dict['Words'][i] == word:
            for x in text_names_list:
                y_axis2.append((word_percentage_dict[x][i] * 100))
                ref_line.append((average_freq[i] * 100))

    fig, ax1 = plt.subplots()
    # f = plt.figure()
    fig.set_figwidth(30)
    fig.set_figheight(5)

    ax1.set_xlabel('Texts')
    ax1.set_ylabel('Frequency', color='royalblue')
    plot_1 = ax1.plot(x_axis, y_axis, marker='o', color='royalblue', label="Absolute Frequency")
    ax1.tick_params(axis='y', labelcolor='royalblue')
    # ax1.xlim([-2,len(x_axis)+2])
    # ax1.xticks(rotation=90)

    # plt.plot(x_axis, y_axis, marker='o', label = "Frequency")
    plt.xlim([-2, len(x_axis) + 2])
    plt.xticks(rotation=90)

    # change font sizes
    plt.rc('axes', labelsize=15)
    plt.rc('axes', titlesize=20)

    ax2 = ax1.twinx()

    ax2.set_ylabel('Percentage %', color='orangered')
    plot_2 = ax2.plot(x_axis, y_axis2, marker='x', color='orangered', label="Relative Frequency")
    ax2.tick_params(axis='y', labelcolor='orangered')

    # plot percentage line
    # plt.plot(x_axis, y_axis2, marker='x')
    # plt.plot(x_axis, ref_line, 'k-', lw=1,dashes=[2, 2], label = "Average Percentage")
    plot_3 = ax2.plot(x_axis, ref_line, 'k-', lw=1, dashes=[2, 2], label="Relative Frequency for Entire Corpus")
    title = "Useage of the word " + "'" + word + "' in each story over time"
    plt.title(title)

    lns = plot_1 + plot_2 + plot_3
    labels = [l.get_label() for l in lns]
    plt.legend(lns, labels, loc=0)

    # plt.show()
    file_name = folder_images + word_type + "_" + word + "_frequency_percentage" + ".png"
    plt.savefig(file_name, bbox_inches='tight', dpi=100)
    print(word + " frequency chart exported")
    plt.close()

