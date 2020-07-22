import re
import json
import os


def insert_new_3keys_and_str(trie_data, sentence, index, curr):
    trie_data[sentence[curr]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]
    return trie_data


def insert_new_2keys_and_str(trie_data, sentence, index, curr):
    trie_data[sentence[curr]][sentence[curr + 1]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]
    return trie_data


def insert_new_key_and_str(trie_data, sentence, index, curr):
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]
    return trie_data


def insert_new_str(trie_data, sentence, index, curr):
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]
    return trie_data


def insert_str_to_data(trie_data, sentence, index, curr):
    if sentence[curr] in trie_data.keys():
        if sentence[curr + 1] in trie_data[sentence[curr]].keys():
            if sentence[curr + 2] in trie_data[sentence[curr]][sentence[curr + 1]].keys():
                if sentence[curr + 3] in trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]].keys():
                    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]].append(
                        index)
                else:
                    trie_data = insert_new_str(trie_data, sentence, index, curr)
            else:
                trie_data = insert_new_key_and_str(trie_data, sentence, index, curr)
        else:
            trie_data = insert_new_2keys_and_str(trie_data, sentence, index, curr)
    else:
        trie_data = insert_new_3keys_and_str(trie_data, sentence, index, curr)

    return trie_data


def insert_sen_to_trie(trie_data, sentence, index):
    curr = 0
    while curr + 3 < len(sentence):
        trie_data = insert_str_to_data(trie_data, sentence, index, curr)
        curr = curr + 1
    return trie_data


def fix_sentence(sentence):
    new_sentence = re.sub('([.,\t\n])+', ' ', sentence[:-1])
    new_sentence = re.sub(' +', ' ', new_sentence)
    return new_sentence.lower()


def insert_line(trie_data, line, sentence_index):
    sentence = fix_sentence(line[:-1])
    trie_data = insert_sen_to_trie(trie_data, sentence, sentence_index)
    return trie_data


def insert_file(file_name, trie_data, sentence_index):
    with open('RFC/' + file_name, 'r+', encoding="utf8") as current_file:
        data_to_json_file = {}
        content = current_file.readlines()
        for line in content:
            if line[:-1]:
                sentence_index = sentence_index + 1
                data_to_json_file[sentence_index] = line[:-1]
                trie_data = insert_line(trie_data, line, sentence_index)
        with open('sentences.json', 'w') as sentences_file:
            json.dump(data_to_json_file, sentences_file)

    return trie_data, sentence_index


def insert_sub_dir(files, sentence_index, trie_data):
    if len(files) > 0:
        for file in files:
            trie_data, sentence_index = insert_file(file, trie_data, sentence_index)
            print("_", end="")
    return sentence_index, trie_data


def init():
    print("loading files and preparing the systems")
    sentence_index = 1
    trie_data = {}
    subdirectories = [x[0] for x in os.walk('RFC')]

    for subdir in subdirectories:
        files = os.walk(subdir).__next__()[2]
        sentence_index, trie_data = insert_sub_dir(files, sentence_index, trie_data)
    print(trie_data['t']['h']['i']['s'])
    with open('trie_data.json', 'w') as trie_file:
        json.dump(trie_data, trie_file)


if __name__ == '__main__':
    init()
