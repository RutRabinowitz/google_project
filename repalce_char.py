import json


def is_seq_in_trie(chr1, chr2, chr3, chr4, trie_data):
    if chr1 in trie_data:
        if chr2 in trie_data[chr1]:
            if chr3 in trie_data[chr1][chr2]:
                if chr4 in trie_data[chr1][chr2][chr3]:
                    return trie_data[chr1][chr2][chr3][chr4]
                else:
                    return []
            else:
                return []
        else:
            return []
    else:
        return []


def replace_first_char(user_text, trie_data):
    idx_list = []
    for char in user_text:
        idx_list += [[x, 5, char, 0] for x in is_seq_in_trie(user_text[0], user_text[1], char, user_text[3], trie_data)]

        if len(idx_list) >= 5:
            break

    return idx_list


def replace_second_char(user_text, trie_data):
    idx_list = []
    if user_text[0] in trie_data:
        for char in trie_data[user_text[0]]:
            idx_list += [[x, 4, char, 1] for x in
                         is_seq_in_trie(user_text[0], user_text[1], char, user_text[3], trie_data)]

            if len(idx_list) >= 5:
                break

    return idx_list


def replace_third_char(user_text, trie_data):
    idx_list = []
    if user_text[0] in trie_data:
        if user_text[1] in trie_data[user_text[0]]:
            for char in trie_data[user_text[0]][user_text[1]]:
                if user_text[3] in trie_data[user_text[0]][user_text[1]][char]:
                    idx_list += [[x, 3, char, 2] for x in
                                 is_seq_in_trie(user_text[0], user_text[1], char, user_text[3], trie_data)]

                if len(idx_list) >= 5:
                    break
    return idx_list


def replace_fourth_char(user_text, trie_data):
    idx_list = []
    if user_text[0] in trie_data:
        if user_text[1] in trie_data[user_text[0]]:
            if user_text[2] in trie_data[user_text[0]][user_text[1]]:
                for char in trie_data[user_text[0]][user_text[1]][user_text[2]]:
                    idx_list += [[x, 4, char, 3] for x in
                                 is_seq_in_trie(user_text[0], user_text[1], user_text[2], char, trie_data)]
                    if len(idx_list) >= 5:
                        break

    return idx_list


def replace_char(user_text, trie_data):
    idx_list = []
    idx_list += replace_fourth_char(user_text, trie_data)
    idx_list += [x for x in replace_third_char(user_text, trie_data) if x[0] not in [y[0] for y in idx_list]]
    if len(idx_list) >= 5:
        return idx_list

    idx_list += [x for x in replace_second_char(user_text, trie_data) if x[0] not in [y[0] for y in idx_list]]
    if len(idx_list) >= 5:
        return idx_list

    idx_list += [x for x in replace_first_char(user_text, trie_data) if x[0] not in [y[0] for y in idx_list]]
    return idx_list
