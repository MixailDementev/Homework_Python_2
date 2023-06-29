# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


import re
from collections import Counter


def count_words(text):
    text = re.sub(r"[^\w\s]", "", text.lower())
    words = text.split()

    word_counts = Counter(words)

    most_common_words = word_counts.most_common(10)

    return most_common_words


text = input("Enter text: ")
result = count_words(text)
print(result)
