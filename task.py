from collections import Counter
def word_frequency():
    sentence=input("Enter a sentence:")
    count=Counter()
    for i in sentence:
        count[i]+=1
    print("Each word with its frequency:")
    return count
print(word_frequency())
