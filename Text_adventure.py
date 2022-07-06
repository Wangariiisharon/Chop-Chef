print("""Welcome to the text adventure game! Have fun friend! \n 
    
   A girl in her teens babysat for a wealthy family one night. 
   The wealthy family had a very large house with many rooms. 
   It was filled with lots of artefacts and old ornaments from 
   all over the world. As the parents were leaving to go out, 
   the father told the girl that once the she put the kids down, 
   she must go down to the basement, watch TV there, and not go 
   wandering around the house.
    
    
   Do you think she obayed?""") 

def scene1():
    c1=input("Obayed or Disobayed?\n")  
    if (c1.lower()=="obayed"): 
     print("""Once the kids are asleep, the girl retires to the 
     basement room to watch TV. However, she cannot concentrate 
     on her show because in the in the corner of the room is a 
     life-size clown statue grinning at her.
     """) 

     scene2() 

    elif (c1.lower()=="disobayed"): 
     print("""A loud bang then followed and roumor has that she dissappeard and not even her body was found till date""")
    
    else:
     print("""Enter correct choice""") 

def scene2(): 
    c2 =input("What do you think she does?\n call the childerns father or hide it further?")   
    if (c2=="call the childerns father"):
        print("""She finally decides to drape a blanket over the 
        statue so she can ignore it. After a while she cant 
        stand looking at the clown statues over-sized feet 
        sticking out from under the blanket.""") 

    elif(c2.lower()=="hide it further"): 
        print("You my friend are really wrong")  
        print("""She instead She finally decides to drape a blanket over the 
        statue so she can ignore it. After a while she cant 
        stand looking at the clown statues over-sized feet 
        sticking out from under the blanket""")  

    else:
     print("""Enter correct choice""")      
    
    