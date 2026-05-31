import tkinter as tk
# from typing import Callable
app = tk.Tk()
app.title("Calculator App")
app.geometry("620x700")
app.config(bg="pink")


entry = tk.Entry(app, width=30, font=("Courier New", 25),borderwidth=15,relief="ridge",justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
# entry.pack()

 # function to handle button click
def click(value):
 entry.insert(tk.END, value)

def clear():
  entry.delete(0,tk.END)

def calculate():
  try:
    result=eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(0,str(result))
  except:
    entry.delete(0,tk.END)
    entry.insert(0,"error")

# button frame
frame = tk.Frame(app)
frame.grid()
# frame.pack()

# buttons
buttons=[
 "7","8","9","/",
 "4","5","6","*",
 "0","1","2","3",
 "c","=","+","-",
]
row=1
col=0

for button in buttons:
 if button=="=":
   action= calculate
   
 elif button=="c":
   action= clear
 else:
   action = lambda b=button: click(b)
 tk.Button(frame,text=button,width=10,height=5,font=("Arial", 8),bg="gray",fg="black",
          command=action).grid(row=row,column=col,padx=5,pady=5)
 
 col += 1

 if col > 3:
     col = 0
     row += 1
    
app.mainloop()  