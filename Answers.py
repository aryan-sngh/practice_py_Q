
##1
# a = int(input("enter the number"))
# b = int(input("enter the 2nd number:"))
# add = a + b
# sub = a - b
# multi = a * b
# divide = a/b
# print(add,sub,multi,divide)


##2
# a = int(input("enter any number:"))
# b = int(input("enter 2nd number:"))
# print(f"before swapping a = {a} and b = {b}")
# temp = 0
# temp = a
# a = b
# b = temp 
# print(f"after swapping a = {a} and b = {b}")

# #3
# a = int(input("enter any number:"))
# b = int(input("enter 2nd number:"))
# print(f"before swap a = {a} and b = {b}")
# a = a+b
# b = a-b
# a = a-b
# print(f"after swap a = {a} and b = {b}")


#4
# a = int(input("enter the number: "))
# if a%2==0:
#     print("even")
# else:
#     print("odd")
    
#5
# a = int(input("enter any number 1:"))
# b = int(input("enter any number 2:"))
# c = int(input("enter any number 3:"))
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
#     print("c is greater")

#6
# n = int(input("enter your percentage :"))
# if n>90 :
#     print("A grade")
# elif n>80 and n<=90:
#     print("b grade")
# elif n>=60 and n<=80:
#     print("c grade")
# else:
#     print("d grade")
    

#7 
# n = int(input("enter your bike price:"))
# Tax = 0
# if n>=100000:
#     tax = 15*n/100
# elif n<100000 and n>50000:
#     tax = 10*n/100
# else:
#     tax = 5*n/100
# print(f"tax = {tax}")
# print(f"on road price = {n+tax}")

#8
# wd = int(input("enter the working days"))
# pd = int(input("enter the per day income"))
# print(f"total salary of month={wd*pd}")

#9
# n = int(input("enter your time period:"))
# salary = int(input("enter your salary:"))
# bonus = 0
# if n>10:
#     bonus = 10*salary/100
# elif n>=6 and n<=10:
#     bonus  = 8*salary/100
# else:
#     bonus = 5*salary/100
# print(bonus)


#10
# a = int(input("enter 1st num:"))
# b = int(input("enter 2nd number:"))
# op = input("enter operator = +,-,/,*")
# answer = 0
# if op == "+":
#     answer = a+b
# elif op == '-':
#     answer = a-b
# elif op == '*':
#     answer = a*b
# elif op == '/':
#     answer = a/b
# else:
#     print('something wrong')
# print(f"final output = {answer}")



#11
# i = 1
# while i<=10:
#     print(i)
#     i+=1

#12
# i = 1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1
    
#13
# i = 1
# while i<=10:
#     if i%2!=0:
#         print(i)
#     i+=1    
    
#14
# i = 1
# sum = 0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)

#15
# i = 1
# evensum = 0
# while i<=10:
#     if i%2==0:
#         evensum+=i
#     i+=1
# print(evensum)

#16 
# i = 1
# oddsum = 0
# while i<=10:
#     if i%2!=0:
#         oddsum+=i
#     i+=1
# print(oddsum)

#17
# i = 1
# evensum = 0
# oddsum = 0
# while i<=10:
#     if i%2==0:
#         evensum+=i
#     else:
#         oddsum+=i
#     i+=1
# print(evensum,oddsum)

#18
# n = int(input("enter the number:"))
# digitsum = 0
# while n>0:
#     u = n%10
#     digitsum +=u
#     n=n//10
# print(digitsum)
    

#19
# n = int(input("enter the numbers"))
# print(f"last digit = {n%10}")


#20
# n = int(input("enter the year:"))
# if n%4==0 or n%400==0:
#     print("leap year")
# else:
#     print("not leap year")

#or
# n = int(input("enter years after 2000:"))
# for i in range(2000,n+1):
#     if i%4==0 or i%400==0:
#         print("leap year-->",i)
#     else:
#         print("not a leap year-->",i)
    
#21
# n = int(input("enter the number for checking prime number:"))
# if n==0 or n==1:
#     print("nither prime nor a composite")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
    
    
#22
