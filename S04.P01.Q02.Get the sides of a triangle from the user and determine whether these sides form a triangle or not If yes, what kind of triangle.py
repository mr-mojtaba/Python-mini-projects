# سید مجتبی موسوی / تکالیف مبحث ساختار تصمیم / سوال 2

print("Enter the sides")
a = int(input("Enter for /  side: "))
b = int(input("Enter for __ side: "))
c = int(input("Enter for  \ side: "))

if a<b+c and b<a+c and c<a+b:
    print("True")
    if a == b and b == c:
        print("متساوی الاضلاع")
    elif a == b or a == c or b == c:
        print("متساوی الساقین")
    elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == c ** 2 + a ** 2 or c ** 2 == a ** 2 + b ** 2:
        print("قائم الزاویه")
    elif a != b and b != c:
        print("مختلف الاضلاع")
else:
    print("False !")
