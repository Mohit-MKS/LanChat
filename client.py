from socket import *
from tkinter import *
from threading import Thread



s = socket(AF_INET, SOCK_STREAM)
def rqst_conn(self):
	ip = str(host.get())
	s.connect((ip,6156))
	thread = Thread(target = receive)
	thread.start()
	

def receive():
	while True:
		rec = s.recv(1024).decode("utf8")
		msg_list.insert(END,"Server: " + rec)

def on_closing():
	s.send(bytes("Client closed","utf8"))
	s.close()
	win.quit()

def send(self):
	msg = my_msg.get()
	msg_list.insert(END,"YOU: " + msg)
	my_msg.set("")
	s.send(bytes(msg,"utf8"))


# GUI window
win = Tk()
win.title("Client")
my_msg = StringVar()
host = StringVar()
Label(win, text="Host: ").pack(anchor = W)
Host = Entry(win,textvariable=host).pack(anchor = W)
connect = Button(win, text = "Connect")
connect.bind("<Button-1>",rqst_conn)
connect.pack(side=TOP,anchor=W)
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