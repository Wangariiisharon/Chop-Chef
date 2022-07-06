class Calculator: 
    def __init__(self,number_one,number_two): 
        self.number_one=number_one 
        self.number_two=number_two 


    def addition(self): 
        sum=self.number_one + self.number_two 
        print(sum)    

    def subtraction(self): 
        difference=self.number_one-self.number_two 
        print(difference)

    def division(self): 
        divide=self.number_one/self.number_two 
        print(divide)

    def multipication(self): 
        product=self.number_one*self.number_two 
        print(product)

    def modulus(self): 
        remainder=self.number_one%self.number_two 
        print(remainder)