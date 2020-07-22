import re
import json
import os

from Bootcamp.google_search_project.for_and_if import if_for_for_for, if_if_for_for, for_if_for_for, for_if_if_for, \
    if_for_if_for, if_if_if_for, is_seq_in_trie
from Bootcamp.google_search_project.repalce_char import replace_char, replace_fourth_char, replace_first_char, \
    replace_second_char, replace_third_char


def add_char_1(user_text):
    with open('sentences.json', 'r') as sentences_file:
        sentences = json.load(sentences_file)
        idx_list = []
        res = []
        idx_list += replace_fourth_char(user_text, trie_data)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if user_text[:3] + idx[2] + user_text[3] in sentence:
                # res.append(
                #     AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 6))
                res += [idx, 2]
        idx_list = replace_third_char(user_text, trie_data)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if user_text[:2] + idx[2] + user_text[2:] in sentence:
                # res.append(
                #     AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 6))
                res += [idx, 4]
        idx_list = replace_second_char(user_text, trie_data)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if user_text[:1] + idx[2] + user_text[1:] in sentence:
                # res.append(
                #     AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 6))
                res += [idx, 6]

        idx_list = replace_first_char(user_text, trie_data)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if idx[2] + user_text in sentence:
                # res.append(
                #     AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 6))
                res += [idx, 8]
        print(res)
        return res
        # if len(res) > 5:
        #     return sorted(res, key=lambda x: (x.score, x.sentence), reverse=True)[:5]
        # return sorted(res, key=lambda x: (x.score, x.sentence), reverse=True)


class AutoCompleteData:
    def __init__(self, cmpleted_sentence, src_text, offs, scores):
        self.completed_sentence = cmpleted_sentence
        self.source_text = src_text
        self.offset = offs
        self.score = scores


# with open('trie_data.json', 'r') as trie_data:
#     trie_data = json.load(trie_data)

trie_file = open('trie_data.json', 'r')
trie_data = json.load(trie_file)





def complete_match(user_text, trie_data):
    res_list = []
    idx_list = is_seq_in_trie(user_text[0], user_text[1], user_text[2], user_text[3])
    if idx_list:
        for idx in idx_list:
            res_list.append([idx, 0])

    return res_list


def fix_user_text(user_text):
    text = re.sub('([,.\t])+', ' ', user_text)
    text = re.sub(' +', ' ', text)
    return text


def get_offset(user_text, sentence):
    for i in range(len(sentence) - len(user_text)):
        if user_text == fix_user_text(sentence[i::i + len(user_text)]):
            return i


def is_one_correct(user_text, sentence):
    boolean = True
    for x, y in zip(user_text, sentence):
        if x != y:
            if not boolean:
                return False
            else:
                boolean = False
    return True


def f1(list, user_text):
    res = []
    with open('sentences.json', 'r') as sentences_file:
        sentences = json.load(sentences_file)
        for idx in list:
            sentence = sentences[str(idx[0])]
            res.append(AutoCompleteData(sentence, sentence, (sentence.lower()).find(user_text), len(user_text) * 2))
    return res


def f(list_, user_text):
    res = f1(list_, user_text)
    if len(res) > 5:
        return sorted(res, key=lambda x: (x.score, x.completed_sentence), reverse=True)[:5]
    return sorted(res, key=lambda x: (x.score, x.completed_sentence), reverse=True)


def match_3_char(user_text):
    res = [[x, 0] for x in if_if_if_for(user_text[0], user_text[1], user_text[2])]
    if len(res) >= 5:
        return f(res, user_text)
    res += [[x, 3] for x in if_if_for_for(user_text[0], user_text[1])]
    if len(res) >= 5:
        return f(res, user_text)

    res += [[x[0], 4] for x in if_for_if_for(user_text[0], user_text[2])]
    if len(res) >= 5:
        return f(res, user_text)
    res += [[x, 4] for x in for_if_if_for(user_text[1], user_text[2])]

    if len(res) >= 5:
        return f(res, user_text)

    res += [[x[0], 10] for x in match_2_char(user_text[1:]) if x[1] == 0]
    return f(res, user_text)


def match_one_char(char):
    res = [[x, 0] for x in if_for_for_for(char)]
    return f(res, char)


def match_2_char(user_text):
    res = [[x, 0] for x in if_if_for_for(user_text[0], user_text[1])]
    if len(res) >= 5:
        return f(res, user_text)
    else:
        res += [[x, 8] for x in match_one_char(user_text[0])]
    if len(res) >= 5:
        return f(res, user_text)
    else:
        res += [[x, 5] for x in for_if_for_for(user_text[1])]
    return f(res, user_text)


def remove_char(user_text, trie_data):
    score = 0
    for i in user_text[::-1]:
        removed = user_text.replace(i, "")
        res = [[x[0], score + 2] for x in match_3_char(removed) if x.score == 6]
        score = score + 1
    return res


def match_4_char(user_text):
    list_ = complete_match(user_text, trie_data)
    if len(list_) >= 5:
        return f(list_[:5], user_text)

    list_ += replace_char(user_text, trie_data)
    # list_ += remove_char(user_text, trie_data)
    # print(list_)
    #     # print(list(set(list_)))
    #     # list_ = list(set(list_))
    if len(list_) >= 5:
        return f(list_, user_text)

    # list_ += add_char_1(user_text)
    return f(list_, user_text)


def get_user_text(trie_data):
    user_text = ""
    print("Please enter your text: ")
    while 1:
        print(user_text, end="")
        user_text += input()
        if user_text[-1] == "#":
            return
        user_text = fix_user_text(user_text)

        if len(user_text) == 4:
            # func, *params = "match_" + str(len(user_text)) + "_char user_text, trie_data".split()
            # locals()[func](*params)
            list_ = match_4_char(user_text)
            for num, i in enumerate(list_):
                print(f'{num + 1}: {i.completed_sentence}')

        elif len(user_text) == 3:
            list_ = match_3_char(user_text)
            for num, i in enumerate(list_):
                print(f'{num + 1}: {i.completed_sentence}')

        elif len(user_text) == 2:
            list_ = match_2_char(user_text)
            for num, i in enumerate(list_):
                print(f'{num + 1}: {i.completed_sentence}')

        elif len(user_text) == 1:
            list_ = match_one_char(user_text)
            for num, i in enumerate(list_):
                print(f'{num + 1}: {i.completed_sentence}')


get_user_text(trie_data)
