import spyral

from hero import Hero

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

#Scene used for battle
class FaceoffScreen(spyral.Scene):
    def __init__(self, hero):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = hero
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

        self.form.selectButton.pos = (WIDTH/2-70, HEIGHT/2)
        self.form.backButton.pos   = (10, 10)
        self.form.answerButton.pos = (WIDTH/2+70, HEIGHT/2)
        self.form.answerField.pos  = (WIDTH/2+150, HEIGHT/3+30)

        self.form.answerButton.visible = False
        self.form.answerField.visible  = False
        
        ## Screen Text
        self.battleTitle = drawFont(self.scene, "Extras/Comic_Book.ttf", "BATTLE", 50)
        self.battleTitle.pos = (WIDTH/2-170, HEIGHT/3+30)



### Temporary addition of cards until game hero is correctly passed to file
### TODO 
        self.hero.addCardToLooseCards("Arithmetic")
        self.hero.addCardToLooseCards("Geometry")
        self.hero.looseCards["Arithmetic"].draw(self)
        self.hero.looseCards["Geometry"].draw(self)

        self.hero.addCardToDeck("Arithmetic")
        self.hero.addCardToDeck("Geometry")
###
        self.drawAllCards()

        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("form.RegisterForm.selectButton.changed", self.startBattle)
        spyral.event.register("form.RegisterForm.backButton.changed", self.backClicked)
        spyral.event.register("form.RegisterForm.answerButton.changed", self.submitAnswer)

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

        for card in self.hero.deck:
            self.hero.deck[card].visible = True
            self.hero.deck[card].handle_deselect()        

#### Submit answer to system
#### TODO implement game logic, damage, if answer is close -> still does damage?
    def submitAnswer(self, event):
        if (event.value == "down"):
            # if answer is correct
            if float(self.form.answerField.value) == float(self.hero.deck[self.selectedSubject].answer):
                print ("True: "+ str(self.hero.deck[self.selectedSubject].damage) +" Damage")
            else:
                print ("False: 0 Damage?")
        self._reset()
            



#### Starts the battle
    def startBattle(self, event):
        if (event.value == "down"):
            count = 0
            subjects = []
            # If no card selected, don't show anything
            try:
                self.form.answerField.visible = False
                self.showQuestion.visible = False
            except:
                pass

            # If there is more than one card selected, don't run
            for card in self.hero.deck:
                if self.hero.deck[card].clicked:
                    count += 1
                    subjects.append(self.hero.deck[card].subject)
                self.hero.deck[card].visible = False
            if count == 1:
                self.selectedSubject = subjects[0]
                self.hero.deck[self.selectedSubject].visible = True

                self.battleTitle.visible       = False
                self.form.selectButton.visible = False
                self.form.answerField.visible  = True
                self.form.answerButton.visible = True

###TODO Show question text on screen
                self.showQuestion = drawFont(self.scene, "Extras/Comic_Book.ttf", self.hero.deck[self.selectedSubject].question, 25)
                self.showQuestion.pos = (WIDTH/2-100, HEIGHT/3+30)
###
        # If there are no card selected, show all cards
            if count == 0:
                for card in self.hero.deck:
                    self.hero.deck[card].visible = True
        


#### Draws all of Hero's cards on screen
    def drawAllCards(self):
        x = WIDTH/12
        y = HEIGHT - 320

        ## Draw deck cards
        for card in self.hero.deck:
            self.hero.deck[card].visible = True
            self.hero.deck[card].setPos(x, y)
            x = x + 400

#### Go back to controlPanelScreen
    def backClicked(self, event):
        if (event.value == "down"):
            spyral.director.pop()
