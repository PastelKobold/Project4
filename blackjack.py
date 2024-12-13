import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageFilter

#Gavin Catron and Sarah Webster 

card_categories = ['♥', '♦', '♣', '♠'] 
cards_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
deck = [(card, category) for category in card_categories for card in cards_list] 

def card_value(card): 
	if card[0] in ['J', 'Q', 'K']: 
		return 10
	elif card[0] == 'A': 
		return 11
	else: 
		return int(card[0]) 

random.shuffle(deck) 
player1_card = [deck.pop(), deck.pop()] 
player2_card = [deck.pop(), deck.pop()] 
player3_card = [deck.pop(), deck.pop()] 
player4_card = [deck.pop(), deck.pop()] 
dealer_card = [deck.pop(), deck.pop()] 
player1_score = sum(card_value(card) for card in player1_card) 
player2_score = sum(card_value(card) for card in player2_card) 
player3_score = sum(card_value(card) for card in player3_card) 
player4_score = sum(card_value(card) for card in player4_card) 
dealer_score = sum(card_value(card) for card in dealer_card) 

"""
while True: 
	player_score = sum(card_value(card) for card in player_card) 
	dealer_score = sum(card_value(card) for card in dealer_card) 
	print("Cards Player Has:", player_card) 
	print("Score Of The Player:", player_score) 
	print("\n") 
	choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower() 
	if choice == "play": 
		new_card = deck.pop() 
		player_card.append(new_card) 
	elif choice == "stop": 
		break
	else: 
		print("Invalid choice. Please try again.") 
		continue

	if player_score > 21: 
		print("Cards Dealer Has:", dealer_card) 
		print("Score Of The Dealer:", dealer_score) 
		print("Cards Player Has:", player_card) 
		print("Score Of The Player:", player_score) 
		print("Dealer wins (Player Loss Because Player Score is exceeding 21)") 
		break
"""
          
while dealer_score < 17: 
	new_card = deck.pop() 
	dealer_card.append(new_card) 
	dealer_score += card_value(new_card) 

print("Cards Dealer Has:", dealer_card) 
print("Score Of The Dealer:", dealer_score) 
print("\n") 

if dealer_score > 21: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player1_card) 
	print("Score Of The Player:", player1_score) 
	print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)") 
elif player1_score > dealer_score: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player1_card) 
	print("Score Of The Player:", player1_score) 
	print("Player wins (Player Has High Score than Dealer)") 
elif dealer_score > player1_score: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player1_card) 
	print("Score Of The Player:", player1_score) 
	print("Dealer wins (Dealer Has High Score than Player)") 
else: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player1_card) 
	print("Score Of The Player:", player1_score) 
	print("It's a tie.")


