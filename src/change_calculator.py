def change_calculator(change):
    options = [50, 20, 10, 5, 2, 1]
    result = {}

    for option in options:
        if option <= change:
            num_coins = change // option  
            change = change - (option * num_coins)
            result[str(option)] = num_coins
        if change == 0:
            break
    
    return result