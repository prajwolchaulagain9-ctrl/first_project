# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# operator=input("Enter operator (+, -, *, /): ")

# if operator=='+':
#     result=num1+num2
#     print("The sum is:", result)
# elif operator=='-':
#     result=num1-num2
#     print("The difference is:", result)
# elif operator=='*': 
#     result=num1*num2
#     print("The product is:", result)
# elif operator=='/':
#     if num2!=0:
#         result=num1/num2
#         print("The quotient is:", result)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operator. Please use +, -, *, or /.")

# operation={"+": num1+num2,
#            "-": num1-num2,
#            "*": num1*num2,
#            "/": num1/num2 if num2!=0 else "Error: Division by zero is not allowed."}
# print(f"The result is :{operation[operator]}")


# age=int(input("Enter your age: "))

# if age>=18:
#     print("You are eligible to vote.")
# elif age<0:
#     print("Invalid age entered.")
# else:
#     print("You are not eligible to vote yet.")

# username= "KingKong"
# password= "Banana123"

# input_username= input("Enter your username: ")
# input_password= input("Enter your password: ")

# if input_username==username and input_password==password:
#     print("Login successful")
# else:
#     print("Invalid username or password"

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))

# if num1>num2:
#     print(f"{num1} is greater than {num2}")
# elif num1<num2:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both numbers are equal")
#     if num1<0:
#         print("Both numbers are negative")
#     elif num1>0:
#         print("Both numbers are positive")
#     else:
#         print("Both numbers are zero")



# sub1=int(input("Enter marks for subject 1: "))
# sub2=int(input("Enter marks for subject 2: "))
# sub3=int(input("Enter marks for subject 3: "))
# sub4=int(input("Enter marks for subject 4: "))

# total_marks= sub1+sub2+sub3+sub4
# print("Total marks:", total_marks)
# percentage= (total_marks/400)*100
# print("Percentage:", percentage)
# if percentage>=70:
#     print("Grdae: Distinction")
# elif percentage>=60:
#     print("Grade: First")
# elif percentage>=40:
#     print("Grade: Pass")
# elif percentage<40:
#     print("Grade: Fail")

# cost_of_bike= int(input("Enter the cost of the bike: "))

# if cost_of_bike>100000:
#     tax= 0.15 * cost_of_bike
#     print("The road tax is:", tax)
# elif 50000<cost_of_bike <=100000:
#     tax= 0.10 * cost_of_bike
#     print("The road tax is:", tax)
# else:
#     tax= 0.05 * cost_of_bike
#     print("The road tax is:", tax)


# time_of_serice= int(input("Enter the time of service in years: "))
# salary= int(input("Enter the salary: "))
# if time_of_serice<=0:
#     print("No bonus for you")
# elif time_of_serice>10:
#     bonus= 0.10 * salary
#     print("The bonus is:", bonus)
# elif 6<=time_of_serice <=10:
#     bonus= 0.08 * salary
#     print("The bonus is:", bonus)
# else:
#     bonus= 0.05 * salary
#     print("The bonus is:", bonus)


# membership= bool(int(input("Are you a member? (1 for Yes, 0 for No): ")))

# print(membership)
# total_bill= int(input("Enter the total bill amount: "))

# if membership==True and total_bill>1000:
#     discount= 0.20 * total_bill
#     final_amount= total_bill - discount
#     print("You get a 20% discount. Final amount to pay:", final_amount)
# elif membership==False and total_bill>1000:
#     discount= 0.10 * total_bill
#     final_amount= total_bill - discount
#     print("You get a 10% discount. Final amount to pay:", final_amount)
    

# earth_weight= float(input("Enter your weight on Earth (in kg): "))
# plater_num= int(input("Enter the planet number (1-7): "))

# if plater_num==1:
#     mercury_weight= earth_weight * 0.38
#     print("Your weight on Mercury is:", mercury_weight, "kg")
# elif plater_num==2:
#     venus_weight= earth_weight * 0.91
#     print("Your weight on Venus is:", venus_weight, "kg")
# elif plater_num==3:
#     mars_weight= earth_weight * 0.38
#     print("Your weight on Mars is:", mars_weight, "kg")
# elif plater_num==4:
#     jupiter_weight= earth_weight * 2.53
#     print("Your weight on Jupiter is:", jupiter_weight, "kg")
# elif plater_num==5:
#     saturn_weight= earth_weight * 1.07
#     print("Your weight on Saturn is:", saturn_weight, "kg")
# elif plater_num==6:
#     uranus_weight= earth_weight * 0.89
#     print("Your weight on Uranus is:", uranus_weight, "kg")
# elif plater_num==7:
#     neptune_weight= earth_weight * 1.14
#     print("Your weight on Neptune is:", neptune_weight, "kg")
# else:
#     print{"Invalid planet number. Please enter a number between 1 and 7.")

# planet_dict={1: {'name':'mercury','gravity':0.38},
#              2: {'name':'venus','gravity':0.91},
#              3: {'name':'mars','gravity':0.38},
#              4: {'name':'jupiter','gravity':2.53},
#              5: {'name':'saturn','gravity':1.07},
#              6: {'name':'uranus','gravity':0.89},
#              7: {'name':'neptune','gravity':1.14}}
# if plater_num in planet_dict:
#     planet_weight= earth_weight * planet_dict[plater_num]
#     print(f"Your weight on {planet_dict[plater_num]["name"]} is: {planet_weight} kg")
# else:
#     print("Invalid planet number. Please enter a number between 1 and 7.")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1==num2==num3:
    print("All three numbers are equal.")
elif num1>num2 and num1>num3:
    print(f"{num1} is the greatest number.")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest number.")
else:
    print(f"{num3} is the greatest number.")

print("Thank you for using the program!")