#Check win conditions
def checkWin():
    #Check for range
    #Left, Right, Up, Diagonal
    dealer_score = sum(card_value(card) for card in dealer_card) 
    while dealer_score < 17: 
            new_card = deck.pop() 
            dealer_card.append(new_card) 
            dealer_score += card_value(new_card)
    dealer_score = sum(card_value(card) for card in dealer_card) 
    dealerscore.config(text = dealer_score)
    count = 0
    for x in dealer_card:
        result = ""
        count += 1
        #dealer_score = sum(card_value(card) for card in player_card)
        for y in x:
            #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
            #      result = y
            #else:
            result = result + y
            arr[0][count].config(text = result)
            #dealerscore.config(text = dealer_score)
    count = 0
    for x in player1_card:
        result = ""
        count += 1
        player1_score = sum(card_value(card) for card in player1_card)
        for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
            result = result + y
            arr[2][count].config(text = result)
            player1score.config(text = player1_score)

    print("Cards Dealer Has:", dealer_card)
    print("Cards Dealer Has:", dealer_card) 
    print("Score Of The Dealer:", dealer_score)
    print("\n") 
    count = 0
    for x in player2_card:
        result = ""
        count += 1
        player2_score = sum(card_value(card) for card in player2_card)
        for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
            result = result + y
            arr[3][count].config(text = result)
            player2score.config(text = player2_score)
    count = 0
    for x in player3_card:
        result = ""
        count += 1
        player3_score = sum(card_value(card) for card in player3_card)
        for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
            result = result + y
            arr[4][count].config(text = result)
            player3score.config(text = player3_score)
    count = 0
    for x in player4_card:
        result = ""
        count += 1
        player4_score = sum(card_value(card) for card in player4_card)
        for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
            result = result + y
            arr[5][count].config(text = result)
            player4score.config(text = player4_score)

    
    if dealer_score > 21: 
          print("Cards Dealer Has:", dealer_card) 
          print("Score Of The Dealer:", dealer_score) 
          print("Cards Player Has:", player1_card) 
          print("Score Of The Player:", player1_score) 
          print("Everyone wins (Dealer Loss Because Dealer Score is exceeding 21)")
          winLbl.config(text= "Player 1 wins") 
          winLbl2.config(text= "Player 2 wins") 
          winLbl3.config(text= "Player 3 wins") 
          winLbl4.config(text= "Player 4 wins")
          return 
    if player1_score > dealer_score and player1_score <= 21: 
          print("Cards Dealer Has:", dealer_card) 
          print("Score Of The Dealer:", dealer_score) 
          print("Cards Player Has:", player1_card) 
          print("Score Of The Player:", player1_score) 
          print("Player wins (Player Has High Score than Dealer)")
          winLbl.config(text= "Player 1 wins") 
    if player2_score > dealer_score and player2_score <= 21: 
          winLbl2.config(text= "Player 2 wins") 
    if player3_score > dealer_score and player3_score <= 21: 
          winLbl3.config(text= "Player 3 wins") 
    if player4_score > dealer_score and player4_score <= 21: 
          winLbl4.config(text= "Player 4 wins")
    if dealer_score > player1_score or player1_score > 21: 
          winLbl.config(text= "Player 1 loses")
    if dealer_score > player2_score or player2_score > 21:
           winLbl2.config(text= "Player 2 loses")
    if dealer_score > player3_score or player3_score > 21:
          winLbl3.config(text= "Player 3 loses")
    if dealer_score > player4_score or player4_score > 21:
          winLbl4.config(text= "Player 4 loses")
    if dealer_score == player1_score:
          winLbl.config(text= "Tie")
    if dealer_score == player2_score:
          winLbl2.config(text= "Tie")
    if dealer_score == player3_score:
          winLbl3.config(text= "Tie")
    if dealer_score == player4_score:
          winLbl4.config(text= "Tie")
"""
            if (x < 4):
                if(arr[x][y]['text']==arr[x+1][y]['text']==arr[x+2][y]['text']==arr[x+3][y]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")
            if (y < 4):
                if(arr[x][y]['text']==arr[x][y+1]['text']==arr[x][y+2]['text']==arr[x][y+3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")
            #Diagonals
            if ((x < 7 and x > 4 and y < 4)):
                if(arr[x][y]['text']==arr[x-1][y+1]['text']==arr[x-2][y+2]['text']==arr[x-3][y+3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")

            if (x > 4  and (x < 7 and y < 7)):
                if((arr[x][y]['text']==arr[x-1][y-1]['text']==arr[x-2][y-2]['text']==arr[x-3][y-3]['text']) and arr[x][y]['text']!= '' and  (not x-3 < 0) and (not y-3 < 0)):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")
            """
#Function to handle when player clicks a button.
def press(x,y):
    """
    global player
    #global red_photo
    #global yellow_photo
    if (winLbl['text'] != "Dealer Wins!" and winLbl['text'] != "Player1 Wins!"):
        if (arr[x][y] == arr[6][y]):
            if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
                arr[x][y].config(text = player)
                if player == "Red":
                    #arr[x][y].config(image=red_photo)
                    player = "Yellow"
                    playerturn.config(text = "Yellow's turn")
                    #showturn.config(image=yellow_photo)
                else:
                    #arr[x][y].config(image=yellow_photo)
                    player = "Red"
                    playerturn.config(text = "Red's turn")
                    #showturn.config(image=red_photo)
                checkWin()
        elif (arr[x+1][y]['text'] == "Red" or arr[x+1][y]['text'] == "Yellow"):
            if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
                arr[x][y].config(text = player)
                if player == "Red":
                    #arr[x][y].config(image=red_photo)
                    player = "Yellow"
                    playerturn.config(text = "Yellow's turn")
                    #showturn.config(image=yellow_photo)
                else:
                    #arr[x][y].config(image=yellow_photo)
                    player = "Red"
                    playerturn.config(text = "Red's turn")
                    #showturn.config(image=red_photo)
                checkWin()
       """         
