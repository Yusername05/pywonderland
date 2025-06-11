import three;
size(200);
currentprojection = perspective(5,2,2);

// Use the outpu of m2diamgras.py here for the coordinates of the polyhedra you want.

//Point coordinates
triple[] pts = {(0.5773502691896255, 0.5773502691896256, 0.5773502691896262), (-0.5773502691896255, 0.5773502691896256, 0.5773502691896262), (0.5773502691896257, -0.5773502691896254, 0.5773502691896262), (-0.5773502691896257, -0.5773502691896254, 0.5773502691896262), (0.5773502691896257, 0.5773502691896265, -0.577350269189625), (-0.5773502691896257, 0.5773502691896266, -0.577350269189625), 
(0.5773502691896267, -0.5773502691896256, -0.577350269189625), (-0.5773502691896267, -0.5773502691896256, -0.577350269189625)};    
//Edge indices
int[][] edges = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {0, 4}, {1, 5}, {4, 5}, {4, 6}, {2, 6}, {3, 7}, {5, 7}, {6, 7}};
//Face indices
int[][] faces = {{0, 2, 3, 1}, {0, 4, 5, 1}, {0, 4, 6, 2}, {1, 5, 7, 3}, {2, 6, 7, 3}, {4, 6, 7, 5}};


// Drawing edges
for (int[] e : edges)
    draw(pts[e[0]]--pts[e[1]], black+linewidth(0.7));

// Drawing faces
for (int[] f : faces) {
  path3 facePath = pts[f[0]];
  for (int i = 1; i < f.length; ++i)
    facePath = facePath -- pts[f[i]];
  facePath = facePath -- cycle;
  draw(surface(facePath), surfacepen=material(
    diffusepen=gray+opacity(0.6),
    emissivepen=gray, 
    specularpen=black));
}

// for (int i = 0; i < pts.length; ++i) {
//     label((string) i, pts[i]);
// }