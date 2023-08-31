payphone = "a b c d e a b e y t"

def generate_word_dict(song):
    words_list = song.split()
    word_dict = {}
    for w in words_list:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1
    return word_dict

dictio = generate_word_dict(payphone)

print(dictio)
print(dictio['a'] + dictio['c'])

