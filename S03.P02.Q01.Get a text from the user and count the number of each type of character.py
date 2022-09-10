# سید مجتبی موسوی
# تکلیف مبحث رشته
# سوال 1

s = input("Enter your text: ")

Sentences = s.count(".") + s.count("!") + s.count("?") + s.count(";")
words = s.count(" ")
characters = len(s)

def countLetters(letters):
    return len([x for x in letters if x.isalpha()])


print("Number of Sentences =", Sentences)
print("Number of Words =", words + 1)
print("Number of Characters =", characters)
print("Number of Letters =",countLetters(s))