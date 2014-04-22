
import operator
import random
from fractions import Fraction

ops = { "+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.floordiv }
diff = { "easy":1, "medium":2, "hard":3 }

#Question


class Question(object):
    def __init__(self, d):
        self.randomList = []
#        self.questiontype = q #Question type differs between each inherited classes
        self.difficulty = diff[d] #We need to talk about this        
        self.question = "" #Randomly Generated Questions
        self.answer = 0 #Answer for randomly generated question
        self.yanswerstr = "" #Question generated by getAnswer function
        self.yanswer = 0 #Answer generated by getAnswer function
        self.range = int(10 * (10.0**(1.0/3.0))**self.difficulty)

    def getAnswer(self): #This will be the function that takes user input and generate the answer and the question string
        pass

    def chkAnswer(self):
        return self.answer == self.youranswer

    def closeness(self):
        return self.youranswer/self.answer

#Arithmetics
#Take Difficulty level(possibly an integer)
#and Question Type, of 'maximize', 'quiz', or 'match'
class Arith(Question):
    def __init__(self, d):
        super(Arith, self).__init__(d)
        self.randomList = [ random.randint(1, self.range) for r in xrange(3) ]
        self.randops = random.sample(ops, 2)
        self.question = self.quiz()
        if "/" in self.question:
            self.answer = round(self.answer,2)
        else:
            self.answer = int(self.answer)

    def quiz(self):
        trandomList = [ float(r) for r in self.randomList ]
        tops = list(self.randops)
        firstNumber = trandomList[random.randrange(len(trandomList))]
        firstOps = tops[random.randrange(len(tops))]
        trandomList.remove(firstNumber)
        tops.remove(firstOps)
        secondNumber = trandomList[random.randrange(len(trandomList))]
        trandomList.remove(secondNumber)
        self.answer = eval(str(firstNumber) + ' ' + firstOps + ' ' + str(secondNumber) + ' ' + tops[0] + ' ' + str(trandomList[0]))
        return str(int(firstNumber)) + ' ' + firstOps + ' ' + str(int(secondNumber)) + ' ' + tops[0] + ' ' + str(int(trandomList[0]))

#    def maximize(self):
#        maxlist = {}
#        for i in range(len(self.randomList)):
#            p = str(self.randomList[i%3]) + ' ' + self.randops[0] + ' ' + str(self.randomList[(i+1)%3]) + ' ' + self.randops[1] + ' ' + str(self.randomList[(i+2)%3])
#            maxlist[p] = eval(p)
#            p = str(self.randomList[i%3]) + ' ' + self.randops[0] + ' ' + str(self.randomList[(i+2)%3]) + ' ' + self.randops[1] + ' ' + str(self.randomList[(i+1)%3])
#            maxlist[p] = eval(p)
#            p = str(self.randomList[i%3]) + ' ' + self.randops[1] + ' ' + str(self.randomList[(i+1)%3]) + ' ' + self.randops[0] + ' ' + str(self.randomList[(i+2)%3])
#            maxlist[p] = eval(p)
#            p = str(self.randomList[i%3]) + ' ' + self.randops[1] + ' ' + str(self.randomList[(i+2)%3]) + ' ' + self.randops[0] + ' ' + str(self.randomList[(i+1)%3])
#            maxlist[p] = eval(p)
            
#        return max(maxlist.iterkeys(), key=lambda k: maxlist[k])
    
#    def match(self):
#        pass


#Decimal Arithmetics.
#Takes Difficulty level(possibly an integer)
#and Question Type, of 'maximize', 'quiz', or 'match'

class decArith(Arith):
    def __init__(self, d):
        super(decArith, self).__init__(d)
        self.randomList = [ round(self.range/2.0 * random.random() + 1, 1 if self.difficulty < 3 else 2) for r in xrange(3) ]
        self.question = self.quiz()
        self.answer = round(eval(self.question),2)

    def quiz(self):
        trandomList = list(self.randomList)
        tops = list(self.randops)
        firstNumber = trandomList[random.randrange(len(trandomList))]
        firstOps = tops[random.randrange(len(tops))]
        trandomList.remove(firstNumber)
        tops.remove(firstOps)
        secondNumber = trandomList[random.randrange(len(trandomList))]
        trandomList.remove(secondNumber)
        return str(firstNumber) + ' ' + firstOps + ' ' + str(secondNumber) + ' ' + tops[0] + ' ' + str(trandomList[0])


class fraction(Question):
    def __init__(self, d, like):
        super(fraction, self).__init__(d)
        self.denominator = random.randrange(self.range/3) + 1
        self.randops = random.sample(ops,1)
        self.randomList = [ Fraction(random.randrange(self.denominator - 1) + 1, self.denominator)
                            for r in xrange(2) ]
        self.quiz()

    def quiz(self):
        randomint = random.randrange(len(self.randomList))
        self.answer = ops[self.randops[0]](self.randomList[(randomint + 1)%len(self.randomList)],
            self.randomList[randomint])
        self.question = str(self.randomList[(randomint + 1)%len(self.randomList)]) + ' ' + self.randops[random.randrange(len(self.randops))] + ' ' + str(self.randomList[randomint])

class statistic(Question):
    def __init__(self, d, q):
        pass