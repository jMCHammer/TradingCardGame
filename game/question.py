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

        if subject == "Arithmetic":
            self.Arithmetic(difficulty)
        elif subject == "Geometry":
            self.Geometry(difficulty)
        else:
            eval("self." + self.difficulty + self.subject + "()");

    #### EACH FUNCTION DEFINED CREATES TWO RANDOM NUMBERS AND CHOOSES A RANDOM OPERATOR
    #### THE ANSWER IS CALCULATED FOR THAT SPECIFIC EQUATION AND IS SET, ALONG WITH EQUATION TEXT. 

# INTEGER REPRESENTATION #
    def Integer(self, diff):
        if diff == "easy":
            self.randomNumOne = random.randint(-9, 10)
        elif diff == "medium":
            self.randomNumOne = random.randint(-15, 16)
        elif diff == "hard":
            self.randomNumOne = random.randint(-25, 26)

#3==========================================================D
# ARITHMETIC QUESTION LOGIC #
# self.randomOpKey = random operator from + - / *
# self.randomNumOne = First Random Number
# self.randomNumTwo = Second Random Number
# self.Answer = Answer of the question
# self.Text = Question string
# Status = Complete

    def Arithmetic(self, diff):
        self.randomOpKey = random.choice(ops.keys())

        if diff == "easy":
            if self.randomOpKey == "/":
                self.randomNumOne = random.randint(0, 10) + 1
                self.randomNumTwo = (random.randint(0, 20) + 1) * self.randomNumOne
            elif self.randomOpKey == "*":
                self.randomNumOne = random.randint(0, 15)
                self.randomNumTwo = random.randint(0, 15)
            else:
                self.randomNumOne = random.randint(0, 20) + 1
                self.randomNumTwo = random.randint(0, 20) + 1
        elif diff == "medium":
            if self.randomOpKey == "/":
                self.randomNumOne = round(random.uniform(0.0, 12.0) + 1,1)
                self.randomNumTwo = round(random.uniform(0.0, 30.0) + 1,1) * self.randomNumOne
            elif self.randomOpKey == "*":
                self.randomNumOne = round(random.uniform(0.0, 20.0),1)
                self.randomNumTwo = round(random.uniform(0.0, 20.0),1)
            else:
                self.randomNumOne = round(random.uniform(0.0, 50.0) + 1,1)
                self.randomNumTwo = round(random.uniform(0.0, 50.0) + 1,1)
        elif diff == "hard":
            if self.randomOpKey == "/":
                self.randomNumOne = round(random.uniform(0.0, 12.0) + 1,1)
                self.randomNumTwo = round(random.uniform(0.0, 50.0),1) * self.randomNumOne
            elif self.randomOpKey == "*":
                self.randomNumOne = round(random.uniform(0.0, 30.0),1)
                self.randomNumTwo = round(random.uniform(0.0, 30.0),1)
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
# Fraction Question Logic #
# Status: Incomplete
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
# Geometry Question Logic #
# self.sh = Shape of the question. Either Triangle, Parallelogram, Trapezoid, Rectangle, or Square
# self.h = height
# self.w = width 
#          top length if shape is a trapezoid
#          base length if shape is a triangle
# self.b = (Apply for Trapezoid only) bottom length
# self.s1 = (Apply for Trapezoid, Parallelogram, and Triangle) Left side length
# self.s2 = (Apply for Trapezoid and Triangle only) Right side length
# self.answer = Answer key of the question. (Either Area or Parameter)
# self.text = Question text
# Status = Incomplete.(Need volume question logics)
#          Need to clean some coding

    def Geometry(self, diff):
        print diff
        gt = geotype[random.randint(0,1)]
        self.sh = random.choice(shape)
        difficulty = 3 if diff == "easy" else (2 if diff == "medium" else 1)

        self.w = random.randint(int(3*pow(difficulty,2) - 19*difficulty + 31),30/difficulty) #width
        self.h = random.randint(int(3*pow(difficulty,2) - 19*difficulty + 31),30/difficulty) #height
        if(gt == "area"):
           self.text = "What is the area of a " + self.sh
        elif(gt == "perimeter"): 
            self.text = "What is the perimeter of a " + self.sh
        if(self.sh == "trapezoid"):
            self.h = self.h + 1 if self.h%2 != 0 else self.h
            print int(7.5*pow(difficulty,2) - 42.5*difficulty + 75)
            self.b = random.randint(self.w,int(7.5*pow(difficulty,2) - 42.5*difficulty + 75)) #bottomlength
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
            self.s2 = self.h if self.l1 == self.w else round(pow(pow(self.l2,2) + pow(self.h,2),.5),1)
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