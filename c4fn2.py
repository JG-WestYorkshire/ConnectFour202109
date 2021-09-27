from c4objects import *
import c4fn
import Config

# =======================================================================================
# Create the board objecxts for the next potential boards from the
# current board object.
# INPUT  brd
# ---------------------------------------------------------------------------------------
def createBoardsXMovesAhead(cBrd, CurrMovesAhead=0, maxMovesAhead=1):

    if cBrd == None: 
        print("Error")
        return

    if not cBrd.gameWon:
        if CurrMovesAhead < (maxMovesAhead - 1):

            # If Reqd: Create the next boards -----------------------
            if cBrd.nextBrdObjCreated == False:
                createNextBoards(cBrd)
            
            # Loop: Create the next boards if not max level -------------
            for nBrd in cBrd.nextBrdObj:
                createBoardsXMovesAhead(nBrd, CurrMovesAhead + 1, maxMovesAhead)


# =======================================================================================
# Create all the potential next boards based on moves 1 to 7 for the board passed.
# ---------------------------------------------------------------------------------------
def createNextBoards(cBrd):

    # Initialise required variables ---------------------------------
    lastPlayer = cBrd.player2MakeLastMove
    nxtPlayer = swapPlayersOver(lastPlayer)
    columnsWithASpace = getColumnsWithSpaces(cBrd)

    for col in columnsWithASpace:
        nxtBrdObj = Board(cBrd, lastMv=col ,prevPlayer=nxtPlayer)
        cBrd.nextBrdObj[col-1] = nxtBrdObj

        # Pass back the highest score for Yellow --------------------
        passBackHighestScores(prevBrd=cBrd, nxtBrd=nxtBrdObj)

    # Set flag to True for next level of boards created -------------
    cBrd.nextBrdObjCreated = True
    return


# =======================================================================================
# Pass the highScoreYellow back towards the current Board, while 
 # the best score is higher than the previous best score. 
# ---------------------------------------------------------------------------------------
def passBackHighestScores(prevBrd=None, nxtBrd=None):
    passBack = False

    # Initialise score if high score from a later move --------------
    if nxtBrd.highScoreMoveNumber > prevBrd.highScoreMoveNumber:
        prevBrd.highScoreYellow = 0

    # Record highest Yellow score if greater than previous highest --
    if nxtBrd.highScoreYellow > prevBrd.highScoreYellow:
        prevBrd.highScoreYellow = nxtBrd.highScoreYellow
        prevBrd.highScoreMoveNumber = nxtBrd.highScoreMoveNumber
        passBack = True

    # Record highest Red score if greater than previous highest --
    if nxtBrd.highScoreRed > prevBrd.highScoreRed:
        prevBrd.highScoreRed = nxtBrd.highScoreRed
        prevBrd.highScoreMoveNumber = nxtBrd.highScoreMoveNumber
        passBack = True

        # Pass back again if not the current board ------------------
        if prevBrd.currentBoard == False and passBack == True:
            passBackHighestScores(prevBrd=prevBrd.previousBrdObj, nxtBrd=prevBrd)
        else: pass

    else: pass
    return


#  ========================================================================
# Swap the players over Red to Yellow to Red.
# INPUT
# ------------------------------------------------------------------------
def swapPlayersOver(playerIn):
    if playerIn == "Computer": return "Guest"
    elif playerIn == "Guest": return "Computer"
    elif playerIn == "R": return "Y"
    elif playerIn == "Y": return "R"
    else: return "Error"


# =======================================================================================
#
# ---------------------------------------------------------------------------------------
def getColumnsWithSpaces(cBrd):
    
    # Initialise function variables ---------------------------------
    resp = []
    
    # Loop through the top row of cells to check for spaces ---------
    for i in range(7):
        posn = 35 + i
        if cBrd.brd[posn] == "-": 
            resp.append(i+1)
        else: pass
    
    return resp
