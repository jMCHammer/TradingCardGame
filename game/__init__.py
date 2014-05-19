import spyral
import startScreen
import division
import question
import additionScreen
import subtractionScreenDuke as sub
import integerScreen as integer
import multiplication as mult

def main():
	q = question.Question("Arithmetic", "easy")
	while(q.randomOpKey != '*'):
		q = question.Question("Arithmetic", "easy")

#	spyral.director.push(division.sinkingScreen(q,"hard"))
#	spyral.director.push(mult.mainScreen(q, "easy"))
#	spyral.director.push(sub.mainScene(q, "hard"))
	spyral.director.push(startScreen.StartScreen())

###################### Integer Screen #######################
# To Test: Comment Top line and uncomment following 2 lines
#	q = question.Question("Integer", "medium")
#	spyral.director.push(integer.mainScreen(q, "medium"))