# سید مجتبی موسوی / تکالیف مبحث حلقه و اعداد تصادفی / سوال 7

from random import choice

names = ["Ali", "Neda", "Hasan", "Maryam", "Hamed", "Zohre", "Amir", "Masume", "Mohsen", "Hanie"]

print()
print("Choose one of the following names in your mind !")

for i in names:
    print(i, end="   ")
print()
print()

conti = input("Press Enter to continue ...")

while True:
    if len(names) == 0:
        print()
        print("Not Found?")
        print("Try Again")
        break
    cho = choice(names)
    user_ch = input(f"Is the name you chose {cho} ? (y/n)")
    if user_ch == "y":
        print()
        print("I WON !")
        break
    elif user_ch == "n":
        names.remove(cho)
    else:
        print()
        print("The GAME was cancelled")
        print("Try Again")
        break
