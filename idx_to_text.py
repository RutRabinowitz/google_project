import json


class AutoCompleteData:
    def __init__(self, cmpleted_sentence, src_text, offs, scores):
        self.completed_sentence = cmpleted_sentence
        self.source_text = src_text
        self.offset = offs
        self.score = scores


# def get_offset(user_text, sentence):
#     for i in range(len(sentence) - len(user_text)):
#         if user_text == fix_user_text(sentence[i::i + len(user_text)]):
#             return i
#
#
# def is_one_correct(user_text, sentence):
#     boolean = True
#     for x, y in zip(user_text, sentence):
#         if x != y:
#             if not boolean:
#                 return False
#             else:
#                 boolean = False
#     return True


def get_text_by_idx(idx_list, user_text):
    res = []
    with open('sentences.json', 'r') as sentences_file:
        sentences = json.load(sentences_file)
        for idx in idx_list:
            sentence = sentences[str(idx[0])]
            if len(idx) == 4:
                re_text = user_text[:idx[3]] + idx[2] + user_text[idx[3] + 1:]
                res.append(AutoCompleteData(sentence, sentence, (sentence.lower()).find(re_text),
                                            len(user_text) * 2 - idx[1]))
            else:
                res.append(AutoCompleteData(sentence, sentence, (sentence.lower()).find(user_text),
                                            len(user_text) * 2 - idx[1]))
    return res


def final_results_by_idx(idx_list, user_text):
    res = get_text_by_idx(idx_list, user_text)
    if len(res) > 5:
        return sorted(res, key=lambda x: (x.score, x.completed_sentence), reverse=True)[:5]
    return sorted(res, key=lambda x: (x.score, x.completed_sentence), reverse=True)
