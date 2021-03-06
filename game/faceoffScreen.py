import spyral
import model
import endGameScreen
import division
import subtractionScreenDuke as subtraction
import integerScreen as integer
import multiplication as mult

from opponent import Opponent
from spyral import Animation, easing
from hero import Hero
from card import Card
import time

WIDTH    = 1200
HEIGHT   = 900
BG_COLOR = (0,0,0)
GREEN    = (0, 255, 0)
RED      = (255, 0, 0)
WHITE    = (200, 200, 200)
SIZE     = (WIDTH, HEIGHT)

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text, size):
        spyral.Sprite.__init__(self,Scene)
        if text == "Correct!":
            f = spyral.Font(font, size, GREEN)
        elif text == "Wrong":
            f = spyral.Font(font, size, RED)
        else:
            f = spyral.Font(font, size, WHITE)
        self.image = f.render(text)

class Fireball(spyral.Sprite):
    def __init__(self, Scene,c):
        spyral.Sprite.__init__(self,Scene)
        self.image = model.resources["fireball"+str(c)]
        self.image = model.resources["fireball"+str(c)]

#### Used to draw a linear animation 
    def draw_linearly(self, starty, endy):
        animation = Animation('y', easing.Linear(starty, endy), duration = 1.5)
        self.animate(animation)

#Scene used for battle
class FaceoffScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = Hero(self)
        self.hero.pos = (WIDTH-180, HEIGHT - 395)
        self.hero.scale_x = .80;
        self.hero.scale_y = .80;
        # Create Opponent Sprite
        self.opponent = Opponent(self);

        self.correct = False
        self.fireball1 = Fireball(self,1)
        self.fireball2 = Fireball(self,2)
        self.background = model.resources[model.currentOpponent + "bg"]
        self.layers = ["bottom", "text"]

        ## Adds widgets to screen
        class RegisterForm(spyral.Form):
            #Buttons
            selectButton = spyral.widgets.Button("Select Card")
            backButton   = spyral.widgets.Button("Back")
            answerButton = spyral.widgets.Button("Submit")

            easyButton   = spyral.widgets.Button("Easy")
            mediumButton = spyral.widgets.Button("Medium")
            hardButton   = spyral.widgets.Button("Hard")
            #Fields
            answerField  = spyral.widgets.TextInput(50, "")

        self.form = RegisterForm(self)
        # Setting positions
        self.form.selectButton.pos = (WIDTH/2-70, HEIGHT/2)
        self.form.backButton.pos   = (10, 10)
        self.form.answerButton.pos = (WIDTH/2+150, HEIGHT/2)
        self.form.answerField.pos  = (WIDTH/2+70, HEIGHT/2)

        self.form.easyButton.pos = (WIDTH/3, HEIGHT/2)
        self.form.mediumButton.pos = (WIDTH/2, HEIGHT/2)
        self.form.hardButton.pos = (WIDTH*2/3, HEIGHT/2)
        # Setting visible
        self.form.answerButton.visible = False
        self.form.answerField.visible  = False
        self.form.easyButton.visible = False
        self.form.mediumButton.visible = False
        self.form.hardButton.visible = False
        
        self.deck = {}
        self.opponentcards = {}
        # Initalize Hero cards
        for card_guts in model.deck:
            card_guts = model.deck[card_guts]
            self.deck[card_guts[0]] = (Card(self, card_guts[0], card_guts[1], card_guts[2]))
        # Initialize Opponent cards
        for card_guts in self.opponent.deck:
            card_guts = self.opponent.deck[card_guts]
            self.opponentcards[card_guts[0]] = (Card(self, card_guts[0], card_guts[1], card_guts[2]))

        self.showOppHealth = [0, 0, 0]
        self.showHealth = [0, 0, 0]
        count = 0
        for card in self.deck:
            self.showHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", "HP: "+str(self.deck[card].health), 25))
        count = 0
        for card in self.opponentcards:
            self.showOppHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", "HP: "+str(self.opponentcards[card].health), 25))
        
        self.drawAllCards()

        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("form.RegisterForm.selectButton.changed", self.startBattle)
        spyral.event.register("form.RegisterForm.backButton.changed", self.backClicked)
        spyral.event.register("form.RegisterForm.answerButton.changed", self.submitAnswer)
        spyral.event.register("form.RegisterForm.easyButton.changed", self.initEasy)
        spyral.event.register("form.RegisterForm.mediumButton.changed", self.initMedium)
        spyral.event.register("form.RegisterForm.hardButton.changed", self.initHard)

    def initEasy(self, event):
        if (event.value == "down"):
            self.initQ("easy")

    def initMedium(self, event):
        if (event.value == "down"):
            self.initQ("medium")

    def initHard(self, event):
        if (event.value == "down"):
            self.initQ("hard")

    def initQ(self, diff):
        self.form.easyButton.visible = False
        self.form.mediumButton.visible = False
        self.form.hardButton.visible = False

        self.deck[self.selectedSubject].initQuestion(diff)
        ##Screen testcase##
