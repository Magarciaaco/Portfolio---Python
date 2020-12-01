# Coded by: Miguel Angel Garcia Acosta
# Contact: MAGA.DevCS@Gmail.com
# --------------------------
# --  VISUAL QUICK SORT:  --
# --------------------------
# ----- ----- ----- ----- --
# -----------------------------------------------------------------------
# Randomly generated Sorting Data Structure with Bar graph as visual aid
# -----------------------------------------------------------------------
#
# ----- ----- ----- IMPORTS ----- ----- ----- #
import matplotlib.pyplot as Plot
from random import randint as Random
# ----- ----- ----- IMPORTS ----- ----- ----- #
#
# START
#
# GRAPHING COORDINATES
Y = [] # F(x) = y
X = [] # Number of elements in the graph
#
# --------------------- QUICK SORT --------------------- # START
#
# PARTITION START
def Partition(Y, LOW, HIGH):
    i = LOW - 1
    x = Y[HIGH]

    for j in range(LOW, HIGH):
        if Y[j] <= x:
            i = i + 1
            Y[i], Y[j] = Y[j], Y[i] # Swap
    Y[i + 1], Y[HIGH] = Y[HIGH], Y[i + 1]
    return i + 1
# PARTITION END
#
# QUICK SORT START
def QuickSort(Y, LOW, HIGH):
    Positions = range(len(X))
    Plot.scatter(Positions, Y)
    Plot.plot(Positions, Y, "RED")
    # initialize: Stack and Top of Stack
    Size = HIGH - LOW + 1
    Stack = [0] * Size

    TOP = - 1

    # Push LOW AND HIGH
    TOP = TOP + 1
    Stack[TOP] = LOW

    TOP = TOP + 1
    Stack[TOP] = HIGH

    # While Stack != empty -- Pop()
    while TOP >= 0:
        Plot.scatter(Positions, Y)
        # Scatter Plot
        print(Y)
        # Pop HIGH and LOW
        HIGH = Stack[TOP]
        TOP = TOP - 1

        LOW = Stack[TOP]
        TOP = TOP - 1
        
        # Pivot element to correct Position
        Pivot = Partition( Y, LOW, HIGH)

        # Push Left
        if Pivot - 1 > LOW:
            TOP = TOP + 1
            Stack[TOP] = LOW

            TOP = TOP + 1
            Stack[TOP] = Pivot - 1

        # Push Right
        if Pivot + 1 < HIGH:
            TOP = TOP + 1
            Stack[TOP] = Pivot + 1

            TOP = TOP + 1
            Stack[TOP] = HIGH

    Plot.plot(Positions, Y, "GREEN")
# QUICK SORT END
#
# --------------------- QUICK SORT --------------------- # END
#
# ---------------------    GRAPH   --------------------- # START
# VISUAL GRAPH START
def __Visual_Grahph__():
    for i in range(0, 20):
        X.append(i) # Add One Element X
        Y.append(Random(0, 10)) # Add Random Value to f(x)

    print(X)
    print(Y)

    Positions = range(len(X))

    Plot.scatter(Positions, Y)
    n = len(Y)
    QuickSort(Y, 0, n - 1)
    Plot.xticks(Positions, X)
    
    Plot.title('QUICK SORT')
    Plot.ylabel('Y (Value)')
    Plot.xlabel('X (Position)')

    Plot.show()
    Plot.clf()
# VISUAL GRAPH END
#
# ---------------------    GRAPH   --------------------- # END
#
__Visual_Grahph__()
#
# END