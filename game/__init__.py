import spyral
import startScreen
import division
import question
import additionScreen

def main():
#	q = question.Question("Arithmetic", "hard")

#	while(q.randomOpKey != "/"):
#		q = question.Question("Arithmetic", "hard")
#	spyral.director.push(division.DivisionScreen(q, "hard"))
	spyral.director.push(startScreen.StartScreen())