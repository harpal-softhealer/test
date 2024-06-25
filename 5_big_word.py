word_lengths = {'apple': 5, 'banana': 8, 'grape': 4, 'kiwi': 4}



def is_small(word):
    return word<5

pure_words = dict(filter(lambda itm : is_small(itm[1]),word_lengths.items()))

print(pure_words)