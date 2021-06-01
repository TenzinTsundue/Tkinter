[blog link](https://realpython.com/python-gui-tkinter/)<br>
[tkinter docs](https://tkdocs.com/tutorial/index.html)

### Tkinter GUI python

import tkinter
Widgets list:
- Button: A button that can contain text and can perform an action when clicked
- Canvas
- Checkbutton
- Entry: A text entry widget that allows only a single line of text
- Frame: A rectangular region used to group related widgets or provide padding between widgets
- Label: A widget used to display text on the screen
- Listbox
- Menubutton
- Menu
- Message
- Radiobutton
- Scale
- Scrollbar
- Text: A text entry widget that allows multiline text entry
- Toplevel
- Spinbox
- PanedWindow
- LabelFrame
- tkMessageBox

Standard attributes:
- Domensions
- Colors
- Fonts
- Anchors
- Relief styles
- Bitmaps
- Cursors

Geometry Management:
- pack()
- grid()
- place()

```
import tkinter as tk

window = tk.Tk()    #window is an instance of Tkinter's Tk class
greeting = tk.Label(
	text = "Hello, Tenzin",
	foreground = "white",   #set text color, can also give hexcode. shortform = fg
	background = "black",    #set background color shortform =bg
	width = 10,   	#tkinter use text unit where width and height of charcter "0"
	height = 5
	)
greeting.pack()	   #size the window small as it can 

button = tk.Button(
	text="Click me",
	width = 25,
	height = 5,
	bg = "blue",
	fg = "#00ffff"
	)
button.pack()

window.mainloop()   #tells python to tun the tkinter event loop until window is closed
```

Operation with entry widget
- get(): Retrieving text
- delete(): Deleting text
- insert(): Inserting text

working with frame
```
import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in frame_a") #master can control which frame a widget is assigned to
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in frame_b")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
```
```
import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in frame_a") #master can control which frame a widget is assigned to
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in frame_b")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
```
Adjusting frame appearance with reliefs
- tk.FLAT
- tk.SUNKEN
- tk.RAISED
- tk.GROOVE
- tk.RIDGE
```
import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()
```

Controlling layout with Geometry
- .pack()
- .place()
- .grid()

pack with fill, side and expand
```
import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)       #fill can be X ot Y or BOTH

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)       #side can be TOP BOTTOM LEFT RIGHT

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)       #your frame will expand and fill the window responsively

window.mainloop()

```

place() to control the precise location that a widget should occupy in a window or Frame with x and y coordinates
```
import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)    #create a frame with size 150*150
frame.pack()

label1=tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)     #create a red label and place at position(0, 0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()
```
grid() geometry manager provides all the power of .pack() in a format that's easier to understnad and mantain it works by splitting a window or Frame into rows and columns.

```
#creating 3 x 3 grid of frames 

import tkinter as tk 

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master = window,
            relief = tk.RAISED,
            borderwidth = 1
            )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row{i}\nColumn{j}")
        label.pack(padx=5, pady=5)
window.mainloop()
```  
```
#Grid layout that expands and contracts smoothly as the window is resized
import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master = window,
            relief = tk.RAISED,
            borderwidth = 1
            )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
```

```
import tkinter as tk 

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0,1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)

window.mainloop()
```

```
import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")    #n & N or e, s , w respectively 

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sn")     #can even cobine direction

window.mainloop()
```

```
import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()
```
.grid()        |     .pack()
sticky="ns"	   fill = tk.Y
sticky="ew"        fill = tk.X
sticky="nsew"      fill = tk.BOTH

Making your application Interactive

```
def handle_click(event):
    print("The button was clicked")

button = tk.Button(text="Click me!")

button.blind("<Button-1>", handle_click)
```

```
#add subtract
import tkinter as tk 

window = tk.Tk()

def increase():
	value = int(lbl_value['text'])
	lbl_value["text"] = f"{value + 1}"

def decrease():
	value = int(lbl_value['text'])
	lbl_value["text"] = f"{value - 1}"

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()
```

```
#roll dice

import random
import tkinter as tk

def roll():
    lbl_result["text"] = str(random.randint(1, 6))

window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Roll", command=roll)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()
```
