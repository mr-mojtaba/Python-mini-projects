# سید مجتبی موسوی / تکالیف مبحث دیکشنری و مجموعه / سوال 2

word = {}

w = input("Enter a word: ")
Meanings = (input("Enter the meanings: ").split(","))

word[w] = Meanings

print(word)

m2 = input("Enter the word to display the meanings: ")
print("Meanings for", m2, "= ", word.get(m2))