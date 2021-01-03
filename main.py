# NOTES
# if you want to get the points on the board positive for player on the bottom
# and negative for that of on the top. you can use Board.returnPoints(board);

# importing necessary modules
from Engine import *
from Variables import *


class main:
    # this method is taking board because it is been modified and will be null if not passed
    @staticmethod
    def onEveryFrame(board):

        x, y = pygame.mouse.get_pos()
        # drawing the board and pieces
        Board.draw_board(pygame, display)

        # drawing the pieces over the board
        Board.draw_pieces(display, board)

        # drawing the moves available for the selected piece
        Board.draw_activated(display, activatedBoard)

        # drawing the big green circle if the piece is elevated over a valid block
        Board.draw_notifier(x, y, display, pygame, showNotifier, activatedBoard)

        # this method draws the pieces which is elevated on the position of the mouse pointer
        Board.draw_elevated(x, y, piece, display)

        # print(chance)
        pygame.display.update()

    @staticmethod
    def initializePygame():
        global playing, clock, display
        pygame.init()
        display = pygame.display.set_mode(
            (dimension, dimension))  # dimension variable is initialized for both height and width
        pygame.display.set_caption("Chess")
        display.fill(bgColor)
        clock = pygame.time.Clock()
        playing = True

    @staticmethod
    def closeOnExit(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    @staticmethod
    def onMouseDown(x, y, board):
        global piece, activatedBlock, showNotifier, activatedBoard, fromx, fromy

        if chance == 'w':
            selfs = Pieces.whites
        else:
            selfs = Pieces.blacks

        # getting the index of the board block which is clicked
        xx, yy = helper.fromAxis(x, y)  # we have passes flipped x and y because in index it is so as done

        # this assigns the clicked block as the activated block
        activatedBlock = helper.fromIndex(yy, xx)

        # this will make changes to the activatedBoard which shows the green dots based on available moves
        if board[y // size][x // size] in selfs:  # if the selected piece is for the activated chance
            activatedBoard = Moves.Available.checkAvailable(board, x // size, y // size, chance)

        # getting the piece elevated and hold in hand
        fromx, fromy = xx, yy  # this variable holds the index from where we have taken the piece up
        piece = board[fromy][fromx]  # this variable holds the piece which is elevated to blit it
        board[fromy][fromx] = 0  # this variable makes that block 0 so that no instance of that piece is formed

        showNotifier = True

    @staticmethod
    def onMouseUp(x, y, board):
        global piece, showNotifier, activatedBoard, fromx, fromy, chance, nextChance

        tx, ty = helper.fromAxis(x, y)

        if helper.fromIndex(ty, tx) in activatedBoard:
            board[ty][tx] = piece
            piece = 0
            # swapping the variables to chance chance
            chance, nextChance = nextChance, chance
        else:
            board[fromy][fromx] = piece
            piece = 0

        showNotifier = False
        activatedBoard = []

        # prints the point in board
        # print(Board.returnPoints(board))

    @staticmethod
    def onKeyDown(key):

        # resetting the board if the r key is pressed
        if key == pygame.K_r:
            global chance

            chance = 'w'
            return Board.create_raw_board()

    @staticmethod
    def startGame():
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


main.startGame()
