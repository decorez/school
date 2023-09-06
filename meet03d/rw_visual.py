import matplotlib.pyplot as plt

from random_walk import Randomwalk

rw = Randomwalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))

fig, axes = plt.subplots(figsize=(15,9), dpi=128 )
axes.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=10)
plt.grid(True)
plt.show()