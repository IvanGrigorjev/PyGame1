import tkinter

lines = 0

master = tkinter.Tk()
master.geometry('600x600')
canvas = tkinter.Canvas(master, bg='#FFFFFF', height=600, width=600)
for i in range(75, 600, 75):
    canvas.create_line(0, i, 600, i, fill='#000000')
    canvas.create_line(i, 0, i, 600, fill='#000000')
for g in range(0, 225, 75):
    lines += 1
    for i in range(0, 600, 150):
        if lines % 2 == 0:
            canvas.create_oval(i + 75, g, i + 75 + 75, g + 75, fill='#FF0000')
        else:
            canvas.create_oval(i, g, i + 75, g + 75, fill='#FF0000')
for g in range(375, 600, 75):
    lines += 1
    for i in range(0, 600, 150):
        if lines % 2 == 0:
            canvas.create_oval(i + 75, g, i + 75 + 75, g + 75, fill='#0C00E5')
        else:
            canvas.create_oval(i, g, i + 75, g + 75, fill='#0C00E5')

canvas.pack()
master.mainloop()
