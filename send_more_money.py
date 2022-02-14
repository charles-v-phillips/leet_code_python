from itertools import permutations

def word_to_number(mapping, word):
    result = ''
    for letter in word:
        result += str(mapping[letter])
    return int(result)

letters = set("sendmoremoney")
perms = permutations(range(10))

for perm in perms:
    mapping = dict(zip(letters,perm))
    if mapping['m'] == 0 or mapping['s'] == 0:
        continue

    send = word_to_number(mapping,'send')
    more = word_to_number(mapping, 'more')
    money = word_to_number(mapping,'money')
    if send + more == money:
        print(mapping)
