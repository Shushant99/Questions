#name: Shushant kumar sharma
#enrollment no: 0103IS231188
#batch: 5th
#batch time: 10:30 to 12:10

# ##Question 1
num = int(input("Enter a number: "))
if num == 0:
    print("The number is zero.")
elif num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

##Question 2
num2 = int(input("Enter a number: "))
if num2 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

##Question 3
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

##Question 4
num3 = int(input("Enter a number one: "))
num4 = int(input("Enter a number two: "))
if num3 > num4:
    print(f"{num3} is the largest number.")  
elif num4 > num3:
    print(f"{num4} is the largest number.")
else:
    print("Both numbers are equal.")

##Question 5
age = int(input("Enter your age: "))
if age < 18:
    print("you are uneligible to vote.")
else:
      print("you are eligible to vote.")

#question 6
alphabat = input("Enter an alphabet: ").lower()
if alphabat in 'aeiou':
    print(f"{alphabat} is a vowel.")
else:
    print(f"{alphabat} is a consonant.")  

#question 7
num5 = int(input("Enter a number: "))
if num5 % 5 == 0 :
      print(f"{num5} is divisible by 5.")

else:
      print(f"{num5} is not divisible by 5.")

#question 8
num6 = int(input("Enter a number: "))
if num6 - 10 < 0:
      print(f"{num6} is single digit.")
elif num6 - 100 < 0:
      print(f"{num6} is two digit.")
else:
        print(f"{num6} is three digit or more.")

#question 9
marks = int(input("Enter your marks: "))
if marks >= 40:
      print("You have passed the exam.")
else:
      print("You have failed the exam.")

#question 10
num7 = int(input("Enter a number: "))
if num7 % 3 == 0 and num7 % 7 == 0:
      print(f"{num7} is multiple of both 3 and 7.")
else:
        print(f"{num7} is not multiple of both 3 and 7.")

#2nd set of questions

#Ladder If & Nested If: 

#Question 1:
num8 = int(input("Enter a number: "))
num9 = int(input("Enter another number: "))
num10 = int(input("Enter a third number: "))
if num8 >= num9 and num8 >= num10:
      print(f"{num8} is the largest number.")
elif num9 >= num8 and num9 >= num10:
      print(f"{num9} is the largest number.")
else:
      print(f"{num10} is the largest number.")

#Question 2:
age = int(input("Enter your age: "))
if age < 13:
      print("You are a child.")
elif 13 <= age <= 19:
            print("You are a teenager.")
elif 20 <= age <= 59:
                  print("You are an adult.")
else: 
      print("You are a senior citizen.")

#Question 3:
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks <= 89:
    print("Grade: B")
elif marks >= 50 and marks <= 74:
    print("Grade: C")
elif marks >= 35 and marks <= 49:
    print("Grade: D")
elif marks < 35 :
    print("Grade: Fail")
else:
    print("Invalid marks entered.")

# Question 4:
side1 = float(input("Enter the length of first side: "))
side2 = float(input("Enter the length of second side: "))
side3 = float(input("Enter the length of third side: "))

if side1 == side2 == side3:
        print("This is an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
        print("This is an isosceles triangle.")
else:
        print("This is a scalene triangle.")

#Question 5:
char = input("Enter a character: ")
if char.isupper():
    print("The character is uppercase.")
elif char.islower():
        print("The character is lowercase.")
elif char.isdigit():
        print("The character is a digit.")
else:
        print("The character is a special symbol.")


# #Question 6:
units = int(input())
cost = 0
if units > 200:
    cost = ((units-200)*10) + 700 + 500
elif units > 100:
    cost = ((units-100)*7) + 500
else:
    cost = units * 5
print(cost)

# #Question 7:
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("num1 is greatest")
        else:
            print("num4 is greatest")
    else:
        if num3 > num4:
            print("num3 is greatest")
        else:
            print("num4 is greatest")
else:
    if num2 > num3:
        if num2 > num4:
            print("num2 is greatest")
        else:
            print("num4 is greatest")
    else:
        if num3 > num4:
            print("num3 is greatest")
        else:
            print("num4 is greatest")

# #Question 8:
year = int(input())
if (year%400 == 0 or year%100 != 0) and year%4 == 0:
    if year%100 == 0:
        print(f"{year} is leap year and century year")

# #Question 9:
weight = int(input())
height = int(input())
height *= height
BMI = weight/height
if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")

# #Question 10:
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 < num2:
    if num1 < num3:
        print("num1 is smallest")
    else:
        print("num3 is smallest")
else:
    if num2 < num3:
        print("num2 is smallest")
    else:
        print("num3 is smallest")

# For loop Problems

# #Question 1:
for i in range(100,1000):
    x = str(i)
    sum = 0
    for y in x:
        sum += int(y) ** 3
    if sum == i:
        print(i)

# #Question 2:
n = int(input())
for i in range(2,n):
    if i == 2:
        print(i)
    for j in range(2,i):
        if j > i/2:
            print(i)
            break
        if i%j == 0:
            break
    
# #Question 3:
for i in range(500):
    if i % 3 != 0:
        continue
    x = str(i)
    sum = 0
    for y in x:
        sum += int(y)
    if sum < 11:
        print(i)

# #Question 4:
n = int(input())
for i in range(n):
    print((n - i)  * ' ' + (i*2+1) * '*')

# #Question 5:
inputstr = input()
inputstr = set(inputstr)
if len(inputstr) == 26:
    print('pangram')

# #Question 6:
prime = []
for i in range(2,101):
    if i == 2:
        print(i)
    for j in range(2,i):
        if j > i/2:
            prime.append(i)
            break
        if i%j == 0:
            break
for i in range(99):
    if i in prime and i+2 in prime:
        print(i,i+2)

# #Question 7:
num = int(input())
x = str(num)
sum = 0
for y in x:
    sum += int(y)
if num%sum == 0:
    print('Harshad')

# #Question 8:
numRows = int((input()))
if numRows == 1:
    print( [[1]] )
x = [[1],[1,1]]
if numRows == 2:
    print(x)
i = 2
while(i < numRows):
    i += 1
    a = x[-1]
    l = [1]
    for y in range(len(a)-1):
        l.append(a[y] + a[y+1])
    l.append(1)
    x.append(l)
print(x)

# #Question 9:
num = int(input())
sum = 0
for i in range(1,num+1):
    sum += i ** 2
print(sum)

# #Question 10:
num = int(input())
x = str(num)
sum = 0
for i in x:
    if i == '0':
        sum += 1
    mul = 1
    for j in range(1,int(i)+1):
        mul *= j
    sum += mul
if sum == num:
    print('strong num')

# Whle loop problems

# #Question 11:
num = int(input()[::-1])
i = 1
prime = True
while prime and i < num:
    i += 1
    if num % i == 0:
        prime = False
if prime:
    print(prime)

# #Question 12:
sum = 0 
while sum < 101:
    num = int(input())
    sum += num

# #Question 13:
num = input()
Duck = False
i = 0
while not Duck and i < (len(num) - 1):
    i += 1
    if num[i] == '0':
        Duck = True
        print('Duck')

# #Question 14:
num = input()
i = -1
while i < len(num)-1:
    pass
    for x in num:
        pass

##Question 15:
num = int(input())
i = 2
largest = 0
while i <= num:
    if num % i == 0:
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    prime = False
                    break
        if prime:
                largest = i
        num = num // i
    else:
            i += 1
print(largest)


