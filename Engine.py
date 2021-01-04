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
        # id of the piece
        name = 'dpawn'
        # the point it holds
        point = 1
        # bliting the color of piece based on player
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Pawn.png")
        else:
            drawable = pygame.image.load("drawables/B_Pawn.png")

        # method to get possible moves
        @staticmethod
        def possibles(board, x, y, chance):

            return Moves.Available.dpawn(board, x, y, chance)

    class upawn:
        name = 'upawn'
        point = -1
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Pawn.png")
        else:
            drawable = pygame.image.load("drawables/B_Pawn.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.upawn(board, x, y, chance)

    class dking:
        name = 'dking'
        point = 200
        if player == 'w':
            drawable = pygame.image.load("drawables/W_King.png")
        else:
            drawable = pygame.image.load("drawables/B_King.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.king(board, x, y, chance)

    class uking:
        name = 'uking'
        point = -200
        if player == 'b':
            drawable = pygame.image.load("drawables/W_King.png")
        else:
            drawable = pygame.image.load("drawables/B_King.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.king(board, x, y, chance)

    class dqueen:
        name = 'dqueen'
        point = 8
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Queen.png")
        else:
            drawable = pygame.image.load("drawables/B_Queen.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.queen(board, x, y, chance)

    class uqueen:
        name = 'uqueen'
        point = -8
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Queen.png")
        else:
            drawable = pygame.image.load("drawables/B_Queen.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.queen(board, x, y, chance)

    class drook:
        name = 'drook'
        point = 5
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Rook.png")
        else:
            drawable = pygame.image.load("drawables/B_Rook.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.rook(board, x, y, chance)

    class urook:
        name = 'urook'
        point = -5
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Rook.png")
        else:
            drawable = pygame.image.load("drawables/B_Rook.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.rook(board, x, y, chance)

    class dbishop:
        name = 'dbishop'
        point = 3
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Bishop.png")
        else:
            drawable = pygame.image.load("drawables/B_Bishop.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.bishop(board, x, y, chance)

    class ubishop:
        name = 'ubishop'
        point = -3
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Bishop.png")
        else:
            drawable = pygame.image.load("drawables/B_Bishop.png")

        @staticmethod
        def possibles(board, x, y, chance):
            return Moves.Available.bishop(board, x, y, chance)

    class dknight:
        name = 'dknight'
        point = 3
        if player == 'w':
            drawable = pygame.image.load("drawables/W_Knight.png")
        else:
            drawable = pygame.image.load("drawables/B_Knight.png")

        @staticmethod
        def possibles(board, x, y, chance):
            try:
                return Moves.Available.knight(board, x, y, chance)
            except:
                return []

    class uknight:
        name = 'uknight'
        point = -3
        if player == 'b':
            drawable = pygame.image.load("drawables/W_Knight.png")
        else:
            drawable = pygame.image.load("drawables/B_Knight.png")

        @staticmethod
        def possibles(board, x, y, chance):
            try:
                return Moves.Available.knight(board, x, y, chance)
            except:
                pass

            return []

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
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [wp, wp, wp, wp, wp, wp, wp, wp],
                [wr, wn, wb, wq, wk, wb, wn, wr]
            ]

        else:
            Board.board = [
                [br, bn, bb, bk, bq, bb, bn, br],
                [bp, bp, bp, bp, bp, bp, bp, bp],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
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

            # this return the pieces' inbuilt path for the available methods
            # this helps reduce the code size
            return board[y][x].possibles(board, x, y, chance)

        # this method is for the pawn residing on the down side on board
        @staticmethod
        def dpawn(board, fx, fy, chance):

            available = []

            # if the piece would not be in the left corner
            if fx != 0:
                # this helper.method returns the list of pieces of opponent team
                if board[fy - 1][fx - 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy - 1, fx - 1))
            # if it is not in the right corner
            if fx != 7:
                if board[fy - 1][fx + 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy - 1, fx + 1))
            # if it has one space in front
            if board[fy - 1][fx] == 0:
                available.append(helper.fromIndex(fy - 1, fx))
                # if it has 2 spaces in front
                if fy == 6:
                    if board[fy - 2][fx] == 0:
                        available.append(helper.fromIndex(fy - 2, fx))

            return available

        # this method is for the pawn residing on the up side on the board
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

        @staticmethod
        def king(board, fx, fy, chance):

            available = []

            # moving the king in sides

            # moving on the right
            if fx != 7:
                if board[fy][fx + 1] == 0 or board[fy][fx + 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy, fx + 1))
            # moving on the left
            if fx != 0:
                if board[fy][fx - 1] == 0 or board[fy][fx - 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy, fx - 1))
            # moving up
            if fy != 0:
                if board[fy - 1][fx] == 0 or board[fy - 1][fx] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy - 1, fx))
            # moving down
            if fy != 7:
                if board[fy + 1][fx] == 0 or board[fy + 1][fx] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy + 1, fx))

            # moving the king on the corners

            # moving on top left
            if fx != 0 and fy != 0:
                if board[fy - 1][fx - 1] == 0 or board[fy - 1][fx - 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy - 1, fx - 1))
            # moving on top right
            if fx != 7 and fy != 0:
                if board[fy - 1][fx + 1] == 0 or board[fy - 1][fx + 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy - 1, fx + 1))
            # moving on bottom left
            if fx != 0 and fy != 7:
                if board[fy + 1][fx - 1] == 0 or board[fy + 1][fx - 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy + 1, fx - 1))
            # moving on bottom right
            if fx != 7 and fy != 7:
                if board[fy + 1][fx + 1] == 0 or board[fy + 1][fx + 1] in helper.listPieces(chance, False):
                    available.append(helper.fromIndex(fy + 1, fx + 1))

            return available

        @staticmethod
        def bishop(board, fx, fy, chance):

            available = []

            # the xoper and yoper is there to make check in all the directions
            # these operators will chance in every look
            for xoper in ['-', '+']:
                for yoper in ['-', '+']:
                    for i in range(1, 8):
                        if xoper == '-':
                            ffx = fx - i
                        else:
                            ffx = fx + i
                        if yoper == '-':
                            ffy = fy - i
                        else:
                            ffy = fy + i

                        # checking if the pointer is getting out of the board
                        if ffx < 0 or ffy < 0:
                            break
                        if ffx > 7 or ffy > 7:
                            break
                        # checking if the space is empty
                        if board[ffy][ffx] == 0:
                            available.append(helper.fromIndex(ffy, ffx))
                        # checking if there is a enemy in the path
                        elif board[ffy][ffx] in helper.listPieces(chance, False):
                            available.append(helper.fromIndex(ffy, ffx))
                            break
                        # checking if the same color piece is in the path
                        elif board[ffy][ffx] in helper.listPieces(chance, True):
                            break

            return available

        @staticmethod
        def rook(board, fx, fy, chance):

            available = []
            for x in ['+', '-']:
                for y in [False, True]:
                    for i in range(1, 8):

                        # changing the axises and operator for efficiency of the code written
                        if y:
                            if x == '-':
                                ffy = fy - i
                                if ffy < 0:
                                    break
                            else:
                                ffy = fy + i
                                if ffy > 7:
                                    break
                            ffx = fx
                        else:
                            if x == '-':
                                ffx = fx - i
                                if ffx < 0:
                                    break
                            else:
                                ffx = fx + i
                                if ffx > 7:
                                    break
                            ffy = fy

                        if board[ffy][ffx] == 0:
                            available.append(helper.fromIndex(ffy, ffx))
                        elif board[ffy][ffx] in helper.listPieces(chance, False):
                            available.append(helper.fromIndex(ffy, ffx))
                            break
                        elif board[ffy][ffx] in helper.listPieces(chance, True):
                            break

            return available

        @staticmethod
        def queen(board, fx, fy, chance):
            available = Moves.Available.bishop(board, fx, fy, chance)
            for i in Moves.Available.rook(board, fx, fy, chance):
                available.append(i)
            return available


