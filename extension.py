from Bootcamp.google_search_project.four_char import complete_match, match_4_char


def gt_4(user_text):
    idx_list1 = []
    idx_list2 = []
    idx_list1 = complete_match(user_text[:4])
    idx_list2 = complete_match(user_text[1:])

    idx_list2 = [x for x in idx_list2 if x in idx_list1]
    if len(idx_list2) <= 5:
        idx_list1 = match_4_char(user_text[1:])
        idx_list2 = [x for x in idx_list1 if x in idx_list2]
    return idx_list2
