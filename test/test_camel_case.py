from src.camel_case import sentence_to_camel_case, camel_to_english

def test_returns_empty_string_given_empty_string():
    assert sentence_to_camel_case("", True) == ""
    assert sentence_to_camel_case("", False) == ""

def test_returns_upper_camel_given_one_lowercase_word():
    assert sentence_to_camel_case("hi", True) == "Hi"

def test_returns_lower_camel_given_one_capitalised_word():
    assert sentence_to_camel_case("Hi", False) == "hi"

def test_returns_upper_camel_given_a_sentence():
    test_sentence = "this sentence"
    test_upper = True
    expected = "ThisSentence"
    assert sentence_to_camel_case(test_sentence, test_upper) == expected

    test_sentence = "This Bigger strange Sentence"
    test_upper = True
    expected = "ThisBiggerStrangeSentence"
    assert sentence_to_camel_case(test_sentence, test_upper) == expected

def test_returns_lower_camel_given_a_sentence():
    assert sentence_to_camel_case("this sentence", False) == "thisSentence"



def test_converts_upper_camel_to_plain_english():
    test_sentence = "ThisBiggerStrangeSentence"
    expected = "This bigger strange sentence."
    result = camel_to_english(test_sentence)
    assert result == expected

def test_converts_lower_camel_to_plain_english():
    test_sentence = "thisBiggerStrangeSentence"
    expected = "This bigger strange sentence."
    result = camel_to_english(test_sentence)
    assert result == expected