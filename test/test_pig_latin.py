from src.pig_latin import pig_latin

def test_returns_empty_string_given_empty_string():
    assert pig_latin("") == ""

def test_adds_way_to_end_of_word_starting_with_vowel():
    # Arrange
    test_input = "algorithm"
    expected = "algorithmway"
    # Act
    result = pig_latin(test_input)
    # Assert
    assert result == expected

def test_moves_first_consonant_of_word_to_end_and_adds_ay():
    # Arrange
    test_input = "northcoders"
    expected = "orthcodersnay"
    # Act
    result = pig_latin(test_input)
    # Assert
    assert result == expected 

def test_moves_consecutive_first_consonants_of_word_to_end_and_adds_ay():
    # Arrange
    test_input = "sheffield"
    expected = "effieldshay"
    # Act
    result = pig_latin(test_input)
    # Assert
    assert result == expected

def test_handles_multiple_words():
    # Arrange
    test_input = "keep on coding"
    expected = "eepkay onway odingcay"
    # Act
    result = pig_latin(test_input)
    # Assert
    assert result == expected

def test_handles_words_with_no_vowels():
    # Arrange
    test_input = "myth"
    expected = "mythay"
    # Act
    result = pig_latin(test_input)
    # Assert
    assert result == expected