import numpy
import matplotlib.pyplot as plt

ob=numpy.loadtxt(open("obstacles.csv","rb"),delimiter=",",skiprows=0)
pin=numpy.loadtxt(open("pins.csv","rb"),delimiter=",",skiprows=0)
ed3=numpy.loadtxt(open("tree_results.csv","rb"),delimiter=",",skiprows=0)

plt.figure(0)

for i in range(len(ob)):
    plt.plot([ob[i][0],ob[i][2]],[ob[i][1],ob[i][1]],color='r')
    plt.plot([ob[i][0],ob[i][2]],[ob[i][3],ob[i][3]],color='r')
    plt.plot([ob[i][0],ob[i][0]],[ob[i][1],ob[i][3]],color='r')
    plt.plot([ob[i][2],ob[i][2]],[ob[i][1],ob[i][3]],color='r')
for i in range(len(ed3)):
    plt.plot([ed3[i][0],ed3[i][1]],[ed3[i][2],ed3[i][3]],color='b')
for i in range(len(pin)):
    plt.scatter(pin[i][0],pin[i][1],color='b')
plt.savefig("tree_plot.jpg")
plt.show()

