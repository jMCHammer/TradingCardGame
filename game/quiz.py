import operator
import random

ops = { "+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.floordiv}

def quiz():
    stuff = [ float(random.randrange(10000))/100.0, float(random.randrange(10000))/100.0, float(random.randrange(10000))/100.0 ]
    randops = random.sample(ops, 2)

    print stuff
    print randops

    x = raw_input("Choose first number (0-2):")
    y = raw_input("Choose first operator (0-1):")
    z = raw_input("Choose second number (0-2):")

    rm1 = stuff[int(x)]
    rm2 = stuff[int(z)]
    stuff.remove(rm1)
    stuff.remove(rm2)
    rm3 = randops[int(y)]
    randops.remove(rm3)
    answers = str(rm1) + rm3 + str(rm2) + randops[0] + str(stuff[0])
    answer = eval(answers)
    print "Your number: " + answers + ' =  '+ str(answer)

    stuff.append(rm1)
    stuff.append(rm2)
    randops.append(rm3)
    maxlist = []

    for i in range(len(stuff)):
        maxlist.append(eval(str(stuff[i%3]) + randops[0] + str(stuff[(i+1)%3]) + randops[1] + str(stuff[(i+2)%3])))
        maxlist.append(eval(str(stuff[i%3]) + randops[0] + str(stuff[(i+2)%3]) + randops[1] + str(stuff[(i+1)%3])))
        maxlist.append(eval(str(stuff[i%3]) + randops[1] + str(stuff[(i+1)%3]) + randops[0] + str(stuff[(i+2)%3])))
        maxlist.append(eval(str(stuff[i%3]) + randops[1] + str(stuff[(i+2)%3]) + randops[0] + str(stuff[(i+1)%3])))

    print "Possible Maximum Number:" + str(max(maxlist))
