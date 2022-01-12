from tkinter import *
from tkinter import messagebox
import pickle
from User import *
from myMode import *
import serial
from serial.tools import list_ports
import struct
from Egram import*
root = Tk()
root.geometry('400x300')
root.title('DCM LOGIN')
Label(root, font=('Times New Roman', 19), justify=CENTER, text="WELCOME TO PACEMAKER DCM").place(x=0, y=30)
global tempuserlist
global userindex
global modes  # 1,2,3,4,5,6,7,8,9,10 aoo,voo,aai,vvi,doo,door,aair,vvir,aoor,voor
global ser_list
global ports
global ser
global eegram
modes = 0
ser_list = [22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



def serial_init():
    global ports
    global ser
    try:
        ports = list(list_ports.comports())
        ser = serial.Serial(port=ports[1].device, baudrate=115200, timeout=None, bytesize=8,
                            stopbits=serial.STOPBITS_ONE)
        if (ser.is_open):
            messagebox.showinfo("System Message", "Device Connected")
        else:
            messagebox.showinfo("System Message", "Connection Failed")
        ser.close()
    except OSError:
        messagebox.showinfo("System Message", "No connection for usb ports")


def serial_send():
    global modes
    global ser_list
    global ser
    ports = list(list_ports.comports())
    ser = serial.Serial(port=ports[1].device, baudrate=115200, timeout=None, bytesize=8, stopbits=serial.STOPBITS_ONE)
    if (modes == 1):  # AOO
        ser_list[1] = 85
        ser_list[2] = 1
        ser_list[3] = tempuserlist[userindex].aoo.getLRL()
        ser_list[4] = tempuserlist[userindex].aoo.getURL()
        ser_list[5] = int(tempuserlist[userindex].aoo.getaAmp()) * 20  # save bytes here
        ser_list[6] = tempuserlist[userindex].aoo.getAPW()

        modes = 0
        send = struct.pack('<BBBBBBfBBBBBBBBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        ser.write(send)

    if (modes == 2):  # VOO
        ser_list[1] = 85
        ser_list[2] = 2
        ser_list[3] = tempuserlist[userindex].voo.getLRL()
        ser_list[4] = tempuserlist[userindex].voo.getURL()
        ser_list[5] = int(tempuserlist[userindex].voo.getVAmp()) * 20
        ser_list[6] = tempuserlist[userindex].voo.getVPW()
        modes = 0
        send = struct.pack('<BBBBBBfBBBBBBBBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        ser.write(send)

    if (modes == 3):  # AAI
        ser_list[1] = 85
        ser_list[2] = 3
        ser_list[3] = tempuserlist[userindex].aai.getLRL()
        ser_list[4] = tempuserlist[userindex].aai.getURL()
        ser_list[5] = int(tempuserlist[userindex].aai.getaAmp()) * 20
        ser_list[6] = tempuserlist[userindex].aai.getAPW()
        ser_list[7] = tempuserlist[userindex].aai.getARP()
        ser_list[8] = tempuserlist[userindex].aai.getAS()
        modes = 0
        send = struct.pack('<BBBBBBfHfBBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], 1, 1, 1, 1, 1)
        ser.write(send)

    if (modes == 4):  # VVI
        ser_list[1] = 85
        ser_list[2] = 4
        ser_list[3] = tempuserlist[userindex].vvi.getLRL()
        ser_list[4] = tempuserlist[userindex].vvi.getURL()
        ser_list[5] = int(tempuserlist[userindex].vvi.getVAmp()) * 20
        ser_list[6] = tempuserlist[userindex].vvi.getVPW()
        ser_list[7] = tempuserlist[userindex].vvi.getVRP()
        ser_list[8] = tempuserlist[userindex].vvi.getVS()
        modes = 0
        send = struct.pack('<BBBBBBfHfBBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], 1, 1, 1, 1, 1)
        ser.write(send)

    if (modes == 5):  # DOO
        ser_list[1] = 85
        ser_list[2] = 5
        ser_list[3] = tempuserlist[userindex].doo.getLRL()
        ser_list[4] = tempuserlist[userindex].doo.getURL()
        ser_list[5] = int(tempuserlist[userindex].doo.getvAmp()) * 20
        ser_list[6] = tempuserlist[userindex].doo.getVPW()
        ser_list[7] = int(tempuserlist[userindex].doo.getaAmp()) * 20
        ser_list[8] = tempuserlist[userindex].doo.getAPW()
        ser_list[9] = int(tempuserlist[userindex].doo.getFAD())
        modes = 0
        send = struct.pack('<BBBBBBfBfHBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], ser_list[9], 1, 1, 1, 1)
        ser.write(send)

    if (modes == 6):  # DOOR
        ser_list[1] = 85
        ser_list[2] = 6
        ser_list[3] = tempuserlist[userindex].door.getLRL()
        ser_list[4] = tempuserlist[userindex].door.getURL()
        ser_list[5] = int(tempuserlist[userindex].door.getvAmp()) * 20
        ser_list[6] = tempuserlist[userindex].door.getVPW()
        ser_list[7] = int(tempuserlist[userindex].door.getaAmp()) * 20
        ser_list[8] = tempuserlist[userindex].door.getAPW()
        ser_list[9] = int(tempuserlist[userindex].door.getFAD())
        ser_list[10] = int(tempuserlist[userindex].door.getMSR())
        ser_list[11] = int(tempuserlist[userindex].door.getReactionT())
        ser_list[12] = int(tempuserlist[userindex].door.getRF())
        ser_list[13] = int(tempuserlist[userindex].door.getRecoveryT())

        modes = 0
        send = struct.pack('<BBBBBBfBfHBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], ser_list[9], ser_list[10], ser_list[11],
                           ser_list[12], ser_list[13])
        ser.write(send)

    if (modes == 7):  # AAIR
        ser_list[1] = 85
        ser_list[2] = 7
        ser_list[3] = tempuserlist[userindex].aair.getLRL()
        ser_list[4] = tempuserlist[userindex].aair.getURL()
        ser_list[5] = int(tempuserlist[userindex].aair.getaAmp()) * 20
        ser_list[6] = tempuserlist[userindex].aair.getAPW()
        ser_list[7] = tempuserlist[userindex].aair.getARP()
        ser_list[8] = int(tempuserlist[userindex].aair.getMSR())
        ser_list[9] = int(tempuserlist[userindex].aair.getReactionT())
        ser_list[10] = int(tempuserlist[userindex].aair.getRF())
        ser_list[11] = int(tempuserlist[userindex].aair.getRecoveryT())
        ser_list[12] = tempuserlist[userindex].aair.getAS()

        modes = 0
        send = struct.pack('<BBBBBBfHBBBBfB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], ser_list[9], ser_list[10], ser_list[11],
                           ser_list[12], 1)
        ser.write(send)

    if (modes == 8):  # VVIR
        ser_list[1] = 85
        ser_list[2] = 8
        ser_list[3] = tempuserlist[userindex].vvir.getLRL()
        ser_list[4] = tempuserlist[userindex].vvir.getURL()
        ser_list[5] = int(tempuserlist[userindex].vvir.getVAmp()) * 20
        ser_list[6] = tempuserlist[userindex].vvir.getVPW()
        ser_list[7] = tempuserlist[userindex].vvir.getVRP()
        ser_list[8] = int(tempuserlist[userindex].vvir.getMSR())
        ser_list[9] = int(tempuserlist[userindex].vvir.getReactionT())
        ser_list[10] = int(tempuserlist[userindex].vvir.getRF())
        ser_list[11] = int(tempuserlist[userindex].vvir.getRecoveryT())
        ser_list[12] = tempuserlist[userindex].vvir.getVS()

        modes = 0
        send = struct.pack('<BBBBBBfHBBBBfB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], ser_list[9], ser_list[10], ser_list[11],
                           ser_list[12], 1)
        ser.write(send)
    if (modes == 9):  # AOOR
        ser_list[1] = 85
        ser_list[2] = 9
        ser_list[3] = tempuserlist[userindex].aoor.getLRL()
        ser_list[4] = tempuserlist[userindex].aoor.getURL()
        ser_list[5] = int(tempuserlist[userindex].aoor.getaAmp()) * 20  # save bytes here
        ser_list[6] = tempuserlist[userindex].aoor.getAPW()
        ser_list[7] = int(tempuserlist[userindex].aoor.getMSR())
        ser_list[8] = int(tempuserlist[userindex].aoor.getReactionT())
        ser_list[9] = int(tempuserlist[userindex].aoor.getRF())
        ser_list[10] = int(tempuserlist[userindex].aoor.getRecoveryT())
        print(ser_list[6])
        modes = 0
        send = struct.pack('<BBBBBBfBBBBBBBBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], ser_list[9], ser_list[10], 1, 1, 1, 1, 1,
                           1, 1)
        print(ser.write(send))

    if (modes == 10):  # VOOR
        ser_list[1] = 85
        ser_list[2] = 10
        ser_list[3] = tempuserlist[userindex].voor.getLRL()
        ser_list[4] = tempuserlist[userindex].voor.getURL()
        ser_list[5] = int(tempuserlist[userindex].voor.getvAmp()) * 20
        ser_list[6] = tempuserlist[userindex].voor.getVPW()
        ser_list[7] = int(tempuserlist[userindex].voor.getMSR())
        ser_list[8] = int(tempuserlist[userindex].voor.getReactionT())
        ser_list[9] = int(tempuserlist[userindex].voor.getRF())
        ser_list[10] = int(tempuserlist[userindex].voor.getRecoveryT())
        modes = 0
        send = struct.pack('<BBBBBBfBBBBBBBBBBB', ser_list[0], ser_list[1], ser_list[2], ser_list[3], ser_list[4],
                           ser_list[5], ser_list[6], ser_list[7], ser_list[8], ser_list[9], ser_list[10], 1, 1, 1, 1, 1,
                           1, 1)
        ser.write(send)
   
    ser.close()


def ShowVVIParameters():
    global modes
    global tempuserlist
    modes = 4
    VVIMode = Tk()
    VVIMode.title("VVI Mode")
    VVIMode.geometry("1350x900")

    def upload():

        try:
            if (60 / int(LRLEntry.get()) * 1000 == int(VRPEntry.get())):
                raise ZeroDivisionError
            if (int(LRLEntry.get()) < int(URLEntry.get())):
                tempuserlist[userindex].vvi.setLRL(LRLEntry.get())
                tempuserlist[userindex].vvi.setURL(URLEntry.get())
                tempuserlist[userindex].vvi.setVAmp(VentAmpEntry.get())
                tempuserlist[userindex].vvi.setVPW(VPWEntry.get())
                tempuserlist[userindex].vvi.setVRP(VRPEntry.get())
                tempuserlist[userindex].vvi.setVS(VSEntry.get())
                print(tempuserlist[userindex].vvi.getLRL())
                # print(tempuserlist[userindex].vvi.getURL())
                # print(tempuserlist[userindex].vvi.getVAmp())
                # print(tempuserlist[userindex].vvi.getVPW())
                # print(tempuserlist[userindex].vvi.getVRP())
                with open('user.pickle', 'wb') as f:
                    for x in tempuserlist:
                        pickle.dump(x, f)
                with open('user.pickle', 'rb') as f:
                    test = pickle.load(f)
                    # test1 = pickle.load(f)
            else:
                raise NameError

        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
        except ZeroDivisionError:
            messagebox.showerror("ERROR", "Time for this LRL equals to VRP")

    
    LRLVar = StringVar()
    Label(VVIMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                      y=200)
    LRLEntry = Entry(VVIMode, textvariable=LRLVar, font=('Times New Roman', 10), width=27)
    LRLEntry.insert(0, tempuserlist[userindex].vvi.getLRL())
    LRLEntry.place(x=75, y=240)

    URLVar = StringVar()
    Label(VVIMode, text='Uper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                     y=200)
    URLEntry = Entry(VVIMode, textvariable=URLVar, font=('Times New Roman', 10), width=27)
    URLEntry.insert(0, tempuserlist[userindex].vvi.getURL())
    URLEntry.place(x=345, y=240)

    VentAmpVar = StringVar()
    Label(VVIMode, text='Ventricular Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(
        x=615, y=200)
    VentAmpEntry = Entry(VVIMode, textvariable=VentAmpVar, font=('Times New Roman', 10), width=27)
    VentAmpEntry.insert(0, tempuserlist[userindex].vvi.getVAmp())
    VentAmpEntry.place(x=615, y=240)

    VPWVar = StringVar()
    Label(VVIMode, text='Ventricular Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    VPWEntry = Entry(VVIMode, textvariable=VPWVar, font=('Times New Roman', 10), width=27)
    VPWEntry.insert(0, tempuserlist[userindex].vvi.getVPW())
    VPWEntry.place(x=885, y=240)

    # print(tt)
    VSVar = StringVar()
    Label(VVIMode, text='Ventricular Sensitivity (Unit: mV)', font=('Times New Roman', 10), width=27).place(
        x=75, y=300)
    VSEntry = Entry(VVIMode, textvariable=VSVar, font=('Times New Roman', 10), width=27)
    VSEntry.insert(0, tempuserlist[userindex].vvi.getVS())
    VSEntry.place(x=75, y=340)

    VRPVar = StringVar()
    Label(VVIMode, text='VRP (Unit: ms)', font=('Times New Roman', 10), width=27).place(x=345, y=300)
    VRPEntry = Entry(VVIMode, textvariable=VRPVar, font=('Times New Roman', 10), width=27)
    VRPEntry.insert(0, tempuserlist[userindex].vvi.getVRP())
    VRPEntry.place(x=345, y=340)

    HysteresisVar = StringVar()
    Label(VVIMode, text='Hysteresis (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                y=300)
    HysteresisEntry = Entry(VVIMode, textvariable=HysteresisVar, font=('Times New Roman', 10), width=27)
    HysteresisEntry.insert(0, "Coming Soon")
    HysteresisEntry.place(x=615, y=340)

    RSVar = StringVar()
    Label(VVIMode, text='Rate Smoothing', font=('Times New Roman', 10), width=27).place(x=885, y=300)
    RSEntry = Entry(VVIMode, textvariable=RSVar, font=('Times New Roman', 10), width=27)
    RSEntry.insert(0, "Coming Soon")
    RSEntry.place(x=885, y=340)

    VVIupload = Button(VVIMode, text='upload', activebackground='Purple', bg='Red',
                       font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    VVIupload.place(x=615, y=400)
    send = Button(VVIMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(VVIMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


def ShowAAIParameters():
    global modes
    global tempuserlist
    modes = 3
    AAIMode = Tk()
    AAIMode.title("AAI Mode")
    AAIMode.geometry("1350x900")

    def upload():
        try:
            if (60 / int(ALRLEntry.get()) * 1000 == int(ARPEntry.get())):
                raise ZeroDivisionError
            if (int(ALRLEntry.get()) < int(AURLEntry.get())):
                tempuserlist[userindex].aai.setLRL(ALRLEntry.get())
                tempuserlist[userindex].aai.setURL(AURLEntry.get())
                tempuserlist[userindex].aai.setaAmp(AtrAmpEntry.get())
                tempuserlist[userindex].aai.setAPW(APWEntry.get())
                tempuserlist[userindex].aai.setARP(ARPEntry.get())
                tempuserlist[userindex].aai.setAS(ASEntry.get())
                # print(tempuserlist[userindex].vvi.getLRL())
                # print(tempuserlist[userindex].vvi.getURL())
                # print(tempuserlist[userindex].vvi.getVAmp())
                # print(tempuserlist[userindex].vvi.getVPW())
                # print(tempuserlist[userindex].vvi.getVRP())
                with open('user.pickle', 'wb') as f:
                    for x in tempuserlist:
                        pickle.dump(x, f)
                with open('user.pickle', 'rb') as f:
                    test = pickle.load(f)
                    # test1 = pickle.load(f)
            else:
                raise NameError
        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
        except ZeroDivisionError:
            messagebox.showerror("ERROR", "Time for this LRL equals to VRP")
    

    ALRLVar = StringVar()
    Label(AAIMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                      y=200)
    ALRLEntry = Entry(AAIMode, textvariable=ALRLVar, font=('Times New Roman', 10), width=27)
    ALRLEntry.insert(0, tempuserlist[userindex].aai.getLRL())
    ALRLEntry.place(x=75, y=240)

    AURLVar = StringVar()
    Label(AAIMode, text='Uper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                     y=200)
    AURLEntry = Entry(AAIMode, textvariable=AURLVar, font=('Times New Roman', 10), width=27)
    AURLEntry.insert(0, tempuserlist[userindex].aai.getURL())
    AURLEntry.place(x=345, y=240)

    AtrAmpVar = StringVar()
    Label(AAIMode, text='Atrial Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                    y=200)
    AtrAmpEntry = Entry(AAIMode, textvariable=AtrAmpVar, font=('Times New Roman', 10), width=27)
    AtrAmpEntry.insert(0, tempuserlist[userindex].aai.getaAmp())
    AtrAmpEntry.place(x=615, y=240)

    APWVar = StringVar()
    Label(AAIMode, text='Atrial Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    APWEntry = Entry(AAIMode, textvariable=APWVar, font=('Times New Roman', 10), width=27)
    APWEntry.insert(0, tempuserlist[userindex].aai.getAPW())
    APWEntry.place(x=885, y=240)

    ASVar = StringVar()
    Label(AAIMode, text='Atrial Sensitivity (Unit: mV)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                       y=300)
    ASEntry = Entry(AAIMode, textvariable=ASVar, font=('Times New Roman', 10), width=27)
    ASEntry.insert(0, tempuserlist[userindex].aai.getAS())
    ASEntry.place(x=75, y=340)

    ARPVar = StringVar()
    Label(AAIMode, text='ARP (Unit: ms)', font=('Times New Roman', 10), width=27).place(x=345, y=300)
    ARPEntry = Entry(AAIMode, textvariable=ARPVar, font=('Times New Roman', 10), width=27)
    ARPEntry.insert(0, tempuserlist[userindex].aai.getARP())
    ARPEntry.place(x=345, y=340)

    AHysteresisVar = StringVar()
    Label(AAIMode, text='Hysteresis (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                y=300)
    AHysteresisEntry = Entry(AAIMode, textvariable=AHysteresisVar, font=('Times New Roman', 10), width=27)
    AHysteresisEntry.insert(0, "Coming Soon")
    AHysteresisEntry.place(x=615, y=340)

    ARSVar = StringVar()
    Label(AAIMode, text='Rate Smoothing', font=('Times New Roman', 10), width=27).place(x=885, y=300)
    ARSEntry = Entry(AAIMode, textvariable=ARSVar, font=('Times New Roman', 10), width=27)
    ARSEntry.insert(0, "Coming Soon")
    ARSEntry.place(x=885, y=340)

    AAIupload = Button(AAIMode, text='upload', activebackground='Purple', bg='Red',
                       font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    AAIupload.place(x=615, y=400)
    send = Button(AAIMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(AAIMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)

def ShowAOOParameters():
    global modes
    global tempuserlist
    modes = 1
    AOOMode = Tk()
    AOOMode.title("AOO Mode")
    AOOMode.geometry("1350x900")

    def upload():
        # a=int(AOOALRLEntry.get()
        try:
            a = int(AOOALRLEntry.get())
            b = int(AOOAURLEntry.get())

            if (int(AOOALRLEntry.get()) < int(AOOAURLEntry.get())):
                tempuserlist[userindex].aoo.setLRL(AOOALRLEntry.get())
                tempuserlist[userindex].aoo.setURL(AOOAURLEntry.get())
                tempuserlist[userindex].aoo.setaAmp(AOOAtrAmpEntry.get())
                tempuserlist[userindex].aoo.setAPW(AOOAPWEntry.get())
                print("gg")
                print(AOOALRLEntry.get())
                print(tempuserlist[userindex].aoo.getLRL())
                # print(type(AOOALRLVar.get()))
                # print(tempuserlist[userindex].vvi.getVAmp())
                # print(tempuserlist[userindex].vvi.getVPW())
                # print(tempuserlist[userindex].vvi.getVRP())
                with open('user.pickle', 'wb') as f:
                    for x in tempuserlist:
                        pickle.dump(x, f)
                with open('user.pickle', 'rb') as f:
                    test = pickle.load(f)
                    # test1 = pickle.load(f)

            else:
                raise NameError
        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")

    

    AOOALRLVar = StringVar()
    Label(AOOMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                      y=200)
    AOOALRLEntry = Entry(AOOMode, textvariable=AOOALRLVar, font=('Times New Roman', 10), width=27)
    AOOALRLEntry.insert(0, tempuserlist[userindex].aoo.getLRL())
    AOOALRLEntry.place(x=75, y=240)

    AOOAURLVar = StringVar()
    Label(AOOMode, text='Uper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                     y=200)
    AOOAURLEntry = Entry(AOOMode, textvariable=AOOAURLVar, font=('Times New Roman', 10), width=27)
    AOOAURLEntry.insert(0, tempuserlist[userindex].aoo.getURL())
    AOOAURLEntry.place(x=345, y=240)

    AOOAtrAmpVar = StringVar()
    Label(AOOMode, text='Atrial Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                    y=200)
    AOOAtrAmpEntry = Entry(AOOMode, textvariable=AOOAtrAmpVar, font=('Times New Roman', 10), width=27)
    AOOAtrAmpEntry.insert(0, tempuserlist[userindex].aoo.getaAmp())
    AOOAtrAmpEntry.place(x=615, y=240)

    AOOAPWVar = StringVar()
    Label(AOOMode, text='Atrial Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    AOOAPWEntry = Entry(AOOMode, textvariable=AOOAPWVar, font=('Times New Roman', 10), width=27)
    AOOAPWEntry.insert(0, tempuserlist[userindex].aoo.getAPW())
    AOOAPWEntry.place(x=885, y=240)

    AOOupload = Button(AOOMode, text='upload', activebackground='Purple', bg='Red',
                       font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    AOOupload.place(x=615, y=400)
    send = Button(AOOMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(AOOMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)

def ShowVOOParameters():
    global modes
    global tempuserlist
    modes = 2
    VOOMode = Tk()
    VOOMode.title("VOO Mode")
    VOOMode.geometry("1350x900")

    def upload():
        try:
            if (int(VOOLRLEntry.get()) < int(VOOURLEntry.get())):
                tempuserlist[userindex].voo.setLRL(VOOLRLEntry.get())
                tempuserlist[userindex].voo.setURL(VOOURLEntry.get())
                tempuserlist[userindex].voo.setVAmp(VOOVentAmpEntry.get())
                tempuserlist[userindex].voo.setVPW(VOOVPWEntry.get())
                # print(tempuserlist[userindex].vvi.getLRL())
                # print(tempuserlist[userindex].vvi.getURL())
                # print(tempuserlist[userindex].vvi.getVAmp())
                # print(tempuserlist[userindex].vvi.getVPW())
                # print(tempuserlist[userindex].vvi.getVRP())
                with open('user.pickle', 'wb') as f:
                    for x in tempuserlist:
                        pickle.dump(x, f)
                with open('user.pickle', 'rb') as f:
                    test = pickle.load(f)
                    # test1 = pickle.load(f)
            else:
                raise NameError
        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
    
    VOOLRLVar = StringVar()
    Label(VOOMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                      y=200)
    VOOLRLEntry = Entry(VOOMode, textvariable=VOOLRLVar, font=('Times New Roman', 10), width=27)
    VOOLRLEntry.insert(0, tempuserlist[userindex].voo.getLRL())
    VOOLRLEntry.place(x=75, y=240)

    VOOURLVar = StringVar()
    Label(VOOMode, text='Uper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                     y=200)
    VOOURLEntry = Entry(VOOMode, textvariable=VOOURLVar, font=('Times New Roman', 10), width=27)
    VOOURLEntry.insert(0, tempuserlist[userindex].voo.getURL())
    VOOURLEntry.place(x=345, y=240)

    VOOVentAmpVar = StringVar()
    Label(VOOMode, text='Ventricular Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(
        x=615, y=200)
    VOOVentAmpEntry = Entry(VOOMode, textvariable=VOOVentAmpVar, font=('Times New Roman', 10), width=27)
    VOOVentAmpEntry.insert(0, tempuserlist[userindex].voo.getVAmp())
    VOOVentAmpEntry.place(x=615, y=240)

    VOOVPWVar = StringVar()
    Label(VOOMode, text='Ventricular Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    VOOVPWEntry = Entry(VOOMode, textvariable=VOOVPWVar, font=('Times New Roman', 10), width=27)
    VOOVPWEntry.insert(0, tempuserlist[userindex].voo.getVPW())
    VOOVPWEntry.place(x=885, y=240)

    VOOupload = Button(VOOMode, text='upload', activebackground='Purple', bg='Red',
                       font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    VOOupload.place(x=615, y=400)
    Canvas(VOOMode, height=70, width=1500, bd=0).place(x=75, y=300)
    send = Button(VOOMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(VOOMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


def ShowDOOParameters():
    global modes
    global tempuserlist
    modes = 5
    DOOMode = Tk()
    DOOMode.title("DOO Mode")
    DOOMode.geometry("1350x900")

    def upload():
        try:
            if (int(DOOLRLEntry.get()) < int(DOOURLEntry.get())):
                tempuserlist[userindex].doo.setLRL(DOOLRLEntry.get())
                tempuserlist[userindex].doo.setURL(DOOURLEntry.get())
                tempuserlist[userindex].doo.setVAmp(VentAmpEntry.get())
                tempuserlist[userindex].doo.setVPW(VPWEntry.get())
                tempuserlist[userindex].doo.setaAmp(AtrAmpEntry.get())
                tempuserlist[userindex].doo.setAPW(APWEntry.get())
                tempuserlist[userindex].doo.setFAD(FADEntry.get())
                # print(tempuserlist[userindex].vvi.getLRL())
                # print(tempuserlist[userindex].vvi.getURL())
                # print(tempuserlist[userindex].vvi.getvAmp())
                # print(tempuserlist[userindex].vvi.getVPW())
                # print(tempuserlist[userindex].vvi.getVRP())
                with open('user.pickle', 'wb') as f:
                    for x in tempuserlist:
                        pickle.dump(x, f)
                with open('user.pickle', 'rb') as f:
                    test = pickle.load(f)
                    # test1 = pickle.load(f)
            else:
                raise NameError
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
    
    DOOLRLVar = StringVar()
    Label(DOOMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                      y=200)
    DOOLRLEntry = Entry(DOOMode, textvariable=DOOLRLVar, font=('Times New Roman', 10), width=27)
    DOOLRLEntry.insert(0, tempuserlist[userindex].doo.getLRL())
    DOOLRLEntry.place(x=75, y=240)

    DOOURLVar = StringVar()
    Label(DOOMode, text='Upper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                      y=200)
    DOOURLEntry = Entry(DOOMode, textvariable=DOOURLVar, font=('Times New Roman', 10), width=27)
    DOOURLEntry.insert(0, tempuserlist[userindex].doo.getURL())
    DOOURLEntry.place(x=345, y=240)

    VentAmpVar = StringVar()
    Label(DOOMode, text='Ventricular Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(
        x=615, y=200)
    VentAmpEntry = Entry(DOOMode, textvariable=VentAmpVar, font=('Times New Roman', 10), width=27)
    VentAmpEntry.insert(0, tempuserlist[userindex].doo.getvAmp())
    VentAmpEntry.place(x=615, y=240)

    VPWVar = StringVar()
    Label(DOOMode, text='Ventricular Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    VPWEntry = Entry(DOOMode, textvariable=VPWVar, font=('Times New Roman', 10), width=27)
    VPWEntry.insert(0, tempuserlist[userindex].doo.getVPW())
    VPWEntry.place(x=885, y=240)

    AtrAmpVar = StringVar()
    Label(DOOMode, text='Atrial Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                    y=300)
    AtrAmpEntry = Entry(DOOMode, textvariable=AtrAmpVar, font=('Times New Roman', 10), width=27)
    AtrAmpEntry.insert(0, tempuserlist[userindex].doo.getaAmp())
    AtrAmpEntry.place(x=75, y=340)

    APWVar = StringVar()
    Label(DOOMode, text='Atrial Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=345, y=300)
    APWEntry = Entry(DOOMode, textvariable=APWVar, font=('Times New Roman', 10), width=27)
    APWEntry.insert(0, tempuserlist[userindex].doo.getAPW())
    APWEntry.place(x=345, y=340)

    FADVar = StringVar()
    Label(DOOMode, text='Fixed AV Delay (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=615, y=300)
    FADEntry = Entry(DOOMode, textvariable=FADVar, font=('Times New Roman', 10), width=27)
    FADEntry.insert(0, tempuserlist[userindex].doo.getFAD())
    FADEntry.place(x=615, y=340)

    DOOupload = Button(DOOMode, text='upload', activebackground='Purple', bg='Red',
                       font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    DOOupload.place(x=615, y=400)
    send = Button(DOOMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(DOOMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


def ShowDOORParameters():
    global modes
    global tempuserlist
    modes = 6
    DOORMode = Tk()
    DOORMode.title("DOOR Mode")
    DOORMode.geometry("1350x900")

    def upload():
        try:
            if (int(DOOLRLEntry.get()) >= int(DOOURLEntry.get())):
                raise NameError
            if (int(MSREntry.get()) > int(DOOURLEntry.get())):
                raise AssertionError
            if (int(MSREntry.get()) <= int(DOOLRLEntry.get())):
                raise IndentationError
            tempuserlist[userindex].door.setLRL(DOOLRLEntry.get())
            tempuserlist[userindex].door.setURL(DOOURLEntry.get())
            tempuserlist[userindex].door.setVAmp(VentAmpEntry.get())
            tempuserlist[userindex].door.setVPW(VPWEntry.get())
            tempuserlist[userindex].door.setaAmp(AtrAmpEntry.get())
            tempuserlist[userindex].door.setAPW(APWEntry.get())
            tempuserlist[userindex].door.setFAD(FADEntry.get())
            tempuserlist[userindex].door.setMSR(MSREntry.get())
            tempuserlist[userindex].door.setReactionT(ReactionTEntry.get())
            tempuserlist[userindex].door.setRF(RFEntry.get())
            tempuserlist[userindex].door.setRecoveryT(RecoveryTEntry.get())

            with open('user.pickle', 'wb') as f:
                for x in tempuserlist:
                    pickle.dump(x, f)
            with open('user.pickle', 'rb') as f:
                test = pickle.load(f)
                # test1 = pickle.load(f)

        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except AssertionError:
            messagebox.showerror("ERROR", "MSR must be lower than upper rate limit")
        except IndentationError:
            messagebox.showerror("ERROR", "MSR must be higher than lower rate limit")

    

    DOOLRLVar = StringVar()
    Label(DOORMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                       y=200)
    DOOLRLEntry = Entry(DOORMode, textvariable=DOOLRLVar, font=('Times New Roman', 10), width=27)
    DOOLRLEntry.insert(0, tempuserlist[userindex].door.getLRL())
    DOOLRLEntry.place(x=75, y=240)

    DOOURLVar = StringVar()
    Label(DOORMode, text='Upper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                       y=200)
    DOOURLEntry = Entry(DOORMode, textvariable=DOOURLVar, font=('Times New Roman', 10), width=27)
    DOOURLEntry.insert(0, tempuserlist[userindex].door.getURL())
    DOOURLEntry.place(x=345, y=240)

    VentAmpVar = StringVar()
    Label(DOORMode, text='Ventricular Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(
        x=615, y=200)
    VentAmpEntry = Entry(DOORMode, textvariable=VentAmpVar, font=('Times New Roman', 10), width=27)
    VentAmpEntry.insert(0, tempuserlist[userindex].door.getvAmp())
    VentAmpEntry.place(x=615, y=240)

    VPWVar = StringVar()
    Label(DOORMode, text='Ventricular Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    VPWEntry = Entry(DOORMode, textvariable=VPWVar, font=('Times New Roman', 10), width=27)
    VPWEntry.insert(0, tempuserlist[userindex].door.getVPW())
    VPWEntry.place(x=885, y=240)

    AtrAmpVar = StringVar()
    Label(DOORMode, text='Atrial Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                     y=300)
    AtrAmpEntry = Entry(DOORMode, textvariable=AtrAmpVar, font=('Times New Roman', 10), width=27)
    AtrAmpEntry.insert(0, tempuserlist[userindex].door.getaAmp())
    AtrAmpEntry.place(x=75, y=340)

    APWVar = StringVar()
    Label(DOORMode, text='Atrial Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=345, y=300)
    APWEntry = Entry(DOORMode, textvariable=APWVar, font=('Times New Roman', 10), width=27)
    APWEntry.insert(0, tempuserlist[userindex].door.getAPW())
    APWEntry.place(x=345, y=340)

    FADVar = StringVar()
    Label(DOORMode, text='Fixed AV Delay (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=615, y=300)
    FADEntry = Entry(DOORMode, textvariable=FADVar, font=('Times New Roman', 10), width=27)
    FADEntry.insert(0, tempuserlist[userindex].door.getFAD())
    FADEntry.place(x=615, y=340)

    MSRVar = StringVar()
    Label(DOORMode, text='Maximun Sensor rate (Unit: ppm)', font=('Times New Roman', 10), width=27).place(
        x=885, y=300)
    MSREntry = Entry(DOORMode, textvariable=MSRVar, font=('Times New Roman', 10), width=27)
    MSREntry.insert(0, tempuserlist[userindex].door.getMSR())
    MSREntry.place(x=885, y=340)

    ReactionTVar = StringVar()
    Label(DOORMode, text='Reaction Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=75, y=400)
    ReactionTEntry = Entry(DOORMode, textvariable=ReactionTVar, font=('Times New Roman', 10), width=27)
    ReactionTEntry.insert(0, tempuserlist[userindex].door.getReactionT())
    ReactionTEntry.place(x=75, y=440)

    RFVar = StringVar()
    Label(DOORMode, text='Response Factor ', font=('Times New Roman', 10), width=27).place(
        x=345, y=400)
    RFEntry = Entry(DOORMode, textvariable=RFVar, font=('Times New Roman', 10), width=27)
    RFEntry.insert(0, tempuserlist[userindex].door.getRF())
    RFEntry.place(x=345, y=440)

    RecoveryTVar = StringVar()
    Label(DOORMode, text='Recovery Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=615, y=400)
    RecoveryTEntry = Entry(DOORMode, textvariable=RecoveryTVar, font=('Times New Roman', 10), width=27)
    RecoveryTEntry.insert(0, tempuserlist[userindex].door.getRecoveryT())
    RecoveryTEntry.place(x=615, y=440)

    DOORupload = Button(DOORMode, text='upload', activebackground='Purple', bg='Red',
                        font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    DOORupload.place(x=885, y=400)
    send = Button(DOORMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(DOORMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


# global tt


def ShowAOORParameters():
    global modes
    global tempuserlist
    modes = 9
    AOORMode = Tk()
    AOORMode.title("AOOR Mode")
    AOORMode.geometry("1350x900")

    def upload():
        try:
            if (int(DOOLRLEntry.get()) >= int(DOOURLEntry.get())):
                raise NameError
            if (int(MSREntry.get()) > int(DOOURLEntry.get())):
                raise AssertionError
            if (int(MSREntry.get()) <= int(DOOLRLEntry.get())):
                raise IndentationError
            tempuserlist[userindex].aoor.setLRL(DOOLRLEntry.get())
            tempuserlist[userindex].aoor.setURL(DOOURLEntry.get())
            tempuserlist[userindex].aoor.setaAmp(AtrAmpEntry.get())
            tempuserlist[userindex].aoor.setAPW(APWEntry.get())
            tempuserlist[userindex].aoor.setMSR(MSREntry.get())
            tempuserlist[userindex].aoor.setReactionT(ReactionTEntry.get())
            tempuserlist[userindex].aoor.setRF(RFEntry.get())
            tempuserlist[userindex].aoor.setRecoveryT(RecoveryTEntry.get())

            with open('user.pickle', 'wb') as f:
                for x in tempuserlist:
                    pickle.dump(x, f)
            with open('user.pickle', 'rb') as f:
                test = pickle.load(f)
                # test1 = pickle.load(f)
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")

        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except AssertionError:
            messagebox.showerror("ERROR", "MSR must be lower than upper rate limit")
        except IndentationError:
            messagebox.showerror("ERROR", "MSR must be higher than lower rate limit")

    DOOLRLVar = StringVar()
    Label(AOORMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                       y=200)
    DOOLRLEntry = Entry(AOORMode, textvariable=DOOLRLVar, font=('Times New Roman', 10), width=27)
    DOOLRLEntry.insert(0, tempuserlist[userindex].aoor.getLRL())
    DOOLRLEntry.place(x=75, y=240)

    DOOURLVar = StringVar()
    Label(AOORMode, text='Upper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                       y=200)
    DOOURLEntry = Entry(AOORMode, textvariable=DOOURLVar, font=('Times New Roman', 10), width=27)
    DOOURLEntry.insert(0, tempuserlist[userindex].aoor.getURL())
    DOOURLEntry.place(x=345, y=240)

    AtrAmpVar = StringVar()
    Label(AOORMode, text='Atrial Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                     y=200)
    AtrAmpEntry = Entry(AOORMode, textvariable=AtrAmpVar, font=('Times New Roman', 10), width=27)
    AtrAmpEntry.insert(0, tempuserlist[userindex].aoor.getaAmp())
    AtrAmpEntry.place(x=615, y=240)

    APWVar = StringVar()
    Label(AOORMode, text='Atrial Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    APWEntry = Entry(AOORMode, textvariable=APWVar, font=('Times New Roman', 10), width=27)
    APWEntry.insert(0, tempuserlist[userindex].aoor.getAPW())
    APWEntry.place(x=885, y=240)

    MSRVar = StringVar()
    Label(AOORMode, text='Maximun Sensor rate (Unit: ppm)', font=('Times New Roman', 10), width=27).place(
        x=75, y=300)
    MSREntry = Entry(AOORMode, textvariable=MSRVar, font=('Times New Roman', 10), width=27)
    MSREntry.insert(0, tempuserlist[userindex].aoor.getMSR())
    MSREntry.place(x=75, y=340)

    ReactionTVar = StringVar()
    Label(AOORMode, text='Reaction Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=345, y=300)
    ReactionTEntry = Entry(AOORMode, textvariable=ReactionTVar, font=('Times New Roman', 10), width=27)
    ReactionTEntry.insert(0, tempuserlist[userindex].aoor.getReactionT())
    ReactionTEntry.place(x=345, y=340)

    RFVar = StringVar()
    Label(AOORMode, text='Response Factor ', font=('Times New Roman', 10), width=27).place(
        x=615, y=300)
    RFEntry = Entry(AOORMode, textvariable=RFVar, font=('Times New Roman', 10), width=27)
    RFEntry.insert(0, tempuserlist[userindex].aoor.getRF())
    RFEntry.place(x=615, y=340)

    RecoveryTVar = StringVar()
    Label(AOORMode, text='Recovery Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=885, y=300)
    RecoveryTEntry = Entry(AOORMode, textvariable=RecoveryTVar, font=('Times New Roman', 10), width=27)
    RecoveryTEntry.insert(0, tempuserlist[userindex].aoor.getRecoveryT())
    RecoveryTEntry.place(x=885, y=340)

    AOORupload = Button(AOORMode, text='upload', activebackground='Purple', bg='Red',
                        font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    AOORupload.place(x=885, y=400)
    send = Button(AOORMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(AOORMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


def ShowVOORParameters():
    global modes
    global tempuserlist
    modes = 10
    VOORMode = Tk()
    VOORMode.title("VOOR Mode")
    VOORMode.geometry("1350x900")

    def upload():
        try:
            if (int(DOOLRLEntry.get()) >= int(DOOURLEntry.get())):
                raise NameError
            if (int(MSREntry.get()) > int(DOOURLEntry.get())):
                raise AssertionError
            if (int(MSREntry.get()) <= int(DOOLRLEntry.get())):
                raise IndentationError
            tempuserlist[userindex].voor.setLRL(DOOLRLEntry.get())
            tempuserlist[userindex].voor.setURL(DOOURLEntry.get())
            tempuserlist[userindex].voor.setVAmp(AtrAmpEntry.get())
            tempuserlist[userindex].voor.setVPW(APWEntry.get())
            tempuserlist[userindex].voor.setMSR(MSREntry.get())
            tempuserlist[userindex].voor.setReactionT(ReactionTEntry.get())
            tempuserlist[userindex].voor.setRF(RFEntry.get())
            tempuserlist[userindex].voor.setRecoveryT(RecoveryTEntry.get())
            # print(tempuserlist[userindex].vvi.getLRL())
            # print(tempuserlist[userindex].vvi.getURL())
            # print(tempuserlist[userindex].vvi.getvAmp())
            # print(tempuserlist[userindex].vvi.getVPW())
            # print(tempuserlist[userindex].vvi.getVRP())
            with open('user.pickle', 'wb') as f:
                for x in tempuserlist:
                    pickle.dump(x, f)
            with open('user.pickle', 'rb') as f:
                test = pickle.load(f)
                # test1 = pickle.load(f)


        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
        except AssertionError:
            messagebox.showerror("ERROR", "MSR must be lower than upper rate limit")
        except IndentationError:
            messagebox.showerror("ERROR", "MSR must be higher than lower rate limit")

    

    DOOLRLVar = StringVar()
    Label(VOORMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                       y=200)
    DOOLRLEntry = Entry(VOORMode, textvariable=DOOLRLVar, font=('Times New Roman', 10), width=27)
    DOOLRLEntry.insert(0, tempuserlist[userindex].voor.getLRL())
    DOOLRLEntry.place(x=75, y=240)

    DOOURLVar = StringVar()
    Label(VOORMode, text='Upper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                       y=200)
    DOOURLEntry = Entry(VOORMode, textvariable=DOOURLVar, font=('Times New Roman', 10), width=27)
    DOOURLEntry.insert(0, tempuserlist[userindex].voor.getURL())
    DOOURLEntry.place(x=345, y=240)

    AtrAmpVar = StringVar()
    Label(VOORMode, text='Ventricular Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                          y=200)
    AtrAmpEntry = Entry(VOORMode, textvariable=AtrAmpVar, font=('Times New Roman', 10), width=27)
    AtrAmpEntry.insert(0, tempuserlist[userindex].voor.getvAmp())
    AtrAmpEntry.place(x=615, y=240)

    APWVar = StringVar()
    Label(VOORMode, text='Ventricular Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    APWEntry = Entry(VOORMode, textvariable=APWVar, font=('Times New Roman', 10), width=27)
    APWEntry.insert(0, tempuserlist[userindex].voor.getVPW())
    APWEntry.place(x=885, y=240)

    MSRVar = StringVar()
    Label(VOORMode, text='Maximun Sensor rate (Unit: ppm)', font=('Times New Roman', 10), width=27).place(
        x=75, y=300)
    MSREntry = Entry(VOORMode, textvariable=MSRVar, font=('Times New Roman', 10), width=27)
    MSREntry.insert(0, tempuserlist[userindex].voor.getMSR())
    MSREntry.place(x=75, y=340)

    ReactionTVar = StringVar()
    Label(VOORMode, text='Reaction Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=345, y=300)
    ReactionTEntry = Entry(VOORMode, textvariable=ReactionTVar, font=('Times New Roman', 10), width=27)
    ReactionTEntry.insert(0, tempuserlist[userindex].voor.getReactionT())
    ReactionTEntry.place(x=345, y=340)

    RFVar = StringVar()
    Label(VOORMode, text='Response Factor ', font=('Times New Roman', 10), width=27).place(
        x=615, y=300)
    RFEntry = Entry(VOORMode, textvariable=RFVar, font=('Times New Roman', 10), width=27)
    RFEntry.insert(0, tempuserlist[userindex].voor.getRF())
    RFEntry.place(x=615, y=340)

    RecoveryTVar = StringVar()
    Label(VOORMode, text='Recovery Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=885, y=300)
    RecoveryTEntry = Entry(VOORMode, textvariable=RecoveryTVar, font=('Times New Roman', 10), width=27)
    RecoveryTEntry.insert(0, tempuserlist[userindex].voor.getRecoveryT())
    RecoveryTEntry.place(x=885, y=340)

    VOORupload = Button(VOORMode, text='upload', activebackground='Purple', bg='Red',
                        font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    VOORupload.place(x=885, y=400)
    send = Button(VOORMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(VOORMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


def ShowAAIRParameters():
    global modes
    global tempuserlist
    modes = 7
    AAIRMode = Tk()
    AAIRMode.title("AAIR Mode")
    AAIRMode.geometry("1350x900")

    def upload():
        try:
            if (int(MSREntry.get()) > int(DOOURLEntry.get())):
                raise AssertionError
            if (int(MSREntry.get()) <= int(DOOLRLEntry.get())):
                raise IndentationError
            if (60 / int(DOOLRLEntry.get()) * 1000 == int(ARPEntry.get())):
                raise ZeroDivisionError
            if (int(DOOLRLEntry.get()) >= int(DOOURLEntry.get())):
                raise NameError
            tempuserlist[userindex].aair.setLRL(DOOLRLEntry.get())
            tempuserlist[userindex].aair.setURL(DOOURLEntry.get())
            tempuserlist[userindex].aair.setaAmp(AtrAmpEntry.get())
            tempuserlist[userindex].aair.setAPW(APWEntry.get())
            tempuserlist[userindex].aair.setMSR(MSREntry.get())
            tempuserlist[userindex].aair.setReactionT(ReactionTEntry.get())
            tempuserlist[userindex].aair.setRF(RFEntry.get())
            tempuserlist[userindex].aair.setRecoveryT(RecoveryTEntry.get())
            tempuserlist[userindex].aair.setARP(ARPEntry.get())
            tempuserlist[userindex].aair.setAS(ASEntry.get())
            # print(tempuserlist[userindex].vvi.getLRL())
            # print(tempuserlist[userindex].vvi.getURL())
            # print(tempuserlist[userindex].vvi.getvAmp())
            # print(tempuserlist[userindex].vvi.getVPW())
            # print(tempuserlist[userindex].vvi.getVRP())
            with open('user.pickle', 'wb') as f:
                for x in tempuserlist:
                    pickle.dump(x, f)
            with open('user.pickle', 'rb') as f:
                test = pickle.load(f)
                # test1 = pickle.load(f)


        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
        except ZeroDivisionError:
            messagebox.showerror("ERROR", "Time for this LRL equals to VRP")
        except AssertionError:
            messagebox.showerror("ERROR", "MSR must be lower than upper rate limit")
        except IndentationError:
            messagebox.showerror("ERROR", "MSR must be higher than lower rate limit")
    

    DOOLRLVar = StringVar()
    Label(AAIRMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                       y=200)
    DOOLRLEntry = Entry(AAIRMode, textvariable=DOOLRLVar, font=('Times New Roman', 10), width=27)
    DOOLRLEntry.insert(0, tempuserlist[userindex].aair.getLRL())
    DOOLRLEntry.place(x=75, y=240)

    DOOURLVar = StringVar()
    Label(AAIRMode, text='Upper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                       y=200)
    DOOURLEntry = Entry(AAIRMode, textvariable=DOOURLVar, font=('Times New Roman', 10), width=27)
    DOOURLEntry.insert(0, tempuserlist[userindex].aair.getURL())
    DOOURLEntry.place(x=345, y=240)

    AtrAmpVar = StringVar()
    Label(AAIRMode, text='Atrial Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                     y=200)
    AtrAmpEntry = Entry(AAIRMode, textvariable=AtrAmpVar, font=('Times New Roman', 10), width=27)
    AtrAmpEntry.insert(0, tempuserlist[userindex].aair.getaAmp())
    AtrAmpEntry.place(x=615, y=240)

    APWVar = StringVar()
    Label(AAIRMode, text='Atrial Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    APWEntry = Entry(AAIRMode, textvariable=APWVar, font=('Times New Roman', 10), width=27)
    APWEntry.insert(0, tempuserlist[userindex].aair.getAPW())
    APWEntry.place(x=885, y=240)

    MSRVar = StringVar()
    Label(AAIRMode, text='Maximun Sensor rate (Unit: ppm)', font=('Times New Roman', 10), width=27).place(
        x=75, y=300)
    MSREntry = Entry(AAIRMode, textvariable=MSRVar, font=('Times New Roman', 10), width=27)
    MSREntry.insert(0, tempuserlist[userindex].aair.getMSR())
    MSREntry.place(x=75, y=340)

    ReactionTVar = StringVar()
    Label(AAIRMode, text='Reaction Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=345, y=300)
    ReactionTEntry = Entry(AAIRMode, textvariable=ReactionTVar, font=('Times New Roman', 10), width=27)
    ReactionTEntry.insert(0, tempuserlist[userindex].aair.getReactionT())
    ReactionTEntry.place(x=345, y=340)

    RFVar = StringVar()
    Label(AAIRMode, text='Response Factor ', font=('Times New Roman', 10), width=27).place(
        x=615, y=300)
    RFEntry = Entry(AAIRMode, textvariable=RFVar, font=('Times New Roman', 10), width=27)
    RFEntry.insert(0, tempuserlist[userindex].aair.getRF())
    RFEntry.place(x=615, y=340)

    RecoveryTVar = StringVar()
    Label(AAIRMode, text='Recovery Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=885, y=300)
    RecoveryTEntry = Entry(AAIRMode, textvariable=RecoveryTVar, font=('Times New Roman', 10), width=27)
    RecoveryTEntry.insert(0, tempuserlist[userindex].aair.getRecoveryT())
    RecoveryTEntry.place(x=885, y=340)

    ARPVar = StringVar()
    Label(AAIRMode, text='ARP (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=75, y=400)
    ARPEntry = Entry(AAIRMode, textvariable=ARPVar, font=('Times New Roman', 10), width=27)
    ARPEntry.insert(0, tempuserlist[userindex].aair.getARP())
    ARPEntry.place(x=75, y=440)

    ASVar = StringVar()
    Label(AAIRMode, text='Atrial Sensitivity (Unit: mV)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                        y=400)
    ASEntry = Entry(AAIRMode, textvariable=ASVar, font=('Times New Roman', 10), width=27)
    ASEntry.insert(0, tempuserlist[userindex].aair.getAS())
    ASEntry.place(x=345, y=440)

    AAIRupload = Button(AAIRMode, text='upload', activebackground='Purple', bg='Red',
                        font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    AAIRupload.place(x=885, y=400)
    send = Button(AAIRMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(AAIRMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


def ShowVVIRParameters():
    global modes
    global tempuserlist
    modes = 8
    VVIRMode = Tk()
    VVIRMode.title("VVIR Mode")
    VVIRMode.geometry("1350x900")

    def upload():
        try:
            if (int(MSREntry.get()) > int(DOOURLEntry.get())):
                raise AssertionError
            if (int(MSREntry.get()) <= int(DOOLRLEntry.get())):
                raise IndentationError
            if (60 / int(DOOLRLEntry.get()) * 1000 == int(VRPEntry.get())):
                raise ZeroDivisionError
            if (int(DOOLRLEntry.get()) >= int(DOOURLEntry.get())):
                raise NameError
            tempuserlist[userindex].vvir.setLRL(DOOLRLEntry.get())
            tempuserlist[userindex].vvir.setURL(DOOURLEntry.get())
            tempuserlist[userindex].vvir.setVAmp(AtrAmpEntry.get())
            tempuserlist[userindex].vvir.setVPW(APWEntry.get())
            tempuserlist[userindex].vvir.setMSR(MSREntry.get())
            tempuserlist[userindex].vvir.setReactionT(ReactionTEntry.get())
            tempuserlist[userindex].vvir.setRF(RFEntry.get())
            tempuserlist[userindex].vvir.setRecoveryT(RecoveryTEntry.get())
            tempuserlist[userindex].vvir.setVRP(VRPEntry.get())
            tempuserlist[userindex].vvir.setVS(VSEntry.get())
            # print(tempuserlist[userindex].vvi.getLRL())
            # print(tempuserlist[userindex].vvi.getURL())
            # print(tempuserlist[userindex].vvi.getvAmp())
            # print(tempuserlist[userindex].vvi.getVPW())
            # print(tempuserlist[userindex].vvi.getVRP())
            with open('user.pickle', 'wb') as f:
                for x in tempuserlist:
                    pickle.dump(x, f)
            with open('user.pickle', 'rb') as f:
                test = pickle.load(f)
                # test1 = pickle.load(f)


        except TypeError:
            messagebox.showerror("ERROR", "Invalid data type")
        except IndexError:
            messagebox.showerror("ERROR", "Data Value out of range")
        except NameError:
            messagebox.showerror("ERROR", "Lower rate limit needs to be smaller than upper rate limit ")
        except ZeroDivisionError:
            messagebox.showerror("ERROR", "Time for this LRL equals to VRP")
        except AssertionError:
            messagebox.showerror("ERROR", "MSR must be lower than upper rate limit")
        except IndentationError:
            messagebox.showerror("ERROR", "MSR must be higher than lower rate limit")
    
    DOOLRLVar = StringVar()
    Label(VVIRMode, text='Lower Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=75,
                                                                                                       y=200)
    DOOLRLEntry = Entry(VVIRMode, textvariable=DOOLRLVar, font=('Times New Roman', 10), width=27)
    DOOLRLEntry.insert(0, tempuserlist[userindex].vvir.getLRL())
    DOOLRLEntry.place(x=75, y=240)

    DOOURLVar = StringVar()
    Label(VVIRMode, text='Upper Rate Limit (Unit: ppm)', font=('Times New Roman', 10), width=27).place(x=345,
                                                                                                       y=200)
    DOOURLEntry = Entry(VVIRMode, textvariable=DOOURLVar, font=('Times New Roman', 10), width=27)
    DOOURLEntry.insert(0, tempuserlist[userindex].vvir.getURL())
    DOOURLEntry.place(x=345, y=240)

    AtrAmpVar = StringVar()
    Label(VVIRMode, text='Ventricular Amplitude (Unit: V)', font=('Times New Roman', 10), width=27).place(x=615,
                                                                                                          y=200)
    AtrAmpEntry = Entry(VVIRMode, textvariable=AtrAmpVar, font=('Times New Roman', 10), width=27)
    AtrAmpEntry.insert(0, tempuserlist[userindex].vvir.getVAmp())
    AtrAmpEntry.place(x=615, y=240)

    APWVar = StringVar()
    Label(VVIRMode, text='Ventricular Pulse Width (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=885, y=200)
    APWEntry = Entry(VVIRMode, textvariable=APWVar, font=('Times New Roman', 10), width=27)
    APWEntry.insert(0, tempuserlist[userindex].vvir.getVPW())
    APWEntry.place(x=885, y=240)

    MSRVar = StringVar()
    Label(VVIRMode, text='Maximun Sensor rate (Unit: ppm)', font=('Times New Roman', 10), width=27).place(
        x=75, y=300)
    MSREntry = Entry(VVIRMode, textvariable=MSRVar, font=('Times New Roman', 10), width=27)
    MSREntry.insert(0, tempuserlist[userindex].vvir.getMSR())
    MSREntry.place(x=75, y=340)

    ReactionTVar = StringVar()
    Label(VVIRMode, text='Reaction Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=345, y=300)
    ReactionTEntry = Entry(VVIRMode, textvariable=ReactionTVar, font=('Times New Roman', 10), width=27)
    ReactionTEntry.insert(0, tempuserlist[userindex].vvir.getReactionT())
    ReactionTEntry.place(x=345, y=340)

    RFVar = StringVar()
    Label(VVIRMode, text='Response Factor ', font=('Times New Roman', 10), width=27).place(
        x=615, y=300)
    RFEntry = Entry(VVIRMode, textvariable=RFVar, font=('Times New Roman', 10), width=27)
    RFEntry.insert(0, tempuserlist[userindex].vvir.getRF())
    RFEntry.place(x=615, y=340)

    RecoveryTVar = StringVar()
    Label(VVIRMode, text='Recovery Time (Unit: sec)', font=('Times New Roman', 10), width=27).place(
        x=885, y=300)
    RecoveryTEntry = Entry(VVIRMode, textvariable=RecoveryTVar, font=('Times New Roman', 10), width=27)
    RecoveryTEntry.insert(0, tempuserlist[userindex].vvir.getRecoveryT())
    RecoveryTEntry.place(x=885, y=340)

    VRPVar = StringVar()
    Label(VVIRMode, text='VRP (Unit: ms)', font=('Times New Roman', 10), width=27).place(
        x=75, y=400)
    VRPEntry = Entry(VVIRMode, textvariable=VRPVar, font=('Times New Roman', 10), width=27)
    VRPEntry.insert(0, tempuserlist[userindex].vvir.getVRP())
    VRPEntry.place(x=75, y=440)

    VSVar = StringVar()
    Label(VVIRMode, text='Ventricular Sensitivity (Unit: mV)', font=('Times New Roman', 10), width=27).place(
        x=345, y=400)
    VSEntry = Entry(VVIRMode, textvariable=VSVar, font=('Times New Roman', 10), width=27)
    VSEntry.insert(0, tempuserlist[userindex].vvir.getVS())
    VSEntry.place(x=345, y=440)

    VVIRupload = Button(VVIRMode, text='upload', activebackground='Purple', bg='Red',
                        font=('Times New Roman', 19), padx=15, pady=8, command=upload)
    VVIRupload.place(x=615, y=400)
    send = Button(VVIRMode, text='send', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=serial_send)
    send.place(x=615, y=500)
    plot = Button(VVIRMode, text='EGRAM', activebackground='Purple', bg='Red',
                  font=('Times New Roman', 19), padx=15, pady=8, command=egram)
    plot.place(x=75, y=500)


# global tt
# def create mode selection interface
def ModeInterface():
    global tempuserlist
    global ports
    global ser
    # serial_int()
    # global tt

    # tt=[]
    # tt.append(1)
    # tt.append(2)
    ModeSelectionWindow = Tk()
    ModeSelectionWindow.title("PaceMaker Modes For  " + str(tempuserlist[userindex].getUN()))
    ModeSelectionWindow.geometry('1350x900')
    Label(ModeSelectionWindow, font=('Times New Roman', 40), text="MODES SELECTION", ).place(x=75, y=20)

    ###print(tempuserlist[userindex].aoo.getLRL())
    # print(tt)

    VVIModeButton = Button(ModeSelectionWindow, text='VVI', activebackground='LightBlue', bg='Blue',
                           font=('Times New Roman', 19), padx=15, pady=8, command=ShowVVIParameters)
    VVIModeButton.place(x=75, y=100)
    AAIModeButton = Button(ModeSelectionWindow, text='AAI', activebackground='LightBlue', bg='Blue',
                           font=('Times New Roman', 19), padx=15, pady=8, command=ShowAAIParameters)
    AAIModeButton.place(x=345, y=100)
    AOOModeButton = Button(ModeSelectionWindow, text='AOO', activebackground='LightBlue', bg='Blue',
                           font=('Times New Roman', 19), padx=15, pady=8, command=ShowAOOParameters)
    AOOModeButton.place(x=615, y=100)
    VOOModeButton = Button(ModeSelectionWindow, text='VOO', activebackground='LightBlue', bg='Blue',
                           font=('Times New Roman', 19), padx=15, pady=8, command=ShowVOOParameters)
    VOOModeButton.place(x=885, y=100)
    DOOModeButton = Button(ModeSelectionWindow, text='DOO', activebackground='LightBlue', bg='Blue',
                           font=('Times New Roman', 19), padx=15, pady=8, command=ShowDOOParameters)
    DOOModeButton.place(x=75, y=200)
    AOORModeButton = Button(ModeSelectionWindow, text='AOOR', activebackground='LightBlue', bg='Blue',
                            font=('Times New Roman', 19), padx=15, pady=8, command=ShowAOORParameters)
    AOORModeButton.place(x=345, y=200)
    VOORModeButton = Button(ModeSelectionWindow, text='VOOR', activebackground='LightBlue', bg='Blue',
                            font=('Times New Roman', 19), padx=15, pady=8, command=ShowVOORParameters)
    VOORModeButton.place(x=615, y=200)
    AAIRModeButton = Button(ModeSelectionWindow, text='AAIR', activebackground='LightBlue', bg='Blue',
                            font=('Times New Roman', 19), padx=15, pady=8, command=ShowAAIRParameters)
    AAIRModeButton.place(x=885, y=200)
    VVIRModeButton = Button(ModeSelectionWindow, text='VVIR', activebackground='LightBlue', bg='Blue',
                            font=('Times New Roman', 19), padx=15, pady=8, command=ShowVVIRParameters)
    VVIRModeButton.place(x=75, y=300)
    DOORModeButton = Button(ModeSelectionWindow, text='DOOR', activebackground='LightBlue', bg='Blue',
                            font=('Times New Roman', 19), padx=15, pady=8, command=ShowDOORParameters)
    DOORModeButton.place(x=345, y=300)
    SerialComState = StringVar()
    SerialComStatel = Label(ModeSelectionWindow, bg='yellow', width=40, text='', font=('Times New Roman', 10))
    SerialComStatel.place(x=75, y=400)

    '''def PrintSelection():
        SerialComStatel.config(text='Serial communication' + SerialComState.get())

    r1 = Radiobutton(ModeSelectionWindow, text='Start Serial Communication', font=('Times New Roman', 10),
                     variable=SerialComState, value=' start',
                     command=PrintSelection)
    r1.place(x=75, y=420)
    r2 = Radiobutton(ModeSelectionWindow, text='End Serial Communication', font=('Times New Roman', 10),
                     variable=SerialComState, value=' end',
                     command=PrintSelection)
    r2.place(x=75, y=440)'''
    Label(ModeSelectionWindow, text='Device Port Number', font=('Times New Roman', 10)).place(x=75, y=420)
    DeviceNumberl = Label(ModeSelectionWindow, bg='red', width=40, text=ports[1].device, font=('Times New Roman', 10))
    DeviceNumberl.place(x=75, y=440)
    Label(ModeSelectionWindow, text='Device Description', font=('Times New Roman', 10)).place(x=75, y=470)
    DeviceNumberl = Label(ModeSelectionWindow, bg='red', width=40, text=ports[1].description, font=('Times New Roman', 10))
    DeviceNumberl.place(x=75, y=500)



def createtempuser():
    global tempuserlist
    tempuser = []
    with open('user.pickle', 'rb') as f:
        while True:
            try:
                temp = pickle.load(f)
                tempuser.append(temp)

            except EOFError:
                break
    tempuserlist = tempuser


def login():
    try:
        global userindex
        users = []
        passwords = []
        with open('user.pickle', 'rb') as f:
            while True:
                try:
                    temp = pickle.load(f)
                    users.append(temp.N)
                    passwords.append(temp.PW)

                except EOFError:
                    break

        User = UsernameE.get()
        Password = int(PasswordE.get())
        if User in users:
            index = users.index(User)
            userindex = index
            print(index)
            if (Password == passwords[index]):
                right = Label(root, text="Welcome!")
                right.grid(row=8, column=5)
                createtempuser()
                serial_init()
                ModeInterface()
                
            else:
                wrong = Label(root, text="Wrong Password")
                wrong.grid(row=8, column=5)
        else:
            wrong = Label(root, text="Invalid Username")
            wrong.grid(row=8, column=5)
    except ValueError:
        messagebox.showerror("ERROR", "Password must be numbers!")


def Register():
    global users, passwords, UsernameE1, PasswordE1, UsernameLabel1, PasswordLabel1
    top = Toplevel()
    top.title('CREATE ACCOUNT')
    top.geometry('400x300')

    def reg():
        global tempuserlist
        createtempuser()

        try:
            if (len(tempuserlist) >= 10):
                raise IndexError
            NUser = UsernameE1.get()
            NPassword = int(PasswordE1.get())
            aoo = AOOmode()
            voo = VOOmode()
            aai = AAImode()
            vvi = VVImode()
            doo = DOOmode()
            door = DOORmode()
            aoor = AOORmode()
            voor = VOORmode()
            aair = AAIRmode()
            vvir = VVIRmode()

            NU = User(NUser, NPassword, aoo, aai, voo, vvi, doo, door, aoor, voor, aair, vvir)
            with open('user.pickle', 'ab') as f:
                pickle.dump(NU, f)
            messagebox.showinfo("New Account Valid",
                                "You have successfully signed up! Now you can log in with your account.")
        except ValueError:
            messagebox.showerror("ERROR", "entries can't be empty and please enter your password in valid data type!")
        except IndexError:
            messagebox.showerror("ERROR", "Reach user number limit")

    UsernameE1 = Entry(top, width=30)
    UsernameE1.place(x=150, y=80)
    PasswordE1 = Entry(top, width=30, show='*')
    PasswordE1.place(x=150, y=130)
    UsernameLabel1 = Label(top, text="Username", font=('Times New Roman', 15)).place(x=25, y=80)
    PasswordLabel1 = Label(top, text="Password", font=('Times New Roman', 15)).place(x=25, y=130)
    Passworddatatype = Label(top, text="Use numbers to create your password!", font=('Times New Roman', 10)).place(x=55,
                                                                                                                   y=165)
    regB = Button(top, text="Create Account", width=11, font=('Times New Roman', 15), command=reg)
    regB.place(x=140, y=200)


def egram():
    global eegram
    eegram=Egram()
    '''global ports
    global ser
    ports = list(list_ports.comports())
    ser = serial.Serial(port=ports[1].device, baudrate=115200, timeout=None, bytesize=8, stopbits=serial.STOPBITS_ONE)
    graph_maker()
    ser.close()'''





UsernameE = Entry(root, width=30)
UsernameE.place(x=150, y=80)
PasswordE = Entry(root, width=30, show='*')
PasswordE.place(x=150, y=130)

UsernameLabel = Label(root, text="Username", font=('Times New Roman', 15)).place(x=55, y=80)
PasswordLabel = Label(root, text="Password", font=('Times New Roman', 15)).place(x=55, y=130)

LoginButton = Button(root, text="Login", width=6, font=('Times New Roman', 15), command=login)
LoginButton.place(x=100, y=180)
RegisterButton = Button(root, text="Register", width=6, font=('Times New Roman', 15), command=Register)
RegisterButton.place(x=200, y=180)
root.mainloop()