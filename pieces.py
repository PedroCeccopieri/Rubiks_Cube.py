def getOriginalPos(color):
    if (len(color) == 3):
        return AllCP[[sorted(i) for i in AllCC].index(sorted(color))]
    else:
        return AllEP[[sorted(i) for i in AllEC].index(sorted(color))]

def getSpeffz(pos, corner = True):

    if (corner):
        
        for p, k in zip(AllCP, AllCS):
            if (pos in p):
                return k[p.index(pos)]
    else:

        for p, k in zip(AllEP, AllES):
            if (pos in p):
                return k[p.index(pos)]

# Corners #

CWBO = [0, 4, 1] # White, Blue, Orange #
CWBR = [0, 4, 3] # White, Blue, Red #
CWGR = [0, 2, 3] # White, Green, Red #
CWGO = [0, 2, 1] # White, Green, Orange#
CYGO = [5, 2, 1] # Yellow, Green, Orange #
CYGR = [5, 2, 3] # Yellow, Green, Red #
CYBR = [5, 4, 3] # Yellow, Blue, Red #
CYBO = [5, 4, 1] # Yellow, Blue, Orange #

AllCC = [CWBO, CWBR, CWGR, CWGO, CYGO, CYGR, CYBR, CYBO] # All Corners Colors of the pieces #

# Corners position #
#                                        #     # Speffz # 
P041 = [[0, 0, 0], [4, 0, 2], [1, 0, 0]] # UBL # ARE #
P043 = [[0, 0, 2], [4, 0, 0], [3, 0, 2]] # UBR # BQN #
P023 = [[0, 2, 2], [2, 0, 2], [3, 0, 0]] # UFR # CJM # 											
P021 = [[0, 2, 0], [2, 0, 0], [1, 0, 2]] # UFL # DIF #

P521 = [[5, 0, 0], [2, 2, 0], [1, 2, 2]] # DFL # ULG #
P523 = [[5, 0, 2], [2, 2, 2], [3, 2, 0]] # DFR # VKP #
P543 = [[5, 2, 2], [4, 2, 0], [3, 2, 2]] # DBR # WTO #
P541 = [[5, 2, 0], [4, 2, 2], [1, 2, 0]] # DBL # XSH #

AllCP = [P041, P043, P023, P021, P521, P523, P543, P541] # All Corners Position in the cube #
AllCS = [["A", "R", "E"], ["B", "Q", "N"], ["C", "J", 'M'], ["D", "I", "F"], ["U", "L", "G"], ["V", "K", "P"], ["W", "T", "O"], ["X", "S", "H"]]

# Edges #

EWB = [0, 4] # White, Blue #
EWR = [0, 3] # White, Red #
EWG = [0, 2] # White, Green #
EWO = [0, 1] # White, Orange #
EGO = [2, 1] # Green, Orange #
EGR = [2, 3] # Green, Red #
EBR = [4, 3] # Blue, Red #
EBO = [4, 1] # Blue, Orange #
EYG = [5, 2] # Yellow, Green #
EYR = [5, 3] # Yellow, Red #
EYB = [5, 4] # Yellow, Blue #
EYO = [5, 1] # Yellow, Orange #

AllEC = [EWB, EWR, EWG, EWO, EGO, EGR, EBR, EBO, EYG, EYR, EYB, EYO] # All Edges Colors of the Pieces #

# Edges position #
#                            #    # Speffz # 
P04 = [[0, 0, 1], [4, 0, 1]] # UB # AQ #
P03 = [[0, 1, 2], [3, 0 ,1]] # UR # BM #
P02 = [[0, 2, 1], [2, 0, 1]] # UF # CI #
P01 = [[0, 1, 0], [1, 0, 1]] # UL # DE #

P21 = [[2, 1, 0], [1, 1, 2]] # FL # LF #
P23 = [[2, 1, 2], [3, 1, 0]] # FR # JP #
P43 = [[4, 1, 0], [3, 1, 2]] # BR # TN #
P41 = [[4, 1, 2], [1, 1, 0]] # BL # RH #

P52 = [[5, 0, 1], [2, 2, 1]] # DF # UK #
P53 = [[5, 1, 2], [3, 2, 1]] # DR # VO #
P54 = [[5, 2, 1], [4, 2, 1]] # DB # WS #
P51 = [[5, 1, 0], [1, 2, 1]] # DL # XG #

AllEP = [P04, P03, P02, P01, P21, P23, P43, P41, P52, P53, P54, P51] # All Edges Position in the cube #
AllES = [["A", "Q"], ["B", "M"], ["C", "I"], ["D", "E"], ["L", "F"], ["J", "P"], ["T", "N"], ["R", "H"], ["U", "K"], ["V", "O"], ["W", "S"], ["X", "G"]]