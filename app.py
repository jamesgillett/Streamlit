'''
Programme to display a 3D cube with lines of user defined styles. 
Created by James Gillett for Prof. David Fanning at the Univeristy of Manchester
'''
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect("equal")
plt.axis('off')

#Labels and axis
def square():
    vertices = [(0,0,1), (1,0,1), (1,0,0),(0,0,0), (0,1,1), (1,1,1), (1,1,0), (0,1,0)]
    letters = ['A','B','C','D','E','F','G','H']
    i=0
    for each in vertices:
        ax.scatter(each[0],each[1],each[2], color='k')
        ax.text(each[0],each[1],each[2], letters[i], size=15, zorder=10, color='k')
        i+=1


#Takes user input and plots square
def styleSquare(lines):   
    style = ('none', 'dotted', 'dashed', 'solid')
               
    #front
    ax.plot([0,1],ys=[0,0], zs=[0,0], color='k', linestyle=style[lines['CD']]) #DC bottom
    ax.plot([0,0],ys=[0,0], zs=[0,1], color='k', linestyle=style[lines['DA']]) #AD left
    ax.plot([1,1],ys=[0,0], zs=[0,1], color='k', linestyle=style[lines['BC']]) #BC right
    ax.plot([0,1],ys=[0,0], zs=[1,1], color='k', linestyle=style[lines['AB']]) #AB top
    
    #back
    ax.plot([0,1],ys=[1,1], zs=[0,0], color='k', linestyle=style[lines['GH']]) #GH bottom
    ax.plot([0,0],ys=[1,1], zs=[0,1], color='k', linestyle=style[lines['HE']]) #EH left
    ax.plot([1,1],ys=[1,1], zs=[0,1], color='k', linestyle=style[lines['FG']]) #FG right
    ax.plot([0,1],ys=[1,1], zs=[1,1], color='k', linestyle=style[lines['EF']]) #EF top
    
    #joins
    ax.plot([0,0],ys=[0,1], zs=[0,0], color='k', linestyle=style[lines['DH']]) #DH bottom_left
    ax.plot([1,1],ys=[0,1], zs=[0,0], color='k', linestyle=style[lines['CG']]) #CG bottom_right
    ax.plot([0,0],ys=[0,1], zs=[1,1], color='k', linestyle=style[lines['AE']]) #AE top_left
    ax.plot([1,1],ys=[0,1], zs=[1,1], color='k', linestyle=style[lines['BF']]) #BF top_right
    
    
#User interface
def interface(lines):
    total = 0
    question = ('AB', 'BC','CD','DA','EF','FG','GH','HE','AE','BF','CG','DH')
    print('Please complete the following: \n 0 = no line \n 1 = dotted \n 2 = dashed \n 3 = solid')
    
    for i2 in question: 
        while True:
            lines[i2] = input(i2 + '= ')
            if lines[i2] == '0' or lines[i2]== '1' or lines[i2]== '2' or lines[i2]== '3':
                break
            else:
                print('Please input 0, 1, 2, or 3')
        lines[i2] = int(lines[i2])
        total += lines[i2]
    print("\n'Score' for cube = " + str(total))
    return(lines)
    

lines = {'AB':'','BC':'','CD':'','DA':'','EF':'','FG':'','GH':'','HE':'','AE':'','BF':'','CG':'','DH':''}    
square()
lines = interface(lines)
styleSquare(lines)

st.pyplot(fig)
plt.show()
