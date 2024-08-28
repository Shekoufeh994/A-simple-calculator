import tkinter
from tkinter import *
from pygame import mixer

calcute = Tk()
calcute.title("Calculator")
calcute.geometry("570x600")
calcute.resizable(False,False)
calcute.configure(bg="black") # Color of background

sum=""
Rsl=""
def display(val):
	global sum
	sum += val
	LblResult.configure(text= sum)
	
        

def calculation():
	global sum
	global Rsl
	Rsl = eval(sum)
	LblResult.configure(text=Rsl)
	
	
    	

        
			
	

def Readnum(num):
	global Rsl
	Rsl = num
	'''
	run = True
	while run:
		ones = Rsl %10
		tens = (Rsl // 10) % 10
		hundreds = Rsl//100
  		
		if Rsl == hundreds:
			'''
	FileLocation = "wav/" + "shomare.mp3"
	mixer.init()
	mixer.music.load(FileLocation)
	mixer.music.play()
	time.sleep(1)
		
			

		
	FileLocation = "wav/" + str(Rsl)
	mixer.init()
	mixer.music.load(FileLocation)
	mixer.music.play()




def clear():
	global sum 
	sum =""
	LblResult.configure(text= sum)

	





LblResult = Label(calcute,width=100,height=2,text="",font=("arial",30,"bold"))
LblResult.pack()


Button(calcute,text="C", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="blue" ,command=lambda:clear()).place(x=10,y=100)
Button(calcute,text="/", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="lightgray",command=lambda:display("/")).place(x=150,y=100)
Button(calcute,text="%", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="lightgray",command=lambda:display("%")).place(x=290,y=100)
Button(calcute,text="*", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="lightgray",command=lambda:display("*")).place(x=430,y=100)
Button(calcute,text="7", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("7")).place(x=10,y=200)
Button(calcute,text="8", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("8")).place(x=150,y=200)
Button(calcute,text="9", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("9")).place(x=290,y=200)
Button(calcute,text="-", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("-")).place(x=430,y=200)
Button(calcute,text="4", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("4")).place(x=10,y=300)
Button(calcute,text="5", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("5")).place(x=150,y=300)
Button(calcute,text="6", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("6")).place(x=290,y=300)
Button(calcute,text="+", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("+")).place(x=430,y=300)
Button(calcute,text="1", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("1")).place(x=10,y=400)
Button(calcute,text="2", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("2")).place(x=150,y=400)
Button(calcute,text="3", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("3")).place(x=290,y=400)
Button(calcute,text="=", width=5, height=3, font=("arial",30,"bold"),bd=1,fg="white",bg="orange",command=lambda:calculation()).place(x=430,y=400)
Button(calcute,text="0", width=11, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display("0")).place(x=10,y=500)
Button(calcute,text=".", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="steelblue",command=lambda:display(".")).place(x=290,y=500)


calcute.mainloop()