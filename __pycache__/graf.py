# import matplotlib.pyplot as plt

fig = plt.figure(figsize = (12,8))
plt.rcParams["font.size"] = "18"
plt.xlim(1, 10)
plt.ylim(-10, 10)
plt.xlabel('$r\ /\ \AA$')
plt.ylabel('$V\ /$ K')
plt.scatter(x, y, s=90, alpha=0.75, facecolor='none', edgecolor='black', label='$(r_i,V_i)$')
plt.scatter(xj, yL, s=60, alpha=0.75, c='r', label='Lagrange')
plt.errorbar(xj, yN, dyN, alpha=0.75, fmt ='o', markersize='4', c='blue', label='Nevill')
plt.legend()
plt.show()
fig.savefig("V(H-H)_inter_py.png", dpi=200)
plt.close(fig)
