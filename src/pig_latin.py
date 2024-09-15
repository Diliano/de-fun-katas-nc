def pig_latin(string):
    if not string:
        return ""
    
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    result = []
    words = string.split(" ")

    for word in words:
        if word[0] in vowels:
            result.append(f"{word}way")
        else:
            for index, c in enumerate(word):
                if c in vowels:
                    result.append(f"{word[index:]}{word[:index]}ay")
                    break
            else:
                    result.append(f"{word}ay") 

    return (" ").join(result)