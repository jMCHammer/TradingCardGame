import random
import math
from operator import add, sub, mul, div
from fractions import Fraction

ops = {"+":add, "-":sub, "*":mul, "/":div}
    

#### FINISHED BESIDES GEOMETRY, WE NEED TO TALK ABOUT WHAT QUESTIONS NEED TO BE DONE FOR THAT ####
class Question:
    def __init__(self, subject, difficulty):
        self.subject = subject
        self.difficulty = difficulty

        eval("self." + self.difficulty + self.subject + "()");

#        if (self.subject == "Addition"):
#            if (self.difficulty == "easy"):
#                self.easyAddition();
#            if (self.difficulty == "medium"):
#                self.mediumAddition();
#            if (self.difficulty == "hard"):
#                self.hardAddition();
#        if (self.subject == "Arithmetic"):
#            if (self.difficulty == "easy"):
#                self.easyArithmetic();
#            if (self.difficulty == "medium"):
#                self.mediumArithmetic();
#            if (self.difficulty == "hard"):
#                self.hardArithmetic();         

    #### EACH FUNCTION DEFINED CREATES TWO RANDOM NUMBERS AND CHOOSES A RANDOM OPERATOR
    #### THE ANSWER IS CALCULATED FOR THAT SPECIFIC EQUATION AND IS SET, ALONG WITH EQUATION TEXT. 
    def easyAddition(self):
        self.randomNumOne = random.randint(0, 100)
        self.randomNumTwo = random.randint(0, 100)
        self.opValue = ops["+"]
        self.answer = self.opValue(self.randomNumOne, self.randomNumTwo)
        self.text = str(self.randomNumOne) + " + " + str(self.randomNumTwo)

    def mediumAddition(self):
        self.randomNumOne = round(random.uniform(0.0, 100.0),1)
        self.randomNumTwo = round(random.uniform(0.0, 100.0),1)
        self.opValue = ops["+"]
        self.answer = self.opValue(self.randomNumOne, self.randomNumTwo)
        self.text = str(self.randomNumOne) + " + " + str(self.randomNumTwo)

    def hardAddition(self):
        self.randomNumOne = round(random.uniform(-100.0, 100.0),1)
        self.randomNumTwo = round(random.uniform(-100.0, 100.0),1)
        self.opValue = ops["+"]
        self.answer = self.opValue(self.randomNumOne, self.randomNumTwo)
        self.text = str(self.randomNumOne) + " + " + str(self.randomNumTwo)
    
    def easyArithmetic(self):
        self.randomOpKey = random.choice(ops.keys())
        if self.randomOpKey == "/":
            self.randomNumOne = random.randint(0, 10) + 1
            self.randomNumTwo = (random.randint(0, 30) + 1) * self.randomNumOne
        else:
            self.randomNumOne = random.randint(0, 50) + 1
            self.randomNumTwo = random.randint(0, 50) + 1

        self.randomOpValue = ops[self.randomOpKey]
        if (self.randomNumOne < self.randomNumTwo):
            self.answer = self.randomOpValue(self.randomNumTwo, self.randomNumOne)
            self.text = str(self.randomNumTwo) + " " + self.randomOpKey + " " + str(self.randomNumOne)
        else :
            self.answer = self.randomOpValue(self.randomNumOne, self.randomNumTwo)
            self.text = str(self.randomNumOne) + " " + self.randomOpKey + " " + str(self.randomNumTwo)

    def mediumArithmetic(self):
        self.randomOpKey = random.choice(ops.keys())
        if self.randomOpKey == "/":
            self.randomNumOne = round(random.uniform(0.0, 10.0) + 1,1)
            self.randomNumTwo = round(random.uniform(0.0, 30.0) + 1,1) * self.randomNumOne
        else:
            self.randomNumOne = round(random.uniform(0.0, 50.0) + 1,1)
            self.randomNumTwo = round(random.uniform(0.0, 50.0) + 1,1)
        
        self.randomOpValue = ops[self.randomOpKey]
        if (self.randomNumOne < self.randomNumTwo):
            self.answer = self.randomOpValue(self.randomNumTwo, self.randomNumOne)
            self.text = str(self.randomNumTwo) + " " + self.randomOpKey + " " + str(self.randomNumOne)
        else :
            self.answer = self.randomOpValue(self.randomNumOne, self.randomNumTwo)
            self.text = str(self.randomNumOne) + " " + self.randomOpKey + " " + str(self.randomNumTwo)

    def hardArithmetic(self):
        self.randomOpKey = random.choice(ops.keys())
        if self.randomOpKey == "/":
            self.randomNumOne = round(random.uniform(0.0, 10.0) + 1,1)
            self.randomNumTwo = round(random.uniform(0.0, 50.0),1) * self.randomNumOne
        else:
            self.randomNumOne = round(random.uniform(0.0, 100.0),1)
            self.randomNumTwo = round(random.uniform(0.0, 100.0),1)

        self.randomOpValue = ops[self.randomOpKey]
        if (self.randomNumOne < self.randomNumTwo):
            self.answer = self.randomOpValue(self.randomNumTwo, self.randomNumOne)
            self.text = str(self.randomNumTwo) + " " + self.randomOpKey + " " + str(self.randomNumOne)
        else :
            self.answer = self.randomOpValue(self.randomNumOne, self.randomNumTwo)
            self.text = str(self.randomNumOne) + " " + self.randomOpKey + " " + str(self.randomNumTwo)

    def easyLikeFraction(self):
        denominator = random.randrange(9)+2
        numerator1 = random.randrange(denominator-1) + 1
        numerator2 = random.randrange(denominator-1) + 1
        self.randomNumOne = str(numerator1) + "/" + str(denominator)
        self.randomNumTwo = str(numerator2) + "/" + str(denominator)

        randomOne = Fraction(self.randomNumOne) #Fraction functions automatically cross out the common divisor, so i am using this separately
        randomTwo = Fraction(self.randomNumTwo)
        self.randomOpKey = random.choice(ops.keys())
        self.randomOpValue = ops[self.randomOpKey]
        if (randomOne < randomTwo):
            self.text = self.randomNumTwo + " " + self.randomOpKey + " " + self.randomNumOne
            self.answer = self.randomOpValue(randomTwo, randomOne)
        else :
            self.text = self.randomNumOne + " " + self.randomOpKey + " " + self.randomNumTwo
            self.answer = self.randomOpValue(randomOne, randomTwo)