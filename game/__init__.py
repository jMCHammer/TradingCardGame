import spyral
import startScreen
import division
import question
import additionScreen
import subtractionScreenDuke as sub
import integerScreen as integer
import multiplication as mult

def main():
#	q = question.Question("Arithmetic", "hard")
#	while(q.randomOpKey != '*'):
#		q = question.Question("Arithmetic", "hard")
#	spyral.director.push(mult.mainScreen(q, "hard"))
	spyral.director.push(startScreen.StartScreen())

###################### Integer Screen #######################
# To Test: Comment Top line and uncomment following 2 lines
#	q = question.Question("Integer", "medium")
#	spyral.director.push(integer.mainScreen(q, "medium"))