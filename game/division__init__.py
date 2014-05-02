import spyral
import startScreen
import division
import question

def main():
	q = question.Question("Arithmetic", "medium")

	while(q.randomOpKey != "/"):
		q = question.Question("Arithmetic", "medium")
	spyral.director.push(division.DivisionScreen(q))
