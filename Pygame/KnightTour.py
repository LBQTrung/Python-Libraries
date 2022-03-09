import pygame
import sys
from random import randint


def draw_background():
    screen.fill(blackTileColor)

    for y in range(n):
        for x in range(n):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, whiteTileColor, (tileSize * x, tileSize * y, tileSize, tileSize), 0)


def draw_tiles():
    for y in range(n):
        for x in range(n):
            if board[y][x] == visitedTile:
                pygame.draw.circle(screen, visitedTileColor,
                                   (tileSize * x + tileSize // 2, tileSize * y + tileSize // 2), tileSize // 4,  0)
            if board[y][x] == knightTile:
                pygame.draw.circle(screen, knightTileColor,
                                   (tileSize * x + tileSize // 2, tileSize * y + tileSize // 2), tileSize // 4, 0)


def can_move(next_knight_x_pos, next_knight_y_pos, move_num):
    x_move = next_knight_x_pos + knightMoves[move_num][0]
    y_move = next_knight_y_pos + knightMoves[move_num][1]

    if not ((0 <= x_move < len(board)) and (0 <= y_move < len(board))):
        return False

    return board[y_move][x_move] == emptyTile


def count_possible_moves(next_knight_x_pos, next_knight_y_pos):
    moves = 0

    for i in range(len(knightMoves)):
        if can_move(next_knight_x_pos, next_knight_y_pos, i):
            moves += 1

    return moves


def move():
    global knightXPos
    global knightYPos

    moves = []

    for i in range(len(knightMoves)):
        x_move = knightXPos + knightMoves[i][0]
        y_move = knightYPos + knightMoves[i][1]

        if can_move(knightXPos, knightYPos, i):
            moves.append(count_possible_moves(x_move, y_move))
        else:
            moves.append(-1)

    smallest_number = 8
    smallest_number_index = 0

    for i in range(len(knightMoves)):
        if moves[i] < smallest_number and moves[i] >= 0:
            smallest_number = moves[i]
            smallest_number_index = i

    board[knightYPos][knightXPos] = visitedTile
    pygame.draw.circle(screen, visitedTileColor,
                       (tileSize * knightXPos + tileSize // 2, tileSize * knightYPos + tileSize // 2), tileSize // 4, 0)

    knightXPos += knightMoves[smallest_number_index][0]
    knightYPos += knightMoves[smallest_number_index][1]

    board[knightYPos][knightXPos] = knightTile
    pygame.draw.circle(screen, knightTileColor,
                       (tileSize * knightXPos + tileSize // 2, tileSize * knightYPos + tileSize // 2), tileSize // 4, 0)


n = 6

screenSize = 800
tileSize = screenSize // n

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize))

clock = pygame.time.Clock()

fps = 5

emptyTile = '.'
visitedTile = 'X'
knightTile = 'K'

whiteTileColor = (254, 205, 157)
blackTileColor = (208, 138, 70)
visitedTileColor = (255, 255, 255)
knightTileColor = (120, 120, 120)

knightMoves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
board = [[emptyTile for _ in range(n)] for _ in range(n)]

knightXPos = randint(0, n - 1)
knightYPos = randint(0, n - 1)

board[knightYPos][knightXPos] = knightTile

moveNum = 0

draw_background()
draw_tiles()

skip = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                fps += 1
            if event.key == pygame.K_a:
                fps -= 1
                if fps == 0:
                    fps = 1
            if event.key == pygame.K_r:
                board = [[emptyTile for _ in range(n)] for _ in range(n)]

                knightXPos = randint(0, n - 1)
                knightYPos = randint(0, n - 1)

                board[knightYPos][knightXPos] = knightTile

                draw_background()
                draw_tiles()

                moveNum = 0
                skip = True

    if moveNum != n * n - 1 and not skip:
        move()
        moveNum += 1

    pygame.display.set_caption("Knight\'s Tour " + str(fps) + "fps")

    pygame.display.update()

    msElapsed = clock.tick(fps)

    skip = False