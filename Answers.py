
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
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#66
# for i in range(5,0,-1):
#     for j in range(i,6): 
#         print(i,end=" ")
#     print()

#67
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

#68
# for i in range(1,6):
#     count = 1
#     for j in range(5,0,-1):
#         if i<j:
#             print(" ",end=" ")
#         else:
#             print(count,end=" ")
#             count+=1
#     print()

#69
# for i in range(1,6):
#     for j in range(5,0,-1):
#         if i<j:
#             print(" ",end=" ")
#         else:
#             print(i,end=" ")
#     print()

#70
# for i in range(1,6):
#     for j in range(5,0,-1):
#         if i<j:
#             print(" ",end=" ")
#         else:
#             print(j,end=" ")
#     print()

#71
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
    
    
#72
# count = 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count+=1
#     print()

#73
# for i in range(0,5): 
#     for j in range(0,i+1):
#         print(i*j,end=" ")
#     print()

#74
# for i in range(0,5):
#     for j in range(0,i+1):
#         if j==0:
#             print('A',end="")
#         elif j==1:
#             print('B',end="")
#         elif j==2:
#             print('C',end="")
#         elif j==3:
#             print('D',end="")
#         elif j==4:
#             print('E',end="")
#         print(" ",end="")
#     print()    
    
#75
# for i in range(0,5):
#     for j in range(0,i+1):
#         if i==0:
#             print('A',end="")
#         elif i==1:
#             print('B',end="")
#         elif i==2:
#             print('C',end="")
#         elif i==3:
#             print('D',end="")
#         elif i==4:
#             print('E',end="")
#         print(" ",end="")
#     print()    


#77
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(j**2,end=" ")
#     print()

#78
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i**2,end=" ")
#     print()

#79
# for i in range(1,10):
#     for j in range(1,i+1):
#         if(i%2!=0):
#             print(i,end=" ")
#     print()

#80
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#81
# for i in range(5,0,-1):
#     for i in range(1,i+1):
#         print("*",end=" ")
#     print()

#82
# for i in range(1,6):
#     for j in range(5,0,-1):
#         if i<j:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()

#83
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")
#     print()

#84
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end="")
#     print()

#88
# n = input("enter the string")
# m = {}
# for i in n:
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# print(m)

#89
# l=[]
# n=int(input("enter the number of elements"))
# for i in range(1,n+1):
#     a=int(input('enter the elememts'))
#     l.append(a)
# print(l)

#90
# l=[]
# n = int(input("enter the number of size in list"))
# for i in range(n):
#     a=int(input("enter the elements"))
#     l.append(a)
# print(l)
# e=[]
# for j in l:
#     if j%2==0:
#         e.append(j)
# print(e)
        
    
#91
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements"))
#     l.append(a)
# print(l)
# e=[]
# for j in l:
#     if j%2!=0:
#         e.append(j)
# print(e)

#92
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# esum=0
# osum=0
# for i in l:
#     if(i%2==0):
#         esum+=i
#     else:
#         osum+=i
# print(esum,osum)

#93
# l=[]
# n=int(input("enter the size of list"))
# for i in range(n):
#     a=int(input("enter the elements"))
#     l.append(a)
# print(l)
# m={}
# for i in l:
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# print(m)

#94
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# max=l[0]
# for i in range(1,len(l)):
#     if l[i]>max:
#         max=l[i]
# print(max)


#95
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# min=l[0]
# for i in range(1,len(l)):
#     if l[i]<min:
#         min=l[i]
# print(min)

#96
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# max=l[0]
# smin=l[0]
# for i in range(1,len(l)):
#     if l[i]>max:
#         smax=max
#         max=l[i]
#     elif l[i]>smax:
#         smax=l[i]
# print(smax)
# print(max)

#97
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# min=l[0]
# smin=l[0]
# for i in range(1,len(l)):
#     if l[i]<min:
#         smin=min
#         min=l[i]
#     elif l[i]<smin:
#         smin=l[i]
# print(smin)
# print(min)

