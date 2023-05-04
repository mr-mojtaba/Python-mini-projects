# سید مجتبی موسوی / تکالیف مبحث لامبدا / سوال 6
#  با استفاده از لامبدا برنامه ای بنویسید تا بفهمید که آیا یک رشته داده شده با یک کاراکتر مشخص شروع می شود یا خیر

e_word = input("Type a Word: ")
e_ch = input("Type a Char: ")

check_ch = lambda ch: True if e_word.startswith(e_ch) else False

print(check_ch(e_ch))
