"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt
class Trees():
    def __init__(self):
        self.s=1
        self.d=[[0,1,0]]

    def plot_tree(self):
        plt.plot([0,0],[0,1])
        for i in range(5):  # creating edges of the tree
            n=[]
            for j in range(len(self.d)): #creating branches of tree
                n.append([self.d[j][0]+self.s*sin(self.d[j][2]-0.1), self.d[j][1]+self.s*cos(self.d[j][2]-0.1), self.d[j][2]-0.1])
                n.append([self.d[j][0]+self.s*sin(self.d[j][2]+0.1), self.d[j][1]+self.s*cos(self.d[j][2]+0.1), self.d[j][2]+0.1])
                plt.plot([self.d[j][0], n[-2][0]],[self.d[j][1], n[-2][1]])
                plt.plot([self.d[j][0], n[-1][0]],[self.d[j][1], n[-1][1]])
            self.d=n
            self.s*=0.6
        plt.title("tree plot")
        plt.savefig('tree.png')

tree = Trees()
tree.plot_tree()
