#  سید مجتبی موسوی / تکالیف مبحث تابع / سوال 4
#  تابعی بنویسید که که یک عدد به عنوان ورودی گرفته تشخیص دهد عدد مربع است یا خیر

n_square = ""


def f_square(num):
    answer = "Not Square!"

    for i in range(2, (num // 2) + 1):
        if i * i == num:
            answer = "Square"
            global n_square
            n_square = i
            break

    return answer


e_number = int(input("Enter Number: "))

print(e_number, "is", f_square(e_number), n_square)
