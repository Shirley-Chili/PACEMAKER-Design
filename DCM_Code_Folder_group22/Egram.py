from tkinter import *
from matplotlib.pylab import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure 
from User import *
import serial
import struct
from tkinter import * 
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
'''
@brief
    The Egram module is used to take the output from the Simulink via serial communication and plot the real-time data to a graph. 
    The graph has a fixed Y-axis and X-axis that will update its value to match the increasing time. 
    The graph will show up once the user presses the “Egram” button in the mode’s parameter interface.
@how to use
    The 
'''
class Egram():
    def __init__(self):
        self.aamp=np.array([])
        self.vamp=np.array([])
        self.window = Tk()
        self.window.title(' Egram ')
        self.window.geometry("800x300")
        self.eegram()
        self.window.mainloop()

    def eegram(self):
        self.Fig = Figure(figsize = (8, 8),dpi = 100)
        self.A = self.Fig.add_subplot(221)
        self.V = self.Fig.add_subplot(222)
        self.Fig.subplots_adjust(hspace = 0.5)
        self.A.set_title('Atrium Signal', fontsize = 14)
        self.V.set_title('Ventricle Signal', fontsize = 14)
        self.A.set_xlabel("Sample of time", fontsize = 12)
        self.A.set_ylabel("Voltage in mV", fontsize = 12)
        self.V.set_xlabel("Sample of time", fontsize = 12)
        self.V.set_ylabel("Voltage in mV", fontsize = 12)
        self.A.set_ylim(-5,5)
        self.A.set_xlim(0,300)
        self.linesA=self.A.plot([],[])[0]
        self.V.set_ylim(-5,5)
        self.V.set_xlim(0,300)
        self.linesV=self.V.plot([],[])[0]
        self.canvas = FigureCanvasTkAgg(self.Fig,master = self.window)  
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.window)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()
        self.window.update()
        self.window.after(1,self.plot)
    def plot(self):
        try:
            ser = serial.Serial(port="COM"+str(8), baudrate=115200)
        except:
            self.window.destroy()
            messagebox.showinfo("Message","Pacemaker not connected")
        ser.reset_input_buffer()
        ser.write(struct.pack('<21B',0x16,0x22,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
        serialdata=ser.read(16)
        ser.close()
        vol = struct.unpack('dd',serialdata)
        a=-5*vol[0]
        v=-5*vol[1]
        if(len(self.aamp)<300):
            self.aamp=np.append(self.aamp,a)
            self.vamp=np.append(self.vamp,v)
        else:
            self.aamp[0:299]=self.aamp[1:300]
            self.vamp[0:299]=self.vamp[1:300]
            self.aamp[299]=a
            self.vamp[299]=v
        self.linesA.set_xdata(np.arange(0,len(self.aamp)))
        self.linesA.set_ydata(self.aamp)
        self.linesV.set_xdata(np.arange(0,len(self.vamp)))
        self.linesV.set_ydata(self.vamp)
        self.canvas.draw()
       
        self.window.after(50,self.plot)
    