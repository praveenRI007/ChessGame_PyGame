
import pygame

# soldier - Done  ,  king - done , rook - done , bishop - inprogress ,  queen - done , horse - done

# for a king to check if its lost : check whether its in check -> check possible moves of king if no moves are present check whether
# the piece making check can be deleted from players self possible moves

class DummyPlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "Dummy"
        self.player = Dummy()
        self.PossibleMoves = []


class Dummy:
    def __init__(self):
        self.PlayerColor = "None Color"
        self.isFirstPlayer = False



class soldier:
    def __init__(self, x, y, player):
        self.name = "pawn"
        self.player = player
        self.x = x
        self.y = y
        self.IsAlive = True
        self.PossibleMoves = []
        self.IsTwoMovesOrOneMoveTaken = False
        self.getAttackMovesOnly = False
        self.GetCheckerPath = False
        self.checkerpath = ""
        self.PossibleMoves = []


    def calculatedefinedmoves(self):
        self.PossibleMoves = []
        if self.getAttackMovesOnly == False:
            if self.player.isTop == True:

                if self.x + 1 < 8 and self.y < 8 and self.x + 1 >= 0 and self.y >= 0:
                    if ChessPieceTrackerList[self.x+1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x + 1, self.y])

                if self.x + 2 < 8 and self.y < 8 and self.x + 2 >= 0 and self.y >= 0 and not self.IsTwoMovesOrOneMoveTaken:
                    if ChessPieceTrackerList[self.x+2][self.y].player.PlayerColor == "None Color" and ChessPieceTrackerList[self.x+1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x + 2, self.y])

                if self.x + 1 < 8 and self.y + 1 < 8 and self.x + 1 >= 0 and self.y + 1 >= 0:
                    if ChessPieceTrackerList[self.x+1][self.y+1].player.PlayerColor != self.player.PlayerColor and ChessPieceTrackerList[self.x+1][self.y+1].player.PlayerColor != "None Color":
                        if ChessPieceTrackerList[self.x+1][self.y+1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "BR"
                        self.PossibleMoves.append([self.x+1,self.y+1])

                if self.x + 1 < 8 and self.y - 1 < 8 and self.x + 1 >= 0 and self.y - 1 >= 0:
                    if ChessPieceTrackerList[self.x+1][self.y-1].player.PlayerColor != self.player.PlayerColor and ChessPieceTrackerList[self.x+1][self.y-1].player.PlayerColor != "None Color":
                        if ChessPieceTrackerList[self.x+1][self.y-1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "BL"
                        self.PossibleMoves.append([self.x + 1, self.y - 1])
            else:
                if self.x - 1 < 8 and self.y < 8 and self.x - 1 >= 0 and self.y >= 0:
                    if ChessPieceTrackerList[self.x-1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x-1,self.y])

                if self.x - 2 < 8 and self.y < 8 and self.x - 2 >= 0 and self.y >= 0 and not self.IsTwoMovesOrOneMoveTaken:
                    if ChessPieceTrackerList[self.x-2][self.y].player.PlayerColor == "None Color" and ChessPieceTrackerList[self.x-1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x-2,self.y])

                if self.x - 1 < 8 and self.y - 1 < 8 and self.x - 1 >= 0 and self.y - 1 >= 0:
                    if ChessPieceTrackerList[self.x-1][self.y-1].player.PlayerColor != self.player.PlayerColor and ChessPieceTrackerList[self.x-1][self.y-1].player.PlayerColor != "None Color":
                        if ChessPieceTrackerList[self.x-1][self.y-1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "TR"
                        self.PossibleMoves.append([self.x-1,self.y-1])

                if self.x - 1 < 8 and self.y + 1 < 8 and self.x - 1 >= 0 and self.y + 1 >= 0:
                    if ChessPieceTrackerList[self.x-1][self.y+1].player.PlayerColor != self.player.PlayerColor and ChessPieceTrackerList[self.x-1][self.y+1].player.PlayerColor != "None Color":
                        if ChessPieceTrackerList[self.x-1][self.y+1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "TL"
                        self.PossibleMoves.append([self.x - 1, self.y + 1])
        else:
            self.PossibleMoves = []
            if self.player.isTop == True:

                if self.x + 1 < 8 and self.y < 8 and self.x + 1 >= 0 and self.y >= 0 and not self.getAttackMovesOnly:
                    if ChessPieceTrackerList[self.x + 1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x + 1, self.y])

                if self.x + 2 < 8 and self.y < 8 and self.x + 2 >= 0 and self.y >= 0 and not self.IsTwoMovesOrOneMoveTaken and not self.getAttackMovesOnly:
                    if ChessPieceTrackerList[self.x + 2][self.y].player.PlayerColor == "None Color" and ChessPieceTrackerList[self.x + 1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x + 2, self.y])

                if self.x + 1 < 8 and self.y + 1 < 8 and self.x + 1 >= 0 and self.y + 1 >= 0 and self.getAttackMovesOnly:
                    if (ChessPieceTrackerList[self.x + 1][self.y + 1].player.PlayerColor != self.player.PlayerColor or ChessPieceTrackerList[self.x + 1][self.y + 1].player.PlayerColor == self.player.PlayerColor) and (ChessPieceTrackerList[self.x + 1][self.y + 1].player.PlayerColor != "None Color" or ChessPieceTrackerList[self.x + 1][self.y + 1].player.PlayerColor == "None Color"):
                        if ChessPieceTrackerList[self.x+1][self.y+1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "BR"
                        self.PossibleMoves.append([self.x + 1, self.y + 1])

                if self.x + 1 < 8 and self.y - 1 < 8 and self.x + 1 >= 0 and self.y - 1 >= 0 and self.getAttackMovesOnly:
                    if (ChessPieceTrackerList[self.x + 1][self.y - 1].player.PlayerColor != self.player.PlayerColor or ChessPieceTrackerList[self.x + 1][self.y - 1].player.PlayerColor == self.player.PlayerColor) and (ChessPieceTrackerList[self.x + 1][self.y - 1].player.PlayerColor != "None Color" or ChessPieceTrackerList[self.x + 1][self.y - 1].player.PlayerColor == "None Color"):
                        if ChessPieceTrackerList[self.x+1][self.y-1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "BL"
                        self.PossibleMoves.append([self.x + 1, self.y - 1])
            else:
                if self.x - 1 < 8 and self.y < 8 and self.x - 1 >= 0 and self.y >= 0 and not self.getAttackMovesOnly:
                    if ChessPieceTrackerList[self.x - 1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x - 1, self.y])

                if self.x - 2 < 8 and self.y < 8 and self.x - 2 >= 0 and self.y >= 0 and not self.IsTwoMovesOrOneMoveTaken and not self.getAttackMovesOnly:
                    if ChessPieceTrackerList[self.x - 2][self.y].player.PlayerColor == "None Color" and ChessPieceTrackerList[self.x - 1][self.y].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([self.x - 2, self.y])

                if self.x - 1 < 8 and self.y - 1 < 8 and self.x - 1 >= 0 and self.y - 1 >= 0 and self.getAttackMovesOnly:
                    if (ChessPieceTrackerList[self.x - 1][self.y - 1].player.PlayerColor != self.player.PlayerColor or ChessPieceTrackerList[self.x - 1][self.y - 1].player.PlayerColor == self.player.PlayerColor) and (ChessPieceTrackerList[self.x - 1][self.y - 1].player.PlayerColor != "None Color" or ChessPieceTrackerList[self.x - 1][self.y - 1].player.PlayerColor == "None Color"):
                        if ChessPieceTrackerList[self.x-1][self.y-1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "TR"
                        self.PossibleMoves.append([self.x - 1, self.y - 1])

                if self.x - 1 < 8 and self.y + 1 < 8 and self.x - 1 >= 0 and self.y + 1 >= 0 and self.getAttackMovesOnly:
                    if (ChessPieceTrackerList[self.x - 1][self.y + 1].player.PlayerColor != self.player.PlayerColor or ChessPieceTrackerList[self.x - 1][self.y + 1].player.PlayerColor == self.player.PlayerColor) and (ChessPieceTrackerList[self.x - 1][self.y + 1].player.PlayerColor != "None Color" or ChessPieceTrackerList[self.x - 1][self.y + 1].player.PlayerColor == "None Color"):
                        if ChessPieceTrackerList[self.x-1][self.y+1].name == "king" and self.GetCheckerPath:
                            self.checkerpath = "TL"
                        self.PossibleMoves.append([self.x - 1, self.y + 1])
            self.getAttackMovesOnly = False
class bishop:
    def __init__(self, x, y, player):
        self.name = "bishop"
        self.player = player
        self.x = x
        self.y = y
        self.IsAlive = True
        self.getAttackMovesOnly = False
        self.GetCheckerPath = False
        self.checkerpath = []
        self.PossibleMoves = []

    def calculatedefinedmoves(self):
        self.PossibleMoves = []
        if self.getAttackMovesOnly == False:

            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BR"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx += 1
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TL"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break

                tempx -= 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BL"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx += 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TR"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx -= 1
                tempy += 1
        else:
            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BR"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx += 1
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TL"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break

                tempx -= 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BL"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx += 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TR"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx -= 1
                tempy += 1

            self.getAttackMovesOnly = False
class rook:
    def __init__(self, x, y, player):
        self.name = "rook"
        self.player = player
        self.x = x
        self.y = y
        self.IsAlive = True
        self.getAttackMovesOnly = False
        self.GetCheckerPath = False
        self.checkerpath = []
        self.PossibleMoves = []

    def calculatedefinedmoves(self):
        self.PossibleMoves = []

        if self.getAttackMovesOnly == False:


            tempx = self.x
            tempy = self.y
            tempx += 1
            while tempx>=0 and tempx<=7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "B"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            while tempx>=0 and tempx<=7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "T"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break

                tempx -= 1

            tempx = self.x
            tempy = self.y
            tempy += 1
            while tempy>=0 and tempy<=7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "R"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempy -= 1
            while tempy>=0 and tempy<=7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "L"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempy -= 1
        else:
            tempx = self.x
            tempy = self.y
            tempx += 1
            while tempx >= 0 and tempx <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "B"
                    if ChessPieceTrackerList[tempx][tempy].name == "king":
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            while tempx >= 0 and tempx <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "T"
                    if ChessPieceTrackerList[tempx][tempy].name == "king":
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break

                tempx -= 1

            tempx = self.x
            tempy = self.y
            tempy += 1
            while tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "R"
                    if ChessPieceTrackerList[tempx][tempy].name == "king":
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempy -= 1
            while tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "L"
                    if ChessPieceTrackerList[tempx][tempy].name == "king":
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempy -= 1
            self.getAttackMovesOnly = False

class horse:
    def __init__(self, x, y, player):
        self.name = "horse"
        self.player = player
        self.x = x
        self.y = y
        self.IsAlive = True
        self.getAttackMovesOnly = False
        self.GetCheckerPath = False
        self.checkerpath = []
        self.PossibleMoves = []

    def calculatedefinedmoves(self):
        self.PossibleMoves = []
        defaultmoves = [[self.x - 2,self.y-1],[self.x - 1,self.y-2],[self.x - 2,self.y+1],[self.x - 1,self.y+2],[self.x + 2,self.y-1],[self.x + 1,self.y-2],[self.x + 2,self.y+1],[self.x + 1,self.y+2]]
        if self.getAttackMovesOnly == False:

            for i in defaultmoves:
                if i[0]>=0 and i[0]<=7 and i[1]>=0 and i[1]<=7:
                    if ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([i[0],i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor != self.player.PlayerColor:
                        self.PossibleMoves.append([i[0],i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == self.player.PlayerColor:
                        pass
        else:
            for i in defaultmoves:
                if i[0]>=0 and i[0]<=7 and i[1]>=0 and i[1]<=7:
                    if ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([i[0],i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor != self.player.PlayerColor:
                        self.PossibleMoves.append([i[0],i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == self.player.PlayerColor:
                        self.PossibleMoves.append([i[0],i[1]])
            self.getAttackMovesOnly = False
class queen:
    def __init__(self, x, y, player):
        self.name = "queen"
        self.player = player
        self.x = x
        self.y = y
        self.IsAlive = True
        self.GetCheckerPath = False
        self.checkerpath = []
        self.PossibleMoves = []

    def calculatedefinedmoves(self):
        self.PossibleMoves = []
        if self.getAttackMovesOnly == False:

            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BR"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx += 1
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TL"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break

                tempx -= 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BL"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx += 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TR"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx -= 1
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempx += 1
            while tempx >= 0 and tempx <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "B"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempx += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            while tempx >= 0 and tempx <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "T"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break

                tempx -= 1

            tempx = self.x
            tempy = self.y
            tempy += 1
            while tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "R"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempy -= 1
            while tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "L"
                    break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    break
                tempy -= 1
        else:
            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BR"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx += 1
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TL"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break

                tempx -= 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx += 1
            tempy -= 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "BL"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx += 1
                tempy -= 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            tempy += 1
            while tempx >= 0 and tempx <= 7 and tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "TR"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx -= 1
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempx += 1
            while tempx >= 0 and tempx <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "B"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempx += 1

            tempx = self.x
            tempy = self.y
            tempx -= 1
            while tempx >= 0 and tempx <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "T"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break

                tempx -= 1

            tempx = self.x
            tempy = self.y
            tempy += 1
            while tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "R"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempy += 1

            tempx = self.x
            tempy = self.y
            tempy -= 1
            while tempy >= 0 and tempy <= 7:

                if ChessPieceTrackerList[tempx][tempy].player.PlayerColor == "None Color":
                    self.PossibleMoves.append([tempx, tempy])
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor != self.player.PlayerColor:
                    if ChessPieceTrackerList[tempx][tempy].name == "king" and self.GetCheckerPath:
                        self.checkerpath = "L"
                    if ChessPieceTrackerList[tempx][tempy].name == 'king':
                        self.PossibleMoves.append([tempx, tempy])
                    else:
                        self.PossibleMoves.append([tempx, tempy])
                        break
                elif ChessPieceTrackerList[tempx][tempy].player.PlayerColor == self.player.PlayerColor:
                    self.PossibleMoves.append([tempx, tempy])
                    break
                tempy -= 1
            self.getAttackMovesOnly = False

class king:
    def __init__(self, x, y, player):
        self.name = "king"
        self.player = player
        self.x = x
        self.y = y
        self.IsAlive = True
        self.PossibleMoves = []
        self.getAttackMovesOnly = False

    def calculatedefinedmoves(self):
        self.PossibleMoves = []
        defaultmoves = [[self.x + 1, self.y], [self.x + 1, self.y - 1], [self.x + 1, self.y + 1],
                        [self.x, self.y - 1], [self.x, self.y + 1], [self.x - 1, self.y - 1],
                        [self.x - 1, self.y], [self.x - 1, self.y + 1]]

        if self.getAttackMovesOnly == False:

            for i in defaultmoves:
                if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7:
                    if ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([i[0], i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor != self.player.PlayerColor:
                        self.PossibleMoves.append([i[0], i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == self.player.PlayerColor:
                        pass
        else:
            for i in defaultmoves:
                if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7:
                    if ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == "None Color":
                        self.PossibleMoves.append([i[0], i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor != self.player.PlayerColor:
                        self.PossibleMoves.append([i[0], i[1]])
                    elif ChessPieceTrackerList[i[0]][i[1]].player.PlayerColor == self.player.PlayerColor:
                        self.PossibleMoves.append([i[0], i[1]])

            self.getAttackMovesOnly = False



class Player:
    def __init__(self, PlayerColor, isTop,isFirstPlayer=False):
        self.PlayerColor = PlayerColor
        self.isTop = isTop
        self.PiecesAliveToPlay = []
        self.isFirstPlayer = isFirstPlayer


ChessPieceTrackerList = [[0]*8 for i in range(8)]
def InitializeGame():

    if player1.isTop:
        if player1.PlayerColor == "White":
            whiteKingPosition = [0,3]
        else:
            BlackKingPosition = [0,3]
    else:
        if player1.PlayerColor == "White":
            whiteKingPosition = [7,4]
        else:
            BlackKingPosition = [7,3]


    screen.fill(BLACK)

    for x in range(8):
        for y in range(8):

            # tile color render
            if ((x + y) % 2 == 0 or (x + y == 0)):
                color = "White"
            else:
                color = "Brown"

            # tupleset1.append((((MARGIN + WIDTH) * column + MARGIN+15),((MARGIN + HEIGHT) * row + MARGIN+15)))

            # if grid[x][y] == 1:
            #     color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * y + MARGIN,
                              (MARGIN + HEIGHT) * x + MARGIN,
                              WIDTH,
                              HEIGHT])

            tempobj = DummyPlayer(x, y)
            # TOP
            if (x == 1):
                tempobj = soldier(x, y, player1 if player1.isTop else player2)

            if (x == 0 and y in [0, 7]):
                tempobj = rook(x, y, player1 if player1.isTop else player2)
            elif (x == 0 and y in [1, 6]):
                tempobj = horse(x, y, player1 if player1.isTop else player2)
            elif (x == 0 and y in [2, 5]):
                tempobj = bishop(x, y, player1 if player1.isTop else player2)
            elif (x == 0 and y == 3):
                if player1.PlayerColor == "White" and player1.isTop:
                    tempobj = king(x, y, player1)
                if player2.PlayerColor == "White" and player2.isTop:
                    tempobj = king(x, y, player2)
                if player1.PlayerColor == "Black" and player1.isTop:
                    tempobj = queen(x, y, player1)
                if player2.PlayerColor == "Black" and player2.isTop:
                    tempobj = queen(x, y, player2)

            elif (x == 0 and y == 4):
                if player1.PlayerColor == "White" and player1.isTop:
                    tempobj = queen(x, y, player1)
                if player2.PlayerColor == "White" and player2.isTop:
                    tempobj = queen(x, y, player2)
                if player1.PlayerColor == "Black" and player1.isTop:
                    tempobj = king(x, y, player1)
                if player2.PlayerColor == "Black" and player2.isTop:
                    tempobj = king(x, y, player2)

            # DOWN
            if (x == 6):
                tempobj = soldier(x, y, player1 if not player1.isTop else player2)

            if (x == 7 and y in [0, 7]):
                tempobj = rook(x, y, player1 if not player1.isTop else player2)
            elif (x == 7 and y in [1, 6]):
                tempobj = horse(x, y, player1 if not player1.isTop else player2)
            elif (x == 7 and y in [2, 5]):
                tempobj = bishop(x, y, player1 if not player1.isTop else player2)

            elif (x == 7 and y == 3):
                if player1.PlayerColor == "White" and not player1.isTop:
                    tempobj = queen(x, y, player1)
                if player2.PlayerColor == "White" and not player2.isTop:
                    tempobj = queen(x, y, player2)
                if player1.PlayerColor == "Black" and not player1.isTop:
                    tempobj = king(x, y, player1)
                if player2.PlayerColor == "Black" and not player2.isTop:
                    tempobj = king(x, y, player2)

            elif (x == 7 and y == 4):
                if player1.PlayerColor == "White" and not player1.isTop:
                    tempobj = king(x, y, player1)
                if player2.PlayerColor == "White" and not player2.isTop:
                    tempobj = king(x, y, player2)
                if player1.PlayerColor == "Black" and not player1.isTop:
                    tempobj = queen(x, y, player1)
                if player2.PlayerColor == "Black" and not player2.isTop:
                    tempobj = queen(x, y, player2)

            if (tempobj.name == "Dummy"):
                pass
            else:

                if (tempobj.player.PlayerColor == "White"):
                    imp = pygame.image.load(f"w_{tempobj.name}.png")
                else:
                    imp = pygame.image.load(f"b_{tempobj.name}.png")

                image = pygame.transform.scale(imp, (50, 60))
                screen.blit(image, (((MARGIN + WIDTH) * y + MARGIN + 15), ((MARGIN + HEIGHT) * x + MARGIN + 15)))

            ChessPieceTrackerList[x][y] =  tempobj

def CheckIfAllyInBetweenKingandEnemy(dir,kingcolor,ki,kj):
    map = {"t":[-1,0],"b":[1,0],"l":[0,-1],"r":[0,1],"tl":[-1,-1],"tr":[-1,1],"bl":[1,-1],"br":[1,1]}
    i = map[dir][0] + ki
    j = map[dir][1] + kj

    piecesInPath =[]

    while i<8 and j<8 and i>=0 and j>=0:
        if ChessPieceTrackerList[i][j].name != "Dummy":
            piecesInPath.append([i,j])

        i = i + map[dir][0]
        j = j + map[dir][1]

    if len(piecesInPath) >= 2:

        if dir in ["t","b","l","r"]:
            if ChessPieceTrackerList[piecesInPath[0][0]][piecesInPath[0][1]].player.PlayerColor == kingcolor:
                if ChessPieceTrackerList[piecesInPath[1][0]][piecesInPath[1][1]].player.PlayerColor != kingcolor and ChessPieceTrackerList[piecesInPath[1][0]][piecesInPath[1][1]].name in ['queen','rook']:
                    return [piecesInPath[0][0],piecesInPath[0][1]]
        else:
            if ChessPieceTrackerList[piecesInPath[0][0]][piecesInPath[0][1]].player.PlayerColor == kingcolor:
                if ChessPieceTrackerList[piecesInPath[1][0]][piecesInPath[1][1]].player.PlayerColor != kingcolor and ChessPieceTrackerList[piecesInPath[1][0]][piecesInPath[1][1]].name in ['queen','bishop']:
                    return [piecesInPath[0][0],piecesInPath[0][1]]

    return []







# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 80
HEIGHT = 80

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

# Set row 1, calcell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [685,735]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# create a surface object, image is drawn on it.
# imp = pygame.image.load("b_pawn.png")
# image = pygame.transform.scale(imp, (50, 60))

# -------- Main Program Loop -----------
isTop = True
isFirstPlayer = True
player1 = Player('White', isTop,isFirstPlayer)
player2 = Player('Black',not isTop)

tempobj = DummyPlayer(0,0)

whiteKingPosition = None
BlackKingPosition = None

InitializeGame()


fromClick = False

tempChessObj = None

TempPossibleEnemymoves = []
TempPossibleAllymoves = []
TempPossibleMovesForRender = []

TotalCheckers = []

tempChessRevertedObj02 = None
tempChessRevertedObj01 = None
Revertedrow = None
Revertedcolumn = None

TempPossibleEnemymoves2 = []

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            if fromClick == False:
                tempChessObj = ChessPieceTrackerList[row][column]
                if(tempChessObj.player.isFirstPlayer):
                    if ChessPieceTrackerList[row][column].name in ["pawn","king","rook","bishop","queen","horse"]:
                        ChessPieceTrackerList[row][column].calculatedefinedmoves()
                        TempPossibleMovesForRender = ChessPieceTrackerList[row][column].PossibleMoves

                        tmp = []

                        # just for kings only

                        for m in range(8):
                            for n in range(8):
                                if ChessPieceTrackerList[m][n].name in ["pawn", "king", "rook", "bishop", "queen","horse"] and ChessPieceTrackerList[m][n].player.PlayerColor != tempChessObj.player.PlayerColor and [m,n] != [row,column]:
                                    if ChessPieceTrackerList[m][n].name in ["pawn","bishop","rook","queen","king","horse"]:
                                        ChessPieceTrackerList[m][n].getAttackMovesOnly = True
                                    ChessPieceTrackerList[m][n].calculatedefinedmoves()
                                    TempPossibleEnemymoves2.extend(ChessPieceTrackerList[m][n].PossibleMoves)

                        if ChessPieceTrackerList[row][column].name == "king":
                            for i in TempPossibleMovesForRender:
                                if i not in TempPossibleEnemymoves2:
                                    tmp.append(i)



                            TempPossibleMovesForRender = tmp



                        TempPossibleEnemymoves2 = []

                        #below code not required i guess
                        if ChessPieceTrackerList[row][column].name == "king" and ChessPieceTrackerList[row][column].player.PlayerColor == "White":
                            if len(TempPossibleMovesForRender) == 0:
                                print("white risk level 1 - tst")
                        if ChessPieceTrackerList[row][column].name == "king" and ChessPieceTrackerList[row][column].player.PlayerColor == "Black":
                            if len(TempPossibleMovesForRender) == 0:
                                print("black risk level 1 - tst")

                        fromClick = True
                    pass
                else:
                    tempChessObj = None




            elif  fromClick == True:

                # make movement
                if tempChessObj.name != "Dummy" and tempChessObj != ChessPieceTrackerList[row][column]:

                    for i in tempChessObj.PossibleMoves:
                        if i[0] == row and i[1] == column:

                            if tempChessObj.name == "pawn":
                                tempChessObj.IsTwoMovesOrOneMoveTaken = True

                            tempChessObj.player.isFirstPlayer = False
                            if ChessPieceTrackerList[row][column].name != "Dummy":
                                ChessPieceTrackerList[row][column].isAlive = False
                                if ChessPieceTrackerList[row][column].name == "king":
                                    print(f'{tempChessObj.player.PlayerColor} wins the game !')
                                print(
                                    f"{tempChessObj.player.PlayerColor} {tempChessObj.name} killed {ChessPieceTrackerList[row][column].player.PlayerColor} {ChessPieceTrackerList[row][column].name}")
                                # keep track of dead pieces

                            tempChessRevertedObj01 = ChessPieceTrackerList[row][column]
                            ChessPieceTrackerList[row][column] = tempChessObj

                            tempChessRevertedObj02 = ChessPieceTrackerList[tempChessObj.x][tempChessObj.y]
                            ChessPieceTrackerList[tempChessObj.x][tempChessObj.y] = DummyPlayer(tempChessObj.x, tempChessObj.y)

                            Revertedrow = ChessPieceTrackerList[row][column].x
                            ChessPieceTrackerList[row][column].x = row

                            Revertedcolumn = ChessPieceTrackerList[row][column].y
                            ChessPieceTrackerList[row][column].y = column

                            if ChessPieceTrackerList[row][column].name == "king" and ChessPieceTrackerList[row][column].player.PlayerColor == "White":
                                whiteKingPosition = [row,column]

                            if ChessPieceTrackerList[row][column].name == "king" and ChessPieceTrackerList[row][column].player.PlayerColor == "Black":
                                BlackKingPosition = [row,column]

                            # get all possible enemy moves
                            for i in range(8):
                                for j in range(8):
                                    if ChessPieceTrackerList[i][j].name in ["pawn", "king", "rook", "bishop", "queen","horse"] and ChessPieceTrackerList[i][j].player.PlayerColor != tempChessObj.player.PlayerColor:
                                        ChessPieceTrackerList[i][j].calculatedefinedmoves()
                                        TempPossibleEnemymoves.extend(ChessPieceTrackerList[i][j].PossibleMoves)


                            # to avoid movement of player's chess pieces that lead to self check
                            if ChessPieceTrackerList[row][column].player.PlayerColor == "White":
                                if (whiteKingPosition in  TempPossibleEnemymoves) :

                                    print('white king in check !')
                                    ChessPieceTrackerList[row][column] = tempChessRevertedObj01
                                    ChessPieceTrackerList[Revertedrow][Revertedcolumn] = tempChessRevertedObj02
                                    ChessPieceTrackerList[Revertedrow][Revertedcolumn].x = Revertedrow
                                    ChessPieceTrackerList[Revertedrow][Revertedcolumn].y = Revertedcolumn
                                    tempChessObj.player.isFirstPlayer = True

                                    if tempChessObj.name == "pawn" and tempChessObj.IsTwoMovesOrOneMoveTaken == True and (tempChessObj.x == 1 or tempChessObj.x == 6):
                                        tempChessObj.IsTwoMovesOrOneMoveTaken = False
                                    
                            else:
                                if (BlackKingPosition in TempPossibleEnemymoves):
                                    print('Black king in check !')
                                    ChessPieceTrackerList[row][column] = tempChessRevertedObj01
                                    ChessPieceTrackerList[Revertedrow][Revertedcolumn] = tempChessRevertedObj02
                                    ChessPieceTrackerList[Revertedrow][Revertedcolumn].x = Revertedrow
                                    ChessPieceTrackerList[Revertedrow][Revertedcolumn].y = Revertedcolumn
                                    tempChessObj.player.isFirstPlayer = True

                                    if tempChessObj.name == "pawn" and tempChessObj.IsTwoMovesOrOneMoveTaken == True and (tempChessObj.x == 1 or tempChessObj.x == 6):
                                        tempChessObj.IsTwoMovesOrOneMoveTaken = False

                                        # get all possible enemy moves


                            # check for Check
                            if ChessPieceTrackerList[row][column].name != "Dummy":
                                ChessPieceTrackerList[row][column].calculatedefinedmoves()
                                if whiteKingPosition in ChessPieceTrackerList[row][column].PossibleMoves:
                                    print('white king in check')
                                    ChessPieceTrackerList[whiteKingPosition[0]][whiteKingPosition[1]].calculatedefinedmoves()
                                    tempStat = False

                                    for i in range(8):
                                        for j in range(8):
                                            if ChessPieceTrackerList[i][j].name in ["pawn", "king", "rook", "bishop","queen", "horse"] and ChessPieceTrackerList[i][j].player.PlayerColor == "Black":
                                                if ChessPieceTrackerList[i][j].name in ["pawn", "bishop", "rook","queen", "king", "horse"]:
                                                    ChessPieceTrackerList[i][j].getAttackMovesOnly = True
                                                ChessPieceTrackerList[i][j].calculatedefinedmoves()
                                                if whiteKingPosition in ChessPieceTrackerList[i][j].PossibleMoves:
                                                    TotalCheckers.append([ChessPieceTrackerList[i][j],i,j])
                                                TempPossibleEnemymoves2.extend(ChessPieceTrackerList[i][j].PossibleMoves)

                                    tmp2 = []
                                    for s in ChessPieceTrackerList[whiteKingPosition[0]][whiteKingPosition[1]].PossibleMoves:
                                        if s not in TempPossibleEnemymoves2:
                                            tmp2.append(s)

                                    ChessPieceTrackerList[whiteKingPosition[0]][whiteKingPosition[1]].PossibleMoves = tmp2

                                    if (len(ChessPieceTrackerList[whiteKingPosition[0]][whiteKingPosition[1]].PossibleMoves) == 0 ) and (len(TotalCheckers) == 2):
                                        print('Black won')
                                        InitializeGame()

                                    if (len(ChessPieceTrackerList[whiteKingPosition[0]][whiteKingPosition[1]].PossibleMoves) == 0 ) and (len(TotalCheckers) == 1):
                                        print('check the checkers path : see if any ally has possible enemycoordinates or can block the path')



                                        ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].GetCheckerPath = True

                                        ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].calculatedefinedmoves()

                                        checkerpath = []

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "T":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i -=1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i,j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "B":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "L":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                j -= 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "R":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                j += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "TL":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i -= 1
                                                j -= 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "TR":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i -= 1
                                                j += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "BL":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i += 1
                                                j -= 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "BR":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i += 1
                                                j += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        allies_can_block = False
                                        allies_can_attack = False
                                        PossibleAllies = []

                                        notpossibleAllies = []

                                        for p in ["t","b","l","r","tl","tr","bl","br"]:
                                            tmp3 = []
                                            tmp3 = CheckIfAllyInBetweenKingandEnemy(p, "White", whiteKingPosition[0], whiteKingPosition[1])
                                            if len(tmp3) > 0:
                                                notpossibleAllies.append(tmp3)


                                        for i in range(8):
                                            for j in range(8):
                                                if ChessPieceTrackerList[i][j].name in ["pawn","rook","bishop", "queen", "horse"] and ChessPieceTrackerList[i][j].player.PlayerColor == "White":
                                                    ChessPieceTrackerList[i][j].calculatedefinedmoves()
                                                    if [i,j] in notpossibleAllies:
                                                        continue
                                                    else:
                                                        TempPossibleAllymoves.extend(ChessPieceTrackerList[i][j].PossibleMoves)

                                        for paths in checkerpath:
                                            if paths in TempPossibleAllymoves:
                                                allies_can_block = True
                                                print('allies can block checker')
                                                break

                                        if [TotalCheckers[0][1], TotalCheckers[0][2]] in TempPossibleAllymoves:
                                            allies_can_attack = True
                                            print('allies can attack checker')

                                        if not allies_can_block and not allies_can_attack:
                                            print('Black won')
                                            InitializeGame()



                                if BlackKingPosition in ChessPieceTrackerList[row][column].PossibleMoves:
                                    print('black king in check')
                                    ChessPieceTrackerList[BlackKingPosition[0]][BlackKingPosition[1]].calculatedefinedmoves()
                                    tempStat = False



                                    for i in range(8):
                                        for j in range(8):
                                            if ChessPieceTrackerList[i][j].name in ["pawn", "king", "rook", "bishop","queen", "horse"] and ChessPieceTrackerList[i][j].player.PlayerColor == "White":
                                                if ChessPieceTrackerList[i][j].name in ["pawn", "bishop", "rook","queen", "king", "horse"]:
                                                    ChessPieceTrackerList[i][j].getAttackMovesOnly = True
                                                ChessPieceTrackerList[i][j].calculatedefinedmoves()
                                                if BlackKingPosition in ChessPieceTrackerList[i][j].PossibleMoves:
                                                    TotalCheckers.append([ChessPieceTrackerList[i][j],i,j])
                                                TempPossibleEnemymoves2.extend(ChessPieceTrackerList[i][j].PossibleMoves)

                                    tmp2 = []
                                    for s in ChessPieceTrackerList[BlackKingPosition[0]][BlackKingPosition[1]].PossibleMoves:
                                        if s not in TempPossibleEnemymoves2:
                                            tmp2.append(s)

                                    ChessPieceTrackerList[BlackKingPosition[0]][BlackKingPosition[1]].PossibleMoves = tmp2

                                    if (len(ChessPieceTrackerList[BlackKingPosition[0]][BlackKingPosition[1]].PossibleMoves) == 0 ) and (len(TotalCheckers) == 2):
                                        print('White won')
                                        InitializeGame()

                                    if (len(ChessPieceTrackerList[BlackKingPosition[0]][BlackKingPosition[1]].PossibleMoves) == 0 ) and (len(TotalCheckers) == 1):
                                        print('check the checkers path : see if any ally has possible enemycoordinates or can block the path')

                                        notpossibleAllies = []

                                        for p in ["t", "b", "l", "r", "tl", "tr", "bl", "br"]:
                                            tmp3 = []
                                            tmp3 = CheckIfAllyInBetweenKingandEnemy(p, "Black", BlackKingPosition[0],
                                                                                    BlackKingPosition[1])
                                            if len(tmp3) > 0:
                                                notpossibleAllies.append(tmp3)

                                        for i in range(8):
                                            for j in range(8):
                                                if ChessPieceTrackerList[i][j].name in ["pawn","rook","bishop", "queen", "horse"] and ChessPieceTrackerList[i][j].player.PlayerColor == "Black":
                                                    ChessPieceTrackerList[i][j].calculatedefinedmoves()
                                                    if [i,j] in notpossibleAllies:
                                                        continue
                                                    else:
                                                        TempPossibleAllymoves.extend(ChessPieceTrackerList[i][j].PossibleMoves)

                                        ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].GetCheckerPath = True

                                        ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].calculatedefinedmoves()

                                        checkerpath = []

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "T":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i -=1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i,j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "B":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "L":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                j -= 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "R":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                j += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "TL":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i -= 1
                                                j -= 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "TR":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i -= 1
                                                j += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "BL":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i += 1
                                                j -= 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break
                                        if ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].checkerpath == "BR":
                                            i = TotalCheckers[0][1]
                                            j = TotalCheckers[0][2]
                                            while True:
                                                i += 1
                                                j += 1
                                                if ChessPieceTrackerList[i][j].name != "king":
                                                    checkerpath.append([i, j])
                                                if ChessPieceTrackerList[i][j].name == "king":
                                                    break

                                        allies_can_block = False
                                        allies_can_attack = False

                                        ChessPieceTrackerList[TotalCheckers[0][1]][TotalCheckers[0][2]].GetCheckerPath = False

                                        for paths in checkerpath:
                                            if paths in TempPossibleAllymoves:
                                                allies_can_block = True
                                                print('allies can block checker')
                                                break

                                        if [TotalCheckers[0][1], TotalCheckers[0][2]] in TempPossibleAllymoves:
                                            allies_can_attack = True
                                            print('allies can attack checker')

                                        if not allies_can_block and not allies_can_attack:
                                            print('White won')
                                            InitializeGame()





                            # if two enemies have eyes on king : then king needs to make move to ecape or king loses
                            # if one enemy has eyes on king : then either king or some other ally can make the move (if no ally moves or king moves left then king loses)

                            tempChessRevertedObj01 = None
                            tempChessRevertedObj01 = None

                            Revertedrow = None
                            Revertedcolumn = None

                            
                            
                            
                            # to put check

                TempPossibleEnemymoves = []
                TempPossibleEnemymoves2 = []
                TempPossibleAllymoves = []
                TotalCheckers = []



                                


                tempChessObj.PossibleMoves = []
                if tempChessObj.player.isFirstPlayer == False:
                    if tempChessObj.player == player1:
                        player1.isFirstPlayer = False
                        player2.isFirstPlayer = True
                        print(f'{player2.PlayerColor}\'s turn')
                    else:
                        player1.isFirstPlayer = True
                        player2.isFirstPlayer = False
                        print(f'{player1.PlayerColor}\'s turn')
                TempPossibleMovesForRender = []


                tempChessObj = None
                fromClick = False


            # Set that location to one
            grid[row][column] = 1

            #print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background

    # Draw the grid
    for row in range(8):
        for column in range(8):


            # tile color render
            if ((row + column) % 2 == 0 or (row + column == 0)):
                color = "White"
            else:
                color = "Brown"

            if ChessPieceTrackerList[row][column].name == "king" and ChessPieceTrackerList[row][column].player.PlayerColor == "White":
                whiteKingPosition = [row,column]

            if ChessPieceTrackerList[row][column].name == "king" and ChessPieceTrackerList[row][column].player.PlayerColor == "Black":
                BlackKingPosition = [row,column]

            if ChessPieceTrackerList[row][column].name != "Dummy" and ChessPieceTrackerList[row][column].IsAlive:

                if (ChessPieceTrackerList[row][column].player.PlayerColor == "White"):
                    imp = pygame.image.load(f"w_{ChessPieceTrackerList[row][column].name}.png")
                else:
                    imp = pygame.image.load(f"b_{ChessPieceTrackerList[row][column].name}.png")


                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

                if len(TempPossibleMovesForRender)>0:
                    for i in TempPossibleMovesForRender:
                        if i[0] == row and i[1] == column:
                            pygame.draw.rect(screen,
                                             "Red",
                                             [(MARGIN + WIDTH) * i[1] + MARGIN,
                                              (MARGIN + HEIGHT) * i[0] + MARGIN,
                                              WIDTH,
                                              HEIGHT])


                image = pygame.transform.scale(imp, (50, 60))
                screen.blit(image,
                            (((MARGIN + WIDTH) * column + MARGIN + 15), ((MARGIN + HEIGHT) * row + MARGIN + 15)))
            else:
                pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

                if len(TempPossibleMovesForRender)>0:
                    for i in TempPossibleMovesForRender:
                        if i[0] == row and i[1] == column:
                            pygame.draw.rect(screen,
                                             "Green",
                                             [(MARGIN + WIDTH) * i[1] + MARGIN,
                                              (MARGIN + HEIGHT) * i[0] + MARGIN,
                                              WIDTH,
                                              HEIGHT])



    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()