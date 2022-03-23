from itertools import islice
#my_list = [1, 2, 3, 4, 5, 6]

new_ = (v ** 3 for v in range(1,11))
print(new_)

print(next(new_))
print(next(new_))
print(next(new_))
print(next(new_))

print(*islice(new_, 10))

new_ = (v ** 3 for v in range(1,11))
print(list(islice(new_, 10)))


def my_gen():
    for i inn range(5):
        yield i

for n in my_gen():
    print(n)



from functools import  reduce

def my_func(el_1, el_2):
    return el_1+ el_2

print(reduce(my_func, [10,20,30, 40]))

from itertools import count

for el in count(7):
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle


c = 0
for el in cycle("ABC"):
    if c > 10:
        break
    print(el)
    c += 1




