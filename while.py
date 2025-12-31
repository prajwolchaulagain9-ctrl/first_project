import random as rd

# #1
# flag=True
# while flag:
#     age1=input("Enter your age (stop to exit): ").lower()
#     if age1  == "stop":
#         break
#     age=int(age1)
#     if age<18:
#         print("You are a minor.")
#     elif age>=18 and age<60:
#         print("You are an adult.")
#     else:
#         print("You are a senior citizen.")
    
#     #2 

# flag=True
# while flag:
#     vehicle_type=input("Enter vehicle type : ").lower()
#     if vehicle_type !='bus':
#         print("waiting")
#     else:
#         print("finally the wait is over")
#         flag=False

# #3

# flag=True
# while flag:
#     fruit=input("Enter fruit name: ").lower()
#     if fruit !='apple':
#         print("try again")
#     else:
#         print("you got it!")
#         flag=False
# #4

# flag=True
# while flag:
#     password=input("Enter password: ")
#     if password !='open sesame':
#         print("try again")
#     else:
#         print("Access granted")
#         flag=False


# #5

# Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
# content_rating= {}
# index=0
# while index < len(Ratings):
#     rating=Ratings[index]
#     if rating in content_rating:
#         content_rating[rating] += 1
#     else:
#         content_rating[rating] = 1
#     index += 1
# print(content_rating)


# #6

# import random as rd
# number_to_guess=rd.randint(1,10)
# guess_needed=0
# flag=True
# while flag:
#     guessed_num=int(input("Gues a number between 1-10: "))
#     guess_needed+=1
#     if number_to_guess==guessed_num:
#         print(f"{guess_needed} guesses needed")
#         break
#     elif number_to_guess>guessed_num:
#         print("Guess higher")
#     else:
#         print("Guess lower")

#7

# username= "insideout"
# password= "123456789"
# flag=True
# count=0
# while count<3:
#     username_input=input("Enter your username: ")
#     password_input= input("Enter your password: ")
#     if username==username_input and password==password_input:
#         print("Login successfull")
#     else:
#         print("Invalid username or password")
#         count=count+1
# else:
#     print("Too many failed attempts")
        

#8

# flag=True
# while flag:
#     num1=rd.randint(1,30)
#     num2=rd.randint(1,30)
#     product_to_guess= num1 * num2
#     print(product_to_guess)
#     while flag:
#         guessed_product= input(f"{num1}*{num2}=         (exit to finish):   ").lower()
#         if guessed_product=='exit':
#             flag=False
#             print("Exit successfull")
#             break
#         guessed_product_int=int(guessed_product)
#         if guessed_product_int==product_to_guess:
#             print("Number found")
#             print("Now next question")
#             break
#         else:
#             print("Incorrect, try again")

#9

# flag=True
# while flag:
#     num=input("Enter a number to check if prime (exit to stop): ").lower()
#     if num=='exit':
#         print("Exit successfull")
#         break
#     num_int=int(num)
#     count=3
#     if num ==1 or num==2:
#         print("The number is prime")
#     else:
#         while count<num_int:
#             if num_int%count==0:
#                 print("The number is NOT prime")
#                 break
#             count+=1
#         else:
#             print("The number is prime")


#10


# flag=True
# secret="Eat"
# while flag:
#     secret_input=input("Enter secret (exit to stop): ")
#     if secret_input=="exit":
#         print("Exit successfull")
#         break
#     elif secret_input !=secret:
#         print("Incorrect, try again")
    
#     else:
#         print("you guessed the word")
#         flag=False

#11

inputs={}
flag=True
while flag:
    name=input("Enter a name")
    if name not in inputs:
        inputs[name]=1
        print(f"You have typed {name} ")



















