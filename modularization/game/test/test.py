import sys
import os
from pathlib import Path
#--------------------------------1-------------------------------------------
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
#--------------------------------1-------------------------------------------

#--------------------------------2-------------------------------------------
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass
#---------------------------------------------------------------------------

from characters import player,boss

var = player.get_player_info()
print('var: ', var)