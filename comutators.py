from cubeClass import Cube
from pieces import *

def comutator(cube, corner):

    if (corner):
        aux = AllCP[2::] + AllCP[0:2] # Buffer = C
    else:
        aux = AllEP[2::] + AllEP[0:2] # Buffer = C

    corners = [cube.getPieceColor(i) for i in aux]

    cornersPos = [getOriginalPos(i) for i in corners]
    order = [aux.index(i) for i in cornersPos]

    visted = []
    cycle = []
    allCycles = []
    loopStart = 0
    nextPiece = order[loopStart]

    while (len(visted) < len(order)):
        
        if (loopStart == nextPiece):
            visted.append(loopStart)
            cycle.append(loopStart)
            allCycles.append(cycle[::])
            cycle.clear()

            while (loopStart in visted and loopStart < len(order)-1):
                loopStart += 1
                nextPiece = order[loopStart]
                
        else:
            visted.append(nextPiece)
            cycle.append(nextPiece)
            nextPiece = order[nextPiece]

    for i in allCycles:
        i.insert(0, i.pop())

    allCycles = [allCycles[0]] + list(reversed(sorted(allCycles[1::], key=len)))

    finalCycle = []

    for cyc in allCycles:

        k = 0

        for j in range(len(cyc)):
        
            if (j < len(cyc) - 1):
                p = aux[cyc[j]][k]
                c = corners[cyc[j]][k]
                t = aux[cyc[j+1]]
                k = [i[0] for i in t].index(c)

                finalCycle.append([[cyc[j], p], [cyc[j+1], t[k]]])

            else:
                p = aux[cyc[j]][k]
                c = corners[cyc[j]][k]
                t = aux[cyc[0]]
                k = [i[0] for i in t].index(c)

                finalCycle.append([[cyc[j], p], [cyc[0], t[k]]])


    parsedFinalCycle = []
    cycleStart = 0
   
    for i in range(len(finalCycle)):

        if (finalCycle[i][1][0] == cycleStart and cycleStart == 0):

            parsedFinalCycle.append(finalCycle[i][0][1])

            if (i < len(finalCycle) - 1):
                cycleStart = finalCycle[i+1][0][0]

        elif (finalCycle[i][1][0] == cycleStart and cycleStart != 0):

            if (finalCycle[i][0][0] == finalCycle[i][1][0] and finalCycle[i][0][1] != finalCycle[i][1][1]):

                parsedFinalCycle.append([finalCycle[i][0][1], finalCycle[i][1][1]])

            elif (finalCycle[i][0][0] != finalCycle[i][1][0]):

                parsedFinalCycle.append(finalCycle[i][0][1])
                parsedFinalCycle.append(finalCycle[i][1][1])
            
            if (i < len(finalCycle) - 1):
                cycleStart = finalCycle[i+1][0][0]

        else:

            parsedFinalCycle.append(finalCycle[i][0][1])

    for idx, j in enumerate(parsedFinalCycle[1::]):
        if (len(j) == 2):

            if (idx % 2 == 1):
                print(" ", end = "")

            print(f"{getSpeffz(j[0], corner)}{getSpeffz(j[1], corner)}*", end = " ")

        else:
            print(getSpeffz(j, corner), end = "")

            if (idx % 2 == 1):
                print(" ", end = "")

    print()
