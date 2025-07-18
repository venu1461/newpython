# count the repeated elements in the  given string
s=input("enter the sentence:")
word_count={}
for word in s.split():
    word_count[word]=word_count.get(word,0)+1
print(word_count)