#這是for的練習
cars = ['ford', 'audi', 'benz']
print(cars[0])
for car in cars:
	print(car)
names = ['Ted', 'Mary', 'Tom']
for name in names:
	print(name)
print(name, car) #只印出cars跟names清單內最後一個東西?

#for loop 練習
students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for hi in students:
    print('hi', hi)

#字串也可當清單
car = 'ford'
#相當於['f', 'o', 'r', 'd']
print(car)
print(len(car))
print('a' in car)
print('fd' in car) #false, 必須要連在一起才行?
print('fo' in car) #True
print('f' and 'd' in car) 