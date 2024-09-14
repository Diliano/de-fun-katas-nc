from src.fold_string import fold_string

def test_returns_empty_string_given_empty_string():
    assert fold_string("") == ""

def test_returns_given_string_if_2_or_less_chars():
    assert fold_string("is") == "is"

def test_handles_one_word_of_even_length():
    # Arrange
    test_input = "code"
    expected = "oced"
    # Act
    result = fold_string(test_input)
    # Assert
    assert result == expected

def test_handles_one_word_of_odd_length():
    # Arrange
    test_input = "coder"
    expected = "ocdre"
    # Act
    result = fold_string(test_input)
    # Assert
    assert result == expected

def test_handles_input_spaces():
    # Arrange
    test_input = "python is cool"
    expected = "typnoh is oclo"
    # Act
    result = fold_string(test_input)
    # Assert
    assert result == expected