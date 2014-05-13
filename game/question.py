import random
import math
from operator import add, sub, mul, div
from fractions import Fraction

ops = {"+":add, "-":sub, "*":mul, "/":div}
shape = ["triangle", "square", "parallelogram", "trapezoid", "rectangle"]
geotype = ["perimeter","area","volume"]
    

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
#3==========================================================D
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
#############################################################
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
#############################################################
    def easyGeometry(self):
        gt = geotype[random.randint(0,1)]
        self.sh = random.choice(shape)
        self.w = random.randint(1,20) #width
        self.h = random.randint(1,20) #height
        if(gt == "area"):
           self.text = "What is the area of a " + self.sh
        elif(gt == "perimeter"): 
            self.text = "What is the perimeter of a " + self.sh
        if(self.sh == "trapezoid"):
            self.h = self.h + 1 if self.h%2 != 0 else self.h
            self.b = random.randint(self.w,30) #bottomlength
            self.l1 = random.randint(1,self.b-self.w)
            self.s1 = round(pow(pow(self.l1,2) + pow(self.h,2),.5),1)
            self.l2 = self.b - self.w - self.l1
            self.s2 = round(pow(pow(self.l2,2) + pow(self.h,2),.5),1)
            if(gt == "area"):
                self.answer = (self.w + self.b)*self.h/2
                self.text += " with top length " + str(self.w) + ", bottom length " + str(self.b) + ", and height length " + str(self.h)
            elif(gt == "perimeter"):
                self.answer = self.w + self.b + self.s1 + self.s2
                self.text += " with bottom length " + str(self.b) + ", top length " + str(self.w) + ", and side length " + str(self.s1) + " and " + str(self.s2)
        elif(self.sh == "triangle"):
            self.w = self.w + 1 if self.w%2 != 0 else self.w
            self.l1 = random.randint(0,self.w+1)
            self.l2 = self.w - self.l1
            self.s1 = self.h if self.l1 == 0 else round(pow(pow(self.l1,2) + pow(self.h,2),.5),1) #side
            self.s2 = self.h if self.li == self.w else round(pow(pow(self.l2,2) + pow(self.h,2),.5),1)
            if(gt == "area"):
                self.answer = self.w*self.h/2
                self.text += " with base length " + str(self.w) + " and height length " + str(self.h)
            elif(gt == "perimeter"):
                self.answer = self.w + self.s1 + self.s2
                self.text += " with base length " + str(self.w) + ", and side length " + str(self.s1) + " and " + str(self.s2)
        elif(self.sh == "parallelogram"):
            self.l1 = random.randint(0, self.h)
            self.s1 = round(pow(pow(self.l1,2) + pow(self.h,2),.5),1)
            if(gt == "area"):
                self.answer = self.w * self.h
                self.text += " with base length " + str(self.w) + " and height length " + str(self.h)
            elif(gt == "perimeter"):
                self.answer = 2*(self.w + self.s1)
                self.text += " with base length " + str(self.w) + ", and side length " + str(self.s1)
        elif(self.sh == "rectangle"):
            if(gt == "area"):
                self.answer = self.w * self.h
            elif(gt == "perimeter"):
                self.answer = 2*(self.w + self.h)
            self.text += " with base length " + str(self.w) + " and height length " + str(self.h)
        elif(self.sh == "square"):
            if(gt == "area"):
                self.answer = pow(self.w, 2)
                self.text += " with length " + str(self.w)
            elif(gt == "perimeter"):
                self.answer = 4*(self.w)
                self.text += " with length " + str(self.w)
    def mediumGeometry(self):
        pass
    def hardGeometry(self):
        pass