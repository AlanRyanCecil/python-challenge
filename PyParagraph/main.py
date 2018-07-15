import os
import re

text_path = os.path.join('raw_data/paragraph_1.txt')

title = '\nParagraph Analysis'
border = '-' * 23

with open(text_path, 'r') as text_file:
    text_data = text_file.read()
    letter_count = len(re.findall('\w', text_data))
    sentence_count = len(re.findall('[\.!?]', text_data))
    word_count = len(re.findall('\w+', text_data))
    word_length = letter_count / word_count
    sentence_length = word_count / sentence_count

    output = [
        title,
        border,
        'Approximate Word Count: {}'.format(word_count),
        'Approximate Sentence Count: {}'.format(sentence_count),
        'Average Letter Count: {}'.format(word_length),
        'Average Sentence Length: {}'.format(sentence_length),
    ]

    for line in output:
        print(line)