#        while(self.deck[self.selectedSubject].q.randomOpKey != "-"):
#            self.deck[self.selectedSubject].initQuestion(diff)
        ##endtestcase##
        if self.selectedSubject == "Multiplication":
            spyral.director.push(division.sinkingScreen(self.deck[self.selectedSubject].q, diff))
        elif self.selectedSubject == "Subtraction":
            spyral.director.push(subtraction.mainScene(self.deck[self.selectedSubject].q, diff))
        elif self.selectedSubject == "Division":
            spyral.director.push(mult.mainScreen(self.deck[self.selectedSubject].q, diff))
        elif self.selectedSubject == "Integer":
            spyral.director.push(integer.mainScreen(self.deck[self.selectedSubject].q, diff))
        self.showQuestion = drawFont(self.scene, "Extras/Comic_Book.ttf", self.deck[self.selectedSubject].question, 25)
        if self.selectedSubject == "Statistics" or self.selectedSubject == "Geometry":
            self.showQuestion.pos = (20, HEIGHT/2 - 20)
            self.form.answerField.pos = (WIDTH/2 - 50, HEIGHT/2 + 20)
            self.form.answerButton.pos = (WIDTH/2 + 50, HEIGHT/2 + 20)
        else:
            self.showQuestion.pos = (WIDTH/2 - 150, HEIGHT/2)
            self.form.answerButton.pos = (WIDTH/2+150, HEIGHT/2)
            self.form.answerField.pos  = (WIDTH/2+70, HEIGHT/2)
        self.form.answerField.visible  = True
        self.form.answerButton.visible = True

################### Battle Logic #########################################
#### Deal Hero Damage to Opponent
    def dealDamage(self, damage):
        #Draw damage from hero to opponent
        #if hero is correct
        try:
            self.herocorrect.visible = False
            self.opponentcorrect.visible = False
        except:
            pass

        if self.correct:
            #tell hero he is correct
            self.herocorrect = drawFont(self.scene, "Extras/Comic_Book.ttf", "Correct!", 25)
            self.herocorrect.pos = (WIDTH-150, HEIGHT - 450)
            #show fireball/damage
            self.fireball1.pos = (WIDTH-100, HEIGHT - 100)
            self.fireball1.draw_linearly(HEIGHT - 100, 15)
            # modify numbers (damage)
            self.opponentcards[self.opponent.selectedSubject].applyDamage(damage)
        else:
            #tell hero he is wrong
            self.herocorrect = drawFont(self.scene, "Extras/Comic_Book.ttf", "Wrong", 25)
            self.herocorrect.pos = (WIDTH-150, HEIGHT - 450)
        
        #if opponent is correct
        if self.opponent.correct:
            #show opponent is correct
            self.opponentcorrect = drawFont(self.scene, "Extras/Comic_Book.ttf", "Correct!", 25)
            self.opponentcorrect.pos = (50, HEIGHT - 450)
            #show fireball/damage
            self.fireball2.draw_linearly(100, HEIGHT - 100)
            # modify numbers (damage)
            self.deck[self.selectedSubject].applyDamage(self.opponentcards[self.opponent.selectedSubject].damage)
        else:
            #show opponent is wrong 
            self.opponentcorrect = drawFont(self.scene, "Extras/Comic_Book.ttf", "Wrong", 25)
            self.opponentcorrect.pos = (50, HEIGHT - 450)
        
        print "Successfully dealt damage"
###

