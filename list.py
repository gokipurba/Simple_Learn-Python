print("write a program to find the largest number in a list")

number = [6, 33, 14, 7, 4]
max = number[0]
for x in number:
    if max < x:
        max = x
print (max)

number.sort(reverse=True)
print(number)

print ("x"*25 + "MATRIKS")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9 ,"GOKI"]
    ]

#print(matrix)
for x in matrix:
    print(x)
    
for y in matrix:
    for y in y:
        print(y)

print ("x"*25 + "Methode LIST")
number = [2, 4, 1, 5, 6]
number2 = number.copy()
number.append(20)
print(number)
print(number2)
number.count(2)
number.pop()
number

print ("x"*25 + "wirte program to remove the duplicates in a list")
numbers = [2, 4, 1, 5, 6, 6, 4, 1, 2]
print(numbers)
unik = []
for number in numbers:
    if number not in unik:
        unik.append(number)
unik.reverse()
print(unik)

print ("x"*25 + "1234")

phone = input("phone: ")
numbers = {
    '1' : "one",
    '2' : 'two',
    '3' : 'three',
    }
for number in numbers:
    number = numbers.get(number)
    print (number)

print ("x"*25 + "1234 Mosh Technique")

phone = input("phone: ")
numbers = {
    '1' : "one",
    '2' : 'two',
    '3' : 'three',
    }
output = ""
for chr in phone:
    output += numbers.get(chr, "!") + " "
print (output)

print ("x"*25 + "emoji")
message = input(">")
message = message.split()
emojies = {
    ":)" : "😊",
    ":(" : "😒",
    }
output = ""
for word in message:
    output += emojies.get(word, word) + " "
print(output)


