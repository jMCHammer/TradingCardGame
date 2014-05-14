import spyral
import startScreen
import division
import question
import additionScreen
import subtractionScreenDuke as sub
import integerScreen as integer

def main():
	spyral.director.push(startScreen.StartScreen())

###################### Integer Screen #######################
# To Test: Comment Top line and uncomment following 2 lines
#	q = question.Question("Arithmetic", "medium")
#	spyral.director.push(integer.mainScreen(q, "medium"))