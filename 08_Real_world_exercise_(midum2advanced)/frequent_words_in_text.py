"""### Exercise 6: **Frequent Words in a Text**
You are given a string of text. Write a program to find the most frequently occurring words (ignore case and punctuation) and display the top 3.
"""
import string
text = "Python is great, and learning python is fun. Python Python Python!"

text = text.lower().split()
# remove punctuations
text = [word.strip(string.punctuation) for word in text]

temp = list(set(text))

def test(word):
    return text.count(word)

temp.sort(key=test, reverse=True)

print("Top 3 most frequently occuring words:")
for i in range(3):
    print(f"{temp[i]} = {test(temp[i])}")