from src.get_tweet_data import get_tweet_data

def test_returns_basic_dictionary_given_empty_tweet():
    test_tweet = ""
    expected = { 
        "tags": [], 
        "mentions": [], 
        "tagCount": 0, 
        "mentionCount": 0, 
        "length": 0
    }
    assert get_tweet_data(test_tweet) == expected

def test_calculates_length_property_and_updates_dict():
    test_tweet = "My awesome tweet"
    expected = { 
        "tags": [], 
        "mentions": [], 
        "tagCount": 0, 
        "mentionCount": 0, 
        "length": 16
    }
    assert get_tweet_data(test_tweet) ==  expected

def test_gathers_mention_data_and_updates_dict():
    test_tweet = "My awesome tweet to @northcoders"
    expected = { 
        "tags": [], 
        "mentions": ["@northcoders"], 
        "tagCount": 0, 
        "mentionCount": 1, 
        "length": 32
    }
    assert get_tweet_data(test_tweet) == expected

def test_gathers_tag_data_and_updates_dict():
    test_tweet = "My awesome tweet about #coding"
    expected = { 
        "tags": ["#coding"], 
        "mentions": [], 
        "tagCount": 1, 
        "mentionCount": 0, 
        "length": 30
    }
    assert get_tweet_data(test_tweet) == expected

def test_updates_tag_and_mention_data_in_dict():
    test_tweet = "My awesome tweet about #coding to @northcoders"
    expected = { 
        "tags": ["#coding"], 
        "mentions": ["@northcoders"], 
        "tagCount": 1, 
        "mentionCount": 1, 
        "length": 46
    }
    assert get_tweet_data(test_tweet) == expected

def test_ignores_duplicate_mentions_and_tags():
    test_tweet = "I am #coding with @northcoders I love #coding and @northcoders"
    expected = { 
        "tags": ["#coding"], 
        "mentions": ["@northcoders"], 
        "tagCount": 1, 
        "mentionCount": 1, 
        "length": 62
    }
    assert get_tweet_data(test_tweet) == expected