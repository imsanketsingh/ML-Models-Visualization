from tkinter import *
from K_Means_Exp import kMeans_
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def show_entry():
    
    p1 = int(e1.get())
    p2 = int(e2.get())
    p3 = int(e3.get())
    p4 = int(e4.get())
    
    fig = kMeans_(p1, p2, p3, p4)
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=6, columnspan=2)
    
master = Tk()
master.title("K-Means Clustering Demo")
label = Label(master, text="K-Means Clustering Demo", bg="black",
            fg="white").grid(row=0, columnspan=2)
Label(master, text="Enter K Value: ").grid(row=1)
Label(master, text="Enter Bucket Size: ").grid(row=2)
Label(master, text="Enter Min Bucket Value: ").grid(row=3)
Label(master, text="Enter Max Bucket Value: ").grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
Button(master, text="Show", command=show_entry).grid(row=5, columnspan=2)
plot_canvas = Canvas(master)
plot_canvas.grid(row=6, columnspan=2)
master.mainloop()