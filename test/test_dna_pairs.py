from src.dna_pairs import dna_pairs

def test_returns_empty_list_given_empty_string():
    assert dna_pairs("") == []

def test_returns_one_pair_given_single_input():
    assert dna_pairs("G") == [["G", "C"]]

def test_returns_multiple_pairs():
    test_input = "AG"
    expected = [["A", "T"], ["G", "C"]]
    assert dna_pairs(test_input) == expected

    test_input = "ATAG"
    expected = [["A", "T"], ["T", "A"], ["A", "T"], ["G", "C"]]
    assert dna_pairs(test_input) == expected

def test_ignores_non_dna_input():
    assert dna_pairs("F") == []