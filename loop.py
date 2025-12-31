# #1
# for x in range(5):
#     x=x+1
#     if x%2==0:
#         print(f"{x} even")
#     else:
#         print(f"{x} odd")

# list = [10,20,30,40]
# sum1=0
# #2
# for x in list:
#     sum1=sum1 + x
#     print(f"Added {x} Running total {sum1}")
# print("-"*20)
# print(f"Total sum: {sum1}")
# #3

# student_names = ["Ram", "Hari", "Sita"]

# print("-- Email Greetings Generated --")

# for x in student_names:
#     print(f"Hi! {x} your course approval is ready")


# #4

# page_count=[45,30,50,40]
# print("--- Book Chapter Summary ---")
# for x in range(len(page_count)):
#     print(f"ch {x} has {page_count[x]} pages")

# #5

# nums= [4,5,3,2]
# product=0
# for x in range (len(nums)):
#     if x==0:
#         product=nums[x]
#     else:
#         product=product*nums[x]
# print(f"Product of all numeric values: {product}")

# #6

# print("-----Multipication of 11 till 10-----")
# for x in range(10):
#     print(f"11*{x+1}={11*(x+1)}")
    
# #7

# students = [

#     {"name": "ram", "math_grade": 43},

#     {"name": "hari", "math_grade": 65},

#     {"name": "sita", "math_grade": 90}

# ]

# for x in students:
#     if x["math_grade"]>=70:
#         x["status"]="approved"
#     else:
#         x["status"]="Rejected"
# print(students)


# #8

# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]

# for x in list1:
#     if x in list2:
#         print(f"{x} is common")

# #9

# lst=[1,2,3,4]
# for x in lst:
#     if str(x) in ("14"):
#         print(x)

# #10

# lst=[1,2,3,4]
# for x in lst:
#     if str(x) in ("124"):
#         print(x)

# #11
# lst=[1,2,3,4]
# for x in lst:
#     if x==3:
#         lst.remove(x)
#         lst.insert(1,"a")
# print(lst)


# #12

# lst=[1,2,3,4,5]
# odd_lst=[]
# even_lst=[]
# for x in lst:
#     if x%2==0:
#         even_lst.append(x)
#     else:
#         odd_lst.append(x)

# print(even_lst)
# print(odd_lst)


# #13
# num=int(input("Enter a number: ")) 
# flag= True
# for x in range(2,num):
#     if num==1 or num==2:
#         break
#     if num%x==0:
#         flag=False
#         break
#     else:
#         pass
# if flag==True:
#     print(f"{num} is prime")
# elif flag==False:
#     print(f"{num} is not prime")

# #14
# lst=[1,2,3,4,"a","b"]
# inegers=[]
# strings=[]
# for x in lst:
#     if type(x)==int:
#         inegers.append(x)
#     else:
#         strings.append(x)
# print(inegers)
# print(strings)

#15

# to_find=input("Enter something: ")
# dig_count=0
# ltr_count=0

# for x in to_find:
#     if x in "0123456789":
#         dig_count=dig_count+1
#     else:
#         ltr_count= ltr_count+1
# print(dig_count)
# print(ltr_count)

#16

# password="password123"
# username="Ram"
# for x in range(3):
#     validation=input("Enter your username: ")
#     val_pass=input("Enter your password: ")
#     if validation==username and val_pass==password:
#         print("logged in succesfully")
#         break
#     else:
#         print("Invalid user name or password. ")
#         print(f"{3-(x+1)} attempts left")

#18

# number=int(input("Enter number to find factorial: "))
# factorial=1
# for x in range(number):
#     factorial= factorial*(number-x)
# print(factorial)

#19

# for x in range (1,10):
#     for y in range(1,11):
#         print(f"{x}*{y}={x*y}")
#         
# #21

# min=int(input("Enter the lowest number: "))
# max=int(input("Enter the largest number: "))
# odd_num=0
# for x in range(min,max):
#     if x%2!=0:
#         odd_num=odd_num+x
# print("the sum of all odd numbers in the range is", odd_num)

