def till_addition(till):
    total = 0
    for currency in till:
        if currency[-1] == "p":
            total += ((float(currency[:-1]) / 100) * till[currency])
        elif currency[0] == "£":
            total += (float(currency[1:]) * till[currency])
    return f"£{total:.2f}"