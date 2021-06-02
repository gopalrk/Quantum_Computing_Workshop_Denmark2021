import numpy as np
import networkx as nx
import dwave_networkx as dnx
import dimod
from dimod.reference.samplers import ExactSolver
import matplotlib.pyplot as plt


# Let us now see how to map graph problem 

G = nx.Graph()
G.add_weighted_edges_from({(0,1,1),(0,2,1),(1,2,1), (1,4,1), (2,3,1), (3,4,1)})

nx.draw(G, with_labels=True)

output_name = 'MaxCutGraph_Workshop.png'
plt.savefig(output_name)

J = {(0,1):1,(0,2):1,(1,2):1,(1,4):1, (2,3):1, (3,4):1}
h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
print("The model that we are going to solve is")
print(model)
print()


# First, we solve it exactly

sampler = ExactSolver()
solution = sampler.sample(model)
print("The exact solution is")
print(solution)
print()


# Finally, we use the *quantum annealer* again with D-Wave's quantum computer 

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite


sampler = EmbeddingComposite(DWaveSampler(solver='Advantage_system1.1'))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("The solution obtained by D-Wave's quantum annealer",sampler_name,"is")
print(response)
print()



# Now, with *simulated annealing*
#sampler = dimod.SimulatedAnnealingSampler()
#response = sampler.sample(model, num_reads=10)
#print("The solution with simulated annealing is")
#print(response)
#print()
