from src.morse import morse_decode, morse_encode

def test_returns_empty_string_given_empty_string():
    assert morse_decode("") == ""

def test_handles_one_word_morse():
    # Arrange
    test_morse = ".... .."
    expected = "HI"
    # Act
    result = morse_decode(test_morse)
    # Assert
    assert result == expected

    # Arrange
    test_morse = ".... . .-.. .-.. ---"
    expected = "HELLO"
    # Act
    result = morse_decode(test_morse)
    # Assert
    assert result == expected

    # Arrange
    test_morse = "-. --- .-. - .... -.-. --- -.. . .-. ..."
    expected = "NORTHCODERS"
    # Act
    result = morse_decode(test_morse)
    # Assert
    assert result == expected

def test_handles_multiple_word_morse():
   # Arrange
    test_morse = "--. --- --- -..   -- --- .-. -. .. -. --.   -. --- .-. - .... -.-. --- -.. . .-. ..."
    expected = "GOOD MORNING NORTHCODERS"
    # Act
    result = morse_decode(test_morse)
    # Assert
    assert result == expected



def test_converts_one_word_string_to_morse():
    # Arrange
    test_morse = "HELLO"
    expected = ".... . .-.. .-.. ---"
    # Act
    result = morse_encode(test_morse)
    # Assert
    assert result == expected

def test_converts_multiple_word_string_to_morse():
    # Arrange
    test_morse = "GOOD MORNING NORTHCODERS"
    expected = "--. --- --- -..   -- --- .-. -. .. -. --.   -. --- .-. - .... -.-. --- -.. . .-. ..."
    # Act
    result = morse_encode(test_morse)
    # Assert
    assert result == expected