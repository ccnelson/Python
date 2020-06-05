import tkinter
import random

PROGRAM_NAME = " Rougé "
n = 20
o = n*2
score = 0
health = 50
levelx = [["#" for i in range(o)]for i in range(n)]

#tkinter settings
root = tkinter.Tk() # root is our 'window'
root.geometry('800x500') # size obvs
#root.wm_iconbitmap("favicon.ico") # icon
text = tkinter.Text(root, background='black', foreground='lawn green', font=('Courier', 12)) # text setup
label = tkinter.Label(root, text="label") # label for fun                   # courier is monospaced
button = tkinter.Button(root, text="OK") # button for fun
root.title(PROGRAM_NAME) # name in taskbar

#build level
room1sizex_max = random.randrange(int((n-1)/2),int(o/2))
room1sizey_max = random.randrange(int((n-1)/2),int(n/2))
room1sizex_min = random.randrange(1,int((n-2)/2))
room1sizey_min = random.randrange(1,int((n-2)/2))
room2sizex_max = random.randrange(n-1,o)
room2sizey_max = random.randrange(n-1,n)
room2sizex_min = random.randrange(1,n-2)
room2sizey_min = random.randrange(1,n-2)
midroom1x = room1sizex_min + int(abs(room1sizex_min - room1sizex_max) / 2)
midroom1y = room1sizey_min + int(abs(room1sizey_min - room1sizey_max) / 2)
midroom2x = room2sizex_min + int(abs(room2sizex_min - room2sizex_max) / 2)
midroom2y = room2sizey_min + int(abs(room2sizey_min - room2sizey_max) / 2)
for i in range(room1sizex_min, room1sizex_max):
    for j in range(room1sizey_min, room1sizey_max):
        levelx[j][i] = "."
for l in range(room2sizex_min, room2sizex_max):
    for m in range(room2sizey_min, room2sizey_max):
        levelx[m][l] = "."
levelx[midroom1y][midroom1x] = "1"
levelx[midroom2y][midroom2x] = "2"
for i in range(midroom1y+1, midroom2y+1):
    levelx[i][midroom1x] = "."
for i in range(midroom1x+1, midroom2x-1):
    levelx[midroom2y][i] = "."
    
#set player xy coords, make em global for now
global yco
global xco
yco = midroom1y
xco = midroom1x

#intial placing of player
levelx[yco][xco] = "i"

#main loop is in here mostly (!!)
def onKeyPress(event):
    #player control
    global yco
    global xco
    keyb = event.char
    if keyb == "w":
        if levelx[yco - 1][xco] != "#":
            levelx[yco][xco] = "."
            yco -= 1
            levelx[yco][xco] = "i"
    elif keyb == "s":
        if levelx[yco + 1][xco] != "#":
            levelx[yco][xco] = "."
            yco += 1
            levelx[yco][xco] = "i"
    elif keyb == "a":
        if levelx[yco][xco -1] != "#":
            levelx[yco][xco] = "."
            xco -= 1
            levelx[yco][xco] = "i"
    elif keyb == "d":
        if levelx[yco][xco +1] != "#":
            levelx[yco][xco] = "."
            xco += 1
            levelx[yco][xco] = "i"
    levelx[yco][xco] = "i"
    
    #print to screen
    text.delete(1.0,'end')  # clears all text
    #text.insert('end', 'You pressed %s\n' % (event.char, ))
    text.insert('end', '\n'*2)
    text.insert('end', '\t')
    for j in range(n):
        for k in range(o):
            text.insert('end', levelx[j][k])
        if j == 2:
            text.insert('end', "\tX: ")
            text.insert('end', xco)
        elif j == 3:
            text.insert('end', "\tY: ")
            text.insert('end', yco)
        elif j == 4:
            text.insert('end', "\tHealth: ")
            text.insert('end', health)
        elif j == 5:
            text.insert('end', "\tScore: ")
            text.insert('end', score)
        if k == o -1:
            text.insert('end', "\n\t")
    text.insert('end', "\n")
    text.see('end') # scroll to end
    #print(keyb)

# program starts here
text.insert('end', '\n'*2)
text.insert('end', '\t')
for j in range(n):              # this prints the initial screen
    for k in range(o):
        text.insert('end', levelx[j][k])
    if j == 2:
        text.insert('end', "\t...welcome...")
    if j == 3:
        text.insert('end', "\tuse wasd to move")
    if k == o -1:
        text.insert('end', "\n\t")

# tkinter stuff - pack, bind, and loop
label.pack(anchor="w") # anchored west
button.pack(anchor="w")
text.pack()         # make the text fill window
root.bind('<KeyPress>', onKeyPress) # when a player presses a button run the function
root.mainloop() # keep looping