class Ai:
    # this method is ready for usage with any kinds of pieces and can give the lists of
    # board of positions of the possible move by the piece

    # this methods takes the arguments chance and returns the list according to that player only

    @staticmethod
    def getAllPositions(board, chance):
        board2 = helper.copyBoard(board)
        if chance == 'w':
            avails = Pieces.whites
        else:
            avails = Pieces.blacks

        positions = []
        for i in range(8):
            for j in range(8):
                if board[i][j] in avails:
                    available = Moves.Available.checkAvailable(board, j, i, 'w')
                    for x in available:
                        if x != 0:
                            tx, ty = helper.toIndex(x)
                            board2[tx][ty] = board2[i][j]
                            board2[i][j] = 0
                            positions.append(board2)
                            board2 = helper.copyBoard(board)
        return positions


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

    @staticmethod
    def copyBoard(board):
        board2 = []
        for i in board:
            ast = []
            for j in i:
                ast.append(j)
            board2.append(ast)
        return board2

    # def toShowNotifier(board,x,y,chance):
    #     xx,yy=helper.fromAxis(x,y)
    #     if chance=='w':
    #         return board[yy][xx] in [Pieces.wp]
    #     else :
    #         return board[yy][xx] in [Pieces.bp]

# pieceObj = Pieces(pygame,player)
