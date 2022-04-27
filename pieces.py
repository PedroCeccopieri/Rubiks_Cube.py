
# Corners #

CGWO = (1, 4, 5) # Green, White, Orange #
CGWR = (1, 2, 5) # Green, White, Red #
CBWO = (3, 4, 5) # Blue, White, Orange #
CBWR = (2, 3, 5) # Blue, White, Red #

CGYO = (1, 4, 6) # Green, Yellow, Orange #
CGYR = (1, 2, 6) # Green, Yellow, Red #
CBYO = (3, 4, 6) # Blue, Yellow, Orange #
CBYR = (2, 3, 6) # Blue, Yellow, Red #

AllCC = (CGWO, CGWR, CBWO, CBWR, CGYO, CGYR, CBYO, CBYR) # All Corners Colors of the pieces #

# Corners position (x,y,z) #
		  # z #		 # x #		# y #
P125 = ((0, 0, 2), (1, 0, 0), (4, 2, 2)) # FRU #
P126 = ((0, 2, 2), (1, 2, 0), (5, 0, 2)) # FRD #															
P145 = ((0, 0, 0), (3, 0, 2), (4, 2, 0)) # FLU #
P146 = ((0, 2, 0), (3, 2, 2), (5, 0, 0)) # FLD #
P325 = ((2, 0, 0), (1, 0, 2), (4, 0, 2)) # BRU #
P326 = ((2, 2, 0), (1, 2, 2), (5, 2, 2)) # BRD #
P345 = ((2, 0, 2), (3, 0, 0), (4, 0, 0)) # BLU #
P346 = ((2, 2, 2), (3, 2, 0), (5, 2, 0)) # BLD #

AllCP = (P125, P126, P145, P146, P325, P326, P345, P346) # All Corners Position in the cube #

# Edges #

EWG = (1, 5) # Green, White #
EWR = (2, 5) # Red, White #
EWB = (3, 5) # Blue, White #
EWO = (4, 5) # Orange, White #

ERB = (2, 3) # Red, Blue #
EOB = (3, 4) # Orange, Blue #
ERG = (1, 2) # Red, Green #
EOG = (1, 4) # Orange, Green #

EYG = (1, 6) # Green, Yellow #
EYR = (2, 6) # Red, Yellow #
EYB = (3, 6) # Blue, Yellow #
EYO = (4, 6) # Orange, Yellow #

AllEC = (EWG, EWR, EWB, EWO, ERB, EOB, ERG, EOG, EYG, EYR, EYB, EYO) # All Edges Colors of the Pieces #

P12 = ((0, 1, 2), (1, 1, 0)) # FR # 0
P14 = ((0, 1, 0), (3, 1, 2)) # FL # 1
P15 = ((0, 0, 1), (4, 2, 1)) # FU # 2
P16 = ((0, 2, 1), (5, 0, 1)) # FD # 3
P23 = ((1, 1, 2), (2, 1, 0)) # RB # 4
P25 = ((1, 0, 1), (4, 1, 2)) # RU # 5
P26 = ((1, 2, 1), (5, 1, 2)) # RD # 6
P34 = ((2, 1, 2), (3, 1, 0)) # BL # 7
P35 = ((2, 0, 1), (4, 0, 1)) # BU # 8
P36 = ((2, 2, 1), (5, 2, 1)) # BD # 9
P45 = ((3, 0, 1), (4, 1, 0)) # LU # 10
P46 = ((3, 2, 1), (5, 1, 0)) # LD # 11

AllEP = (P12, P14, P15, P16, P23, P25, P26, P34, P35, P36, P45, P46) # All Edges Position in the cube #