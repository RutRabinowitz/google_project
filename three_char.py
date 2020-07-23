import itertools

from Bootcamp.google_search_project.for_and_if import for_if_if_for, if_for_if_for, if_if_for_for, if_if_if_for
from Bootcamp.google_search_project.two_char import match_2_char


def remove_duplicates(idx_list):
    idx_list.sort()
    return list(idx for idx, _ in itertools.groupby(idx_list))


def match(func, score, char1, char2):
    return [[x, score] for x in func(char1, char2)]


def match_3_char(user_text):
    func_list = [[if_if_for_for, 3, user_text[0], user_text[1]], [if_for_if_for, 4, user_text[0], user_text[2]],
                 [for_if_if_for, 4, user_text[1], user_text[2]]]
    idx_list = [[x, 0] for x in if_if_if_for(user_text[0], user_text[1], user_text[2])]

    if len(idx_list) >= 5:
        return idx_list
    for func in func_list:
        idx_list += match(func[0], func[1], func[2], func[3])
        if len(idx_list) >= 5:
            return idx_list

    idx_list += [[x[0], 10] for x in match_2_char(user_text[1:]) if x[1] == 0]
    return idx_list
