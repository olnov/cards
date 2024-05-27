# import random
# from PIL import Image, ImageTk
from cards import random
from PIL import Image, ImageTk
from tkinter import Label

class cardDeck:

    def __init__(self) -> None:
        self.suits=["diamonds","clubs","hearts","spades"]
        self.values=range(2,15)
        self.deck=[]
        self.player=[]
        self.dealer=[]
        self.images={}
        self.player_score=0
        self.dealer_score=0

    def __get_card(self):
        card=random.choice(self.deck)
        print (f"Random card: {card}")
        return card
    
    def __remove_card(self, card):
        self.deck.remove(card)
        print (f"Cards in the deck:{len(self.deck)}")
        return self.deck

    def shuffle(self,dealer_label,player_label,score_text):
        #Resetting the deck
        self.deck=[]
        #Resetting player and dealer
        self.player=[]
        self.dealer=[]
        self.dealer_score=0
        self.player_score=0
        for suit in self.suits:
            for value in self.values:
                self.deck.append(f"{value}_of_{suit}")
        print(self.deck)
        print(f"deck lenght is: {len(self.deck)}")
        #Resetting scores
        score_text.configure(text=f"Dealer - {self.dealer_score} : {self.player_score} - Player")
        #Dealer's card
        dealer_card=self.__get_card()
        self.dealer.append(dealer_card)
        self.__remove_card(dealer_card)
        #Player's card 
        player_card=self.__get_card()
        self.player.append(player_card)
        self.__remove_card(player_card)
        #Dealing cards
        dealer_label.config(image=self.images[self.dealer[-1]])
        print(f"Dealer deck: {self.dealer}")
        player_label.config(image=self.images[self.player[-1]])
        print(f'Player deck: {self.player}')
        return self.deck
    
    def deal_cards(self,dealer_label,player_label,deck_frame,score_text):
        try:
            #Dealer's card. Gettin a card from the deck to dealer and removing from the deck
            dealer_card=self.__get_card()
            self.dealer.append(dealer_card)
            self.__remove_card(dealer_card)
            #Player's card. Getting a card from the deck to player and removing from the deck
            player_card=self.__get_card()
            self.player.append(player_card)
            self.__remove_card(player_card)
            #Updating cards on the screen.
            dealer_label.config(image=self.images[self.dealer[-1]])
            print(f"Dealer deck: {self.dealer}")
            player_label.config(image=self.images[self.player[-1]])
            print(f'Player deck: {self.player}')
            deck_frame.config(text=f"Cards in deck: {len(self.deck)}")
            print (f"Remaining cards in the deck: {len(self.deck)}")
            if int(self.dealer[-1][0:1])>int(self.player[-1][0:1]) and len(self.deck)!=0:
                self.dealer_score+=1
                print (f"Dealer card: {self.dealer[-1][0:1]}")
                print (f"Player card: {self.player[-1][0:1]}")
                print (f"Delaer score: {self.dealer_score}")
                score_text.configure(text=f"Dealer - {self.dealer_score} : {self.player_score} - Player")
            elif int(self.dealer[-1][0:1])<int(self.player[-1][0:1]) and len(self.deck)!=0:
                self.player_score+=1
                print (f"Dealer card: {self.dealer[-1][0:1]}")
                print (f"Player card: {self.player[-1][0:1]}")
                print(f"Player score: {self.player_score}")
                score_text.configure(text=f"Dealer - {self.dealer_score} : {self.player_score} - Player")
            else:
                pass
        except:
            if self.dealer_score>self.player_score:
                print (f" The winner is Dealer")
                score_text.configure(text=f"Dealer wins!")
            else:
                print(f"The winner is Player")
                score_text.configure(text=f"Player wins!")
            print(f"No more cards in the deck")
        return self.dealer_score, self.player_score
     
    def load_images(self):
        for suit in self.suits:
            for value in self.values:
                card_name = f"{value}_of_{suit}"
                image_path = f"images/{card_name}.png"
                self.images[card_name] = ImageTk.PhotoImage(Image.open(image_path).resize((150,218)))