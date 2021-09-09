from datetime import date
from datetime import datetime

import Tkinter as tk
from Tkinter import *

from time import gmtime, strftime
import time
import matplotlib.pyplot as plt
import numpy as np
import math

import csv

import random
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation


class PlotClass():

    def __init__(self):
        self.x = np.arange(-5, 5, 0.1)
        lfunc = lambda t : 5*np.sin(2*math.pi*self.x)
        self.y = 3*math.pi*np.exp(-(lfunc(self.x)))

    def mat_plot_style(self, title="Visualization"):
        plt.cla()
        plt.style.use('fivethirtyeight')
        plt.plot(self.x, self.y)
        plt.title(title)
        plt.tight_layout()

    def mat_plot_output(self, otherargument=False):
        plt.show()

    def restart_func(self):
        self.x = []
        self.y = []
        self.index = count()

    def stop_func(self):
        self.ani.event_source.stop()

    def start_func(self):
        self.ani.event_source.start()

    def save_csv(self):
        today = date.today()
        todays_date = today.strftime("%d/%m/%Y")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(todays_date, current_time)

        f = open(self.e1.get() + 'data.csv', 'w')

        writer = csv.writer(f)

        header = ['name', 'date', 'time', "x_values", "y_values"]
        data = [self.e1.get(), todays_date, current_time, self.x[0], self.y[0]]

        print(header, data)
        writer.writerow(header)

        writer.writerow(data)
        for i in range(len(self.x)-1):
            writer.writerow([None, None, None, self.x[i]+1, self.y[i]+1])
        f.close()
        self.mat_plot_style(self.e1.get())
        self.mat_plot_output()

    def tkinter_func(self):
        master = tk.Tk()
        tk.Label(master, text="Visualization Name: ").pack()

        self.e1 = tk.Entry(master)

        self.e1.pack()

        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()

        x = ws/2.3
        y = hs/3

        master.geometry('+%d+%d' % (x, y))

        tk.Button(master, text='Save', command=self.save_csv).pack()
        tk.Label(master, text="Note that the buttons below only work for DynamicClass").pack()
        tk.Button(master, text='Start', command=self.start_func).pack()
        tk.Button(master, text='Stop', command=self.stop_func).pack()
        tk.Button(master, text='Reset', command=self.restart_func).pack()

class DynamicClass(PlotClass):

    def __init__(self):
        self.x = []
        self.y = []
        self.index = count()

    def animate(self, otherargument=False):
        self.x.append(next(self.index))
        self.y.append(self.x[-1] + random.randint(0, 100))
        self.mat_plot_style(self.e1.get())

    def do_the_animation(self):
        self.ani = FuncAnimation(plt.gcf(), self.animate, interval=250)
        self.mat_plot_output()

class ROSClass(PlotClass, DynamicClass):

    def animate(self, otherargument=False):
        data = pd.read_csv('/home/elias/kthfsdv/data.csv')
        self.x = data['x_value']
        self.y = data['resultq']
        self.mat_plot_style(self.e1.get())

    def restart_func(self):
        self.x = []
        self.y = []
        self.index = count()


def dynamic_func():
    d = DynamicClass()
    d.tkinter_func()
    d.animate()
    d.do_the_animation()
    d.morebuttons()

dynamic_func()

def ros_func():
    r = ROSClass()
    r.tkinter_func()
    r.do_the_animation()

#ros_func()

def plot_func():
    p = PlotClass()
    p.tkinter_func()
    p.mat_plot_style()
    p.mat_plot_output()

#plot_func()
