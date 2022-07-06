import random 
def guess():  
    name=input("Whats your name? \n") 
    print(f"Hey {name} lets play a guessing game!") 
    print("I'm thinking of a number and you gotta guess which one it is. Legooo") 
    number=int(input("Enter your number: \n")) 
    guess_list=[1,2,3,4,5,6,7,8,9,10] 
    guess_number=random.choice(guess_list) 
    if number==guess_number: 
        print(f"Thats right!.I guessed{guess_number} You're a champion") 
    else:
        print("Your guess is too low.Try again")  


guess()        

