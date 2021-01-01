from Variables import *
import pygame
#   NOTES

#   The MAIN CLASS
#   the main class contains important functions to clear out code
#   you don't have to create the instance of main class to use it
#   just use main.<method name> to use the methods

#   THE HELPER CLASS
#   the helper class contains function to help reduce brain usage
#   it also can work without instantiating




class Pieces:
    wk, wq, wb, wn, wp, wr = 0, 0, 0, 0, 0, 0  # these variables are been initialized as global class variable using
    bk, bq, bb, bn, bp, br = 0, 0, 0, 0, 0, 0  # the value 0 which will later be initialized by pygame.surface image
    ac = 0  # this will be initialized by a green dot image to show available steps available in chess


    wk = pygame.image.load("W_King.png")
    wq = pygame.image.load("W_Queen.png")
    wb = pygame.image.load("W_Bishop.png")
    wn = pygame.image.load("W_Knight.png")
    wp = pygame.image.load("W_Pawn.png")
    wr = pygame.image.load("W_Rook.png")
    # black pieces
    bk = pygame.image.load("B_King.png")
    bq = pygame.image.load("B_Queen.png")
    bb = pygame.image.load("B_Bishop.png")
    bn = pygame.image.load("B_Knight.png")
    bp = pygame.image.load("B_Pawn.png")
    br = pygame.image.load("B_Rook.png")
    # activated notifier
    ac = pygame.image.load("activated.png")
    # class variables

    k, q, b, n, p, r = wk, wq, wb, wn, wp, wr  # this variable refers to the player that will refer in down side
    kk, qq, bb, nn, pp, rr = bk, bq, bb, bn, bp, br  # this variable refers to the player in the upper side

    whites=[wk, wq, wb, wn, wp, wr]
    blacks=[bk, bq, bb, bn, bp, br]

    # this constructor loads all the images and stores them in class variables which we
    # can return using methods later
    def __init__(self, object,
                 playerColor):  # This object refers to object of pygame class # playerColor is taken to create the board accordingly
        # white pieces
        # self.wk = object.image.load("W_King.png")
        # self.wq = object.image.load("W_Queen.png")
        # self.wb = object.image.load("W_Bishop.png")
        # self.wn = object.image.load("W_Knight.png")
        # self.wp = object.image.load("W_Pawn.png")
        # self.wr = object.image.load("W_Rook.png")
        # # black pieces
        # self.bk = object.image.load("B_King.png")
        # self.bq = object.image.load("B_Queen.png")
        # self.bb = object.image.load("B_Bishop.png")
        # self.bn = object.image.load("B_Knight.png")
        # self.bp = object.image.load("B_Pawn.png")
        # self.br = object.image.load("B_Rook.png")
        # # activated notifier
        # self.ac = object.image.load("activated.png")

        # if the player color is black then reversing the variables
        if playerColor == 'b':
            self.wk, self.wq, self.wb, self.wn, self.wp, self.wr, self.bk, self.bq, self.bb, self.bn, self.bp, self.br = self.bk, self.bq, self.bb, self.bn, self.bp, self.br, self.wk, self.wq, self.wb, self.wn, self.wp, self.wr
        self.updateVals()

    def updateVals(self):
        self.k, self.q, self.b, self.n, self.p, self.r = self.wk, self.wq, self.wb, self.wn, self.wp, self.wr
        self.kk, self.qq, self.bb, self.nn, self.pp, self.rr = self.bk, self.bq, self.bb, self.bn, self.bp, self.br

    # Return all pygame.surface objects
    def allImages(self):
        return self.wk, self.wq, self.wb, self.wn, self.wp, self.wr, self.bk, self.bq, self.bb, self.bn, self.bp, self.br, self.ac


