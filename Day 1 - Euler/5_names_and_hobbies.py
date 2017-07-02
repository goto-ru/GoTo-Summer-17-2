import random

persons = ["Вася", "Дед", "Сова", "Сосед"]
hobbies = ["пить", "сидеть на дваче",  "играть на трубе", "спать"]

for person in persons:
    print("{0} очень любит {1}. Вот так вот.".format(
        person, random.choice(hobbies)))
