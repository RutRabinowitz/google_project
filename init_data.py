import re
import json
import os

trie_data = {}


def insert_new_3keys_and_str(sentence, index, curr):
    # print(index)
    trie_data[sentence[curr]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]


def insert_new_2keys_and_str(sentence, index, curr):
    trie_data[sentence[curr]][sentence[curr + 1]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]


def insert_new_key_and_str(sentence, index, curr):
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]] = {}
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]


def insert_new_str(sentence, index, curr):
    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]] = [index]


def insert_str_to_data(sentence, index, curr):
    global trie_data
    if sentence[curr] in trie_data:
        if sentence[curr + 1] in trie_data[sentence[curr]]:
            if sentence[curr + 2] in trie_data[sentence[curr]][sentence[curr + 1]]:
                if sentence[curr + 3] in trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]]:
                    trie_data[sentence[curr]][sentence[curr + 1]][sentence[curr + 2]][sentence[curr + 3]].append(index)
                else:
                    insert_new_str(sentence, index, curr)
            else:
                insert_new_key_and_str(sentence, index, curr)
        else:
            insert_new_2keys_and_str(sentence, index, curr)
    else:
        insert_new_3keys_and_str(sentence, index, curr)


def insert_sen_to_trie(sentence, index):
    curr = 0
    while curr + 3 < len(sentence):
        insert_str_to_data(sentence, index, curr)
        curr = curr + 1


def fix_sentence(sentence):
    new_sentence = re.sub('([.,\t\n])+', ' ', sentence[:-1])
    new_sentence = re.sub(' +', ' ', new_sentence)
    return new_sentence.lower()


def insert_line(line, sentence_index):
    sentence = fix_sentence(line[:-1])
    insert_sen_to_trie(sentence, sentence_index)


def insert_file(file_name, sentence_index, data_to_json_file):
    with open('RFC/' + file_name, 'r+', encoding="utf8") as current_file:
        content = current_file.readlines()
        for line in content:
            if line[:-1]:
                sentence_index = sentence_index + 1
                data_to_json_file[sentence_index] = line[:-1]
                insert_line(line[:-1], sentence_index)

    return sentence_index, data_to_json_file


def insert_sub_dir(files, sentence_index, data_to_json_file):
    if len(files) > 0:
        for file in files:
            sentence_index, data_to_json_file = insert_file(file, sentence_index, data_to_json_file)
            print("_", end="")
    return sentence_index, data_to_json_file


def init():
    print("loading files and preparing the systems")
    data_to_json_file = {}
    sentence_index = 1
    subdirectories = [x[0] for x in os.walk('RFC')]

    for subdir in subdirectories:
        files = os.walk(subdir).__next__()[2]
        sentence_index, data_to_json_file = insert_sub_dir(files, sentence_index, data_to_json_file)

    with open('sentences.json', 'w') as sentences_file:
        json.dump(data_to_json_file, sentences_file)
        print(data_to_json_file)


init()
with open('trie_data.json', 'w') as trie_file:
    json.dump(trie_data, trie_file)
