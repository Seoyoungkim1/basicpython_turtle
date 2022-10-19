from tkinter import *
from tkinter import ttk, messagebox


GUI = Tk()
GUI.title('โปรแกรมคำนวณราคาปลา รถพุ่มพวงของฉัน')
GUI.geometry('700x600')


bg = PhotoImage(file='car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา (กิโลกรัม)',font=(None,20))
L.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def Cal():
	try:
		quan = float(v_quantity.get())
		calc = quan * 39
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc))
	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1')

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20)





GUI.mainloop()
