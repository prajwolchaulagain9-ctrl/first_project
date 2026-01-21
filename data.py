# #1
# items=['sql','123','python']
# new= list(filter(lambda x: x not in "0123456789",items))
# print(new)

# #2
# products = [
#  {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
#  {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':
# False}
# ]
# filterd= list(filter(lambda x: x['instock']==True ,products))
# print(filterd)

# #3

# def calculate_sum(start,end):
#     sum=0
#     for x in range(start,end):
#         sum= sum+x
#     return sum
# print(calculate_sum(9,746))

# #4

# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     if b!=0:
#         return a/b
#     else:
#         return "Invalid input"
    
# def main_calculator():
#     operation= input("+,-,*,/ or 0 for exit: ")
#     if operation=='0':
#         print("Exit successfull")
#         return
#     elif operation not in "+-*/":
#         print("Invalid operation")
#         return
        
#     a=int(input("enter first num for calculation: "))
#     b=int(input("enter second num for calculation: "))
#     if operation=='+':
#         print(add(a,b))
#     elif operation=='-':
#         print(subtract(a,b))
#     elif operation=='*':
#         print(multiply(a,b))
#     else:
#         print(divide(a,b))
# main_calculator()

# #5

# course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, {'title': 'CorporateFinance', 'genre': 'commerce'},
#            {'title': 'Modern World History', 'genre': 'history'} ]

# filterd_course=list(filter(lambda x: x['genre']=='history',course))
# print(filterd_course)

# #6

# emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net','shyam.kumar@workcorp.com']
# blacklist = ('@hooya.com', '@malware.net')

# spams= list(filter(lambda x: x.endswith(blacklist),emails)) 
# print(spams)

# #7

# price = [100, 50, 200, 75] 
# price_after_dis= list(map(lambda x: x-(x*(20/100)),price))
# print(price_after_dis)


# #8

# def skip_two(list8):
#     new_list=[]
#     for x in range(1,len(list8),3):
#         if x >11:
#             return new_list
#         new_list.append(list8[x])
#     return new_list
# list8= [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
# print(skip_two(list8))

# #9


# def remove_at_idx(input_list, index):
#     if index < 0 or index >= len(input_list):
#         return "Invalid index"
#     for i in range(index, len(input_list) - 1):
#         input_list[i] = input_list[i + 1]
#     input_list.pop()
#     return input_list

# print(remove_at_idx([1,2,3,4,5,6,7,8,90],3))

# #10

# def cleaned_input(string):
#     new_string=''
#     for x in string:
#         if x.isalpha():
#             new_string=new_string+x
#         else:
#             new_string=new_string+'#'
#     print(new_string)
# cleaned_input("dnfj@nd$dsk&nf(fl^)")

# #11

# users_db={1:{'username':'admin','password':'admin123','email':'admin@example.com'},
#           2:{'username':'user1','password':'user123','email':'user1@example.com'},
#           3:{'username':'user2','password':'user234','email':'user2@example.com'}
# }

# def register_user(username,password,email):
#     for x in users_db.values():
#         if username in x['username']:
#             print("User already exists")
#         else:
#             new_key=max(users_db.keys())+1
#             users_db[new_key]= {'username':username, 'password':password,'email':email}

# def login_user(username,password):
#     for x in users_db:
#         if username not in x["username"]:
#             print("User doesn't exist")
#         elif password not in x['password']:
#             print("Incorrecr passowrd")
#         elif username in x['username'] and password in x['password']:
#             print(f"Wlecome back {username}")

# register_user('ram','ram123','ram@email.com')
            
# #12


# inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]
# def add_product(name, price, quantity):
#     for product in inventory:
#         if product['name'] == name:
#             print("Product already exists.")
#             return
#     if price <= 0 or quantity <= 0:
#         print("Price and quantity must be positive numbers.")
#         return
#     inventory.append({'name': name, 'price': price, 'quantity': quantity})
#     print(f"Product {name} added successfully.")
# def view_products():
#     print(f"{'Name':<15}{'Price':<10}{'Quantity':<10}")
#     for product in inventory:
#         print(f"{product['name']:<15}{product['price']:<10}{product['quantity']:<10}")
# def update_product(name, price=None, quantity=None):
#     for product in inventory:
#         if product['name'] == name:
#             if price is not None:
#                 if price <= 0:
#                     print("Price must be a positive number.")
#                     return
#                 product['price'] = price
#             if quantity is not None:
#                 if quantity <= 0:
#                     print("Quantity must be a positive number.")
#                     return
#                 product['quantity'] = quantity
#             print(f"Product {name} updated successfully.")
#             return
#     print("Product not found.")
# def delete_product(name):
#     for product in inventory:
#         if product['name'] == name:
#             inventory.remove(product)
#             print(f"Product {name} deleted successfully.")
#             return
#     print("Product not found.")
# def calculate_total_value():
#     total_value = sum(product['price'] * product['quantity'] for product in inventory)
#     print(f"Total inventory value: {total_value}")
# def menu():
#     while True:
#         print("\nMenu:")
#         print("1. Add new product")
#         print("2. View all products")
#         print("3. Update product details")
#         print("4. Delete a product")
#         print("5. Calculate total inventory value")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             name = input("Enter product name: ")
#             price = float(input("Enter product price: "))
#             quantity = int(input("Enter product quantity: "))
#             add_product(name, price, quantity)
#         elif choice == '2':
#             view_products()
#         elif choice == '3':
#             name = input("Enter product name to update: ")
#             price_input = input("Enter new price (or leave blank to skip): ")
#             quantity_input = input("Enter new quantity (or leave blank to skip): ")
#             price = float(price_input) if price_input else None
#             quantity = int(quantity_input) if quantity_input else None
#             update_product(name, price, quantity)
#         elif choice == '4':
#             name = input("Enter product name to delete: ")
#             delete_product(name)
#         elif choice == '5':
#             calculate_total_value()
#         elif choice == '6':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")




































