def my_func():
    num_1 = float(input("Введите число №1: "))
    num_2 = float(input("Введите число №2: "))
    div = num_1 / num_2
    return div

res = my_func()
print(res)

#-----------------------------------------------

def my_func(name, surname, year, city, mail, phone):
    return f"Имя- {name}, Фамилия- {surname}, Год рождения -{year},Город проживания- {city},Почта- {mail},Телефон- {phone}"

name = input("Пожалуйста введите свое имя: ")
surname = input("Пожалуйста введите свою фамилию: ")
year = int(input("Пожалуйста введите свой год рождения: "))
city = input("Пожалуйста введите свой город проживания: ")
mail = input("Пожалуйста введите e-mail адрес: ")
phone = input("Пожалуйста введите свой телефон: ")

print(my_func(name, surname, year, city, mail, phone))


#--------------------------------------------------------------------

def my_func():
    a_1= int(input("Введите число №1 "))
    a_2 = int(input("Введите число №2 "))
    a_3 = int(input("Введите число №3 "))
    """Находим два наибольших числа, а затем суммируем их"""
    if a_1 >= a_3 and a_2 >= a_3:
        return a_1 + a_2
    elif a_1 >= a_2 and a_3 >= a_2:
        return a_1 + a_3
    elif a_2 >= a_1 and a_3 >= a_1:
        return a_2 + a_3

print(my_func())

#----------------------------------------------------------------

def my_func():
    x= int(input("Введите число №1: "))
    y= int(input("Введите число №2: "))
    total= x ** y
    return total
print(my_func())

x= int(input("Введите число х "))
y= int(input("Введите число y "))
while x > 0:
     res = x ** y
     print(res)
     break

#---------------------------------------------------------------



#---------------------------------------------------------------

def int_func():
    text= str(input("Введите слова начинающиеся с маленьких латинских букв: ")).title()
    return text

print(int_func())

#---------------------------------------------------------------------------------

def my_func (*args):
    word = input("Введите слова ")
    print(word.title())
    return
my_func()