class Board:

    board = []
    dimension = 0

    def create_raw_board(p):
        # initializing the variables for ease in creating the board
        wk, wq, wb, wn, wp, wr, bk, bq, bb, bn, bp, br = p.wk, p.wq, p.wb, p.wn, p.wp, p.wr, p.bk, p.bq, p.bb, p.bn, p.bp, p.br

        # you can edit this board variable to change the initial board position
        # if its the black piece dominating then the king and queen side will change
        if player=='w':
            Board.board = [
                [br, bn, bb, bq, bk, bb, bn, br],
                [bp, bp, bp, bp, bp, bp, bp, bp],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [wp, wp, wp, wp, wp, wp, wp, wp],
                [wr, wn, wb, wq, wk, wb, wn, wr]
            ]

        else:
            Board.board = [
                [br, bn, bb, bk, bq, bb, bn, br],
                [bp, bp, bp, bp, bp, bp, bp, bp],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [0, 0, 0, 0, 0, 0, 0, 0, ],
                [wp, wp, wp, wp, wp, wp, wp, wp],
                [wr, wn, wb, wk, wq, wb, wn, wr]
            ]


        return Board.board

    def draw_board(pyg, display, dim):
        block = int(dim / 8)
        cnt = 0
        for i in range(8):
            for j in range(8):
                axis = (i * block, j * block, block, block)
                if cnt % 2 == 0:
                    pyg.draw.rect(display, darkBlock, axis)
                else:
                    pyg.draw.rect(display, lightBlock, axis)
                cnt += 1
            cnt -= 1

    def draw_pieces(display, board):

        cnt1 = 0
        for rows in board:
            cnt2 = 0
            for piece in rows:
                if piece != 0:
                    axis = (int   ( ( (   cnt2 * size )  +size / 2)   - 32 ), int  ( ( ( cnt1 * size) + size / 2) -32) )
                    display.blit(piece, axis)
                cnt2 += 1
            cnt1 += 1

    # this method draws the piece when we hold a piece and move it
    def draw_elevated(x,y,piece,display):
        if piece!=0:
            display.blit(piece,(x-32,y-32))     # we are blitting at -32 because the size of piece is 64x64 so to keep it in centre we have to do so

    # this method will draw a transparent green square where the piece tends to go
    def draw_notifier(x,y,display,pygame,to):

        if to:
            xx,yy=helper.fromAxis(x,y)
            # this draws a green rectangle
            #pygame.draw.rect(display, notifierColor, (xx*size,yy*size,size,size))

            # this draws a transparent rectangle on the board
            display.blit(notifierColor,(xx*size,yy*size,size,size))

            # this draw a circle in between
            # display.blit(pygame.image.load("notifier.png"),(((xx*size)+(size/2))-32,(yy*size)+(size/2)-32))

    # This method is used so the live chance pieces will blit over the notifier
    def draw_pieces_overNotifier(display, board,chance):
        if chance=='w':
            avail=[Pieces.wp,Pieces.wb,Pieces.wn,Pieces.wr,Pieces.wq,Pieces.wk]
        else :
            avail=[Pieces.wp,Pieces.wb,Pieces.wk,Pieces.wn,Pieces.wq,Pieces.wr]

        board2=[]

        for i in range(7):
            lst = []
            for j in range(7):
                if board[i][j] in avail:
                    lst.append(board[i][j])
                board2.append(lst)
        Board.draw_pieces(display,board2)






class Moves:
    class Available:




        # this method is for the pawn residing on the down side on board
        # this method is ready for use
        def dpawn(pygame,board,fx,fy,tx='0',ty='0'):

            available=[]

            # if the piece would not be in the left corner
            if fx!=0:
                if board[fy-1][fx-1] in helper.listPieces(chance,player=='b'):     # this helper.method returns the list of pieces of opponent team
                    available.append(helper.fromIndex(fy-1,fx-1))
            # if it is not in the right corner
            if fx!=7:
                if board[fy-1][fx+1] in helper.listPieces(chance,player=='b'):      # this helper.method returns the list of opponent team pieces
                    available.append(helper.fromIndex(fy-1, fx+1))
            # if it has one space in front
            if board[fy-1][fx] ==0:
                available.append(helper.fromIndex(fy - 1, fx))
                # if it has 2 spaces in front
                if fy==6:
                    if board[fy-2][fx] == 0:
                        available.append(helper.fromIndex(fy-2,fx))

            print(available)





class Ai:
    pass


class helper:
    # returns board indexes starting from 0
    def fromAxis(x,y):
        return (x//size),(y//size)

    # returns serial value from 1 to 64
    def fromIndex(x,y):
        return (x) * 8 + y + 1  # added one at the end because we have to start from 1
    # returns x and y index value
    def toIndex(serial):
        if serial % 8 != 0:
            return serial // 8, (serial % 8)-1
        else:
            return (serial // 8)-1, 7
    # returns the true x and y values
    def toAxis(x,y):
        return x*size,y*size

    def listPieces(chance,who):
        if chance=='w':
            if who:
                return Pieces.whites
            else :
                return Pieces.blacks


    # def toShowNotifier(board,x,y,chance):
    #     xx,yy=helper.fromAxis(x,y)
    #     if chance=='w':
    #         return board[yy][xx] in [Pieces.wp]
    #     else :
    #         return board[yy][xx] in [Pieces.bp]
