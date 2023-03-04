"""Count words in file."""


# put your code here.


#open file
text = open("test.txt")

#make an empty dictionary to store later values in
all_words = {}

# separate words from spaces (parse)

for line in text:
    line = line.rstrip()
    words = line.split(" ")


    for word in words:
        #for each new word, add the word to a dictionary and count as 1
        #for each existing word, increase the value by 1
        all_words[word] = all_words.get(word, 0) + 1

#print the key and value pairs
print(all_words)