with open("words.txt", "w") as word:
    word.write("mary\n")
    word.write("army")

with open("words.txt", "r") as word:
    whole = word.read().split("\n")
    word1 = whole[0]
    word2 = whole[1]

if sorted(word1) == sorted(word2):
    print ("The words are anagrams")
else:
    print("The words are not anagrams")