#98
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# primeList=[]
# for i in l:
#     if(i==1 or i==0):
#         print("neither prime nor composite",i)
#     else:
#         for j in range(2,i):
#             if(i%j==0):
#                 break
#         else:
#             primeList.append(i)
# print(primeList)
    
    
#99
'''already done'''

#100
# n = "aryan"
# m = n[::-1]
# print(m)
    
        
#101
# n = "aryansingh"
# m={}
# for i in n:
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# print(m)

#102
# def add(a,b,c):
#     summ=a+b+c
#     return summ

# print(add(2,3,4))

#103
# def evenFinder(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(evenFinder(int(input("enter the number"))))

#104
# def totalSum(sum):
#     for i in range(1,11):
#         sum+=i
#     return sum
# print(totalSum(sum=0))
    
    
#105
# def countt(evenCount,oddCount):
#     for i in range(1,12):
#         if i%2==0:
#             evenCount+=1
#         else:
#             oddCount+=1
#     return evenCount,oddCount

# print(countt(evenCount=0,oddCount=0))
            
#106
# def summ(evenSum,oddSum):
#     for i in range(1,11):
#         if i%2==0:
#             evenSum+=i
#         else:
#             oddSum+=i
#     return evenSum,oddSum

# print(summ(evenSum=0,oddSum=0))


#107
# def table(n):
#     i=1
#     while(i<=10):
#         print(f"{n}x{i}={n*i}")
#         i+=1
# table(n=5) 


#108
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# print(factorial(n=5))    

#109
# def primeFinder(n):
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")

# n=int(input("enter the number"))    
# if n==0 or n==1:
#     print("neither prime nor composite")
# else:
#     primeFinder(n)
    
    
#110
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the element"))
#     l.append(a)
# print(l)
# for i in range(len(l)):
#     temp=l[0]
#     l[0]=l[len(l)-1]
#     l[len(l)-1]=temp
# print(l)

#or
# def swap(l):
#     for i in range(0,len(l)):
#         temp = l[0]
#         l[0]=l[len(l)-1]
#         l[len(l)-1]=temp
#     return l
# l=[1,2,3,4,5]
# print(swap(l))

#111
# def swap(l,n1,n2):
#     for i in range(len(l)):
#         temp = l[n1]
#         l[n1] = l[n2]
#         l[n2] = temp
#     return l
# l=[1,2,3,4,5]
# print(swap(l,1,3))


#112
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# print(len(l))

#113
'''already done'''

#114
'''already done'''

#115
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# item=int(input("enter the element to find"))
# for i in l:
#     if item==i:
#         print("true")
#         break
# else:
#     print("false")

#116
# l=[1,2,4,5,2,1]
# print(l)
# l.clear()
# print(l)

#117
# l=[1,2,3,4,5]
# l.reverse()
# print(l)

#118
# l1=[1,2,3,4,5,6]
# l2=[22,53,67,34]
# print(l1)
# print(l2)
# l2.copy()
# print(l2)

#119
'''done'''

#120
# l=[1,2,3,4,5]
# sum=0
# for i in l:
#     sum+=i
# print(f"average of list={sum/len(l)}")


#122
# l=[1,2,3,4,5]
# multi=1
# for i in l:
#     multi*=i
# print(multi)

#123
# l=[12,3,4,55,3]
# min = l[0]
# for i in range(len(l)):
#     if l[i]<min:
#         min=l[i]
#         break
# print(min)

#124
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# max=l[0]
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
# print(max)

#125
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# max=l[0]
# smax=l[0]
# for i in range(len(l)):
#     if l[i]>max:
#         smax=max
#         max=l[i]
#     elif l[i]>smax:
#         smax=l[i]
# print(smax,max)


#126
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# min=l[0]
# smin=l[0]
# for i in range(len(l)):
#     if l[i]<min:
#         smin=min
#         min=l[i]
#     elif l[i]<smin:
#         smin=l[i]
# print(min,smin)

