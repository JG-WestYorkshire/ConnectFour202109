from c4objects import *

# =======================================================================================
# Print out details to the screen
# ---------------------------------------------------------------------------------------


# Print the board to the screen -----------------------------------------------
#
def prtBoard(cBrd):
    # Print the board header row ------------------------------------
    print("\n  Board Id:",cBrd.brdId,sep="")
    print("  ---------------------------------  ",end="")
    print("Last move by:",cBrd.player2MakeLastMove,"  ",sep="",end="")
    print("In column:",cBrd.lastMove,sep="")


    # Print the board -----------------------------------------------
    for i in range(35,-1,-7):
        print("   ¦ ",cBrd.brd[i],  " ",cBrd.brd[i+1]," ",cBrd.brd[i+2]," ",
                   cBrd.brd[i+3]," ",cBrd.brd[i+4]," ",cBrd.brd[i+5]," ",
                   cBrd.brd[i+6]," ¦")

    # Print the board footer rows -----------------------------------
    print("  ---------------------------------\n      1   2   3   4   5   6   7",end="")
    
    # Print the scores for the printed board on the end of the footer-
    print("   Counts: Red=(",cBrd.countOf1RedInRow,",",cBrd.countOf2RedInRow,",",cBrd.countOf3RedInRow,",",cBrd.countOf4RedInRow,") ",cBrd.boardScoreRed,
          "  Yellow=(",cBrd.countOf1YellowInRow,",",cBrd.countOf2YellowInRow,",",cBrd.countOf3YellowInRow,",",cBrd.countOf4YellowInRow,") ",cBrd.boardScoreYellow,sep="",end="\n")


# Print the board scores to the screen ----------------------------------------
#
def prtScores(cBrd,mxLvl,plyr):
    # Print scores for the current board ----------------------------
    print("\n\nCurrent Board:")
    print("(",cBrd.boardScoreRed,",",cBrd.boardScoreYellow,")", " NxtMvBy=",plyr,", bScY=",cBrd.bestScoreYellow,
          " bMvY=",cBrd.bestMoveYellow,", cBrd=",cBrd.currentBoard,", maxBrdId=",Board.brdCount,sep="")

    # Print out the scores for future boards ------------------------
    print("\nMoves:\nOne        Two        Three      Four        Five")

    print(" ")
    for brd1 in cBrd.nextBrdObj:
        prtScores4Board(brd1,1)

        if mxLvl > 1: 
            for brd2 in brd1.nextBrdObj:
                prtScores4Board(brd2,2)

                if mxLvl > 2: 
                    for brd3 in brd2.nextBrdObj:
                        prtScores4Board(brd3,3)


# Print the scores for the next potential board ---------------------
def prtScores4Board(cBrd,indent):
    if cBrd != None:
        if indent == 1:   print("",end="")
        elif indent == 2: print("           ",end="")
        elif indent == 3: print("                      ",end="")
        else:          print("                                 ",end="")
        
        print("Mv=",cBrd.lastMove,", by=",cBrd.player2MakeLastMove,", bId=",cBrd.brdId,sep="",end="")
        print(",(R=",cBrd.boardScoreRed,",Y=",cBrd.boardScoreYellow,"),",sep="",end="")
        print("bScY=",cBrd.bestScoreYellow,", bMvY=",cBrd.bestMoveYellow,sep="",end="")
        print(", cBrd=",cBrd.currentBoard,sep="")


# =============================================================================
# Find the lowest empty row on the board for the requested column.
# INPUT - 1. cBrd = the current board object.
#         2. col = the column that the token is to be placed in.
# -------------------------------------------------------------------------
def findEmptyCellInColumn(cBrd,col):
    startPosn = col - 1
    for posn in range(startPosn,42,7):
        if cBrd.brd[posn] == "-":
            return posn

# ========================================================================
# Get the choice of column from the player.
# INPUT
# ------------------------------------------------------------------------
def getPlayersNextMove():
    moveInValid = True
    while moveInValid:
        col = int(input("\nWhat column do you want to play in?.."))
        if col in(1,2,3,4,5,6,7):
            moveInValid = False
    
    return col


# ========================================================================
# Swap the players over Red to Yellow to Red.
# INPUT
# ------------------------------------------------------------------------
def swapPlayersOver(playerIn):
    if playerIn == "Computer": return "Guest"
    else: return "Computer"


# =============================================================================
# Make a move from the player/computer using the selected column
# -----------------------------------------------------------------------------

def makePlayerMove(cBrd):
    col = getPlayersNextMove()
    nBrd = makeMoveToNextBoard(cBrd,col)
    #prtBoard(nBrd)
    return nBrd

def makeComputerMove(cBrd):
    col = findBestComputerMove(cBrd)
    nBrd = makeMoveToNextBoard(cBrd,col)
    #prtBoard(nBrd)
    return nBrd

def makeMoveToNextBoard(cBrd,col):
    if cBrd.nextBrdObjCreated == False:
        createNextBoards(cBrd)
    cBrd.setCurrentBoard(False)
    nBrd = cBrd.nextBrdObj[col-1]
    nBrd.setCurrentBoard(True)
    return nBrd


# ========================================================================
# Create the board objecxts for the next potential boards from the
# current board object.
# INPUT  brd
# ------------------------------------------------------------------------

def swapPlayerColour(playerIn):
    if playerIn == "R": return "Y"
    else: return "R"


def createBoardsXMovesAhead(brd,lvl,maxLvl):
    if lvl < maxLvl:

        # initialise the best score and moves for Yellow ------------
        brd.bestScoreYellow = 0
        brd.bestMoveYellow = []

        # If Reqd: Create the next boards for available moves -------
        if brd.nextBrdObjCreated == False:
            createNextBoards(brd)
        
        # Loop: Create the next boards if not max level -------------
        for nBrd in brd.nextBrdObj:
            createBoardsXMovesAhead(nBrd,(lvl+1),maxLvl)


def createNextBoards(cBrd):
        # Create all the potential boards after this board ---

        lastPlayer = cBrd.player2MakeLastMove
        nxtPlayer = swapPlayerColour(lastPlayer)
        cBrd.nextBrdObjCreated = True

        for col in range(1,8,1):
            # Check if there is space to play in the column
            validColumn = isThereSpaceInColumn(col,cBrd)

            if validColumn:
                nextBoardObj = Board(cBrd, col, nxtPlayer)
                cBrd.nextBrdObj[col-1] = nextBoardObj
            else:  
                print(" -- error -- ")


def isThereSpaceInColumn(col,cBrd):
        # Check if there is space left to place a token in this column.
        posn = 34 + (col - 1)
        if cBrd.brd[posn]=="-": 
            return True
        else: 
            return False 



# ========================================================================

def doYouWant2MoveFirst():
    ans = input("\n\nDo you want to move first?..")
    if ans in("Y","y","Yes","yes","YES"): 
        return True
    else: 
        return False


# ========================================================================
# Check if the game has been won.
# ------------------------------------------------------------------------
def checkIfGameWon(cBrd):
    if cBrd.gameWon == True: 
        print("\n\n\n*****  The game has been won by -",cBrd.gameWonColour,"   *****\n\n")
        return False
    else: 
        return True


# ========================================================================
# Determine the best move for the Computer to make
# 
# INPUT --- cBrd (the current board)
# OUTPUT -- the column of the best move
# ------------------------------------------------------------------------

def findBestComputerMove(cBrd):
    return cBrd.bestMoveYellow[0]


