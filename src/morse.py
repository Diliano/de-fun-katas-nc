def morse_decode(morse):
    if not morse:
        return ""
    
    morse_dict = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", "-..-": "X", "-.--": "Y", "--..": "Z",
        "-----": 0, ".----": 1, "..---": 2, "...--": 3, "....-": 4,
        ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9
    }
    result = []

    morse_words = morse.split("   ")

    for morse_word in morse_words:
        letters = []
        morse_letters = morse_word.split(" ")
        for morse_letter in morse_letters:
            letters.append(morse_dict[morse_letter])
        result.append(("").join(letters))

    return (" ").join(result)



def morse_encode(string):
    morse_dict = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", "-..-": "X", "-.--": "Y", "--..": "Z",
        "-----": 0, ".----": 1, "..---": 2, "...--": 3, "....-": 4,
        ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9
    }
    key_list = list(morse_dict.keys())
    value_list = list(morse_dict.values())

    result = []
    words = string.split(" ")

    for word in words:
        morse_letters = []
        for c in word:
            position = value_list.index(c)
            morse_letters.append(key_list[position])
        result.append((" ").join(morse_letters))
    
    return ("   ").join(result)