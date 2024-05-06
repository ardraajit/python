from tkinter import *


def buttonClick(number):
    global operator
    operator=operator+str(number)
    input_value.set(operator)

def buttonClear():
    global oprator
    operator=""
    input_value.set("")

def buttonEqual():
    global operator
    result=str(eval(operator))
    input_value.set(result)
    operator=""
    


main=Tk()
main.title("calculator")

operator=""
input_value=StringVar()
display_test=Entry(main,font=("ariel",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,bg="yellow",justify=RIGHT)
display_test.grid(columnspan=4)

#row1
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="7",command=lambda:buttonClick(7))
btn_7.grid(row=1,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="8",command=lambda:buttonClick(8))
btn_7.grid(row=1,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="9",command=lambda:buttonClick(9))
btn_7.grid(row=1,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="+",command=lambda:buttonClick("+"))
btn_7.grid(row=1,column=3)

#row2
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="4",command=lambda:buttonClick(4))
btn_7.grid(row=2,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="5",command=lambda:buttonClick(5))
btn_7.grid(row=2,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="6",command=lambda:buttonClick(6))
btn_7.grid(row=2,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="-",command=lambda:buttonClick("-"))
btn_7.grid(row=2,column=3)

#row3
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="1",command=lambda:buttonClick(1))
btn_7.grid(row=3,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="2",command=lambda:buttonClick(2))
btn_7.grid(row=3,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="3",command=lambda:buttonClick(3))
btn_7.grid(row=3,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="*",command=lambda:buttonClick("*"))
btn_7.grid(row=3,column=3)

#row4
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="0",command=lambda:buttonClick(0))
btn_7.grid(row=4,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="c",command=lambda:buttonClear())
btn_7.grid(row=4,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="=",command=lambda:buttonEqual())
btn_7.grid(row=4,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="/",command=lambda:buttonClick("/"))
btn_7.grid(row=4,column=3)

main.mainloop()