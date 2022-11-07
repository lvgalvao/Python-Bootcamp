import tkinter
root = tkinter.Tk(  )
for r in range(3):
   for c in range(4):
      tkinter.Label(root, text='R%s/C%s'%(r,c),
         borderwidth=1 ).grid(row=r,column=c)
root.mainloop(  )

for r in range (4):
    for c in range (3):
        tkinter.Label(root, text=f'{r}/{c}',borderwidth=1).grid

root.mainloop(  )