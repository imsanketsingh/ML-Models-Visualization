from tkinter import *
from K_Means_Exp import kMeans_
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="ML Algo Visualizer", page_icon="🥽")

st.markdown("""
        <style>
            .greeting {
                font-size:20px;
                position: absolute;
                left: 50%;
                transform: translate(-50%, -50%);
                text-align: center;
                animation: fadeIn 3s;
            }

            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
        </style>
        """, unsafe_allow_html=True)

st.markdown('<h1 class="greeting">Hey Stranger, you are welcome!</h1>', unsafe_allow_html=True)

choose = option_menu("", ["Blank", "KMeans"],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#24A608"},
    }
    ) 
if choose == "Blank":
    st.markdown('<p class="greeting">Choose the Algo</p>', unsafe_allow_html=True)

if choose == "KMeans":
    st.markdown('<p class="greeting">Kindly check the new window just opened</p>', unsafe_allow_html=True)

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
