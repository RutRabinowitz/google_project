
from Bootcamp.google_search_project.for_and_if import if_if_for_for, for_if_for_for
from Bootcamp.google_search_project.idx_to_text import final_results_by_idx
from Bootcamp.google_search_project.one_char import match_one_char


def match_2_char(user_text):
    res = [[x, 0] for x in if_if_for_for(user_text[0], user_text[1])]
    if len(res) >= 5:
        return final_results_by_idx(res, user_text)
    else:
        res += [[x, 8] for x in match_one_char(user_text[0])]
    if len(res) >= 5:
        return final_results_by_idx(res, user_text)
    else:
        res += [[x, 5] for x in for_if_for_for(user_text[1])]
    return final_results_by_idx(res, user_text)