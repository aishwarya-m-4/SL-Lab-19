# Write a python class to reverse a sentence (initialized via constructor) word
# by word. Example: “I am here” should be reversed as “here am I”. Create instances of this class
# for each of the three strings input by the user and display the reversed string for each, in
# descending order of number of vowels in the string.
from operator import itemgetter

sentences = []


class reverseSentence:

    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        temp = ""
        temparr = []
        # array of words
        temparr = self.sentence.split(" ")
        temparr.reverse()
        # making a string of reversed word
        for word in temparr:
            temp += word
            temp += " "

        # Calculating number of vowels
        count = 0
        for i in range(0, len(temp)):
            if (temp[i] == 'a' or temp[i] == 'e' or temp[i] == 'i' or temp[i] == 'o' or temp[i] == 'u'):
                count += 1
        # Saving in list as dictionary(count of vowels: sentence)
        sentences.append({"count": count, "sentence": temp})


s1 = reverseSentence(input("Enter the first sentence: "))
s1.reverse()
s2 = reverseSentence(input("Enter the second sentence: "))
s2.reverse()
s3 = reverseSentence(input("Enter the third sentence: "))
s3.reverse()

# Sorting in descending order based on number of vowels
sortedArr = sorted(sentences, key=itemgetter('count'), reverse=True)

# printing only the sentence
for sentence in sortedArr:
    print(sentence['sentence'])
