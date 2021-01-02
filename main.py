class main:
    # this method is taking board because it is been modified and will be null if not passed
    def onEveryFrame(board):

        x, y = pygame.mouse.get_pos()
        # drawing the board and pieces
        Board.draw_board(pygame, display, dimension)

        Board.draw_pieces(display, board)

        Board.draw_activated(display, activatedBoard)

        Board.draw_notifier(x, y, display, pygame, showNotifier, activatedBoard)

        Board.draw_elevated(x, y, piece, display)

        pygame.display.update()

    def initializePygame(x=0):
        global playing, clock, display
        pygame.init()
        display = pygame.display.set_mode(
            (dimension, dimension))  # dimension variable is initialized for both height and width
        pygame.display.set_caption("Chess")
        display.fill(bgColor)
        clock = pygame.time.Clock()
        playing = True

    def closeOnExit(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(print("bye"))
    def onMouseDown(x, y, board):
        global piece, activatedBlock, showNotifier, activatedBoard

        # this will make the touched block the activated block we will make changes to it afterwords
        xx, yy = helper.fromAxis(y, x)  # we have passes flipped x and y because in index it is so as done

        activatedBlock = helper.fromIndex(xx, yy)

        activatedBoard = Moves.Available.checkAvailable(board, x // size, y // size)

        fy, fx = helper.fromAxis(x, y)
        piece = board[fx][fy]
        board[fx][fy] = 0

        # if helper.toShowNotifier(board,x,y,chance):
        showNotifier = True

    def onMouseUp(x, y, board):
        global piece, showNotifier, activatedBoard

        if activatedBlock != 0:
            fx, fy = helper.toIndex(activatedBlock)
            tx, ty = helper.fromAxis(x, y)
            if piece != 0:
                board[ty][tx] = piece
            piece = 0
        showNotifier = False
        activatedBoard = []

    def onKeyDown(key):

        # resetting the board if the r key is pressed
        if key == pygame.K_r:
            return Board.create_raw_board()

    def startGame(x=0):
        # Initializing and constructing all instantiated modules and variables
        main.initializePygame()
        # piece = Pieces(pygame, player)  # the player variable passes the main human player's color of pieces
        board = Board.create_raw_board()  # getting the raw initial board in the board variable

        while True:

            for event in pygame.event.get():
                # This will close the pygame window when clicked the cross
                main.closeOnExit(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # this method contains all the methods for activating and moves
                    main.onMouseDown(event.pos[0], event.pos[1], board)
                if event.type == pygame.MOUSEBUTTONUP:
                    # This method contains all the events that will be handled in this situation
                    main.onMouseUp(event.pos[0], event.pos[1], board)
                if event.type == pygame.KEYDOWN:
                    # This method contains all code to perform key shortcuts during play
                    board = main.onKeyDown(event.key)

            main.onEveryFrame(board)


import pygame

# Importing and initializing the pygame and other important modules
from Engine import *
from Variables import *

# Important variables
# board variables


main.startGame()