## 22
# min=int(input("Enter the lowest number: "))
# max=int(input("Enter the largest number: "))
# even_num=0
# for x in range(min,max):
#     if x%2==0:
#         even_num=even_num+x
# print("the sum of all odd numbers in the range is", even_num)  

##23
# something=input("Enter something: ")
# space_count=0
# for x in something:
#     if x==" ":
#         space_count+=1
# print(f"There are {space_count} spaces")

##24
# lst=[1,2,3,4]
# for x in range(len(lst)):
#     lst[x]=(lst[x])**3
# print(lst)

##25

# a="programming"
# b=""
# for x in range(len(a)):
#     b=b + a[-1-x]
# print(b) 

#26

# for x in range(50):
#     print(x)
#     if x==7:
#         break

# #27

# a=input("Enter something: ")
# for x in a:
#     print(x)

# #28

# a=["ram","shyam",1,2]
# for x in a:
#     if type(x)==str:
#         print(f"Hello! {x}")


##29

# a=["ram","shyam",1,2]
# lst=[]
# for x in a:
#     lst.append(f"Dr.{x}")

# print(lst)

##30

# lst=[]
# flag=True
# while flag:
#     num=(input("Enter the numbers to add in list(Exit for end): ")).lower()
    
#     if num=="exit":
#         break
#     else:
#         lst.append(int(num))
# print(lst)
# lst1=[]
# for x in lst:
#     lst1.append(x**2)
# print(lst1)

##31

# lst1=[111, 32, -9, -45, -17, 9, 85, -10,111]
# pos_list=[]
# for x in lst1:
#     if x not in pos_list:
#         if x>0:
#             pos_list.append(x)

# print(pos_list)


# #32
# list=[0,1,2,3,4,5,6]

# for x in list:
#     if str(x) not in "36":
#         print(x)


##33

# lst=[1,"1"]
# type_list=[]
# for x in lst:
#     type_list.append(type(x))
# print(type_list)

##34

# for x in range(5):
#     pass
# else:
#     print("Done")

##35

# num=105
# print(num)
# for x in range(50):
#     num= num-7
#     print(num)
#     if num==7:
#         break
    

##36

# bad_chars = [';', ':', '!', "*"]
# string = "py;th* o:n ! ;py * t*h:o !n"
# for x in string:
#     if x in bad_chars:
#         string=string.replace(x,"")
# string=string.replace(" ","")
# print(string)

# #37

# nums=[1,33523,234236,32,321,423,412,12142,242,234]
# odd_count=0
# even_count=0
# for x in nums:
#     if x%2==0:
#         even_count=even_count+1
#     else:
#         odd_count=odd_count+1
# print(odd_count)
# print(even_count)

##38

# for x in range(3,100):
#     if x%3==0 or x%5==0:
#         print(x)

##39

# odd_sum=0
# even_sum=0

# for x in range(1,101):
#     if x%2==0:
#         even_sum=even_sum +x
#     else:
#         odd_sum=odd_sum+x
# print(even_sum)
# print(odd_sum)

##40

# nums=["1001","2001","3001","3003"]
# for x in nums:
#     rev_num=x[::-1]
#     if x==rev_num:
#         print(f"{x} is palindrome")
#     else:
#         print(f"{x} is not palindrome")

##41

# nums=[153,370,371,4007,23423,34,23234,1634,54748,912985153]
# for x in nums:
#     a=str(x)
#     armstron_sum=0
#     for y in range(len(a)):
#         armstron_sum= armstron_sum + (int(a[y]))**(len(a))
#     if armstron_sum==x:
#         print(f"{a} is armstrong number")
#     else:
#         print(f"{a} is not armstron number")
        
    
##42

# something=input("Enter something: ")
# for x in something:
#     if x in "aeiou":
#         something=something.replace(x,"")
# something=something.replace(" ","")
# print(something)



 











    