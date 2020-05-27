# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
i = 0
for char in word:
    if char.lower() == 'а':
        i += 1
    else:
        pass
print(i)


# Вывести количество гласных букв в слове
word = 'Архангельск'
i = 0
vowels = ['й', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'ю', 'ё', 'и']
for char in word:
    if char.lower() in vowels:
        i += 1
    else:
        pass
print(i)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
print(len(sentence))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for i in sentence:
    print(i[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence = sentence.split()
sent_len = len(sentence)
all_chars = 0
for i in sentence:
    all_chars += len(i)
mid_len = all_chars / sent_len
print(int(mid_len))
