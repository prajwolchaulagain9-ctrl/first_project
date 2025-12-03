# name=input("Enter your name: ")
# first=name.lower()
# then= first.strip()
# final= then.split()
# print("_".join(final))

# password= input("Enter your password: ")

# step1=password.lower()
# step2= step1.replace("a","@")
# step3= step2.replace("e","3")
# step4= step3.replace("i","1")
# step5= step4.replace("o","0")
# step6= step5.replace("s","$")
# print("Your secret code is",step6+"0##9")

# email= input("Enter your email: ")
# step1=email.rfind("@")
# step2=email[:step1]
# print("Your username is",step2)

# number= input("Enter a number: ")
# step1= number.replace(" ","").replace("-","").replace("+","")


# print("Your number is",step1)





# name= input("Enter your name: ")
# first= name.lower()
# then= first.title()
# print(then)


# tagline=input("Enter your tagline: ")
# print("*"*30)

# step1=tagline.strip()
# step2=step1.title()
# step3=step2.center(31)
# print(step3)
# print("*"*30)



# Password=input("Enter your password: ")
# print("*"*30)

# step1=len(Password)
# step2=Password[0]
# step3=Password[-1]
# print((step2+"*"*step1+step3).center(31))

# print("*"*30)




# print("*"*30)
# sec_code=input("Enter your secret code: ")
# step1=sec_code.maketrans("aeiou","✈️🐘🍦🍊☂️")
# step2=sec_code.translate(step1).center(30)
# print(step2)
# print("*"*30)

# print("*"*100)
# url= input("Enter your website URL: ")
# step1=url.replace("http://","").replace("https://","").replace("www.","")
# print(step1)
# step2=step1.split("/")[0]
# print(f'Clean URL: {step1}'.center(100))
# print(f'Domain Name: {step2}'.center(100))
# print("*"*100)

# file_name= input("Enter your file name: ")
# print("*"*100)
# step1=file_name.lower()
# step2=step1.replace(",","").replace("#","").replace("(","").replace(")","").replace("jpeg","jpg").replace("png","jpg")
# step3=step2.split()
# step4="_".join(step3)
# print(f"Clean File Name: {step4}".center(101))

# print("*"*100)



sent= input("Enter a sentence: ")
step1= sent.title()
step2= step1.split()
step3= step2[-1::-1]
step4= " ".join(step3)
print(step4)


