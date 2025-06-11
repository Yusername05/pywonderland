import matplotlib.pyplot as plt
from itertools import chain

import polytopes.models as models

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

P = models.PlottingPolyhedra((4,2,3), (1,0,0), ax)
P.build_geometry()
P.plot_edges()
P.plot_faces()

vertex_coords_string = str(list(tuple(x) for x in P.vertices_coords)).replace('[', '{').replace(']', '}')
edges_indices_string = str(list(x for x in (chain.from_iterable(P.edge_indices)))).replace('[', '{').replace(']', '}')
faces_indices_string = str(list(x for x in (chain.from_iterable(P.face_indices)))).replace('[', '{').replace(']', '}')

print(f"//Point coordinates\ntriple[] pts = {vertex_coords_string};\n//Edge indices\nint[][] edges = {edges_indices_string};\n//Face indices\nint[][] faces = {faces_indices_string};")