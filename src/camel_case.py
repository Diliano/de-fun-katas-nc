import re

def sentence_to_camel_case(sentence, upper):
    if not sentence:
        return ""
    
    words = sentence.split()

    for i in range(len(words)):
        words[i] = words[i].capitalize()
    if not upper:
        words[0] = words[0].lower()

    return ("").join(words)


def camel_to_english(sentence):
    regex = re.compile(r"[A-Z][^A-Z]*")
    words = regex.findall(sentence)

    for i in range(len(words)):
        words[i] = words[i].lower()

    if sentence[0].isupper():
        words[0] = words[0].capitalize()
        return (" ").join(words) + "."
    else:
        lower_regex = re.compile(r"^[a-z]*")
        first_word = lower_regex.findall(sentence)[0].capitalize()
        return first_word + " " + (" ").join(words) + "."