import random
import math
from operator import add, sub, mul, div
from fractions import Fraction

ops = {"+":add, "-":sub, "*":mul, "/":div}
shape = ["triangle", "square", "parallelogram", "trapezoid", "rectangle"]
geotype = ["perimeter","area","volume"]
itype = ["compare","representation"]
stattype = ["min","max","median","mean"]

#### FINISHED BESIDES GEOMETRY, WE NEED TO TALK ABOUT WHAT QUESTIONS NEED TO BE DONE FOR THAT ####
class Question:
    def __init__(self, subject, difficulty):
        self.subject = subject
        self.difficulty = difficulty

        # if subject == "Arithmetic":
        #     self.Arithmetic(difficulty)
        # elif subject == "Geometry":
        #     self.Geometry(difficulty)
        # elif subjec
        # else:
        eval("self." + self.subject + "(\"" + self.difficulty + "\")");
            

    #### EACH FUNCTION DEFINED CREATES TWO RANDOM NUMBERS AND CHOOSES A RANDOM OPERATOR
    #### THE ANSWER IS CALCULATED FOR THAT SPECIFIC EQUATION AND IS SET, ALONG WITH EQUATION TEXT. 

# INTEGER REPRESENTATION #
    def Integer(self, diff):
        self.qtype = "compare"
        difficulty = 1 if diff == "easy" else (2 if diff == "medium" else 3)
        intrange = int(2.5*pow(difficulty,2) - 2.5*difficulty + 10)
        if self.qtype == "compare":
            self.comparator = random.randint(0,1) # 0 = min, 1 = max
            self.randomNumOne = random.randint(-intrange, intrange)
            self.randomNumTwo = random.choice(range(-intrange - 1, self.randomNumOne - 1) + range(self.randomNumOne + 1, intrange + 1))
            if(self.comparator == 1):
                self.answer = max(self.randomNumOne, self.randomNumTwo)
                self.text = "Which of the following is greater: " + str(self.randomNumOne) + " or " + str(self.randomNumTwo)
            else:
                self.answer = min(self.randomNumOne, self.randomNumTwo)
                self.text = "Which of the following is smaller: " + str(self.randomNumOne) + " or " + str(self.randomNumTwo)

        elif self.qtype == "representation":
            self.randomNumOne = random.randint(-intrange, intrange)
            self.randomNumTwo = random.randint(-intrange - self.randomNumOne, intrange) if self.randomNumOne < 0 else random.randint(-intrange, intrange - self.randomNumOne)
            self.randomNumThree = random.randint(-intrange - (self.randomNumOne + self.randomNumTwo), intrange) if self.randomNumOne + self.randomNumTwo < 0 else random.randint(-intrange, intrange - (self.randomNumOne + self.randomNumTwo))


#3==========================================================D
# ARITHMETIC QUESTION LOGIC #
# self.randomOpKey = random operator from + - / *
# self.randomNumOne = First Random Number
# self.randomNumTwo = Second Random Number
# self.Answer = Answer of the question
# self.Text = Question string
# Status = Complete

    def Addition(self, diff):
        self.Arithmetic(diff, '+')

    def Subtraction(self, diff):
        self.Arithmetic(diff, '-')

    def Multiplication(self, diff):
        self.Arithmetic(diff, '*')

    def Division(self, diff):
        self.Arithmetic(diff, '/')
            
    def Arithmetic(self, diff, op = ''):
        if (op == ''):
            self.randomOpKey = random.choice(ops.keys())
        else:
            self.randomOpKey = op

        if diff == "easy":
            if self.randomOpKey == "/" or self.randomOpKey == "*":
                self.randomNumOne = random.randint(0, 10) + 1
                self.randomNumTwo = (random.randint(0, 20) + 1) * self.randomNumOne
            else:
                self.randomNumOne = random.randint(0, 20) + 1
                self.randomNumTwo = random.randint(0, 20) + 1
        elif diff == "medium":
            if self.randomOpKey == "/" or self.randomOpKey == "*":
                self.randomNumOne = round(random.uniform(0.0, 12.0) + 1,1)
                self.randomNumTwo = round(random.uniform(0.0, 30.0) + 1,1) * self.randomNumOne
            else:
                self.randomNumOne = round(random.uniform(0.0, 50.0) + 1,1)
                self.randomNumTwo = round(random.uniform(0.0, 50.0) + 1,1)
        elif diff == "hard":
            if self.randomOpKey == "/" or self.randomOpKey == "*":
                self.randomNumOne = round(random.uniform(0.0, 12.0) + 1,1)
                self.randomNumTwo = round(random.uniform(0.0, 50.0),1) * self.randomNumOne
            else:
                self.randomNumOne = round(random.uniform(0.0, 100.0),1)
                self.randomNumTwo = round(random.uniform(0.0, 100.0),1)

        if self.randomOpKey == "*":
            self.randomOpValue = ops['/']
        else:
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

    def Geometry(self, diff):
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
                self.text += " with base length " + str(self.w) + ", and side length " + str(self.s1) + "\n and " + str(self.s2)
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
    def Statistics(self, diff):
        self.qtype = random.choice(stattype)
        difficulty = 20 if diff == "hard" else (15 if diff == "medium" else 10)
        self.listNum = []

        for i in range(0,difficulty):
            num = random.randint(0, difficulty)
            self.listNum.append(num)

        if self.qtype == "min":
            self.answer = min(self.listNum)
            self.text = "What is the minimum of following:\n" + str(self.listNum)
        elif self.qtype == "max":
            self.answer = max(self.listNum)
            self.text = "What is the maximum of following:\n" + str(self.listNum)
        elif self.qtype == "mean":
            self.answer = sum(self.listNum)/float(len(self.listNum))
            self.text = "What is the mean of following:\n" + str(self.listNum)
        else:
            if len(self.listNum)%2 != 0:
                self.answer = sorted(self.listNum)[len(self.listNum)/2]
            else:
                self.answer = (sorted(self.listNum)[len(self.listNum)/2]
                    + sorted(self.listNum)[len(self.listNum)/2 + 1])/2.0
            self.text = "What is the median of following:\n" + str(self.listNum)