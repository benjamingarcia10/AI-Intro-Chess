from Pieces import *
from BoardState import *
from Main import *

singlePawnBoard = BoardState()

singlePawnBoard.addPiece(Pawn(3, 3, 'white', PAWN_WHITE))

rookTakesQueen = BoardState()

rookTakesQueen.addPiece(Pawn(4,3,'black',PAWN_BLACK))
rookTakesQueen.addPiece(Pawn(3,4,'white',PAWN_WHITE))
rookTakesQueen.addPiece(Rook(5,6,'white', ROOK_WHITE))
rookTakesQueen.addPiece(Queen(5,1,'black', QUEEN_BLACK))


itsBaitMate = BoardState()

itsBaitMate.addPiece(Queen(1,3,'black', QUEEN_BLACK))
itsBaitMate.addPiece(Knight(3,3,'white', KNIGHT_WHITE))
itsBaitMate.addPiece(Rook(3,6,'white', ROOK_WHITE))


doYourJob = BoardState()

doYourJob.addPiece(Queen(3,2,'black', QUEEN_BLACK))
doYourJob.addPiece(Knight(3,6,'white', KNIGHT_WHITE))
doYourJob.addPiece(Rook(5,5,'black', ROOK_BLACK))
doYourJob.addPiece(King(3,7,'white', KING_WHITE))

you_might_be_outnumbered = BoardState()

# you_might_be_outnumbered.addPiece()
print("Capital Letter: Black, Lower Case: White")
print("Single Pawn Board", singlePawnBoard)
print("White Score:", singlePawnBoard.evaluate('white'))
print()

print("Rook Takes Queen: Before State", rookTakesQueen)
print("Black Score:", rookTakesQueen.evaluate('black'))
print("White Score:", rookTakesQueen.evaluate('white'))

tree_state = abMinMax('white', rookTakesQueen.createTree('white'), 'max').state
print("Rook Takes Queen: After State", tree_state)
print("Black Score:", tree_state.evaluate('black'))
print("White Score:", tree_state.evaluate('white'))
print('\n')

print("Its Bait Mate", itsBaitMate)
print("Black Score:",itsBaitMate.evaluate('black'))
print("White Score:", itsBaitMate.evaluate('white'))

print("Its Bait Mate: After State", abMinMax('black', itsBaitMate.createTree('black'), 'max').state)
print("Black Score:", tree_state.evaluate('black'))
print("White Score:", tree_state.evaluate('white'))
print('\n')

print("Do Your Job", doYourJob)
print("Black Score:",doYourJob.evaluate('black'))
print("White Score:", doYourJob.evaluate('white'))

print("Do Your Job: After State", abMinMax('white', doYourJob.createTree('white'), 'max').state)
print("Black Score:", tree_state.evaluate('black'))
print("White Score:", tree_state.evaluate('white'))
print('\n')