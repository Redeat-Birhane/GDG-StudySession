from collections import Counter
def word_frequency():
    sentence=input("Enetr a sentence:")
    count=Counter()
    for i in sentence:
        count[i]+=1
    print("Each word with it frequency:")
    return count
print(word_frequency())