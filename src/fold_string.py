def fold_string(string):
    words = string.split(" ")
    result = []

    for word in words:
        length = len(word)

        if length <= 2:
            result.append(word)
        else:
            index = length // 2
            start = word[:index][::-1]

            if length % 2 == 0:
                result.append(start + word[index:][::-1])
            else:
                result.append(start + word[index] + word[index + 1:][::-1])

    return (" ").join(result)