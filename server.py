from socket import *
from tkinter import *
from threading import Thread

s = socket(AF_INET,SOCK_STREAM)

def start_server(self):
	global c
	s.bind((ip,6156))
	s.listen(5)
	c,a=s.accept()
	msg_list.insert(END,"Connected to " + a[0])
	c.send(bytes("Connection Established to " + ip,"utf8"))
	thread = Thread(target = receive)
	thread.start()

def receive():
	global c
	while True:
		rec = "Client: " + c.recv(1024).decode("utf8")
		msg_list.insert(END,rec)




def send(self):
	global c
	msg = my_msg.get()
	msg_list.insert(END,"YOU:    " + msg)
	my_msg.set("")
	c.send(bytes(msg,"utf8"))		


def on_closing():
	global c
	c.send(bytes("Server closed","utf8"))
	c.close()
	win.quit()




# To get server ip to tell client whom to connect
t = socket(AF_INET, SOCK_DGRAM)
t.connect(("192.168", 80))
ip = t.getsockname()[0]
t.close()


# GUI window
win = Tk()
win.title("Client")
my_msg = StringVar()
start = Button(win, text="Start Server")
start.bind("<Button-1>", start_server)
start.pack(anchor = NE)
host_ip = Label(win,text="Server: "+str(ip)).pack(side=TOP,anchor=NE)
my_msg.set("Type your message.")
scrollbar = Scrollbar(win)
msg_list = Listbox(win, height=20, width=80 ,yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack()
msg_entry = Entry(win,textvariable=my_msg)
msg_entry.bind("<Return>",send)
msg_entry.pack()
send_button = Button(win,text="Send")
send_button.bind("<Button-1>",send)
send_button.pack(side=BOTTOM)
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()