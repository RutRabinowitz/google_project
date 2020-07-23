import json

with open('trie_data.json', 'r') as trie_data:
    trie_data = json.load(trie_data)


def is_seq_in_trie(chr1, chr2, chr3, chr4):
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


def for_for_for_for():
    res = []
    for chr1 in trie_data:
        for chr2 in trie_data[chr1]:
            for chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def for_for_for_if(chr4):
    res = []
    for chr1 in trie_data:
        for chr2 in trie_data[chr1]:
            for chr3 in trie_data[chr1][chr2]:
                if chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def for_for_if_for(chr3):
    res = []
    for chr1 in trie_data:
        for chr2 in trie_data[chr1]:
            if chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def for_if_for_for(chr2):
    res = []
    for chr1 in trie_data:
        if chr2 in trie_data[chr1]:
            for chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def if_for_for_for(chr1):
    res = []
    if chr1 in trie_data:
        for chr2 in trie_data[chr1]:
            for chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def if_if_for_for(chr1, chr2):
    res = []
    if chr1 in trie_data:
        if chr2 in trie_data[chr1]:
            for chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def if_for_if_for(chr1, chr3):
    res = []
    if chr1 in trie_data:
        for chr2 in trie_data[chr1]:
            if chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def for_if_if_for(chr2, chr3):
    res = []
    for chr1 in trie_data:
        if chr2 in trie_data[chr1]:
            if chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def if_if_if_for(chr1, chr2, chr3):
    res = []
    if chr1 in trie_data:
        if chr2 in trie_data[chr1]:
            if chr3 in trie_data[chr1][chr2]:
                for chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res


def if_if_for_if(chr1, chr2, chr4):
    res = []
    if chr1 in trie_data:
        if chr2 in trie_data[chr1]:
            for chr3 in trie_data[chr1][chr2]:
                if chr4 in trie_data[chr1][chr2][chr3]:
                    res += trie_data[chr1][chr2][chr3][chr4]
                    if len(res) >= 5:
                        return res
    return res
