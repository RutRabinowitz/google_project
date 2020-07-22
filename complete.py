import re
import json


class AutoCompletetrie_data:
    def __init__(self, cmpleted_sentence, src_text, offs, scores):
        completed_sentence = cmpleted_sentence
        source_text = src_text
        offset = offs
        score = scores


i = 0

trie_data = {}


user_trie_data = "aargo"
counter = 0


def replace_first_char(user_text):



def replace_char(word_len_5):
    counter = 0
    for i in abc:
        # trie_data[i][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]]
        print(trie_data[i][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]])
        print(i + user_trie_data[1] + user_trie_data[2] + user_trie_data[3] + user_trie_data[4])
        counter = counter + 1

    for i in abc:
        # trie_data[i][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]]
        print(trie_data[user_trie_data[0]][i][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]])
        print(user_trie_data[0] + i + user_trie_data[2] + user_trie_data[3] + user_trie_data[4])
        counter = counter + 1

    for i in abc:
        # trie_data[i][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]]
        print(trie_data[user_trie_data[0]][user_trie_data[1]][i][user_trie_data[4]])
        print(user_trie_data[0] + user_trie_data[1] + i + user_trie_data[3] + user_trie_data[4])
        counter = counter + 1

    for i in abc:
        # trie_data[i][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]]
        print(trie_data[user_trie_data[0]][user_trie_data[1]][user_trie_data[2]][i][user_trie_data[4]])
        print(user_trie_data[0] + user_trie_data[1] + user_trie_data[2] + i + user_trie_data[4])
        counter = counter + 1

    for i in abc:
        # trie_data[i][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]]
        print(trie_data[user_trie_data[0]][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][i])
        print(user_trie_data[0] + user_trie_data[1] + user_trie_data[2] + user_trie_data[3] + i)
        counter = counter + 1


def sub_str(user_trie_data):
    res = []
    for i in trie_data:
        if user_trie_data == i[user_trie_data[0]][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][
            user_trie_data[4]]:
            res.append(i[user_trie_data[0]][user_trie_data[1]][user_trie_data[2]][user_trie_data[3]][user_trie_data[4]])

    return res


def fix_user_text(user_text, src_text):
    text = re.sub('([,.\t])+', ' ', user_text)
    text = re.sub(' +', ' ', text)
    print(text)


def add_char():
    pass
