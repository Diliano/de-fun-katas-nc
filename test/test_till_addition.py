from src.till_addition import till_addition

def test_returns_0_given_empty_dict():
    assert till_addition({}) == "£0.00"

def test_handles_pence():
    test_till = {"1p": 1, "2p": 1, "5p": 1, "10p": 1, "20p": 1}
    expected = "£0.38"
    assert till_addition(test_till) == expected

def test_handles_pounds():
    test_till = {"£1": 1, "£2": 1}
    expected = "£3.00"
    assert till_addition(test_till) == expected

def test_handles_pence_and_pounds():
    test_till = {"5p": 1, "10p": 1, "20p": 1, "50p": 1, "£1": 1}
    expected = "£1.85"
    assert till_addition(test_till) ==  expected

def test_handles_multiple_quantities():
    test_till = {"5p": 2, "10p": 5, "20p": 10, "50p": 15, "£1": 1, "£50": 3}
    expected = "£161.10"
    assert till_addition(test_till) ==  expected