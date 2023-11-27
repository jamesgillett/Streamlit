'''
Programme to display a 3D cube with lines of user defined styles. 
Created by James Gillett for Prof. David Fanning at the Univeristy of Manchester
'''
import streamlit as st
import io
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1]) 
plt.axis('off')

# Labels and axis
def square():
    vertices = [(0,0,1), (1,0,1), (1,0,0),(0,0,0), (0,1,1), (1,1,1), (1,1,0), (0,1,0)]
    letters = ['A','B','C','D','E','F','G','H']
    i=0
    for each in vertices:
        ax.scatter(each[0],each[1],each[2], color='k')
        ax.text(each[0],each[1],each[2], letters[i], size=15, zorder=10, color='k')
        i+=1

# Takes user input and plots square
def styleSquare(lines):   
    style = ('none', 'dotted', 'dashed', 'solid')
               
    #front
    ax.plot([0,1],ys=[0,0], zs=[0,0], color='k', linestyle=style[lines['CD']]) #CD bottom
    ax.plot([0,0],ys=[0,0], zs=[0,1], color='k', linestyle=style[lines['DA']]) #DA left
    ax.plot([1,1],ys=[0,0], zs=[0,1], color='k', linestyle=style[lines['BC']]) #BC right
    ax.plot([0,1],ys=[0,0], zs=[1,1], color='k', linestyle=style[lines['AB']]) #AB top
    
    #back
    ax.plot([0,1],ys=[1,1], zs=[0,0], color='k', linestyle=style[lines['GH']]) #GH bottom
    ax.plot([0,0],ys=[1,1], zs=[0,1], color='k', linestyle=style[lines['HE']]) #HE left
    ax.plot([1,1],ys=[1,1], zs=[0,1], color='k', linestyle=style[lines['FG']]) #FG right
    ax.plot([0,1],ys=[1,1], zs=[1,1], color='k', linestyle=style[lines['EF']]) #EF top
    
    #joins
    ax.plot([0,0],ys=[0,1], zs=[0,0], color='k', linestyle=style[lines['DH']]) #DH bottom_left
    ax.plot([1,1],ys=[0,1], zs=[0,0], color='k', linestyle=style[lines['CG']]) #CG bottom_right
    ax.plot([0,0],ys=[0,1], zs=[1,1], color='k', linestyle=style[lines['AE']]) #AE top_left
    ax.plot([1,1],ys=[0,1], zs=[1,1], color='k', linestyle=style[lines['BF']]) #BF top_right

# User interface 
def interface(lines):
    total = 0
    question = ('AB', 'BC', 'CD', 'DA', 'EF', 'FG', 'GH', 'HE', 'AE', 'BF', 'CG', 'DH')
    style_options = ("0", "1", "2", "3")

    # Create a dictionary to store user responses
    lines = {q: "" for q in question}
    st.write('0 = no line | 1 = dotted | 2 = dashed | 3 = solid')

    # Create three columns
    cols = st.columns(3)

    # Iterate through columns
    for i, col in enumerate(cols):
        # Iterate through questions in each column
        for q in question[i::3]:
            lines[q] = col.radio(q, style_options, horizontal=True)

    while True:
        for i2 in question: 
            if lines[i2] == "n":
                lines[i2] = 0
            elif lines[i2] =="d":
                lines[i2] = 1
            elif lines[i2] =="da":
                lines[i2]= 2
            elif lines[i2] =="s":
                lines[i2] = 3
            lines[i2] = int(lines[i2])
            total += lines[i2]
        break
    col1,col2 = st.columns(2)   
    with col1: st.write("Total = ", total) 
    with col2: 
    # Add a button to clear the inputs
        if st.button("Clear Inputs"):
        # Reset the state in st.session_state
            st.experimental_rerun()   
    
    return(lines)

st.title("The Quotation Cube")

lines = {'AB':'','BC':'','CD':'','DA':'','EF':'','FG':'','GH':'','HE':'','AE':'','BF':'','CG':'','DH':''}    
square()

lines = interface(lines)

styleSquare(lines)
st.pyplot(fig)

# Download button
fn = 'cube.png'
img = io.BytesIO()
plt.savefig(img, format='png')

btn = st.download_button(
   label="Download cube",
   data=img,
   file_name=fn,
   mime="image/png"
)