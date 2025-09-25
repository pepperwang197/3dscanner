import matplotlib.pyplot as plt
import json

with open("fwuck.json", "r") as f:
    all_data = json.load(f)

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.scatter(all_data[0], all_data[1], s=15, marker="s", c=all_data[2], cmap="RdPu", norm="linear")

plt.show()