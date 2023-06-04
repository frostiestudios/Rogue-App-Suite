from tkinter import *
from tkinter import ttk
import webbrowser
import json
import socket
import threading
import sqlite3
PLY = "\u25B6"
PAU = "\u23F8"
PRE = "\u23F4"
NEX = "\u23F3"


conn = sqlite3.connect('rr.db')
cursor = conn.cursor()
cursor.execute("SELECT name, ip FROM computers")
data = cursor.fetchall()
pcname = [row[0] for row in data]
print(pcname)
ips = [row[1] for row in data]
print(ips)
def send_content():
    ip_address = ip_combobox.get()
    message = command_combobox.get()
    threading.Thread(target=lambda: send(ip_address, message)).start()
    print(f'Sending:{message}')
def send(ip_address, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, 12345))
    s.sendall(message.encode())
    s.close()
def dbo():
    new_name = newpc_name_combobox.get()
    new_ip = newpc_ip_combobox.get()
    print(new_name)
    print(new_ip)

root = Tk()
root.title("Command Hub Server")

ip_combobox = ttk.Combobox(root, values=[row[1] for row in data])
command_combobox = ttk.Combobox(root, values=['C','S'])

newpc_name_combobox = ttk.Entry(root)
newpc_ip_combobox = ttk.Entry(root)

ttk.Label(root,text="Select Dest").grid(row=3,column=0)
ttk.Label(root,text="Select Command").grid(row=4,column=0)
ttk.Label(root,text="Power System Commands").grid(row=1,column=1)
ttk.Button(root,text="EXEC",command=send_content).grid(row=2,column=1)
ip_combobox.grid(row=3,column=1)
command_combobox.grid(row=4,column=1)

ttk.Label(root,text="New PC").grid(row=1,column=3,columnspan=2)

ttk.Label(root,text="Name").grid(row=2,column=3)
newpc_name_combobox.grid(row=2,column=4)

ttk.Label(root,text="IP").grid(row=3,column=3)
newpc_ip_combobox.grid(row=3,column=4)

ttk.Button(root,text="Enter",command=dbo).grid(row=4,column=4)


root.mainloop()