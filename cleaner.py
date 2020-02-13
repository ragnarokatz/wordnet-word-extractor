f = open("data.verb", "r")
contents = f.read()
lines = contents.split("\n");
print(lines[29])

lines = lines[29:]

all_words = []

for line in lines:
    line = line.split('|')[0]
    words = line.split(' ')
    for word in words:
        if word.isalpha():
            all_words.append(word.lower())

all_words = list(set(all_words))
all_words = [ word for word in all_words if len(word) <= 6 and len(word) >= 3]
print (len(all_words))

with open("verbs.txt", "w") as output:
    for word in all_words:
        output.write("%s\n" % word)