#127
'''already done'''

#128
'''already done'''

#129 , 130, 131,132,133

#134
# m={}
# for i in range(5):
#     a=int(input('enter element'))
#     m[i]=a
# print(m)
# x=sorted(m.values())
# print(x)


#135 
# m={'2':1,"5":2,"4":3}
# m.update({'6':8})
# print(m)

#136
# m={}
# n=int(input("enter the size of dict"))
# for i in range(n):
#     x=int(input("enter the keys:"))
#     z=int(input("enter the values"))
#     m[x]=z
# print(m)
# item=int(input("enter the item to find?:"))
# for i in m.keys():
#     if i==item:
#         print("yess")
#         break
# else:
#     print("not found")

#137
# m={}
# n=int(input("enter the size of dict"))
# for i in range(n):
#     m[i]=i**2
# print(m)


#138
# m={}
# n=int(input("enter the size of dict:"))
# for i in range(1,n+1):
#     m[i]=i**3
# print(m)

#139
# n=input("enter the string to find frequency:")
# m={}
# for i in n:
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# print(m)

#140
# t=(1,2,4,22,4,5)
# sum=0
# for i in t:
#     sum+=i
# print(sum)

#141
# t=(1,2,3,44,52,4)
# max=t[0]
# smax=t[0]
# for i in range(len(t)):
#     if t[i]>max:
#         smax=max
#         max=t[i]
#     elif t[i]>smax:
#         smax=t[i]
# print(smax,max)

#142
# t=(1,2,3,44,52,4)
# print(t)
# l=list(t)
# print(l)

#143
# l=[1, 2, 3, 44, 52, 4]
# print(l)
# t=tuple(l)
# print(t)

#144
# def fact(n):
#     if(n<=1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

#145
# def fib(n):
#     if(n<=1):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input("enter the number to check fib"))
# for i in range(n+1):
#     print(fib(i),end=" ")

#146
# l=[1,2,4,5,455,6]
# for i in range(len(l)):
#     for j in range(len(l)-1,-1,-1):
#         if l[i]+l[j]==9:
#             print(i,end=" ")
    
    
#147
# n="aryanchaudhary"
# if(len(n)<=10):
#     print(n)
# else:
#     print(n[0:11],"....")

#148
# l1=[1,2,3,4,5,6]
# l2=[1,2,4,4,5,6]
# l3=[]
# for i in range(len(l1)):
#     a=l1[i]+l2[i]
#     l3.append(a)
# print(l3)

#149
# l=[]
# n=int(input("enter the row:"))
# x=int(input("enrer the colunm:"))
# for i in range(n):
#     k=[]
#     for j in range(x):
#         a=int(input("enter the elements:"))
#         k.append(a)
#     l.append(k)
# print(l)
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j],end=" ")
#     print()
        
        
#150
# l=[]
# n=int(input("enter the row:"))
# h=int(input("enter the column"))
# for i in range(n):
#     k=[]
#     for j in range(h):
#         a=int(input("enter the elements:"))
#         k.append(a)
#     l.append(k)
# print(l)
# sum=0
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         sum+=l[i][j]
# print(sum)

#151
# l=[]
# n=int(input("enter the row:"))
# h=int(input("enter the column:"))
# for i in range(n):
#     k=[]
#     for j in range(h):
#         a=int(input("enter the elements:"))
#         k.append(a)
#     l.append(k)
# print(l)
# multi=1
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         multi*=l[i][j]
# print(multi)

#152
# l=[]
# n=int(input("enter the size of list:"))
# for i in range(n):
#     a=int(input("enter the elements:"))
#     l.append(a)
# print(l)
# l.sort()
# print(f"after sorting ={l}")
# item = int(input("enter the number to find there index:"))
# low = 0
# high = len(l)-1
# while(low<=high):
#     mid=(low+high)//2
#     if item==l[mid]:
#         print(mid)
#         break
#     elif item>l[mid]:
#         low=mid+1
#     else:
#         high=mid-1