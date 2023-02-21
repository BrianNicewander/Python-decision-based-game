'''
This file asks the user their name and age and then pass it to the main file.
'''
class playerOne:
    
    def __init__(self): #self has to be the first part.
        self.name = "Defult" #This is a defult var to start with.
        self.age = 0 #This is a defult var to start with.
        self.inventory = ["Sword", "Mace", "Flail"] #Assign a wepon down below.
           
    def setName(self):
        try:
            name = input("Please enter your name: ")
            if name.istitle():
                self.name = name
            else:
                raise Exception() #This throws an error so it goes to the except.
        except:
            print("That is not a valid name.")
            self.setName() #This reruns the function again.

    def setAge(self):
        try:
            age = int(input("Please enter your age: "))
            if age > 0 and age <= 100:
                self.age = age
            else:
                raise Exception() #This throws an error so it goes to the except.
        except:
            print("That is not a valid age.")
            self.setAge() #This reruns the function again.

    """
    setNameAndAge function runs both name and age.
    I made this function, so I only had to call one function in my main code.
    """
    def setNameAndAge(self):
        self.setName()
        self.setAge()
