#-*- coding: utf-8 -*-
# CS1210: HW2
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the intructional team.
#
def signed():
    return(["cjdittmer"])

######################################################################
# Import randint and shuffle from random module.
from random import randint, shuffle

######################################################################
# createDeck() produces a new, cannonically ordered, 52 card deck
# using a nested comprehension. Providing a value less than 13
# produces a smaller deck, like the semi-standard 40 card 4 suit 1-10
# deck used in many older card games (including tarot cards). Here,
# we'll use it with default values.
#
def createDeck(N=13, S=('spades', 'hearts', 'clubs', 'diamonds')):
    return([ (v, s) for s in S for v in range(1, N+1) ])
######################################################################
# Construct the representation of a given card using special unicode
# characters for hearts, diamonds, clubs, and spades. The input is a
# legal card, c, which is a (v, s) tuple. The output is a 2 or
# 3-character string 'vs' or 'vvs', where 's' here is the unicode
# character corresponding to the four standard suites (spades, hearts,
# diamonds or clubs -- provided), and v is a 1 or 2 digit string
# corresponding to the integers 2-10 and the special symbols 'A', 'K',
# 'Q', and 'J'.
#
# Example:
#    >>> displayCard((1, 'spades'))
#    'A♠'
#    >>> displayCard((12, 'hearts'))
#    'Q♡'
#
def displayCard(c):
    suits = {'spades':'\u2660', 'hearts':'\u2661', 'diamonds':'\u2662', 'clubs':'\u2663'}   # Creates a dict to call on for the suit symbols
    cards = {1:'A', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'} # Creates a dict to call for the specific numbers
    card, type = c   #sets the given tuple as two different values in the function
    return(cards[card] + suits[type])   #calls the dictionarys and returns the values
'''
print(displayCard((1, 'spades')))
print(displayCard((12, 'hearts')))
'''

######################################################################
# Print out an indexed representation of the state of the table:
# foundation piles are numbered 0-3, corner piles 4-7.
#
# Example:
#   >>> showTable(F, C)
#     F0: 9♡...9♡
#     F1: 2♢...2♢
#     F2: 7♡...7♡
#     F3: 8♡...8♡
#     C4:
#     C5:
#     C6:
#     C7:
# Or, mid-game:
#     F0: 8♣...A♢
#     F1: J♣...J♣
#     F2: A♠...A♠
#     F3: 
#     C4: K♡...K♡
#     C5: 
#     C6: 
#     C7:
#
def showTable(F, C):
    for x in range(0, len(F), 1):
        try:
            print('F'+ str(x) + ':', displayCard(F[x][0])+'...'+displayCard(F[x][len(F[x])-1])) #if there is a value of F then it will print
        except:
            print('F'+ str(x) + ':')    #if no value is present it will print this
    for x in range(0, len(C), 1):
        try:
            print('C'+ str(x+4) + ':', displayCard(C[x][0])+'...'+displayCard(C[x][len(C[x])-1]))   #same as for F
        except:
            print('C'+ str(x+4) + ':')
            
'''          
F1 = [['9♡'],['2♢'],['7♡'],['8♡']]
C1 =[[],[],[],[]]
F2 = [['8♣','7♢','6♣','5♢','4♣','3♢','2♣','A♢'],['J♣'],['A♠'],[]]
C2 = [['K♡'],[],[],[]]
showTable(F1, C1)
showTable(F2,C2)
'''
######################################################################
# Print out an indexed list of the cards in input list H, representing
# a hand. Entries are numbered starting at 8 (indexes 0-3 are reserved
# for foundation piles, and 4-7 are reserved for corners). The
# indexing is used to select cards for play.
#
# Example:
#   >>> showHand(H[0])
#   Hand: 8:A♢ 9:4♢ 10:3♡ 11:5♠ 12:6♠ 13:7♠ 14:8♠
#   >>> showHand(H[1])
#   Hand: 8:9♣ 9:5♢ 10:8♢ 11:9♢ 12:10♡ 13:A♠ 14:4♠
#
def showHand(H):
    displayList = []
    for x in range(0, len(H),1):    # loop to go through every value in hand
        displayList.append(str(x+8)+':' + displayCard(H[x]) + ' ')  #adds displayCard return to display list
    handString = ''.join(displayList)
    print('Hand: ' + handString)
'''
H = [(5, 'clubs'), (12, 'clubs'), (3, 'diamonds')]
showHand(H)
'''

######################################################################
# We'll use deal(N, D) to set up the game. Given a deck (presumably
# produced by createDeck()), shuffle it, then deal 7 cards to each of
# N players, and seed the foundation piles with 4 additional cards.
# Returns D, H, F, where D is what remains of the deck, H is a list of
# N 7-card "hands", and F is a list of lists corresponding to the four
# "seeded" foundation piles.
# 
# Example:
#   >>> D, H, F = deal(2, D)
#   >>> len(D)
#   34
#   >>> len(H)
#   2
#   >>> H[0][:3]
#   [(5, 'clubs'), (12, 'clubs'), (3, 'diamonds')]
#   >>> F[2]
#   [(11, 'hearts')]
#

def deal(N, D):
    shuffle(D)
    playerDecks = [[] for _ in range(N)]    #create basis for player decks
    foundationPiles = [[],[],[],[]]     #create basis for foundation piles
    for player in playerDecks:  #takes each player deck
        for x in range(7):  
            player.append(D.pop(0)) #runs through 7 cards and adds them to player deck while removing it from the overall deck
    for pile in foundationPiles:
        pile.append(D.pop(0))   #adds starting card to foundation pile
    return(D, playerDecks, foundationPiles)
'''
D, H, F = deal(2, createDeck())
C = [[],[],[],[]]

print(len(D))
print(len(H))
print(H[0][:3])
print(F[2])
'''
        

######################################################################
# Returns True if card c can be appended to stack S. To be legal, c
# must be one less in value than S[-1], and should be of the "other"
# color (red vs black).
#
# Hint: Remember, S might be empty, in which case the answer should
# not be True.
#
# Hint: Use the encapsulated altcolor(c1, c2) helper function to check
# for alternating colors.
#
# Example:
#   >>> legal([(2, 'diamonds')], (1, 'spades'))
#   True
#   >>> legal([(2, 'diamonds')], (1, 'hearts'))
#   False
#
def legal(S, c):
    def altcolor(c1, c2):
        if c1 == 'clubs' or c1 == 'spades': #Checks color of card 1
            colorChecker1 = 'black'
        elif c1 == 'hearts' or c1 == 'diamonds':
            colorChecker1 = 'red'
        else:
            return(False)
        if c2 == 'clubs' or c2 == 'spades': #Checks color of card 2
            colorChecker2 = 'black'
        elif c2 == 'hearts' or c2 == 'diamonds':
            colorChecker2 = 'red'
        else:
            return(False)
        if colorChecker1 == colorChecker2: #If they are the same color return false
            return(False)
        else:                              #If they are different colors return true
            return(True)
 
    if c[0] == 13 and S == []: #if the card is a king and an empty pile return true
        return(True)
    try:
        if (S[-1][0])-1 == c[0] and altcolor(S[-1][1], c[1]):   #If the card is legal in terms of the other rules and the result of altcolor
            return(True)
        else:
            return(False)
    except:
        return(False)
'''
print(legal([(2, 'diamonds')], (1, 'spades')))
print(legal([(2, 'diamonds')], (1, 'hearts')))
print(legal([],(13, 'hearts') ))
'''


######################################################################
# Governs game play for N players (2 by default). This function sets
# up the game variables, D, H, F and C, then chooses the first player
# randomly from the N players. By convention, player 0 is the user,
# while all other player numbers are played by the auto player.
#
# Each turn, the current player draws a card from the deck D, if any
# remain, and then is free to make as many moves as he/she chooses. 
#
# Hint: fill out the remainder of the function, replacing the pass
# statements and respecting the comments.
# 

def play(N=2):
    # Set up the game.
    D, H, F = deal(N, createDeck())

    C = [ [] for i in range(4) ]   # Corners, initially empty.

    # Randomly choose a player to start the game.
    player = randint(0, N-1)   # Complete this portion
    print('Player {} moves first.'.format(player))

    # Start the play loop; we'll need to exit explicitly when
    # termination conditions are realized.
    while True:
        # Draw a card if there are any left in the deck.
        if len(D)>0:
            H[player].append(D.pop(0))# Complete this portion

        print('\n\nPlayer {} ({} cards) to move.'.format(player, len(H[player])))
        print('Deck has {} cards left.'.format(len(D)))

        # Now show the table.
        showTable(F, C)

        # Let the current player have a go.
        if player != 0:
            automove(F, C, H[player])
        else:
            usermove(F, C, H[player])

        # Check to see if player is out; if so, end the game.
        if H[player] == []:
            print('\n\nPlayer {} wins!'.format(player))
            showTable(F, C)
            break

        # Otherwise, go on to next player.
        if player < N-1:
            player = player + 1
        else:
            player = 0 # Complete this portion


######################################################################
# Prompts a user to play their hand.  See transcript for sample
# operation.
#
def usermove(F, C, hand):  # F = foundation piles, C =  Corner piles, hand = players hand
    # valid() is an internal helper function that checks if the index
    # i indicates a valid F, C or hand index.  To be valid, it cannot
    # be an empty pile or an out-of-range hand index. Remember, 0-3
    # are foundation piles, 4-7 are corner piles, and 8 and up index
    # into the hand.
    def valid(i):
        pass    # Complete this function

    # Ensure the hand is sorted, integrating newly drawn card.
    hand.sort()
    
    # Give some instruction.
    print('Enter your move as "src dst": press "/" to refresh display; "." when done')

    # Manage any number of moves.
    while True:           # Until the user quits with a .
        # Display current hand.
        showHand(hand)
        # Read inputs and construct a tuple.
        move = []
        while not move or not valid(move[0]) or not valid(move[1]):
            move = input("Your move? ").split()
            if len(move) == 1:
                if move[0] == '.':
                    return
                elif move[0] == '/':
                    
                    print( "\n" *1000)
                    showTable(F, C)
                    showHand(hand)
                    print('Enter your move as "src dst": press "/" to refresh display; "." when done')
                    
                    break
            try:
                move = [int(move[0]), int(move[1])]
                # Execute the command, which looks like [from, to].
                # Remember, 0-3 are foundations, 4-7 are corners, 8+
                # are from your hand.
                #
                # What follows here is an if/elif/else statement for
                # each of the following cases.

                # Playing a card from your hand to a foundation pile.
                
                if 0 <= move[1] <= 3 and 8 <=move[0] <= len(hand)+8 and legal(F[move[1]], hand[move[0]-8]):
                    F[move[1]].append(hand.pop(move[0]-8))
                    
                # Moving a foundation pile to a foundation pile.
                
                elif 0 <= move[1] <= 3 and  0 <= move[0] <= 3 and legal(F[move[1]], F[move[0]][0]):
                    F[move[1]].extend(F[move[0]]) 
                    F[move[0]] = []

                # Playing a card from your hand to a corner pile (K only to empty pile).
                elif 4 <= move[1] <=7 and 8 <=move[0] <= len(hand)+8 and legal(C[move[1]-4], hand[move[0]-8]):
                    C[move[1]-4].append(hand.pop(move[0]-8))

                # Moving a foundation pile to a corner pile.;
                elif 4 <= move[1] <= 7 and  0 <= move[0] <= 3 and legal(C[move[1]-4], F[move[0]][0]):
                    C[move[1]-4].extend(F[move[0]]) 
                    F[move[0]] = []

                # Otherwise, print "Illegal move" warning.
                else:
                    print("Illegal move")  
            except:
                # Any failure to process ends up here.
                print('Ill-formed move {}'.format(move))
            showTable(F, C)
            showHand(hand)

            # If the hand is empty, return. Otherwise, reset move and
            # keep trying.
            if not hand:
                return
            move = []

######################################################################
# Plays a hand automatically using a fixed but not particularly
# brilliant strategy. The strategy involves consolidating the table
# (to collapse foundation and corner piles), then scanning cards in
# your hand from highest to lowest, trying to place each card. The
# process is repeated until no card can be placed. See transcript for
# an example.
#
def automove(F, C, hand):
    # Keep playing cards while you're able to move something.
    moved = True
    while moved:
        moved = False    # Change back to True if you move a card.

        # Start by consolidating the table.
        consolidate(F, C)

        # Sort the hand (destructively) so that you consider highest
        # value cards first.
        hand.sort()

        # Scan cards in hand from high to low value, which makes removing
        # elements easier.
        for i in range(len(hand)-1, -1, -1):
            # If current card is a king, place in an empty corner
            # location (guaranteed to be one).
            try:
                if hand[i][0] == 13:
                    for x in range(4):
                        if C[x] == []:
                            C[x].append(hand.pop(i))
            except:
                pass

            # Otherwise, try to place current card on an existing
            # corner or foundation pile.
            for j in range(4):
                # Here, you have an if/elif/else that checks each of
                # the stated conditions.
                # Place current card on corner pile.
                try:
                    if legal(C[j], hand[i]):
                        C[j].append(hand.pop(i))

                # Place current card on foundation pile.
                    elif legal(F[j], hand[i]):
                        F[j].append(hand.pop(i))

                # Start a new foundation pile.
                    elif F[j] == [] and hand[i][0] == 13:
                        F[j].append(hand.pop(i))
                except:
                    pass
                

######################################################################
# consolidate(F, C) looks for opportunities to consolidate by moving a
# foundation pile to a corner pile or onto another foundation pile. It
# is used by the auto player to consolidate elements on the table to
# make it more playable.
#
# Example:
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1: 10♣...10♣
#     F2: J♡...J♡
#     F3: Q♠...Q♠
#     C4: K♢...K♢
#     C5:
#     C6:
#     C7:
#   >>> consolidate(F, C)
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1:
#     F2: 
#     F3: 
#     C4: K♢...10♣
#     C5:
#     C6:
#     C7:
#
def consolidate(F, C):
    # Consider moving one foundation onto another.
    for i in range(4):
        for j in range(4):
            try:
                if legal(F[j], F[i][0]):
                    F[j].extend(F[i]) 
                    F[i] = []
            except:
                pass
                
    # Consider moving a foundation onto a corner.
    for i in range(4):
        for j in range(4):          
            try:
                if F[i][0][0] == 13 and C[j] == []:
                    C[j].extend(F[i]) 
                    F[i] = []
                if legal(C[j], F[i][0]):
                    C[j].extend(F[i]) 
                    F[i] = []
            except:
                pass
    return 
'''
print(F,C)      
consolidate(F,C)
print(F,C)  
'''
######################################################################

if __name__ == '__main__':
    # Play two-player version by default.
    play(2)

