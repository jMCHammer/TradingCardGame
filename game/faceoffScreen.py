import spyral
import model

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
        f = spyral.Font(font, size)
        self.image = f.render(text)

#### Used to draw a vertical linear animation 
    def draw_linearly(self, x, starty, endy):
        animation = Animation('y', easing.Linear(starty, endy), duration = 1.5)
        self.animate(animation)

#Scene used for battle
class FaceoffScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = Hero(self)
### TODO Pass on selected Opponent from StartFaceoffScreen
        self.opponent = Opponent("Youngster Joey")
###
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")
        self.layers = ["bottom", "text"]

        ## Adds widgets to screen
        class RegisterForm(spyral.Form):
            #Buttons
            selectButton = spyral.widgets.Button("Select Card")
            backButton   = spyral.widgets.Button("Back")
            answerButton = spyral.widgets.Button("Submit")
            #Fields
            answerField  = spyral.widgets.TextInput(50, "")

        self.form = RegisterForm(self)
        # Setting positions
        self.form.selectButton.pos = (WIDTH/2-70, HEIGHT/2)
        self.form.backButton.pos   = (10, 10)
        self.form.answerButton.pos = (WIDTH/2+70, HEIGHT/2)
        self.form.answerField.pos  = (WIDTH/2+150, HEIGHT/3+30)
        # Setting visible
        self.form.answerButton.visible = False
        self.form.answerField.visible  = False
        
        self.deck = {}
        # Initalize all cards
        for card_guts in model.deck:
            card_guts = model.deck[card_guts]
            self.deck[card_guts[0]] = (Card(self, card_guts[0], card_guts[1], card_guts[2]))

        ## Screen Text
        self.battleTitle = drawFont(self.scene, "Extras/Comic_Book.ttf", "BATTLE", 50)
        self.battleTitle.pos = (WIDTH/2-170, HEIGHT/3+30)

        self.showOppHealth = [0, 0, 0]
        self.showHealth = [0, 0, 0]
        count = 0
        for card in self.deck:
            self.showHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", str(self.deck[card].health), 25))

        self.drawAllCards()

        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("form.RegisterForm.selectButton.changed", self.startBattle)
        spyral.event.register("form.RegisterForm.backButton.changed", self.backClicked)
        spyral.event.register("form.RegisterForm.answerButton.changed", self.submitAnswer)




################### Battle Logic #########################################
#### Deal Hero Damage to Opponent
    def dealDamage(self, damage):
        # Draw damage on screen
        self.showDamage = drawFont(self.scene, "Extras/Comic_Book.ttf", str(damage), 35)
        self.showDamage.pos = (WIDTH-150, HEIGHT-100)
        self.showDamage.draw_linearly(WIDTH-150, HEIGHT - 100, 100)

        # Deal damage
        # TODO 
###TODO Temporary
        self.opponent.deck[self.opponent.selectedSubject].applyDamage(damage)
###

#### Starts the battle
    def startBattle(self, event):
        if (event.value == "down"):
            count = 0
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
                if self.deck[card].clicked:
                    subjects.append(self.deck[card].subject)
                    self.deck[card].visible = False
                    print self.deck
                    print self.showHealth
                    self.showHealth[count].visible = False
                    count += 1

            # If there is one card selected, start battle
            if count == 1:
                self.selectedSubject = subjects[0]
                self.deck[self.selectedSubject].visible = True

                self.battleTitle.visible       = False
                self.form.selectButton.visible = False
                self.form.answerField.visible  = True
                self.form.answerButton.visible = True

###TODO Show question text on screen
                self.showQuestion = drawFont(self.scene, "Extras/Comic_Book.ttf", self.deck[self.selectedSubject].question, 25)
                self.showQuestion.pos = (WIDTH/2-100, HEIGHT/3+30)
###
        # If there are no card selected, show all cards
            if count == 0:
                for card in self.deck:
                    self.deck[card].visible = True
                    self.showHealth[count].visible = True

        
################### Event Handlers ############################################
#### Submit answer to system
#### TODO implement game logic, damage, if answer is close -> still does damage?
    def submitAnswer(self, event):
        if (event.value == "down"):
            # if answer is correct
            if float(self.form.answerField.value) == float(self.deck[self.selectedSubject].answer):
                self.dealDamage(self.deck[self.selectedSubject].damage)
            else:
                print ("False: 0 Damage?")
        self._reset()

################### Drawing Functions #########################################
#### Resets screen
    def _reset(self):
        # Show appropriate buttons and titles
        self.form.selectButton.visible = True
        self.form.answerButton.visible = False
        self.form.answerField.visible  = False

        self.showQuestion.visible = False
        self.battleTitle.visible  = True

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
            self.deck[card].visible = True
            self.deck[card].pos = (x, y)
            x = x + 400
            count += 1


    def setPositions(self):
        topx = WIDTH/6
        topy = 15
        bottomx = WIDTH/6
        bottomy = HEIGHT - 300
        dxl = WIDTH/(len(model.looseCards) + 1)
        dxd = WIDTH/(len(model.deck) + 1)

        print self.cards
        print model.deck
        print model.looseCards
        # Delete any cards that were moved
        for subject in self.cards:
            card = self.cards[subject]
            if subject in model.looseCards:
                # Draw cards
                card.pos = (topx,topy)
                topx = topx + dxl
            else:
                card.pos = (bottomx,bottomy)
                bottomx = bottomx + dxd

        ## Draw Opponent's deck cards
###############################MAJOR TODO ######################## Figure out why project is only drawing one set of cards
        y = 10
        x = WIDTH/12
        count = 0
        for card in self.opponent.deck:
            try:    
                self.showOppHealth[count].visible = False
#                del self.showHealth[count]
            except:
                pass
            # Init health counters
            self.showOppHealth[count] = (drawFont(self.scene, "Extras/Comic_Book.ttf", str(self.opponent.deck[card].health), 25))
            # Draw Health counters on screen
            self.showOppHealth[count].layer = "text"
            self.showOppHealth[count].pos = (x + 70, y + 295)
            # Draw cards on screen
            self.opponent.deck[card].layer = "text"
            self.opponent.deck[card].visible = True
            self.opponent.deck[card].pos = (x, y)
            x = x + 400
            count += 1


################### Exit ######################################################
#### Go back to controlPanelScreen
    def backClicked(self, event):
        if (event.value == "down"):
            spyral.director.pop()
