import re
import json


class AutoCompleteData:
    def __init__(self, cmpleted_sentence, src_text, offs, scores):
        completed_sentence = cmpleted_sentence
        source_text = src_text
        offset = offs
        score = scores


i = 0

data = {}

print(ord('z'))
# TODO: what about space?
abc = [chr(c) for c in range(48, 123)]
abc.append(' ')
abc.append('$')
print(ord('1'))

for a in abc:
    data[a] = {}
    for b in abc:
        data[a][b] = {}
        for c in abc:
            data[a][b][c] = {}
            for d in abc:
                data[a][b][c][d] = []


print("Rut Rabinowitz")

with open("rfc7535.txt", "r") as file:
    dict_ = {}
    content = file.readlines()
    # print(content)
    for line in content:
        if line[:-1]:
            i = i + 1
            dict_[i] = line[:-1]
            tmp = re.sub('([-()+|&*%#@!/\'\".,:\t\n])+', ' ', line[:-1])
            tmp = re.sub(' +', ' ', tmp)
            tmp = tmp.lower()
            print(tmp)
            u = 0
            while(u + 3 < len(tmp)):
                data[tmp[u]][tmp[u + 1]][tmp[u + 2]][tmp[u + 3]].append(i)
                if(len(data[tmp[u]][tmp[u + 1]][tmp[u + 2]][tmp[u + 3]]) > 5):
                    print(tmp[u]+tmp[u + 1]+tmp[u + 2]+tmp[u + 3])
                u = u + 1



with open('sentences.json', 'w') as data_file:
    json.dump(dict_, data_file)




# data = {}
# json_file = open('sentences.json')
# sentences = json.load(json_file)
# for key in sentences.keys():


print("end")

user_data = "aargo"
counter = 0


def replace_char(word_len_5):
    counter = 0
    for i in abc:
        # data[i][user_data[1]][user_data[2]][user_data[3]][user_data[4]]
        print(data[i][user_data[1]][user_data[2]][user_data[3]][user_data[4]])
        print(i + user_data[1] + user_data[2] + user_data[3] + user_data[4])
        counter = counter + 1

    for i in abc:
        # data[i][user_data[1]][user_data[2]][user_data[3]][user_data[4]]
        print(data[user_data[0]][i][user_data[2]][user_data[3]][user_data[4]])
        print(user_data[0] + i + user_data[2] + user_data[3] + user_data[4])
        counter = counter + 1

    for i in abc:
        # data[i][user_data[1]][user_data[2]][user_data[3]][user_data[4]]
        print(data[user_data[0]][user_data[1]][i][user_data[4]])
        print(user_data[0] + user_data[1] + i + user_data[3] + user_data[4])
        counter = counter + 1

    for i in abc:
        # data[i][user_data[1]][user_data[2]][user_data[3]][user_data[4]]
        print(data[user_data[0]][user_data[1]][user_data[2]][i][user_data[4]])
        print(user_data[0] + user_data[1] + user_data[2] + i + user_data[4])
        counter = counter + 1

    for i in abc:
        # data[i][user_data[1]][user_data[2]][user_data[3]][user_data[4]]
        print(data[user_data[0]][user_data[1]][user_data[2]][user_data[3]][i])
        print(user_data[0] + user_data[1] + user_data[2] + user_data[3] + i)
        counter = counter + 1


def sub_str(user_data):
    res = []
    for i in data:
        if user_data == i[user_data[0]][user_data[1]][user_data[2]][user_data[3]][user_data[4]]:
            res.append(i[user_data[0]][user_data[1]][user_data[2]][user_data[3]][user_data[4]])

    return res


def fix_user_text(user_text, src_text):
    text = re.sub('([,.\t])+', ' ', user_text)
    text = re.sub(' +', ' ', text)
    print(text)


def add_char():
    pass
