from Bootcamp.google_search_project.for_and_if import trie_data
from Bootcamp.google_search_project.idx_to_text import final_results_by_idx
from Bootcamp.google_search_project.repalce_char import replace_char, is_seq_in_trie
from Bootcamp.google_search_project.three_char import match_3_char


def complete_match(user_text):
    res_list = []
    idx_list = is_seq_in_trie(user_text[0], user_text[1], user_text[2], user_text[3], trie_data)
    if idx_list:
        for idx in idx_list:
            res_list.append([idx, 0])

    return res_list


def remove_char(user_text):
    score = 0
    for i in user_text[::-1]:
        removed = user_text.replace(i, "")
        res = [[x[0], score + 2] for x in match_3_char(removed) if x.score == 6]
        score = score + 1
    return res


def match_4_char(user_text):
    idx_list = complete_match(user_text)
    if len(idx_list) >= 5:
        return final_results_by_idx(idx_list[:5], user_text)

    idx_list += replace_char(user_text, trie_data)
    # idx_list += remove_char(user_text, trie_data)
    if len(idx_list) >= 5:
        return final_results_by_idx(idx_list, user_text)

    # idx_list += add_char_1(user_text)
    return final_results_by_idx(idx_list, user_text)
