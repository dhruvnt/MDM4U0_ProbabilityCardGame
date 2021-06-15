#Dhruv Thakor 720416

import random
import xlwt

book = xlwt.Workbook(encoding="utf-8") 
sheet1 = book.add_sheet("Sheet1")
sheet1.write(0, 0, 'Dealer_Card_Draws')
sheet1.write(0, 1, 'Player_Card_Draws')

dealer=[]
player=[]
#By:Dhruv
dealer_wins=0
player_wins=0

num_trials=65000
card_choices=["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
for i in range(num_trials):
    index=i+1
    dealer_draw=random.choice(card_choices)
    dealer.append(dealer_draw)
    sheet1.write((i+1),0,dealer_draw)

    player_draw=random.choice(card_choices)
    player.append(player_draw)
    sheet1.write((i+1),1,dealer_draw)


    if dealer_draw in['3','5','7','9','jack','queen','king']:
        dealer_wins+=1
    if player_draw in['2','4','6','8','10','ace']:
        player_wins+=1

if dealer_wins>player_wins:
    winner="Dealer"
else:
    winner="Player"
print(dealer,player)
print(dealer_wins,player_wins)
sheet1.write(0, 3, "TOTAL DEALER WINS")
sheet1.write(0, 4, "TOTAL PLAYER WINS")
sheet1.write(1, 3, dealer_wins)
sheet1.write(1, 4, player_wins)
sheet1.write(0, 6, "WINNER:")
sheet1.write(1, 6, winner)
sheet1.write(0, 8, "TOTAL DRAWS:")
sheet1.write(1, 8, num_trials)

book.save('desktop/game_results.xls')
