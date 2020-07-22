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


def is_seq_in_trie(chr1, chr2, chr3, chr4, trie_data):
    if chr1 in trie_data:
        if chr2 in trie_data[chr1]:
            if chr3 in trie_data[chr1][chr2]:
                if chr4 in trie_data[chr1][chr2][chr3]:
                    return trie_data[chr1][chr2][chr3][chr4]
                else: return []
            else:
                return []
        else:
            return []
    else:
        return []


def replace_first_char(user_text, char):
    idx_list = []
    for char in user_text:
        idx_list += is_seq_in_trie(user_text[0], user_text[1], char, user_text[3], trie_data):
        if len(idx_list) >= 5:
            return idx_list


def replace_second_char(user_text):
    if user_text[0] in trie_data:
        idx_list = []
        for char in trie_data[user_text[0]]:
            idx_list += is_seq_in_trie(user_text[0], user_text[1], char, user_text[3], trie_data):
            if len(idx_list) >= 5:
                return idx_list


def replace_third_char(user_text):
    if user_text[0] in trie_data:
        if user_text[1] in trie_data[user_text[0]]:
            idx_list = []
            for char in trie_data[user_text[0]][user_text[1]]:
                idx_list += is_seq_in_trie(user_text[0], user_text[1], char, user_text[3], trie_data):
                if len(idx_list) >= 5:
                    return idx_list


def replace_fourth_char(user_text):
    if user_text[0] in trie_data:
        if user_text[1] in trie_data[user_text[0]]:
            if user_text[2] in trie_data[user_text[0]][user_text[1]]:
                idx_list = []
                for char in trie_data[user_text[0]][user_text[1]][user_text[2]]:
                    idx_list += is_seq_in_trie(user_text[0], user_text[1], char, user_text[3], trie_data):
                    if len(idx_list) >= 5:
                        return idx_list


def replace_char(user_text):
    idx_list = replace_fourth_char(user_text)
    


def sub_str(user_text, trie_data):
    return is_seq_in_trie(user_text[0], user_text[1], user_text[2], user_text[3], trie_data)




def fix_user_text(user_text, src_text):
    text = re.sub('([,.\t])+', ' ', user_text)
    text = re.sub(' +', ' ', text)
    print(text)


def add_char():
    pass
