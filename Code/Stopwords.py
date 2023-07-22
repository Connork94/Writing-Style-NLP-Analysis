

stop_words = ["git","purty","perned","pecooliar","sech","yo","ho",
              "takin","nothin","lookin","thirty","heading","fifty",
              "n","derned","gal","gong","steve","s","uh", "don", "e."] +\
             ["steve","king","kane","]","eh","'re","'m",
             "'ve","hell","shet","elkins","cai","ast","riz","gim","'s","ai","git","conan",
              "“","’","”","—","u","s","o'donnell","kinda"] +\
            ["gorm","hybori","alsir","achaian","u","el","gordon","dern","ali","shin",
             "san","amalric","john","godric","laramie","al","mr.","afdal","shah","nay",
             "ye","willoughby","joel","etienne","gomez","tom","harrison","cormac","alafdal",
            "oh","von","sir","xaltotun","adam","abd","kull","ju-ju","fist","yar","dick","khosatral",
            "natala","mitra","saul","esau","leg","foot","—","cousin","pal","jim",
            "thou","afzal","ak","ta","kerim","ga-nor","e-book","allah","joe","suleiman",
            "pyrrhas","n'longa","di"] +\
            ["t'other", "t'other'n","t'other'in","el","ali","us—","jim","'em","i—i","till","agen","bein","gordon",
             "yar","'n","v","‘"] +\
            ["rid","jest","goin","headin","ten","sorry",]

# stop words specific to non-noun analysis
# this functions by created lists of stop words for use except in the analyses which they are relevant.
non_noun_stop_words = ["ear", "ruffian","bar-keep","saddle-bags","sword",".45","cap'n","saddle","whiskey",
                       "hatred","corral"]

non_adj_stop_words = ["damned","everlasting"]

non_vrb_stop_words = ["shoot","survive"]


adj_stop_words = stop_words + non_noun_stop_words + non_vrb_stop_words
noun_stop_words = stop_words + non_adj_stop_words + non_vrb_stop_words
verb_stop_words = stop_words + non_adj_stop_words + non_noun_stop_words

hypadj_stop_words = ["six-shooter","six-shooters",
             "gun-belt","war-dance","war-party","hand-to","all-fours","hoss-thief","twenty-one","a-purpose",
             "seventy-five","breech-clout"]


blank_stop_words = []