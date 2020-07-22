
from Bootcamp.google_search_project.for_and_if import for_if_if_for, if_for_if_for, if_if_for_for, if_if_if_for
from Bootcamp.google_search_project.idx_to_text import final_results_by_idx
from Bootcamp.google_search_project.two_char import match_2_char


def match_3_char(user_text):
    res = [[x, 0] for x in if_if_if_for(user_text[0], user_text[1], user_text[2])]
    if len(res) >= 5:
        return final_results_by_idx(res, user_text)
    res += [[x, 3] for x in if_if_for_for(user_text[0], user_text[1])]
    if len(res) >= 5:
        return final_results_by_idx(res, user_text)

    res += [[x[0], 4] for x in if_for_if_for(user_text[0], user_text[2])]
    if len(res) >= 5:
        return final_results_by_idx(res, user_text)
    res += [[x, 4] for x in for_if_if_for(user_text[1], user_text[2])]

    if len(res) >= 5:
        return final_results_by_idx(res, user_text)

    res += [[x[0], 10] for x in match_2_char(user_text[1:]) if x[1] == 0]
    return final_results_by_idx(res, user_text)