def playerturn():
      global player1_card
      global player2_card
      global player3_card
      global player4_card
      global dealer_card
      global currentplayer
      if currentplayer == 1:
            count = 0
            for x in player1_card:
                  result = ""
                  count += 1
                  player1_score = sum(card_value(card) for card in player1_card)
                  for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
                              result = result + y
                              arr[2][count].config(text = result)
                              player1score.config(text = player1_score)
      if currentplayer == 2:
            count = 0
            for x in player2_card:
                  result = ""
                  count += 1
                  player2_score = sum(card_value(card) for card in player2_card)
                  for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
                              result = result + y
                              arr[3][count].config(text = result)
                              player2score.config(text = player2_score)
      if currentplayer == 3:
            count = 0
            for x in player3_card:
                  result = ""
                  count += 1
                  player3_score = sum(card_value(card) for card in player3_card)
                  for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
                              result = result + y
                              arr[4][count].config(text = result)
                              player3score.config(text = player3_score)
      if currentplayer == 4:
            count = 0
            for x in player4_card:
                  result = ""
                  count += 1
                  player4_score = sum(card_value(card) for card in player4_card)
                  for y in x:
                        #if (y != 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
                        #      result = y
                        #else:
                              result = result + y
                              arr[5][count].config(text = result)
                              player4score.config(text = player4_score)
                              
                              
def Hit():
    global currentplayer
    new_card = deck.pop()
    if currentplayer == 1:
        player1_card.append(new_card)
    if currentplayer == 2:
        player2_card.append(new_card)
    if currentplayer == 3:
        player3_card.append(new_card)
    if currentplayer == 4:
        player4_card.append(new_card)
    playerturn()
    
def Stop():
      #later increment player and if last player then call checkwin
      for x in range(cols):
        for y in range(rows):
            if x == 0:
                #do nothing because it never changes
                arr[x][y].config(text='')
            else:
                arr[x][y].config(text='')
      global currentplayer
      if currentplayer != 4:
            currentplayer = currentplayer + 1
            if currentplayer == 2:
                player1turnl.config(text="Player2's turn")
            if currentplayer == 3:
                player1turnl.config(text="Player3's turn")
            if currentplayer == 4:
                player1turnl.config(text="Player4's turn")
            return
      else:
        player1turnl.config(text="Reset Game")
        checkWin()

#Help button that explains game
def help():
    messagebox.showinfo("Game instructions","Players choose yellow or red discs. They drop the discs into the grid, starting in the middle or at the edge to stack their colored discs upwards, horizontally, or diagonally. Use strategy to block opponents while aiming to be the first player to get 4 in a row to win.")

#Resets game
def resetB(arr):
    global photo
    global player1_card
    global player2_card
    global player3_card
    global player4_card
    global dealer_card
    global currentplayer
    currentplayer = 1
    for x in range(cols):
        for y in range(rows):
            if x == 1:
                #do nothing because it never changes
                arr[x][y].config(text='')
            else:
                arr[x][y].config(text='')
    winLbl.config(text = '')
    winLbl2.config(text = '')
    winLbl3.config(text = '')
    winLbl4.config(text = '')
            #card_categories = ['♥', '♦', '♣', '♠'] 
            #cards_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
            #deck = [(card, category) for category in card_categories for card in cards_list] 
    random.shuffle(deck)
    player1_card = [deck.pop(), deck.pop()] 
    player2_card = [deck.pop(), deck.pop()] 
    player3_card = [deck.pop(), deck.pop()] 
    player4_card = [deck.pop(), deck.pop()] 
    dealer_card = [deck.pop(), deck.pop()] 
    player1_score = sum(card_value(card) for card in player1_card) 
    player2_score = sum(card_value(card) for card in player2_card) 
    player3_score = sum(card_value(card) for card in player3_card) 
    player4_score = sum(card_value(card) for card in player4_card) 
    dealer_score = sum(card_value(card) for card in dealer_card) 
    player1turnl.config(text="Player1's turn")
    player1score.config(text = '0')
    player2score.config(text = '0')
    player3score.config(text = '0')
    player4score.config(text = '0')
    dealerscore.config(text = '')

