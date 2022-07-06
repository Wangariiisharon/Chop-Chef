import random 
class Customer:
    def __init__(self,cardname): 
        self.cardname=cardname  
        self.cardnumber=0
        self.amountlist=[] 
        self.chopscore=0  


    def expenditure(self,amount):
       if amount>0:
           self.amountlist.append(amount)
           print(self.amountlist)
       print(f"Your expenditure amount is {amount}")  


    def card_number(self):
        if len(self.amountlist)>3: 
           number=["123Card","124Card","125Card","126Card","127Card","128Card"]
           self.cardnumber=random.choice(number) 
           print(f"Your card number is {self.cardnumber}")    

        else:
            print(f"You have no card number")  

    def credit_core(self): 
        for amount in self.amountlist:
            credit_points=amount//500 
            self.chopscore+=credit_points 
            print(f"your credit score is {self.chopscore}")
            

    def reward(self):
        reward_food={80:"Chips Masala",160:"Chicken Tikka",320:"Biriani Lambchops",640:"Sushi",1280:"Oysters",2560:"White Truffle"}
        for food in reward_food.keys(): 
            if food==self.chopscore:  
                print(f"your reward delicasy is {reward_food.values()} ")   

            else:
                print(f"Your creditscore is not rewardable")   
                  

      



    
      
            







 





      
        

               

        
             
         

      


       
         
     
  





