import spyral
import model
import endGameScreen
import division
import subtractionScreenDuke as subtraction

from opponent import Opponent
from spyral import Animation, easing
from hero import Hero
from card import Card

WIDTH    = 1200
HEIGHT   = 900
BG_COLOR = (0,0,0)
WHITE    = (255, 255, 255)
SIZE     = (WIDTH, HEIGHT)

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text, size):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, size, WHITE)
        self.image = f.render(text)

class Fireball(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self,Scene)
        self.image = model.resources["fireball"]
  #      self.visible = False

#### Used to draw a linear animation 
  #  def draw_linearly(self, startx, endx, starty, endy):
    def draw_linearly(self, startx, starty, endy):
  #      self.visible = True
        animation = Animation('y', easing.Linear(starty, endy), duration = 1.5)
  #      animation2 = Animation('x', easing.Linear(startx, endx), duration = 1.5)
  #      animation = animation1 & animation2
        self.animate(animation)

  #      self.visible = False


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
        
        self.fireball = Fireball(self)
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
            self.showHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", str(self.deck[card].health), 25))
        count = 0
        for card in self.opponentcards:
            self.showOppHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", str(self.opponentcards[card].health), 25))
        
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
        if self.selectedSubject == "Addition":
            if self.deck[self.selectedSubject].q.randomOpKey == "/":
                spyral.director.push(division.sinkingScreen(self.deck[self.selectedSubject].q, diff))
            elif self.deck[self.selectedSubject].q.randomOpKey == "-":
                spyral.director.push(subtraction.mainScene(self.deck[self.selectedSubject].q, diff))
        self.showQuestion = drawFont(self.scene, "Extras/Comic_Book.ttf", self.deck[self.selectedSubject].question, 25)
        self.showQuestion.pos = (WIDTH/2-100, HEIGHT/2)
        self.form.answerField.visible  = True
        self.form.answerButton.visible = True

################### Battle Logic #########################################
#### Deal Hero Damage to Opponent
    def dealDamage(self, damage):
        #Draw damage on screen
        #Draw damage from hero to opponent
        self.fireball.pos(self.opponentcards[self.opponent.selectedSubject].x, HEIGHT - 100)

        self.fireball.draw_linearly(self.opponentcards[self.opponent.selectedSubject].x,
                                    #self.deck[self.selectedSubject].x, 
                                    #self.deck[self.selectedSubject].y, 
                                    HEIGHT - 100,
                                    #self.opponentcards[self.opponent.selectedSubject].x, 
                                    self.opponentcards[self.opponent.selectedSubject].y)

        #Draw damage from opponent to hero 
  #      self.fireball.draw_linearly(self.opponentcards[self.opponent.selectedSubject].x, 
   #                                 self.opponentcards[self.opponent.selectedSubject].y, 
    #                                self.deck[self.selectedSubject].x, 
     #                               self.deck[self.selectedSubject].y)

        # Deal damage
        self.opponentcards[self.opponent.selectedSubject].applyDamage(damage)
        print "Successfully dealth damage"
###

#### Starts the battle
    def startBattle(self, event):
#TODO
        print self.deck
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
        if (event.value == "down"):
            # if answer is correct
            try:
                if float(self.form.answerField.value) == float(self.deck[self.selectedSubject].answer):
                    self.dealDamage(self.deck[self.selectedSubject].damage)
                print "Opponent's answer: " + str(self.opponent.answerQuestion())
                self._reset()
            except(ValueError):
                pass

#    def submitScreenAnswer(self, correct):
#        if correct:
#            self.dealDamage(self.deck[self.selectedSubject].damage)
#        self._reset()

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
            self.showHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", str(self.deck[card].health), 25))
            # Draw Health counters on screen
            self.showHealth[count].layer = "text"
            self.showHealth[count].pos = (x + 70, y - 35)
            # Draw cards on screen
            self.deck[card].layer = "text"
            if self.deck[card].alive:
                self.deck[card].visible = True
            self.deck[card].pos = (x, y)
            x = x + 400
            count += 1

        # Opponent cards
        x = WIDTH/5
        y = 15
        count = 0
        for card in self.opponentcards:
            try:    
                self.showOppHealth[count].visible = False
#                del self.showHealth[count]
            except:
                pass
            # Init health counters
            self.showOppHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", str(self.opponentcards[card].health), 25))
            self.showOppHealth[count].layer = "text"
            self.showOppHealth[count].pos = (x + 70, y + 300)
            # Draw cards on screen
            self.opponentcards[card].layer = "text"
            if self.opponentcards[card].alive:
                self.opponentcards[card].visible = True
            #Card placement
            self.opponentcards[card].pos = (x, y)
            x = x + 200
            count += 1

################### Exit ###################################################
#### Go back to controlPanelScreen
    def backClicked(self, event):
        if (event.value == "down"):
            spyral.director.pop()

