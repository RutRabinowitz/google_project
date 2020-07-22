from Bootcamp.google_search_project.complete import AutoCompleteData, get_offset
from Bootcamp.google_search_project.repalce_char import replace_fourth_char, replace_third_char, replace_second_char, \
    replace_first_char

import json


def add_char_1(user_text):
    idx_list = []
    res = []
    idx_list += replace_fourth_char(user_text)
    with open('sentences.json', 'r') as sentences_file:
        sentences = json.load(sentences_file)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if user_text[:3] + idx[2] + user_text[3] in sentence:
                res.append(AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 4))
    idx_list = replace_third_char(user_text)
    with open('sentences.json', 'r') as sentences_file:
        sentences = json.load(sentences_file)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if user_text[:2] + idx[2] + user_text[2:] in sentence:
                res.append(AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 6))

    idx_list = replace_second_char(user_text)
    with open('sentences.json', 'r') as sentences_file:
        sentences = json.load(sentences_file)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if user_text[:1] + idx[2] + user_text[1:] in sentence:
                res.append(
                    AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 8))

    idx_list = replace_first_char(user_text)
    with open('sentences.json', 'r') as sentences_file:
        sentences = json.load(sentences_file)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if idx[2] + user_text in sentence:
                res.append(AutoCompleteData(sentence, sentence, get_offset(user_text, sentence), len(user_text) * 2 - 10))

    if len(res) > 5:
        return sorted(res, key=lambda x: (x.score, x.sentence), reverse=True)[:5]
    return sorted(res, key=lambda x: (x.score, x.sentence), reverse=True)