#### Starts the battle
    def startBattle(self, event):
        subj = self.opponent.pickCard()
        while not self.opponentcards[subj].alive:
            subj = self.opponent.pickCard()
        if (event.value == "down"):
            count = 0
            c = 0
            subjects = []
            # If no card selected, don't show anything
            try:    
                self.form.answerField.visible = False
                self.showQuestion.visible = False
                self.showDamage.visible = False

                del self.showQuestion
                del self.showDamage
            except:
                pass

            # If there is more than one card selected, don't run
            for card in self.deck:
                self.showHealth[c].visible = False
                self.deck[card].visible = False
                if self.deck[card].clicked:
                    subjects.append(self.deck[card].subject)
                    self.deck[card].visible = True
                    self.showHealth[c].visible = True
                    count += 1
                c += 1

            # If there is one card selected, start battle
            if count == 1:
                self.selectedSubject = subjects[0]
                self.deck[self.selectedSubject].visible = True

                self.form.selectButton.visible = False

                self.form.easyButton.visible   = True
                self.form.mediumButton.visible = True
                self.form.hardButton.visible   = True

                c = 0
                # Show opponent's selected card
                for card in self.opponentcards:
                    if not card == subj:
                        self.opponentcards[card].visible = False
                        self.showOppHealth[c].visible = False
                    c += 1

        # If there are no card selected, show all cards
            if count == 0:
                for card in self.deck:
                    self.deck[card].visible = True
                    self.showHealth[count].visible = True
                    count += 1

        
################### Event Handlers ############################################
#### Submit answer to system
    def submitAnswer(self, event):
        self.opponent.answerQuestion()
        if (event.value == "down"):
            # if answer is correct
            try:
                if float(self.form.answerField.value) == float(self.deck[self.selectedSubject].answer):
                    self.correct = True
                else:
                    self.correct = False
                self.dealDamage(self.deck[self.selectedSubject].damage)
                print "Opponent's answer: " + str(self.opponent.correct)
                self._reset()
            except(ValueError):
                pass

    def submitScreenAnswer(self, correct):
        self.opponent.answerQuestion()
        if correct:
            self.correct = True
        else:
            self.correct = False
        self.dealDamage(self.deck[self.selectedSubject].damage)
        self._reset()

################### Drawing Functions #########################################
#### Resets screen
    def _reset(self):
        dead = True
        for card in self.deck:
            if self.deck[card].alive:
                dead = False
        if dead:
            model.opponentDead = False
            spyral.director.replace(endGameScreen.EndGameScreen())
        dead = True
        for card in self.opponentcards:
            if self.opponentcards[card].alive:
                dead = False
        if dead:
            model.opponentDead = True
            spyral.director.replace(endGameScreen.EndGameScreen())

        # Show appropriate buttons and titles
        self.form.selectButton.visible = True
        self.form.answerButton.visible = False
        self.form.answerField.visible  = False
        self.form.easyButton.visible   = False
        self.form.mediumButton.visible = False
        self.form.hardButton.visible   = False

        self.showQuestion.visible = False

        # reset values
        self.form.answerField.value = ""
        for card in self.deck:
            self.deck[card].handle_deselect()    
        self.drawAllCards()

#### Draws all cards on screen
    def drawAllCards(self):
        x = WIDTH/12
        y = HEIGHT - 320
        count = 0

        ## Draw Hero's deck cards
        for card in self.deck:
            try:    
                self.showHealth[count].visible = False
#                del self.showHealth[count]
            except:
                pass
            # Init health counters
            self.showHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf","HP: "+str(self.deck[card].health), 25))
            # Draw Health counters on screen
            self.showHealth[count].layer = "text"
            self.showHealth[count].pos = (x + 70, y - 35)
            # Draw cards on screen
            self.deck[card].layer = "text"
            if self.deck[card].alive:
                self.deck[card].visible = True
            else:
                self.deck[card].visible = False
            self.deck[card].pos = (x, y)
            x = x + 320
            count += 1

        # Opponent cards
        x = WIDTH/4
        y = 15
        count = 0
        for card in self.opponentcards:
            try:    
                self.showOppHealth[count].visible = False
#                del self.showHealth[count]
            except:
                pass
            # Init health counters
            self.showOppHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", "HP: "+str(self.opponentcards[card].health), 25))
            self.showOppHealth[count].layer = "text"
            self.showOppHealth[count].pos = (x + 70, y + 300)
            # Draw cards on screen
            self.opponentcards[card].layer = "text"
            if self.opponentcards[card].alive:
                self.opponentcards[card].visible = True
            else:
                self.opponentcards[card].visible = False 
            #Card placement
            self.opponentcards[card].pos = (x, y)
            x = x + 400
            count += 1
        count = 0

################### Exit ###################################################
#### Go back to controlPanelScreen
    def backClicked(self, event):
        if (event.value == "down"):
            spyral.director.pop()

