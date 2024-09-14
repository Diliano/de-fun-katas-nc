from src.calculate_divisors import calculate_divisors

def test_returns_0_given_impossible_input():
    assert calculate_divisors(3) == 0
    assert calculate_divisors(-10) == 0

def test_returns_3_given_one_multiple_of_3():
    assert calculate_divisors(4) == 3

def test_returns_8_given_one_multiple_of_3_and_one_of_5():
    assert calculate_divisors(6) == 8

def test_calculates_total_given_many_multiples_of_3_and_5():
    assert calculate_divisors(10) == 23
    assert calculate_divisors(12) == 33