root = Tk()
root.geometry('300x300')
#Make player
player = 1
currentplayer = player
#Loading colors for game
photo = PhotoImage(file = 'cardsfolder\Ace of Spades.png')
photo2 = PhotoImage(file = 'cardsfolder\Empty.png')
#red_photo = PhotoImage(file = "Red.png")
#yellow_photo = PhotoImage(file = "Yellow.png")
#Creating game grid
rows, cols = (6, 6)
arr = [[0 for y in range(cols)] for x in range(rows)]
for x in range(cols):
    for y in range(rows):
          if x == 1:
                #for seperation between dealer and players
                arr[x][y] = Button(root, text='', command= lambda x1=x, y1=y: press(x1,y1) , height = 30, width = 30, image=photo2)
                arr[x][y].grid(row = x, column = y)
          else:
                arr[x][y] = Button(root, text='', command= lambda x1=x, y1=y: press(x1,y1) , height = 2, width = 4)#, image=photo)
                arr[x][y].grid(row = x, column = y)
            
        	#arr[x][y] = Button(root, text='', command= lambda x1=x, y1=y: press(x1,y1) , height = 30, width = 30, image=photo)
            #arr[x][y].grid(row = x, column = y)

#Creating buttons
#showturn = Button(root, text='', height = 30, width = 30, image=red_photo)
#showturn.grid(row = 8, column = 11)

start = Button(root, text="start",  command = lambda: playerturn(), height = 3, width = 10)
start.grid(row = 33, column=1,columnspan=4)

stop = Button(root, text="STOP",  command = lambda: Stop(), height = 3, width = 10)
stop.grid(row = 31, column=1,columnspan=4)

Hitb = Button(root, text="HIT",  command = lambda: Hit(), height = 3, width = 10)
Hitb.grid(row = 29, column=1,columnspan=4)

info = Button(root, text="Help",  command = lambda: help(), height = 3, width = 10)
info.grid(row = 27, column=1,columnspan=4)

reset = Button(root, text = "Reset", command = lambda: resetB(arr), height = 3, width = 10)
reset.grid(row = 25, column = 1, columnspan=4)

winLbl = Label(root)
winLbl2 = Label(root)
winLbl3 = Label(root)
winLbl4 = Label(root)
dealerscore = Label(root, text="")
dealerscore2 = Label(root, text="Dealer Score:")
player1turnl = Label(root, text="Player1's turn")
player1score = Label(root, text="0")
player2score = Label(root, text="0")
player3score = Label(root, text="0")
player4score = Label(root, text="0")
player1score2 = Label(root, text="Player1 Score:")
player2score2 = Label(root, text="Player2 Score:")
player3score2 = Label(root, text="Player3 Score:")
player4score2 = Label(root, text="Player4 Score:")

winLbl.grid(row = 8, column = 1, columnspan=3)
winLbl2.grid(row = 9, column = 1, columnspan=3)
winLbl3.grid(row = 10, column = 1, columnspan=3)
winLbl4.grid(row = 11, column = 1, columnspan=3)
dealerscore2.grid(row = 8, column=4, columnspan=3)
dealerscore.grid(row = 8, column=6, columnspan=3)
player1turnl.grid(row = 12, column=1, columnspan=3)
player1score2.grid(row = 11, column=4, columnspan=3)
player1score.grid(row = 11, column=6, columnspan=3)
player2score.grid(row = 12, column=6, columnspan=3)
player2score2.grid(row = 12, column=4, columnspan=3)
player3score.grid(row = 13, column=6, columnspan=3)
player3score2.grid(row = 13, column=4, columnspan=3)
player4score.grid(row = 14, column=6, columnspan=3)
player4score2.grid(row = 14, column=4, columnspan=3)



root.mainloop()
