import random
import math
from operator import add, sub, mul, div

ops = {"+":add, "-":sub, "*":mul, "/":div}


#### FINISHED BESIDES GEOMETRY, WE NEED TO TALK ABOUT WHAT QUESTIONS NEED TO BE DONE FOR THAT ####
class Question:
    def __init__(self, subject, difficulty):
        self.subject = subject
        self.difficulty = difficulty

        if (self.subject == "Addition"):
            if (self.difficulty == "easy"):
                self.easyAddition();
            if (self.difficulty == "medium"):
                self.mediumAddition();
            if (self.difficulty == "hard"):
                self.hardAddition();
        if (self.subject == "Arithmetic"):
            if (self.difficulty == "easy"):
                self.easyArithmetic();
            if (self.difficulty == "medium"):
                self.mediumArithmetic();
            if (self.difficulty == "hard"):
                self.hardArithmetic();         

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
        self.randomNumOne = random.randint(0, 100)
        self.randomNumTwo = random.randint(0, 100)
        self.randomOpKey = random.choice(ops.keys())
        self.randomOpValue = ops[self.randomOpKey]
        if (self.randomNumOne < self.randomNumTwo):
            self.answer = self.randomOpValue(self.randomNumTwo, self.randomNumOne)
            self.text = str(self.randomNumTwo) + " " + self.randomOpKey + " " + str(self.randomNumOne)
        else :
            self.answer = self.randomOpValue(self.randomNumOne, self.randomNumTwo)
            self.text = str(self.randomNumOne) + " " + self.randomOpKey + " " + str(self.randomNumTwo)

    def mediumArithmetic(self):
        self.randomNumOne = round(random.uniform(0.0, 100.0),1)
        self.randomNumTwo = round(random.uniform(0.0, 100.0),1)
        self.randomOpKey = random.choice(ops.keys())
        self.randomOpValue = ops[self.randomOpKey]
        if (self.randomNumOne < self.randomNumTwo):
            self.answer = self.randomOpValue(self.randomNumTwo, self.randomNumOne)
            self.text = str(self.randomNumTwo) + " " + self.randomOpKey + " " + str(self.randomNumOne)
        else :
            self.answer = self.randomOpValue(self.randomNumOne, self.randomNumTwo)
            self.text = str(self.randomNumOne) + " " + self.randomOpKey + " " + str(self.randomNumTwo)

    def hardArithmetic(self):
        self.randomNumOne = round(random.uniform(-100.0, 100.0),1)
        self.randomNumTwo = round(random.uniform(-100.0, 100.0),1)
        self.randomOpKey = random.choice(ops.keys())
        self.randomOpValue = ops[self.randomOpKey]
        if (self.randomNumOne < self.randomNumTwo):
            self.answer = self.randomOpValue(self.randomNumTwo, self.randomNumOne)
            self.text = str(self.randomNumTwo) + " " + self.randomOpKey + " " + str(self.randomNumOne)
        else :
            self.answer = self.randomOpValue(self.randomNumOne, self.randomNumTwo)
            self.text = str(self.randomNumOne) + " " + self.randomOpKey + " " + str(self.randomNumTwo)
