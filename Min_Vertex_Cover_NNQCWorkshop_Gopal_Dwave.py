import networkx as nx
import dwave_networkx as dnx
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dimod.reference.samplers import ExactSolver
import time
import matplotlib.pyplot as plt
import dimod


#66%%%%%%%%%%%%%%%%%%% 1st Example %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

sampler = dimod.ExactSolver()  # small testing sampler

G = dnx.chimera_graph(1, 1, 4)
G.remove_node(7)  # to give a unique solution
res=dnx.min_vertex_cover(G, sampler, lagrange=2.0)
print(res)





#66%%%%%%%%%%%%%%%%%%% 2nd Example %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# create a graph
s5 = nx.star_graph(5)
#s5 = nx.star_graph(20)
# Solve on a qpu
start_time = time.time()
sampler = EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(s5, sampler))
print("Solution on Quantum Computer--- %s seconds ---" % (time.time() - start_time))

# Solve on a Classical Computer
start_time = time.time()
sampler = ExactSolver()
print(dnx.min_vertex_cover(s5, sampler))
print("Solution on Classical Computer--- %s seconds ---" % (time.time() - start_time))

