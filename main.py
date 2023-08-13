import string

import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def get_most_common_words(text, num_common_words):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)

    filtered_text = [word.lower() for word in word_tokens if word not in string.punctuation and word not in stop_words]

    word_counter = Counter(filtered_text)

    for word, count in word_counter.most_common(num_common_words):
        print(f'Слово "{word}" встречается {count} раз(а)')

text = """
In computing, stop Words are words which are filtered out before or after processing of text. Computing
When building the vocabulary of an information retrieval system, it is a waste of space to include common words like 'is', 'the', and 'an' in the index.
"""

get_most_common_words(text, 5)
