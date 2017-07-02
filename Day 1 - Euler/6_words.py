word = input("Введите слово:").lower()
words = [word]
while True:
    new_word = input("Вам на '{0}':".format(word[-1])).lower()
    if new_word[0] == word[-1] and new_word not in words:
        print("Все правильно!")
        word = new_word
        words.append(word)
    else:
        print("Неправильно!")
        print("Уже было: {0}".format(",".join(words)))
