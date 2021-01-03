from Variables import *


#   NOTES

#   The MAIN CLASS
#   the main class contains important functions to clear out code
#   you don't have to create the instance of main class to use it
#   just use main.<method name> to use the methods

#   THE HELPER CLASS
#   the helper class contains function to help reduce brain usage
#   it also can work without instantiating


class Pieces:
    class dpawn:
        name = 'dpawn'
        point = 1
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Pawn.png")
        else:
            drawable = pygame.image.load("drawables/B_Pawn.png")

    class upawn:
        name = 'upawn'
        point = -1
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Pawn.png")
        else:
            drawable = pygame.image.load("drawables/B_Pawn.png")

    class dking:
        name = 'dking'
        point = 200
        if player == 'w':
            drawable = pygame.image.load("drawables/W_King.png")
        else:
            drawable = pygame.image.load("drawables/B_King.png")

    class uking:
        name = 'uking'
        point = -200
        if player == 'b':
            drawable = pygame.image.load("drawables/W_King.png")
        else:
            drawable = pygame.image.load("drawables/B_King.png")

    class dqueen:
        name = 'dqueen'
        point = 8
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Queen.png")
        else:
            drawable = pygame.image.load("drawables/B_Queen.png")

    class uqueen:
        name = 'uqueen'
        point = -8
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Queen.png")
        else:
            drawable = pygame.image.load("drawables/B_Queen.png")

    class drook:
        name = 'drook'
        point = 5
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Rook.png")
        else:
            drawable = pygame.image.load("drawables/B_Rook.png")

    class urook:
        name = 'urook'
        point = -5
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Rook.png")
        else:
            drawable = pygame.image.load("drawables/B_Rook.png")

    class dbishop:
        name = 'dbishop'
        point = 3
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Bishop.png")
        else:
            drawable = pygame.image.load("drawables/B_Bishop.png")

    class ubishop:
        name = 'ubishop'
        point = -3
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Bishop.png")
        else:
            drawable = pygame.image.load("drawables/B_Bishop.png")

    class dknight:
        name = 'dknight'
        point = 3
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Knight.png")
        else:
            drawable = pygame.image.load("drawables/B_Knight.png")

    class uknight:
        name = 'uknight'
        point = -3
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Knight.png")
        else:
            drawable = pygame.image.load("drawables/B_Knight.png")

    ac = pygame.image.load("drawables/activated.png")

    blacks = [upawn, uking, uqueen, urook, ubishop, uknight]
    whites = [dpawn, dking, dqueen, drook, dbishop, dknight]

    if player == 'b':
        whites, blacks = blacks, whites


class Board:
    board = []
    dimension = 0

    @staticmethod
    def create_raw_board():

        # initializing the board variables using the pieces class
        wp, wr, wn, wb, wq, wk = Pieces.dpawn, Pieces.drook, Pieces.dknight, Pieces.dbishop, Pieces.dqueen, Pieces.dking
        bp, br, bn, bb, bq, bk = Pieces.upawn, Pieces.urook, Pieces.uknight, Pieces.ubishop, Pieces.uqueen, Pieces.uking

        # you can edit this board variable to change the initial board position
        # if its the black piece dominating then the king and queen side will change
        if player == 'w':
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

    @staticmethod
    def draw_board(pyg, display):
        block = size
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

    @staticmethod
    def draw_pieces(display, board):

        cnt1 = 0
        for rows in board:
            cnt2 = 0
            for piece in rows:
                if piece != 0:
                    axis = (int(((cnt2 * size) + size / 2) - 32), int(((cnt1 * size) + size / 2) - 32))
                    display.blit(piece.drawable, axis)
                cnt2 += 1
            cnt1 += 1

    # this method draws the piece when we hold a piece and move it
    @staticmethod
    def draw_elevated(x, y, piece, display):
        if piece != 0:
            display.blit(piece.drawable, (x - 32,
                                          y - 32))  # we are blitting at -32 because the size of piece is 64x64 so to keep it in centre we have to do so

    # this method will draw a transparent green square where the piece tends to go
    @staticmethod
    def draw_notifier(x, y, display, pygame, to, activated):

        if to:
            xx, yy = helper.fromAxis(x, y)
            # this draws a green rectangle
            # pygame.draw.rect(display, notifierColor, (xx*size,yy*size,size,size))

            # this draws a transparent rectangle on the board
            # display.blit(notifierColor,(xx*size,yy*size,size,size))

            # this draw a circle in between
            if helper.fromIndex(yy, xx) in activated:
                display.blit(pygame.image.load("drawables/notifier.png"),
                             (((xx * size) + (size / 2)) - 32, (yy * size) + (size / 2) - 32))

    @staticmethod
    def draw_activated(display, ACboard):
        for i in ACboard:
            x, y = helper.toIndex(i)
            xx, yy = helper.toAxis(x, y)
            display.blit(Pieces.ac, ((yy + (size / 2) - 32), ((xx + (size / 2) - 32))))

    @staticmethod
    def returnPoints(board):
        points = 0
        for rows in board:
            for blocks in rows:
                if blocks != 0:
                    points += blocks.point
        return points


