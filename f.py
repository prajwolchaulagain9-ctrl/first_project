##1

# sentence=input("Enter a sentence: ")
# vowels=set()
# for x in sentence:
#     if x in "aeiou":
#         vowels.add(x)
# print("Total vowels found=",len(vowels))

##2


# word_dict={}
# no_of_turns=int(input("Enter number of turns to perform: "))
# for x in range(1,no_of_turns+1):
#     operation= int(input("Enter operation to perform: 1.Add Word 2.Display Words 3.Remove Word 4.Exit: "))
#     if operation==4:
#         print("Exit successful")
#         break
#     elif operation==1:
#         word_to_add= input("Enter word to add: ")
#         if word_to_add not in word_dict:
#             meaning=input(f"Enter the meaning of {word_to_add}: ")
#             word_dict[word_to_add]=meaning
#             print(f"{word_to_add} added succesfully to dictionary")
#         else:
#             print(f"({word_to_add} already exists)")
#     elif operation==2:
#         for word in sorted(word_dict):
#             print(f"{word}: {word_dict[word]}")
#         print("Displayed successfully in alphabetical order")
#     else:
#         word_to_remove=input("Enter word to remove: ")
#         if word_to_remove in word_dict:
#             word_dict.pop(word_to_remove)
#             print(f"Word removed successfully")
#         else:
#             print("Word not in dictionary")

##3


# quiz_questions={
#     '1':{
#         'question':'Which of the following chracter comments in python?',
#         'options': {'a':'#', 'b':'//', 'c':'/', 'd':'!'},
#         'correct answer':'a'
#     },
#     '2':{
#         'question':'Which of the following statemets is used to create an empty set in Python?',
#         'options':{'a':'()', 'b':'{}','c':'{ }','d':'set()'},
#         'correct answer': 'd'
#     },
#     '3':{
#         'question':'Which method is used to add an element to a list in Python?',
#         'options':{'a':'add()','b':'append()','c':'update()','d':'addlist()'},
#         'correct answer':'b'
#     }
# }
# import random as rd

# a=list(quiz_questions.keys())
# rd.shuffle(a)
# print(a)

# score=0
# num=0
# for x in quiz_questions:
#     num=num+1
#     print(str(num) + ") "+quiz_questions[x]['question'])
#     for j in quiz_questions[x]['options']:
#         print(j+f": {quiz_questions[x]['options'][j]}")    
#     answer=input("Enter the answer a,b,c,d: ")
#     if answer in quiz_questions[x]['correct answer']:
#         score=score+1
# print(f"Your score is {score}")


##4


# item_num=int(input("Enter the no of items you purchased: "))
# price_arr=[]
# for x in range (item_num):
#     item_price=float(input(f"Enter the price of items {x+1}: "))
#     price_arr.append(item_price)

# print(f"The total price for items you pruchased is {sum(price_arr)}")

    


items=[1,2,3,4]
i=0
while i<len(items):
    if items[i]%2==0:
        print(items[i])
    i=i+1



























