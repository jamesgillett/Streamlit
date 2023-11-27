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
def styleSquare(lines, colors=None):   
    style = ('none', 'dotted', 'dashed', 'solid')

    for key in lines.keys():
        segment_style = style[lines[key]]

        start, end = key[0], key[1]

        start_index = ord(start) - ord('A')
        end_index = ord(end) - ord('A')

        if colors and colors[key] != '':
            segment_color = colors[key]
        else:
            segment_color = 'k'  # Default to black if color is not specified

        ax.plot([vertices[start_index][0], vertices[end_index][0]],
                [vertices[start_index][1], vertices[end_index][1]],
                [vertices[start_index][2], vertices[end_index][2]],
                color=segment_color, linestyle=segment_style)

# User interface 
def interface(lines, colors):
    total = 0
    question = ('AB', 'BC', 'CD', 'DA', 'EF', 'FG', 'GH', 'HE', 'AE', 'BF', 'CG', 'DH')
    style_options = ("0", "1", "2", "3")

    show_color_dropdown = st.checkbox("Show Color Dropdown", value=True)

    if show_color_dropdown:
        color_options = ('black', 'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown')
    else:
        color_options = [None] * len(question)

    # Create a dictionary to store user responses
    lines = {q: "" for q in question}
    colors = {q: "" for q in question}

    st.write('0 = no line | 1 = dotted | 2 = dashed | 3 = solid')

    # Create three columns
    cols = st.columns(3)

    # Iterate through columns
    for i, col in enumerate(cols):
        # Iterate through questions in each column
        for q in question[i::3]:
            lines[q] = col.radio(f"{q} Style", style_options, horizontal=True)
            if show_color_dropdown:
                colors[q] = col.selectbox(f"{q} Color", color_options)

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
    col1, col2 = st.columns(2)   
    with col1: st.write("Total = ", total) 

    return lines, colors

st.title("The Quotation Cube")

vertices = [(0, 0, 1), (1, 0, 1), (1, 0, 0), (0, 0, 0), (0, 1, 1), (1, 1, 1), (1, 1, 0), (0, 1, 0)]
lines = {'AB': '', 'BC': '', 'CD': '', 'DA': '', 'EF': '', 'FG': '', 'GH': '', 'HE': '', 'AE': '', 'BF': '', 'CG': '', 'DH': ''}
colors = {'AB': '', 'BC': '', 'CD': '', 'DA': '', 'EF': '', 'FG': '', 'GH': '', 'HE': '', 'AE': '', 'BF': '', 'CG': '', 'DH': ''}

square()

lines, colors = interface(lines, colors)

styleSquare(lines, colors)
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
