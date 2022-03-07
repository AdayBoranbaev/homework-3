my_list = [1, 3, 5, [43, 44], False ,{2: 'two', 5 : 'five'}, range(1,10),bytearray(b"fourty")]

for i, smt in enumerate(my_list, 1):
    print(f"{i}) {smt} - {type(smt)}")

#----------------------------------------

my_list = list(input("Введите числа для обмена элементов - "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

#----------------------------------------

month = int(input("Введите месяц от 1 до 12"))

month_dirt = {1: "январь", 2: "февраль" , 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

if month in month_dirt:
    print(f"{month}-й месяц года это {month_dirt[month]}")
    print(f"{month}-й месяц года это {month_list[month - 1]}")
else:
    print("Число не входит в промежуток от 1 до 12")

#------------------------------------------------------


string = input("Введите строку из нескольких слов ").split()

for n, i in enumerate(string, 1):
    print(f"{n}) {i:.10}")

#--------------------------------------------

my_list = [9, 8, 7 , 6, 5, 4, 3, 3, 3, 2, 1]
new_number = int(input("Введите нвой элемент рейтинга в виде натурального числа: "))
i = 0
for n in my_list:
    if new_number <= n:
        i+= 1
    else:
        break
my_list.insert(i, new_number)
print(my_list)
