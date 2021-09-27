class Board(object):

    brdCount = 0
    scoreMultiplier1Red = scoreMultiplier1Yellow = 1
    scoreMultiplier2Red = scoreMultiplier2Yellow = 5
    scoreMultiplier3Red = scoreMultiplier3Yellow = 25
    scoreMultiplier4Red = scoreMultiplier4Yellow = 100

    # ===================================================================================
    # Initialise a new board
    # -----------------------------------------------------------------------------------
    def __init__(self, prevBrdObj=None, lastMv=0, prevPlayer="?"):

        # Increment the class counter and set the board Id ----------
        Board.brdCount += 1
        # print("Creating Board No. ",Board.brdCount)
        self.brdId = Board.brdCount

        # Initialise the main variables -----------------------------
        self.previousBrdObj = prevBrdObj
        self.nextBrdObj = [None,None,None,None,None,None,None]
        self.nextBrdObjCreated = False
        self.lastMove = lastMv
        self.player2MakeLastMove = prevPlayer
        self.currentBoard = False
        self.prevBrdId = 0

        # Initialise the scoring variables --------------------------
        self.countOf1RedInRow = self.countOf2RedInRow = self.countOf3RedInRow = self.countOf4RedInRow = 0
        self.countOf1YellowInRow = self.countOf2YellowInRow = self.countOf3YellowInRow = self.countOf4YellowInRow = 0
        self.boardScoreYellow = self.boardScoreRed = 0
        self.bestScoreYellow = 0
        self.bestMoveYellow = [] 

        # Set the brd atribute, depending on whether this is the ----
        # first board in the game or not-----------------------------
        if prevBrdObj != None:
            # A previous board exists ---------------------
            self.brd = prevBrdObj.brd[:]
            posn = self.__getFirstEmptyPosn(lastMv)
            self.brd[posn] = self.player2MakeLastMove
            self.prevBrdId = prevBrdObj.brdId
        else:
            # No previous board exists --------------------
            self.currentBoard = True
            self.brd=["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",
            "-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",]

        # Create all the sets of four cells in a row & score --------
        self.__scoreThisBoard()

        # Check whether the score for this board needs to be --------
        # carried backwards to wards the current board       --------
        self.passBestScore(self.boardScoreYellow,self.lastMove)

        # Determine if the game has been won ------------------------
        self.gameWonColour = ""
        self.gameWon = False

        if self.countOf4RedInRow > 0:
            self.gameWon = True
            self.gameWonColour = "Red"
        if self.countOf4YellowInRow > 0:
            self.gameWon = True
            self.gameWonColour = "Yellow"

        #print("New Board:  No=",self.brdId," Prev No=",self.prevBrdId," R-Sc=",self.boardScoreRed," Y-Sc=",self.boardScoreYellow," bYSc=",self.bestScoreYellow,sep="")


    # ===================================================================================
    # Set the value of the attribute 'isThisCurrentBoard' to either Tue or False
    # -----------------------------------------------------------------------------------
    def setCurrentBoard(self,val):
        self.currentBoard = val


    # ===================================================================================
    # Print a board
    # -----------------------------------------------------------------------------------
    def __repr__(self) -> str:
        resp = "Board Id=" + str(self.brdId)
        return resp


    def __getFirstEmptyPosn(self, column):
        # Find the first empty cell to place a token, given the column.
        posn = column - 1
        posnFound = False
        while ((posnFound == False) and (posn < 42)):
            if self.brd[posn] == "-":
                posnFound = True
            else:
                posn += 7
        return posn



    def __scoreThisBoard(self):

        # Score the horizontal rows ---------------------------------
        for stPosn in [0,1,2,3,7,8,9,10,14,15,16,17,21,22,23,24,28,29,30,31,35,36,37,38]:
            four = [self.brd[stPosn], self.brd[stPosn+1],self.brd[stPosn+2],self.brd[stPosn+3]]
            self.__scoreSetOfFour(four)

        # Score the vertical rows -----------------------------------
        for stPosn in range(21):
            four = [self.brd[stPosn], self.brd[stPosn+7],self.brd[stPosn+14],self.brd[stPosn+21]]
            self.__scoreSetOfFour(four)

        # Score the diagonal rows -----------------------------------
        for stPosn in [0,1,2,3,7,8,9,10,14,15,16,17]: 
            four = [self.brd[stPosn], self.brd[stPosn+8],self.brd[stPosn+16],self.brd[stPosn+24]]
            self.__scoreSetOfFour(four)
        for stPosn in [3,4,5,6,10,11,12,13,17,18,19,20]:   
            four = [self.brd[stPosn], self.brd[stPosn+6],self.brd[stPosn+12],self.brd[stPosn+18]]
            self.__scoreSetOfFour(four)


    def __scoreSetOfFour(self,four):
        redCount = 0
        yellowCount = 0

        # Count the number of Red & Yellow tokens in row of four ----
        for token in range(4):
            if four[token]=="R": redCount += 1
            if four[token]=="Y": yellowCount += 1 

        if redCount > 0 and yellowCount == 0: 
            if redCount == 1: 
                self.countOf1RedInRow += 1
                self.boardScoreRed += Board.scoreMultiplier1Red
            elif redCount == 2: 
                self.countOf2RedInRow += 1
                self.boardScoreRed += Board.scoreMultiplier2Red
            elif redCount == 3: 
                self.countOf3RedInRow += 1
                self.boardScoreRed += Board.scoreMultiplier3Red
            elif redCount == 4: 
                self.countOf4RedInRow += 1
                self.boardScoreRed += Board.scoreMultiplier4Red

        if yellowCount > 0 and redCount == 0: 
            if yellowCount == 1: 
                self.countOf1YellowInRow += 1
                self.boardScoreYellow += Board.scoreMultiplier1Yellow
            elif yellowCount == 2: 
                self.countOf2YellowInRow += 1
                self.boardScoreYellow += Board.scoreMultiplier2Yellow
            elif yellowCount == 3: 
                self.countOf3YellowInRow += 1
                self.boardScoreYellow += Board.scoreMultiplier3Yellow
            elif yellowCount == 4: 
                self.countOf4YellowInRow += 1
                self.boardScoreYellow += Board.scoreMultiplier4Yellow


# =======================================================================================
# Set the value of the attribute 'isThisCurrentBoard' to either Tue or False
# ---------------------------------------------------------------------------------------
    def passBestScore(self,bestScY,bestMvY):

        # Does the best score need to change for this board
        if bestScY > self.bestScoreYellow:
            # Set the new best score --------------------------------
            self.bestScoreYellow = bestScY
            self.bestMoveYellow = []
            self.bestMoveYellow.append(bestMvY)

            # Check to see if the new best score has to cascade -----
            # back further towards the current board            -----
            if self.currentBoard == False:
                prevBrdObj = self.previousBrdObj
                prevBrdObj.passBestScore(self.bestScoreYellow, self.lastMove)

        elif bestScY == self.bestScoreYellow:
            self.bestMoveYellow.append(bestMvY)
            
        else: pass


