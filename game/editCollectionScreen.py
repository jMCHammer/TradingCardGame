import spyral
import model

from card import Card
from hero import Hero
from spyral import Vec2D

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
        self.background = spyral.image.Image("Extras/editCollectionBackgroundTemplate.png").scale(Vec2D(1200,900))
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

        self.cards = {}
        # Initalize all cards
        for card_guts in model.looseCards:
            card_guts = model.looseCards[card_guts]
            self.cards[card_guts[0]] = (Card(self, card_guts[0], card_guts[1], card_guts[2]))
        for card_guts in model.deck:
            card_guts = model.deck[card_guts]
            self.cards[card_guts[0]] = (Card(self, card_guts[0], card_guts[1], card_guts[2]))

        self.setPositions()

        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("form.RegisterForm.addButton.changed", self.addToDeck)
        spyral.event.register("form.RegisterForm.removeButton.changed", self.removeFromDeck)
        spyral.event.register("form.RegisterForm.backButton.changed", self.backClicked)

    # Draws cards in their proper positions on the screen
    def setPositions(self):
        topx = WIDTH/6
        topy = 15
        bottomx = WIDTH/6
        bottomy = HEIGHT - 300
        dxl = WIDTH/(len(model.looseCards) + 1)
        dxd = WIDTH/(len(model.deck) + 1)
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
        



#### Event Handlers
    def addToDeck(self, event):
        if (event.value == "down"):
            for subject in self.cards: 
                card = self.cards[subject]
                if card.clicked:
                    card.handle_deselect()
                    if len(model.deck) < 3 and subject in model.looseCards:
                        model.deck[subject] = model.looseCards[subject]
                        del model.looseCards[subject]
                    else:
                        print ("A deck can't have more than 3 cards OR Card isn't in looseCards")
                    self.setPositions()

    def removeFromDeck(self, event):
        if (event.value == "down"):
            for subject in self.cards: 
                card = self.cards[subject]
                if card.clicked:
                    card.handle_deselect()
                    if subject in model.deck:
                        model.looseCards[subject] = model.deck[subject]
                        del model.deck[subject]
                    else:
                        print ("subject isn't in deck")
                    self.setPositions()

#### Go back to controlPanelScreen
    def backClicked(self, event):
        if (event.value == "down"):
            ##TODO GET RID OF
            spyral.director.pop()

################### Add or Remove Cards from Deck #############################
#### Adds new card to looseCards from allCards
    def addCardToLooseCards(self, subject):
        if subject in model.allCards:
            model.looseCards[subject] = model.allCards[subject]
        else:
            print ("Card doesn't exist")
