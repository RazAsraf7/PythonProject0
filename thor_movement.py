import sys
import math

# Solve this puzzle by writing the shortest code.
# Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
# These comments should be burnt after reading!

# lx: the X position of the light of power
# ly: the Y position of the light of power
# tx: Thor's starting X position
# ty: Thor's starting Y position
lx, ly, tx, ty = [int(i) for i in input().split()]
remaining_turns = int(input())  # The level of Thor's remaining energy, representing the number of moves he can still make.

# game loop
while remaining_turns > 0:
    remaining_turns -= 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    initialTX = tx
    initialTY = ty
    directionX = ''
    directionY = ''
    if tx > lx and ty > ly:
        directionX = "W"
        directionY = "N"
        print(directionY, directionX)
        tx -= 1
        ty += 1
    elif tx < lx and ty < ly:
        directionX = "E"
        directionY = "S"
        print(directionY, directionX)
        tx += 1 
        ty -= 1
    elif tx < lx and ty > ly:
        directionX = "E"
        directionY = "N"
        print(directionY, directionX)
        tx += 1 
        ty += 1
    elif tx > lx and ty < ly:
        directionX = "W"
        directionY = "S"
        print(directionY, directionX)
        tx -= 1
        ty -= 1
    else:
        if tx > lx:
            directionX = "W"
            tx -= 1
        elif tx < lx:
            directionX = "E"
            tx += 1
        if ty > ly:
            directionY = "N"
            ty += 1
        elif ty < ly:
            directionY = "S"
            ty -= 1