class Moves:
    class Available:

        @staticmethod
        def checkAvailable(board, x, y, chance):

            if board[y][x] == Pieces.dpawn:
                return Moves.Available.dpawn(board, x, y, chance)
            elif board[y][x] == Pieces.upawn:
                return Moves.Available.upawn(board, x, y, chance)

            return []

        # this method is for the pawn residing on the down side on board
        # this method is ready for use
        @staticmethod
        def dpawn(board, fx, fy, chance):

            available = []

            # if the piece would not be in the left corner
            if fx != 0:
                if board[fy - 1][fx - 1] in helper.listPieces(chance,
                                                              False):  # this helper.method returns the list of pieces of opponent team
                    available.append(helper.fromIndex(fy - 1, fx - 1))
            # if it is not in the right corner
            if fx != 7:
                if board[fy - 1][fx + 1] in helper.listPieces(chance,
                                                              False):  # this helper.method returns the list of opponent team pieces
                    available.append(helper.fromIndex(fy - 1, fx + 1))
            # if it has one space in front
            if board[fy - 1][fx] == 0:
                available.append(helper.fromIndex(fy - 1, fx))
                # if it has 2 spaces in front
                if fy == 6:
                    if board[fy - 2][fx] == 0:
                        available.append(helper.fromIndex(fy - 2, fx))

            return available

        @staticmethod
        def upawn(board, fx, fy, chance):

            available = []

            # if piece would not be in the left corner
            if fx != 0:
                if board[fy + 1][fx - 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy + 1, fx - 1))
            # if it is not in the right corner
            if fx != 7:
                if board[fy + 1][fx + 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy + 1, fx + 1))
            # if it has one space in front
            if board[fy + 1][fx] == 0:
                available.append(helper.fromIndex(fy + 1, fx))
                # if it has 2 spaces in front
                if fy == 1:
                    if board[fy + 2][fx] == 0:
                        available.append(helper.fromIndex(fy + 2, fx))

            return available


class Ai:
    @staticmethod
    def getAllPositions(board, chance):
        pass


class helper:
    # returns board indexes starting from 0
    @staticmethod
    def fromAxis(x, y):
        return (x // size), (y // size)

    # returns serial value from 1 to 64
    @staticmethod
    def fromIndex(x, y):
        return (x) * 8 + y + 1  # added one at the end because we have to start from 1

    # returns x and y index value
    @staticmethod
    def toIndex(serial):
        if serial % 8 != 0:
            return serial // 8, (serial % 8) - 1
        else:
            return (serial // 8) - 1, 7

    # returns the true x and y values
    @staticmethod
    def toAxis(x, y):
        return x * size, y * size

    @staticmethod
    def listPieces(chance, who):

        if chance == 'w':
            if who:
                return Pieces.whites
            else:
                return Pieces.blacks
        elif chance == 'b':

            if who:
                return Pieces.blacks
            else:
                return Pieces.whites

    # def toShowNotifier(board,x,y,chance):
    #     xx,yy=helper.fromAxis(x,y)
    #     if chance=='w':
    #         return board[yy][xx] in [Pieces.wp]
    #     else :
    #         return board[yy][xx] in [Pieces.bp]

# pieceObj = Pieces(pygame,player)
