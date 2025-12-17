#question1
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1==num2==num3:
    print("All three numbers are equal.")
elif num1>=num2 and num1>=num3:
    print(f"{num1} is the greatest number.")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is the greatest number.")
else:
    print(f"{num3} is the greatest number.")

#question2

month_num=int(input("Enter month number (1-12): "))
month={1:"January",
       2:"February",
       3:"March",
       4:"April",
       5:"May",
       6:"June",
       7:"July",
       8:"August",
       9:"September",
       10:"October",
       11:"November",
       12:"December"}

if month_num in month:
    print(f"The month is {month[month_num]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

#question3

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")
temp=a
a=b
b=temp
print(f"After swapping: a = {a}, b = {b}")

#question4


membership=bool(int(input("Enter 1 for member, 0 for non-member: ")))
age=int(input("Enter your age: "))

if age<12:
    print("the ticket is free.")
elif 12<=age<=60:
    if membership:
        print("The ticket price is 150.")
    else:
        print("The ticket price is 200.")
elif age<0:
    print("Invalid age entered.")
else:
    print("You get a senior citizen discount. The ticket price is 100.")

#question5

electricity_usage=int(input("Enter electricity usage in units: "))
if electricity_usage<=100:
    bill_amount=electricity_usage*5
    print("The bill amount is:", bill_amount)
elif 100<electricity_usage<=300:
    bill_amount=100*5+(electricity_usage-100)*8
    print("The bill amount is:", bill_amount)
elif electricity_usage>300:
    bill_amount=100*5+200*8+(electricity_usage-300)*10
    print("The bill amount is:", bill_amount)

#question6

player1=input("Enter Player 1 choice (rock/paper/scissors): ").lower()
player2=input("Enter Player 2 choice (rock/paper/scissors): ").lower()

if player1==player2:
    print("It's a tie!")
elif player1=="rock":
    if player2=="scissors":
        print("Player 1 wins!")
    elif player2=="paper":
        print("Player 2 wins!")
elif player1=="paper":
    if player2=="rock":
        print("Player 1 wins!")
    elif player2=="scissors":
        print("Player 2 wins!")
elif player1=="scissors":
    if player2=="paper":
        print("Player 1 wins!")
    elif player2=="rock":
        print("Player 2 wins!")
else:
    print("Invalid input. Please enter rock, paper, or scissors.")

#question7

class1= int(input("Enter the number of students in Class 1: "))
class2= int(input("Enter the number of students in Class 2: "))
class3= int(input("Enter the number of students in Class 3: "))

total_students= class1 + class2 + class3

desk_needed= total_students //2
if total_students %2 !=0:
    desk_needed +=1
print("Total desks needed:", desk_needed)

#quesion8

lift_position= 5
requested_floor= int(input("Enter the requested floor (1-7): "))
if requested_floor <1 or requested_floor >7:
    print("Invalid floor number. Please enter a number between 1 and 7.")
elif requested_floor == lift_position:
    print("stay at current floor.")
elif requested_floor > lift_position:
    print("Move up to floor", requested_floor)
else:
    print("Move down to floor", requested_floor)

# question9

num=int(input("Enter a number: "))

if num>0:
    print("The number is positive.")
    if num %2==0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("Enter a positive number")

#question10

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")
    if num1<0:
        print("Both numbers are negative")
    elif num1>0:
        print("Both numbers are positive")
    else:
        print("Both numbers are zero")

#question11

num=int(input("Enter a number: "))

if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)

#question12

import random

fact_no= random.randint(0,5)

if fact_no==0:
    print("Flamingos turn pink from eating shrimp.")
elif fact_no==1:
    print("The only food that doesn't spoil is honey.")
elif fact_no==2:
    print("Shrimps can only swim backwards.")
elif fact_no==3:
    print("A taste bud's lifespan is about 10 days.")
elif fact_no==4:
    print("It is impossible to sneeze while sleeping")
else:
    print("It is illegal to sing-off in North Carolina.")

#question13
membership= bool(int(input("Are you a member? (1 for Yes, 0 for No): ")))

print(membership)
total_bill= int(input("Enter the total bill amount: "))

if membership and total_bill>1000:
    discount= 0.20 * total_bill
    final_amount= total_bill - discount
    print("You get a 20% discount. Final amount to pay:", final_amount)
elif total_bill>1000:
    discount= 0.10 * total_bill
    final_amount= total_bill - discount
    print("You get a 10% discount. Final amount to pay:", final_amount)
else:
    print("No discount applicable. Final amount to pay:", total_bill)

#question14

earth_weight= float(input("Enter your weight on Earth (in kg): "))
planet_num= int(input("Enter the planet number (1-7): "))

if planet_num==1:
    mercury_weight= earth_weight * 0.38
    print("Your weight on Mercury is:", mercury_weight, "kg")
elif planet_num==2:
    venus_weight= earth_weight * 0.91
    print("Your weight on Venus is:", venus_weight, "kg")
elif planet_num==3:
    mars_weight= earth_weight * 0.38
    print("Your weight on Mars is:", mars_weight, "kg")
elif planet_num==4:
    jupiter_weight= earth_weight * 2.53
    print("Your weight on Jupiter is:", jupiter_weight, "kg")
