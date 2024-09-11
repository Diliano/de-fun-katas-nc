from src.change_calculator import change_calculator

# 1p, 2p, 5p, 10p, 20p, 50p are options

def test_returns_single_coin_given_input_with_a_coin_value():
    assert change_calculator(1) == {"1": 1}
    assert change_calculator(2) == {"2": 1}

def test_returns_correct_combination_of_single_coins_required():
    assert change_calculator(7) == {"5": 1, "2": 1}
    assert change_calculator(13) == {"10": 1, "2": 1, "1": 1}

def test_handles_multiple_of_the_same_coin_needed():
    assert change_calculator(40) == {"20": 2}
    assert change_calculator(90) == {"50": 1, "20": 2}