import pyspeedtest 
from tkinter import *
def rkt_Speed_test(): 
	r = pyspeedtest.SpeedTest(t.get()) 
	ping.set(r.ping()) 
	k_download.set(r.download()) 
rkt = Tk() 
rkt.title("GUI WIFI SPEEDTESTER (RKT)")
rkt.configure(bg='purple')
ping = StringVar() 
k_download = StringVar() 
Label(rkt,text='Enter a router IP:',bg='purple').grid(row=0, sticky=W) 
Label(rkt,text='Ping Result:',bg='purple').grid(row=3, sticky=W) 
Label(rkt,text='Download Result:',bg='purple').grid(row=4, sticky=W)
result = Label(rkt,text="", textvariable=ping,bg='purple').grid(row=3, column=1, sticky=W) 
result2 = Label(rkt,text="", textvariable=k_download,bg='purple' ).grid(row=4, column=1, sticky=W) 
t = Entry(rkt) 
t.grid(row=0, column=1) 
b = Button(rkt,text='Check',command=rkt_Speed_test) 
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=3, pady=3) 
rkt.mainloop() 