elif planet_num==5:
    saturn_weight= earth_weight * 1.07
    print("Your weight on Saturn is:", saturn_weight, "kg")
elif planet_num==6:
    uranus_weight= earth_weight * 0.89
    print("Your weight on Uranus is:", uranus_weight, "kg")
elif planet_num==7:
    neptune_weight= earth_weight * 1.14
    print("Your weight on Neptune is:", neptune_weight, "kg")
else:
    print("Invalid planet number. Please enter a number between 1 and 7.")

#question15
sub1=int(input("Enter marks for subject 1: "))
sub2=int(input("Enter marks for subject 2: "))
sub3=int(input("Enter marks for subject 3: "))
sub4=int(input("Enter marks for subject 4: "))

total_marks= sub1+sub2+sub3+sub4
print("Total marks:", total_marks)
percentage= (total_marks/400)*100
print("Percentage:", percentage)
if percentage>=70:
    print("Grdae: Distinction")
elif percentage>=60:
    print("Grade: First")
elif percentage>=40:
    print("Grade: Pass")
elif percentage<40:
    print("Grade: Fail")

#question16

cost_of_bike= int(input("Enter the cost of the bike: "))

if cost_of_bike>100000:
    tax= 0.15 * cost_of_bike
    print("The road tax is:", tax)
elif 50000<cost_of_bike <=100000:
    tax= 0.10 * cost_of_bike
    print("The road tax is:", tax)
else:
    tax= 0.05 * cost_of_bike
    print("The road tax is:", tax)

#question17

time_of_serice= int(input("Enter the time of service in years: "))
salary= int(input("Enter the salary: "))
if time_of_serice<=0:
    print("No bonus for you")
elif time_of_serice>10:
    bonus= 0.10 * salary
    print("The bonus is:", bonus)
elif 6<=time_of_serice <=10:
    bonus= 0.08 * salary
    print("The bonus is:", bonus)
else:
    bonus= 0.05 * salary
    print("The bonus is:", bonus)

#question18

sub_sore=int(input("Enter the subject score (0-100): "))

if sub_sore<0 or sub_sore>100:
    print("Invalid score. Please enter a score between 0 and 100.")
elif sub_sore>90:
    print("Congratulations! You have achieved a high grade.")
elif sub_sore>=50:
    print("Nice work! but you can do better.")
else:
    print("Unfortunately, you have failed. Please retake the course.")

#question19

age=int(input("Enter your age: "))
degree_completed= bool(int(input("Have you completed your degree? (1 for Yes, 0 for No): ")))

if age>=18 and degree_completed:
    work_experience= int(input("Enter your years of work experience: "))
    if work_experience>=3:
        print("Highly Eligible")
    elif 1<=work_experience<3:
        print("Eligible")
    elif work_experience<1:
        print("Under Review")
else:
    print("Not Eligible")


#question20

age=int(input("Enter your age: "))
gender=input("Enter your gender (M/F): ").upper()
num_of_days=int(input("Enter number of days you have want to work: "))
if gender in ["M","F"]:
    if 18<=age<30:
        if gender=="M":
            wages=num_of_days*700
            print("Your wages are:", wages)
        else:
            wages=num_of_days*750
            print("Your wages are:", wages)
    elif 30<=age<=40:
        if gender=="M":
            wages=num_of_days*800
            print("Your wages are:", wages)
        else:
            wages=num_of_days*850
            print("Your wages are:", wages)
    else:
        print("Not eligible for work.")
else:
    print("Please input only M or F for gender")

#question21

account_balance= 50000
card_valid=True
correct_pin="123"
input_pin= input("Enter your card PIN: ")

if card_valid and input_pin==correct_pin:
    menu="""
    1. Withdraw
    2. Check Balance
    3.Exit"""
    print(menu)
    task=int(input(f"Select an option from the menu:) "))
    if task==1:
        withdraw_amt=int(input("Enter amount to withdraw: "))
        if withdraw_amt<=account_balance:
            account_balance -=withdraw_amt
            print(f"Please collect your cash. Your new balance is: {account_balance}")
        else:
            print("Insufficient balance.")
    elif task==2:
        print(f"Your account balance is: {account_balance}")
    elif task==3:
        print("Thank you for visiting")
    else:
        print("Invalid input. Please select a valid option.")
else:
    print("Card is invalid or PIN is incorrect.")


#question22

print("Welcome to the Magic Forest")

choice1=input("Do you want to go north or south").lower()

if choice1=="south":
    print("Game over")
else:
    choice2=input("Do you want to cross the river or follow the path? (c for cross and f for follow)").lower()
    if choice2=="c":
        print("Game over")
    else:
        choice3=input("Choose fairy,ogre or elf (f/o/e)").lower()
        if choice3=="o" or choice3=="e":
            print("Game over")
        else:
            print("You win!")

#question23
print("Welcome to the Haunted House")

option1=input("choose to go upstairs or downstairs (u/d)").lower()
if option1=="d":
    print("Game over")
else:
    option2=input("do you want to enter or stay outside (e/s)").lower()
    if option2=='e':
        print("Game over")
    else:
        option3=input("ghost, vampire or werewolf (g/v/w)").lower()
        if option3=="g" or option3=="v":
            print("Game over")
        else:
            print("You win!")




















