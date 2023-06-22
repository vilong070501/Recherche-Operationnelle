import sys
sys.path.insert(0, '../src/')

import utils as ut

dist = 1000
ut.pretty_print(dist)
ut.plot_functions_mixte(dist, ut.cost_deneigement_1, ut.cost_deneigement_2, ut.cost_deneigement_mixte)
