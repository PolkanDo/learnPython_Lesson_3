file_name_1 = "referat.txt"
file_name_2 = "referat_2.txt"

"""Opening file, and reading its info."""
with open(file_name_1, 'r', encoding='utf-8') as f:
    info = ''
    for line in f:
        info += line

"""Working with file info"""
len_info = len(info)
print(len_info)
num_word_info = info.split()
print(len(num_word_info))
info = info.replace(".", "!")
print(info)

"""Creating new file, with changes"""
with open(file_name_2, 'w') as f2:
    f2.write(info)