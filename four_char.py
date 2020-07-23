from Bootcamp.google_search_project.add_char import add_char_1
from Bootcamp.google_search_project.for_and_if import trie_data
from Bootcamp.google_search_project.repalce_char import replace_char, is_seq_in_trie
from Bootcamp.google_search_project.three_char import match_3_char


def complete_match(user_text):
    res_list = [[x, 0] for x in is_seq_in_trie(user_text[0], user_text[1], user_text[2], user_text[3], trie_data)]
    return res_list


def remove_char(user_text):
    score = 0
    for i in user_text[::-1]:
        removed = user_text.replace(i, "")
        res = [[x[0], score + 2] for x in match_3_char(removed) if x[1] == 6]
        score = score + 1
    return res


def match_4_char(user_text):
    idx_list = complete_match(user_text)

    if len(idx_list) >= 5:
        return idx_list

    idx_list += [x for x in replace_char(user_text, trie_data) if x[0] not in [y[0] for y in idx_list]]

    if len(idx_list) >= 5:
        return idx_list

    idx_list += [x for x in add_char_1(user_text) if x[0] not in [y[0] for y in idx_list]]

    return idx_list
