import spyral
import controlPanelScreen
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

#Scene used to edit Deck used in battle
class EditCollectionScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = Hero(self.scene)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")
        self.layers = ["bottom", "text"]

        deckTitle = drawFont(self.scene, "Extras/Comic_Book.ttf", "Deck", 50)
        screenTitle = drawFont(self.scene, "Extras/Comic_Book.ttf", "Edit Collection", 50)
        screenTitle.pos = (WIDTH/2-170, HEIGHT/3+30)
        deckTitle.pos = (WIDTH/2-50, HEIGHT*2/3-85)

        class RegisterForm(spyral.Form):
            addButton = spyral.widgets.Button("Add to Deck")
            removeButton = spyral.widgets.Button("Remove from Deck")
            backButton = spyral.widgets.Button("Back")

        form = RegisterForm(self)
        form.addButton.pos = (WIDTH/2-70, HEIGHT/2)
        form.removeButton.pos = (WIDTH/2+40, HEIGHT/2)
        form.backButton.pos = (10, 10)

#### Temporary addition of Cards to deck
        self.hero.addCardToLooseCards("Arithmetic")
        self.hero.addCardToLooseCards("Geometry")
        self.hero.looseCards["Arithmetic"].draw(self)
        self.hero.looseCards["Geometry"].draw(self)
####

        self.drawAllCards() 
        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("form.RegisterForm.addButton.changed", self.addToDeck)
        spyral.event.register("form.RegisterForm.removeButton.changed", self.removeFromDeck)
        spyral.event.register("form.RegisterForm.backButton.changed", self.backClicked)

#### Draws all of Hero's cards on screen
    def drawAllCards(self):
        x = WIDTH/12
        y = 10
        
        ## Draw loose cards
        for card in self.hero.looseCards:
            self.hero.looseCards[card].visible = True
            self.hero.looseCards[card].setPos(x,y)
            x = x + 220

        x = WIDTH/12
        y = HEIGHT-315

        ## Draw deck cards
        for card in self.hero.deck:
            self.hero.deck[card].visible = True
            self.hero.deck[card].setPos(x, y)
            x = x + 220

#### Event Handlers
    def addToDeck(self, event):
        subjects = []
        if (event.value == "down"):
            for card in self.hero.looseCards: 
                if self.hero.looseCards[card].clicked:
                    self.hero.looseCards[card].handle_deselect()
                    subjects.append(self.hero.looseCards[card].subject)
            for subject in subjects:
                self.hero.addCardToDeck(subject)
            self.drawAllCards()


    def removeFromDeck(self, event):
        subjects = []
        if (event.value == "down"):
            for card in self.hero.deck: 
                if self.hero.deck[card].clicked:
                    self.hero.deck[card].handle_deselect()
                    subjects.append(self.hero.deck[card].subject)
            for subject in subjects:
                self.hero.removeCardFromDeck(subject)
            self.drawAllCards()

#### Go back to controlPanelScreen
    def backClicked(self, event):
        if (event.value == "down"):
            spyral.director.pop()

