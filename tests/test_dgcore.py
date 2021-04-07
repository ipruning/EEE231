import sys
from pathlib import Path

current_folder = Path(__file__).absolute().parent
father_folder = str(current_folder.parent)
sys.path.append(father_folder)

import directedgraph

MyGraph = directedgraph.dgcore.Graph("MyGraph")
MyGraph.print_graph_details()