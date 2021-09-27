# =======================================================================================
# =======================================================================================
# Print out details to the screen
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

from c4fn import *
import Config

# =======================================================================================
# Print the board to the screen 
# ---------------------------------------------------------------------------------------
def prtBoard(cBrd):
    # Print the board header row ------------------------------------
    print("\n=========================================================================================")
    print("\n  Board Id:",cBrd.brdId,sep="")
    print("  ---------------------------------  ",end="")
    print("Last move by:",cBrd.player2MakeLastMove,"  ",sep="",end="")
    print("In column:",cBrd.lastMove,"  ",sep="", end="")
    print("Total No. Moves:",cBrd.moveNumber,sep="")

    # Print the board -----------------------------------------------
    for i in range(35,-1,-7):
        print("   ¦ ",cBrd.brd[i],  " ",cBrd.brd[i+1]," ",cBrd.brd[i+2]," ",
                   cBrd.brd[i+3]," ",cBrd.brd[i+4]," ",cBrd.brd[i+5]," ",
                   cBrd.brd[i+6]," ¦")

    # Print the board footer rows -----------------------------------
    print("  ---------------------------------\n      1   2   3   4   5   6   7",end="")
    
    # Print the scores for the printed board on the end of the footer-
    print("     Counts: Red=(",cBrd.redCountInRows[0],",",cBrd.redCountInRows[1],",",cBrd.redCountInRows[2],",",cBrd.redCountInRows[3],") ",
          "  Yellow=(",cBrd.yellowCountInRows[0],",",cBrd.yellowCountInRows[1],",",cBrd.yellowCountInRows[2],",",cBrd.yellowCountInRows[3],") ",
          sep="",end="\n")


# =======================================================================================
# Print the board scores to the screen 
# ---------------------------------------------------------------------------------------
def prtScores(cBrd,mxLvl,plyr):
    # Print scores for the current board ----------------------------
    print("\n  Current Board: (Id:",cBrd.brdId,")",sep="")
    print("  ---------------------------------------------------------------------------------")
    print("  Current Score:(R:",cBrd.boardScoreRed,",Y:",cBrd.boardScoreYellow,")  Next Move By:",plyr,sep="")
    print("\n  Computer Move Options -")
    prtHighestScores()

    # Print out the scores for future boards ------------------------
    print("\n\n  Future Potential Moves:")
    print("  ---------------------------------------------------------------------------------")
    print("  Computer   Guest      Computer   Guest      Computer   Guest")
    print("  ¦          ¦          ¦          ¦          ¦          ¦")

    if cBrd.nextBrdObjCreated:
        for nBrd in cBrd.nextBrdObj:
            prtScores4Board(nBrd,indent=0)

#    for mv  in range(1,8,1):
#        if mv != 1: print("\n",sep="",end="")
#        brd1 = cBrd.nextBrdObj[mv-1]
#        prtScores4Board(brd1,indent=0)

#        if mxLvl > 2: 
#            for brd2 in brd1.nextBrdObj:
#                prtScores4Board(brd2,1)#

#                if mxLvl > 3: 
#                    for brd3 in brd2.nextBrdObj:
#                        prtScores4Board(brd3,2)
#    print("\n================================================================================================\n\n")





# =======================================================================================
# Print the scores for the next potential board 
# ---------------------------------------------------------------------------------------
def prtScores4Board(cBrd,indent=0):
    if cBrd != None:
        if indent == 0: pass
        elif indent == 1: print("             ",end="")
        elif indent == 2: print("                        ",end="")
        else:          print("                                   ",end="")
        
        print("  Mv={0:d}, B.Id={1:<3d}, Sc=(R:{2:<2d} ,Y:{3:<2d}), H.Sc=(Y:{4:<2d})"
            .format(cBrd.lastMove, cBrd.brdId, cBrd.boardScoreRed, cBrd.boardScoreYellow, cBrd.highScoreYellow))

        if cBrd.currentBoard:
            prtHighestScores()


# =======================================================================================
# Print the scores based on the Highest Potential Score(s) for the Computer 
# ---------------------------------------------------------------------------------------
def prtHighestScores():
    cBrd = Config.currentBoard

    if cBrd.nextBrdObjCreated:
        bestScores, nxtMoveYellow = getHighestYellowScores()
        print("    1. Highest Yellow Scores:({0:>6.1%}, {1:>6.1%}, {2:>6.1%}, {3:>6.1%}, {4:>6.1%}, {5:>6.1%}, {6:>6.1%}) - Recommended Move is {7}"
            .format(bestScores[0],bestScores[1],bestScores[2],bestScores[3],bestScores[4],bestScores[5],bestScores[6],nxtMoveYellow))
        
        bestScores, nxtMoveYellow = canYellowWinWithNextMove()
        print("    2. Yellow Wins:          ({0:>6.1%}, {1:>6.1%}, {2:>6.1%}, {3:>6.1%}, {4:>6.1%}, {5:>6.1%}, {6:>6.1%}) - Recommended Move is {7}"
            .format(bestScores[0],bestScores[1],bestScores[2],bestScores[3],bestScores[4],bestScores[5],bestScores[6],nxtMoveYellow))
        
        bestScores, nxtMoveYellow = canYellowBlockRedWin()
        print("    3. Block a Red Win:      ({0:>6.1%}, {1:>6.1%}, {2:>6.1%}, {3:>6.1%}, {4:>6.1%}, {5:>6.1%}, {6:>6.1%}) - Recommended Move is {7}"
            .format(bestScores[0],bestScores[1],bestScores[2],bestScores[3],bestScores[4],bestScores[5],bestScores[6],nxtMoveYellow))
    else:
        pass



#    for nxtBrd in cBrd.nextBrdObj:
#        print(nxtBrd.highScoreYellow,sep="",end="")
#        if nxtBrd.lastMove != 7: print(", ",sep="",end="")
#    print(") ",sep="",end="")    
#    print("Selected Moves:",cBrd.highestScoringMovesYellow,sep="")


# =======================================================================================
# Print details of winner if game has been won
# ---------------------------------------------------------------------------------------
def prtGameWon(cBrd):
    print("\n\n\n")
    prtBoard(cBrd)
    print("\n\n\n*****  The game has been won by -",cBrd.gameWonPlayer,"(",cBrd.gameWonColour,")   *****\n\n")
