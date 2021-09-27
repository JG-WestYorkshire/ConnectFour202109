# ====================================================================
# ====================================================================
# Connect Four Game
# ====================================================================
# ====================================================================

from c4objects import *
from c4fn import *


# Initialise game objects -----------------
#
currBoard=Board()
 

# Initialise game variables ---------------
#
gameCanContinue = True 
maxLevel = 2

playerMoveFirst = doYouWant2MoveFirst()
if playerMoveFirst == True:
    player = "Guest"
    playerColour = "R"
else: 
    player = "Computer"
    playerColour = "Y"

currBoard.player2MakeLastMove = swapPlayerColour(playerColour)
createBoardsXMovesAhead(currBoard,0,maxLevel)


# Print game headers ----------------------------------------------------------
#
print("\n----    CONNECT FOUR    ----\n============================\n")


# ============================================================================= 
# Main Game loop 
# -----------------------------------------------------------------------------
while gameCanContinue:

    if player == "Guest":
        prtBoard(currBoard)
        currBoard = makePlayerMove(currBoard)
    elif player == "Computer":
        createBoardsXMovesAhead(currBoard,0,maxLevel)
        prtBoard(currBoard)
        prtScores(currBoard,maxLevel,player)
        currBoard = makeComputerMove(currBoard) 
    
    gameCanContinue = checkIfGameWon(currBoard)
    player = swapPlayersOver(player)
