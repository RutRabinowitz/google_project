import re
import json
from Bootcamp.google_search_project.four_char import match_4_char
from Bootcamp.google_search_project.idx_to_text import final_results_by_idx
from Bootcamp.google_search_project.one_char import match_one_char
from Bootcamp.google_search_project.three_char import match_3_char
from Bootcamp.google_search_project.two_char import match_2_char

trie_file = open('trie_data.json', 'r')
trie_data = json.load(trie_file)


def fix_user_text(user_text):
    text = re.sub('([,.\t])+', ' ', user_text)
    text = re.sub(' +', ' ', text)
    return text


def match(user_text):
    func_list = [match_one_char, match_2_char, match_3_char, match_4_char]
    if len(user_text) <= 4:
        return final_results_by_idx((func_list[len(user_text) - 1](user_text)), user_text)

    return []


def print_results(auto_complete_data_list):
    for num, i in enumerate(auto_complete_data_list):
        print(f'{num + 1}: {i.completed_sentence}      {i.score}       {i.offset}')


def get_user_text():
    user_text = ""
    print("Google 🔎")
    while True:
        print(user_text, end="")
        user_text += input()

        if user_text[-1] == "#":
            return
        results = match(fix_user_text(user_text))
        print_results(results)


get_user_text()
