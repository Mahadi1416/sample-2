# how to use input
name = input(" What is your name? ")
color = input('what is your favourite color? ')
print(name + 'likes' +color)
# practise of input
bitrh_date = input('what is your birth date write here? ')
your_age = 2021 - int(bitrh_date)
print(your_age)
# practice of input
your_weight= input('write in pound? ')
kg = 0.45 * int(your_weight)
print(kg)
# formatted string impotant ****
first = 'mahadi'
second = 'Hassan'
msg = f'{first} {second} is a coder'
print(msg)
# string  ****
name = 'mahadi'
print(name.upper())
print(name.lower())
print(name.find('m'))
print(name.replace('mahadi','ratul'))
# have to careful about letter
course = 'python fir begainner'
print("python" in course)
# if statement
is_hot = False
is_cold = True

if is_hot:
    print('Drink a lot of water')

elif is_cold:
    print('wear warm clothes ')

else:
    print('its a lovely day')

print('enjoy your day')
# if statement
house_price = 100000
good_credid = True

if good_credid:
    print(f'houses price put down {house_price * 0.1} ')

else:
    print(f'houses price put down {house_price * 0.2} ')

# logical operator and e
has_high_income = True
has_good_credid = False

if has_high_income and has_good_credid:
    print('eligable for loan')

# logical operator or
has_high_income = True
has_good_credid = False

if has_high_income or has_good_credid:
    print('eligable for loan')

# logical operator not , (if i did not use here not it will not be correct)
has_high_income = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print('eligable for loan')

# logical operator temperatue
name_character = "masdfghj"

if len(name_character) < 3:
    print('Name should be at list 3 character')
else:
    print("good name")

#
weight = int(input("weight? "))
unit = input('(L)bs or (k)g: ')

if unit.upper() == "L":
    conerted = weight * 0.45
    print(f'you are {conerted} bs')

else:
    conerted = weight / 0.45
    print(f'you are {conerted} kg')

# guess game


secret_number = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :
    guess = int(input('guess any number from 1 to 10.You have three option?  '))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break

else :
        print('sorry you lose')

# while if practrise
command = ""
while True:

    command = input('>  ')
    if command.lower() == "start":
        print("Your car is start")
    elif command.lower() == " Stopped ":
        print("car stopped")
    elif command.lower() == "help":
        print('''
        start = to start the car
        stop = to stop the car
        help = how to do ''')

    elif command.lower() == "quit":
        break

    else:
        print("sorry i dint understannd you")

    # for loop
    # for list we use this []
    # renge() we use for creating a renge of number

    for item in range(10):
        print(item)

    for item in range(5, 10):
        print(item)

    for item in range(5, 10, 2):
        print(item)

 # for


prices =[6,7,7,7,7,7,7,7,7,7]

total = 0
for price in prices:
    total = total + price
    print(f'{total} is your total expenses')


# find max number

numbers = [4,5,56,6,6]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

# matrix

matrix=[
    [1,3,5],
    [6,7,8],
    [9,10,11]

]
matrix[0][1] = 20
print(matrix[0][1])

# martix practice

matrix=[
    [1,3,5],
    [6,7,8],
    [9,10,11]

]
for row in matrix:
    for item in row:
        print(item)


# how to add a number in a list but last
number = [1,3,4,6,7,8,9,6]
number.append(20)
print(number)
# # how to add a number in a list but first
number = [1,3,4,6,7,8,9,6]
number.insert(0,20)
print(number)
## remove
number = [1,3,4,6,7,8,9,6]
number.remove (6)
print(number)
# remove all list number
number = [1,3,4,6,7,8,9,6]
number.clear ()
print(number)
# pop for remove last item
number = [1,3,4,6,7,8,9,6]
number.pop()
print(number)


#### any number to cheak have in the list
number = [1,23,4,5,6]
print(3 in number)
# count how many same number have in the list
number = [1,2,3,4,5,6,7,8,8,]
print(number.count(2))
# make item serial perfect
number = [1,2,3,4,5,6,7,8,8,]
number.sort()
print(number)
# reverse list
number = [1,2,3,4,5,6,7,8,8,]
number.sort()
number.reverse()
print(number)
# copy of a list
number = [1,3,4,5,5]
numbers2 = number.copy()
print(numbers2)
# remove dublicate of a list i dont understand
# tupple like list but does not change only can count and number point
number = (1,3,3)
print(number[1])
# unpacking tuple
number = (1,3,5)
x = number[0]
y = number[1]
z = number[2]
print(x)
# unpacking standard way
number = ( 1,2,3)
x,y,z = number
print(x)
# packages
from ecommerce.shiping import cal_shiping

cal_shiping()
cal_shiping()

# for import all file of shiping

from ecommerce import shiping

shiping.cal_shiping()
###
import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

# randomly choice any number or man
import random

members = ["sds","sdasdsa","sdssds"]
leader = random.choice(members)
print(leader)
# dice game()
import random

class Dice:
    def roll():
        f = random.randint(1, 6)
        s = random.randint(1, 6)
        return f, s


dice = Dice
print(dice.roll())





































