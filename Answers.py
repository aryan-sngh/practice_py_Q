
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
# n = input("enter a character")
# vowelCount = 0
# nonVowelCount = 0
# for i in n:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         vowelCount+=1 
#     else:
#         nonVowelCount+=1
# print(vowelCount,nonVowelCount)

#23
#n = int(input("enter your unit:"))
# price = 0
# if n<=100:
#     price = 0
# elif n>100 and n<=300:
#     price = (n-100)*2
# else:
#     price = 0 + (200*2) + (n-300)*5
# print(price)

#24
# n = int(input("enter the number of days"))
# price = 0
# if n<=5:
#     price = n*2
# elif n>5 and n<=10:
#     price = n*3
# elif n>10 and n<=15:
#     price = n*4
# else:
#     price = n*5
# print(price)

#25
# n = int(input("enter the kilometer:"))
# price = 0
# if n<=10:
#     price = n*11
# elif n>10 and n<=100:
#     price = (10*11) + (n-10)*10
# else:
#     price = (10*11) + (90*10) + (n-100)*9
# print(price)

#26
# n = int(input("enter the number for digitsum"))
# digitsum = 0
# while n>0:
#     u = n%10
#     sq = u**2
#     digitsum += sq
#     n = n//10
# print(f"square of digit = {digitsum}")    

#27 
# n = int(input("enter the number for cube of digit"))
# digitsum = 0
# while n>0:
#     u = n%10
#     sq = u**3
#     digitsum +=sq
#     n = n//10
# print(f"cube of digit = {digitsum}")

#28
# n = int(input("enter the number for product of digit"))
# product = 1
# while n>0:
#     u = n%10
#     product*=u
#     n = n//10
# print(f"product of digit = {product}")


#29
# n = int(input("enter number for reverse"))
# rev = 0
# while n>0:
#     u = n%10
#     rev = rev*10 + u
#     n = n//10
# print(rev)

#30
# n = int(input("enter number for checking palindrome"))
# og = n
# rev = 0
# while n>0:
#     u = n%10
#     rev = rev*10 + u
#     n = n//10
# print(rev)
# if rev == og:
#     print("palindrome")
# else:
#     print("not palindrome")
    
#31
# n = int(input("enter the number for checking a armstomg"))
# og = n
# digitcube = 0
# while n>0:
#     u = n%10
#     cb = u**3
#     n = n//10
# print(digitcube)
# if digitcube == u:
#     print("armstong")
# else:
#     print("not armstong")
    

#32
# for i in range(1,11):
#     print(i)
    
#33
# for i in range(1,11):
#     if i%2==0:
#         print(i)
    
#34
# for i in range(1,11):
#     if i%2!=0:
#         print(i)
        
#35
# sum = 0
# for i in range(1,11):
#     sum+=i
# print(sum)


#36
# evenSum = 0
# for i in range(1,11):
#     if i%2==0:
#         evenSum+=i
# print(evenSum)
    
#37
# oddsum = 0
# for i in range(1,11):
#     if i%2!=0:
#         oddsum+=i
# print(oddsum)

#38
# evenSum = 0
# oddSum = 0
# for i in range(1,11):
#     if i%2==0:
#         evenSum+=i
#     else:
#         oddSum+=i
# print(evenSum,oddSum)        

#39
# fact = 1
# n = int(input("enter the number for factorial:"))
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#40
# n = input("enter the string for finding a length")
# length = 0
# for i in n:
#     length+=1
# print(length)


#41
# a = input("enter the string 1")
# b = input("enter the string 2")
# if len(a) == len(b):
#     print("equal")
# else:
#     print("not equal")
    
#42
# n = input("enter the string for checking vowel or consond:")
# vowelCount = 0
# consondCount = 0
# for i in n:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         vowelCount+=1
#     else:
#         consondCount+=1
        
# print(vowelCount,consondCount)

# #43
# n = input("enter the string:")
# for i in range(len(n)-1,-1,-1):
#     print(n[i],end="")
    
#44
# for i in range(10,0,-1):
#     print(i)

#45
# n = input("enter the string")
# item = input("enter the finding char:")
# freq =0
# other = 0
# for i in n:
#     if item == i:
#         freq+=1
#     else:
#         other+=1
# print(freq,other)        

#46
# n = input("enter the string")
# for i in range(0,len(n)):
#     print(f"{n[i]}-->{i}")
    
#47
# n = int(input("enter the term"))
# for i in range(2,n+1):
#     for j in range(2,n+1):
#         if(i%j==0):
#            break
#     if(i==j):
#         print("prime",i)
    
#48
# evenSum = 0
# oddSum = 0
# for i in range(12,38):
#     if(i%2==0):
#         evenSum+=i
#     else:
#         oddSum+=i
# print(evenSum,oddSum)

#49
# for i in range(100,501):
#     if i%11==0 and i%2!=0:
#         print(i)
            

#50
# i = 1
# while(i<=10):
#     print(f"{i}-->{i**2}")
#     i+=1


#51
# i = 1
# while(i<=30):
#     print(i*10,end=",")
#     i+=1

#52
# i = 105
# while(i>=1):
#     print(i,end=",")
#     i-=7

#53
# i = 10
# while(i>=1):
#     print(i)
#     i-=1

#54
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")
#     print()


#55
# i = 1
# n = int(input("enter a number which table you want?:"))
# while(i<=10):
#     print(f"{n}x{i}={n*i}")
#     i+=1


#56
# n = int(input("enter the number:"))
# i=1
# while(i<=n):
#     if i%2==0:
#         print(i)
#     i+=1
    
    
#57
'''already done'''

#58
# n = int(input("enter the terms:"))
# if n==1:
#     print("1")
# elif n==2:
#     print("1,1")
# else:
#     a=0
#     b=1
#     print(b,end=" ")
#     c=0
#     while(n>0):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
#         n-=1
    
    
#59
# i=1
# n = int(input("ENTER the number to find factorial:"))
# fact=1
# while(i<=n):
#     fact*=i
#     i+=1
# print(fact)
    
#60
'''already done'''

#61
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#62
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

#63
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#64
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#65
