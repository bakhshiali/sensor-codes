import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import unittest

def rgb_to_hsv(r,g,b):
    maxP = 255.0;
    if r <= maxP and g <= maxP and b <= maxP:
        r = r / maxP;
        g = g / maxP;
        b = b / maxP;
        max_val = max(r, g, b);
        min_val = min(r, g, b);
        v = max_val;
        if max_val == 0.0:
            s = 0;
            h = 0;
        elif max_val - min_val == 0.0 :
            s = 0;
            h = 0;
        else:
            s = (max_val - min_val) / max_val;

            if max_val == r:
                h = 60 * ((g - b) / (max_val - min_val)) + 0;
            elif max_val == g :
                h = 60 * ((b - r) / (max_val - min_val)) + 120;
            else:
                h = 60 * ((r - g) / (max_val - min_val)) + 240;
        return h,s,v
    else:
        print("warning: rgb value must be lower than/eaqual to 255!")
def hue_to_wavelength(hue):
    if hue >= 0 and hue <= 270:
        wavelength = 620 - 170 / 270 * hue;
        print("wavelength: ",wavelength," nm")
def rgb_to_wavelength(r,g,b):
    [h,s,v]=rgb_to_hsv(r,g,b);
    wavelength = hue_to_wavelength(h)
    print("wavelength: ",wavelength," nm")
def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 750:
        A = 1.
    else:
        A=0.5
    if wavelength < 380:
        wavelength = 380.
    if wavelength >750:
        wavelength = 750.
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R,G,B,A)

def draw_spectrum():
    clim=(350,780)
    norm = plt.Normalize(*clim)
    wl = np.arange(clim[0],clim[1]+1,2)
    colorlist = list(zip(norm(wl),[wavelength_to_rgb(w) for w in wl]))
    spectralmap = matplotlib.colors.LinearSegmentedColormap.from_list("spectrum", colorlist)
    fig, axs = plt.subplots(1, 1, figsize=(8,4), tight_layout=True)
    wavelengths = np.linspace(200, 1000, 1000)
    spectrum = (5 + np.sin(wavelengths*0.1)**2) * np.exp(-0.00002*(wavelengths-600)**2)
    plt.plot(wavelengths, spectrum, color='darkred')
    y = np.linspace(0, 6, 100)
    X,Y = np.meshgrid(wavelengths, y)
    extent=(np.min(wavelengths), np.max(wavelengths), np.min(y), np.max(y))
    plt.imshow(X, clim=clim,  extent=extent, cmap=spectralmap, aspect='auto')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.fill_between(wavelengths, spectrum, 8, color='w')
    plt.savefig('WavelengthColors.png', dpi=200)
    plt.show()
import sys
import math
from tkinter import Tk, Canvas, IntVar, Label, LabelFrame, Scale, HORIZONTAL,ttk
def rgbc_to_rgb(r,g,b,c):
    print(r,g,b)
    return r,g,b
def get():
    red = 136
    green = 174
    blue = 133
    c=12
    r,g,b=rgbc_to_rgb(red,green,blue,c)
    return r,g,b
import serial
def connect(event):
    com=com_cb.get();
    print(com)
    r=""
    g=""
    b=""
    s=""
    try:
        ser = serial.Serial(com.split(' - ')[0],baudrate=9600,
                            bytesize=8, timeout=2,
                            stopbits=serial.STOPBITS_ONE)  # open serial port
        print(ser.name)
        comlabel.config(text ="Sensor is connected to "+com.split(' - ')[1]+".")
    #ser.close()
    #while True:
        for i in range(0,10):
            try:
                ser.flushInput()
                s = ser.readline().decode("utf-8") 
                import csv,time
                
                print(s)
                if len(s.split(' '))==3:
                    r=s.split(' ')[0];
                    g=s.split(' ')[1];
                    b=s.split(' ')[2];
                    if int(r)<=255.0 and int(g)<=255.0 and int(b)<=255.0:
                        with open("test_data.csv","a") as f:
                            writer = csv.writer(f,delimiter=",")
                            writer.writerow([time.time(),s])
                        canvas.config(bg="#%02x%02x%02x" % (int(r),int(g),int(b)))
                        rgbLabel.config(text ="RGB :  "+str(r)+", "+str(g)+", "+str(b))
                        [h,s,v] = rgb_to_hsv(int(r),int(g),int(b))
                        hsvLabel.config(text ="HSV :  "+str(round(h,2))+
                                    ", "+str(round(s,2))+", "+str(round(v,2)))
            except Exception as e:
                print(str(e))
                print("Keyboard Interrupt")
                break
    except:
        print("An exception occurred, try again!")
    try:
        return ser
    except:
        print("Sensor is disconnected.")
tk = Tk()
tk.wm_title("TCS Color-Ali Bakhshi")

selectlabel = Label(text="Please select a com:")
selectlabel.pack()

from serial.tools import list_ports

ports =list_ports.comports()
com_cb = ttk.Combobox(tk)
com_cb['values'] = ports
com_cb['state'] = 'readonly'  # normal
com_cb.pack()
com_cb.bind('<<ComboboxSelected>>', connect)

comlabel = Label(text="Sensor is not connected.")
comlabel.pack()

canvas = Canvas(width=400, height=300, bg="#%02x%02x%02x" % (0, 0, 0))
canvas.pack()

rgbFrame = LabelFrame(tk, text="RGB")
rgbFrame.pack(fill="both", expand="yes")
rgbLabel = Label(rgbFrame,text="RGB :  ")
rgbLabel.pack()

hsvFrame = LabelFrame(tk, text="HSV")
hsvFrame.pack(fill="both", expand="yes")
hsvLabel = Label(hsvFrame,text="HSV :  ")
hsvLabel.pack()


#################### GUI ########################################
def main():
    print ("Start of main()")
    def rgb_update():
        [r,g,b]=get()
        canvas.config(bg="#%02x%02x%02x" % (r, g, b))
        rgbLabel.config(text ="RGB :  "+str(r)+", "+str(g)+", "+str(b))
        [h,s,v] = rgb_to_hsv(r,g,b)
        hsvLabel.config(text ="HSV :  "+str(round(h,2))+
                        ", "+str(round(s,2))+", "+str(round(v,2)))
    rgb_update()
    tk.mainloop()
if __name__ == "__main__":
    sys.exit(main())
