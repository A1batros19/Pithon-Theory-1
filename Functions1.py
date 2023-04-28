#Функции
def sayHello(): #def - назначить функцию sayHello - название функции () - аргумента НЕТ
    print('Hello') #список действий, которые выполняет функция
    print('World')
    print('EveryBody')
sayHello() #вызываем функцию получаем все действия, которые она выполняет!

sayHello()
print('pause')
sayHello() #К одной и той же функции можно обращаться много раз!

#Создадим ещё одну функцию С АРГУМЕНТОМ
def square(x):
    print('Квадрат числа', x,'=',x**2)
square(5)
square(10)
#Квадрат числа 5 = 25
#Квадрат числа 10 = 100

#С Циклом FOR
for i in range(1,11): #Все значения i c 1-11 не вкл.
    square(i)

#Создадим ещё одну функцию С 2мя АРГУМЕНТАМИ

def multiplay(a, b): #Функция вкл 2 аргумента
    print(a*b)  #Выводит произведение a*b
multiplay(2, 3)
multiplay(70, 100)
#6
#7000

#Проверка на четность
#Программа ФУНКЦИИ
def even(a):
    if a%2==0:
        print(a,'Четное')
    else:
        print(a,'Не четное')
#ГЛАВНАЯ программа
for i in range(20, 30): #Числа от 20-30
    even(i)
#Выводит все числа от 20-30 определяя четность!

# ФАКТОРИАЛ
#Программа ФУНКЦИИ
def factorial(n):
    pr=1
    for i in range(1,n+1):
        pr=pr*i
    print(pr)
#ГЛАВНАЯ программа
factorial(3)

#Ещё один пример применения функции:

if 5>3:
    def primer():
        print('ВСЁ ВЕРНО!')
else:
    def primer():
        print('ТАКОГО НЕ БЫВАЕТ!')
primer() #В зависимости от логики будет выводиться функция!


#ЕЩЁ:
#ФУНКЦИИ - Блок кода (создаём, потом можно выполнять его многократно!)
#ФУНКЦИИ - def и имя функции
def funct1():
    print('Hello1')  #Сколько угододно строчек
    print('Hello2')
print('это действие находится ВНЕ функции')
#Функцию нужно вызвать!!! Вот так просто:
funct1()
funct1()  #Вызывать можно сколько угодно раз!
# У ФУНКЦИИ может быть АРГУМЕНТ и возвращаемое значение
def funct2(x): #Назначаем функцию funct2 И (x) - Значение которое мы будем потом подставлять в funct2(10)
    return x*2  #Определяем, что функция возвращает
a = funct2(10) #Определяем АРГУМЕНТ
print(a)
#Можно вывести и так:
print(funct2(100))

#ФУНКЦИЯ может принимать любое количество АРГУМЕНТОВ!!!
def sum_numbers(x,y): #sum_numbers -название функ (x,y) - значения которые подставляем
    return x+y    #Расчетная часть функции(логика)
e=sum_numbers(4,5)
print(e)

#ФУНКЦИЯ принимает аргумент, но ничего не возвращает!!!
def funct5(some_argument):
    print(some_argument)
    print('dsfdsfsdf')
a = funct5(5)
print(a)
#Выведет 5 потому что мы вызываем функцию от (5)

#ФУНКЦИЯ ничего не принимает но возвращает!!!
def funct6():
    return 5
print(funct6())
#Функция возвращает 5
a = funct6()
print(a)
#Переменная a = 5

def funct7(x):
    print(x)
    print('sdfsdfsdf')
    return 3*x
a=funct7(10)
print(a)

#ИНДЕКС массы тела через ФУНКЦИЮ!!!
name1 = 'Tom'
height1 = 1.90
weight1 = 80

name2 = 'Ben'
height2 = 1.80
weight2 = 70

name3 = 'Bil'
height3 = 1.70
weight3 = 60

def bmi_calc(name,height,weight): #Значение переменных можно задавать другими переменными
    bmi = weight/(height**2)
    print('Индекс массы тела:', bmi)
    if bmi<25:
        return name+ ' ' 'Не имеет лишний вес'
    else:
        return name+ ' ' 'Имеет лишний вес'

bmi1=bmi_calc(name1,height1,weight1)
bmi2=bmi_calc(name2,height2,weight2)
bmi3=bmi_calc(name3,height3,weight3)

print(bmi1)
print(bmi2)
print(bmi3)

#ЗАДАЧА 1
def convert(miles):
    return miles * 0.62
mil=convert(5)
print(mil)



