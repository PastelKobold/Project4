#Add rules/logic & ranking

# Rank = 1 (Royal Flush)/ The lower the number the better
class Card :
    number = 0
    color = 'x'
    house = 'y'

    def getColor(self) :
        return self.color

    def getHouse(self) :
        return self.house

class Rank :
    rank = 0

    def getRank(self):
        return self.rank
    
    #Rank 1
    def findRank(self, player):
        #From players hand find ranks
        black_house = 0
        red_house = 0
        #Might make a function in player that finds if all are the same house instead of trying to find it here

        # for i in range(player.card):
        #     if(player.card[i].getHouse() == 'black'):
        #         black_house += 1
        #     else:
        #         red_house += 1
        # if(black_house == len(player.card) or red_house == len(player.card)):
            
    
    
    
class Deck :
    cards = []
