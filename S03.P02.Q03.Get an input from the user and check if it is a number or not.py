# سید مجتبی موسوی
# تکلیف مبحث رشته
# سوال 3

p = input("Enter your phone number: ")
c = p.isnumeric()
if c == True:
    print(c, ", All characters are numeric")
else:
    print(c, ", One or all characters are not numeric")