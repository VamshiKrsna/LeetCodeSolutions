allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
counter = 0
allowed = set(allowed)
for word in words:
    for char in word:
        if char not in allowed:
            counter += 1
            break

print(counter)

print(len(words)-counter)