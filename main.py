from cards import cardDeck, Tk, Frame, Label, LabelFrame, Button, Text
from PIL import Image, ImageTk

def main():
    root = Tk()
    card_deck=cardDeck()
    card_deck.load_images()
    root.title("Card rubmle")
    root.geometry("900x500")
    root.configure(background="green")

    cards_frame=Frame(root, background="green")
    cards_frame.pack(pady=20)

    deck_frame=LabelFrame(cards_frame,text="Cards in deck: 50",bd=0)
    deck_frame.grid(row=0, column=0, padx=20, pady=20)

    dealer_frame=LabelFrame(cards_frame, text="Dealer", bd=0)
    dealer_frame.grid(row=0, column=1, padx=20, ipadx=20)

    player_frame=LabelFrame(cards_frame, text="Player", bd=0)
    player_frame.grid(row=0, column=2, ipadx=20)

    #Put cards in frames
    deck_label=Label(deck_frame,text="")
    deck_label.pack(pady=20)
    deck_image=ImageTk.PhotoImage(Image.open("images/back_small.png").resize((150,218)))
    deck_label.configure(image=deck_image)

    dealer_label=Label(dealer_frame, text="")
    dealer_label.pack(pady=20)

    player_label=Label(player_frame,text="")
    player_label.pack(pady=20)

    #Number of cards in the deck
    # start_game_text=Text(root, height=5, width=52)
    # start_game_label=Label(root, text=f"Cards in the deck: {len(card_deck.shuffle(dealer_label,player_label))}",font=("Tahoma",14),background="green")
    # start_game_label.pack()

    #Counting scores
    score_text=Text(root,height=5, width=22)
    score_text=Label(root, text=f"Dealer - 0 : 0 - Player", background="green")
    score_text.pack()

    #Creating buttons
    get_cards_button=Button(root, text="Play", font=("Helvetica",14), command=lambda: card_deck.deal_cards(dealer_label,player_label,deck_frame,score_text))
    get_cards_button.pack(pady=20)

    shuffle_button=Button(root, text="Shuffle cards", font=("Helvetica",14),command=lambda: card_deck.shuffle(dealer_label, player_label, score_text))
    shuffle_button.pack()

    #Shuffling the deck
    card_deck.shuffle(dealer_label,player_label,score_text)

    root.mainloop()

if __name__=="__main__":
    main()