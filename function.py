import random as rd

random_num=rd.randint(1,50)
def guess_game(random_num):
    guess_remain=7
    while guess_remain!=0:
        Guess=int(input("Guess a number between 1 and 50 : "))
        if Guess==random_num:
            print("Number found")
        else:
            guess_remain-= 1
            if Guess>random_num:
                print("Too high")
            else:
                print("Too low")
            print(f"{guess_remain} guesses remainining")
            if guess_remain==0:
                print("Game over") 

def area(l,b):
    print(l*b)

if __name__=='__main__':
    guess_game(random_num)
    area(10,20)