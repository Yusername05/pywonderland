import numpy as np
import matplotlib.pyplot as plt
import polytopes.models as models


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

P = models.PlottingPolyhedra((5,2,3), (1,1,1), ax)
P.build_geometry()
P.plot_edges()
#P.plot_faces()

domain_segment_1 = np.array([
        P.mid_point_coords([0,1,10,11]),
        P.mid_point_coords([0,1]),
        P.mid_point_coords([0]),
        P.mid_point_coords([0,11])
    ])

domain_segment_2 = np.array([
        P.mid_point_coords([0,1]),
        P.mid_point_coords(list(range(0,10))),
        P.mid_point_coords([0,9]),
        P.mid_point_coords([0])
    ])

domain_segment_3 = np.array([
        P.mid_point_coords([0,9]),
        P.mid_point_coords([11,0,9,14,13,12]),
        P.mid_point_coords([0,11]),
        P.mid_point_coords([0])
    ])

domain_edges = np.array([
        P.mid_point_coords([0,1,10,11]),
        P.mid_point_coords([0,1]),
        P.mid_point_coords(list(range(0,10))),
        P.mid_point_coords([0,9]),
        P.mid_point_coords([11,0,9,14,13,12]),
        P.mid_point_coords([0,11])
    ])

P.plot_domain_segment(domain_segment_1, facecolors='red', edgecolors='r', alpha=0.3, linewidths=0)
P.plot_domain_segment(domain_segment_2, facecolors='red', edgecolors='r', alpha=0.3, linewidths=0)
P.plot_domain_segment(domain_segment_3, facecolors='red', edgecolors='r', alpha=0.3, linewidths=0)
P.plot_domain_segment(domain_edges, facecolors='black', edgecolors='b', alpha=0, linewidths=0.5)

#P.plot_vertex_labels()

ax.axis("off")
ax.set_proj_type('ortho')
ax.set_aspect('equal')

plt.show()