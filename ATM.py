from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class atm:

    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(110 * blank_space + "ATM System")
        self.root.geometry("800x760+280+0")
        self.root.configure(background='gainsboro')
        #=======================================================FRAMES==========================================================================================

        MainFrame = Frame(self.root, bd=20, width=784, height=700, relief=RIDGE)
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column =0, padx=12)
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column =0, padx=8)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0, column =0, padx=3)

        TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column =1, padx=3)

        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0, column =2, padx=3)
        #===========================================================Functions======================================================================================

        def enter_pin():
            pinNumber = self.txtReceipt.get("1.0", "end-1c")
            if ((pinNumber == str("2213")) or (pinNumber == str("4323")) or (pinNumber == str("5982"))):
                self.txtReceipt.delete("1.0",END)
                
                self.txtReceipt.insert(END,'\t\t       ATM' + "\n\n")
                self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
                self.txtReceipt.insert(END,'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
                self.txtReceipt.insert(END,'Balance \t\t\t Request New pin' + "\n\n\n\n")
                self.txtReceipt.insert(END,'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")
                

                self.img_arrow_Right = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\rArrow1.png")

                self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state =NORMAL, command = loan,  image=self.img_arrow_Right).grid(row=0, column =2, pady=2, padx=2)

                self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state =NORMAL, command = deposit, image=self.img_arrow_Right).grid(row=1, column =2, pady=2, padx=2)

                self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state =NORMAL, command = request_new_pin, image=self.img_arrow_Right).grid(row=2, column =2, pady=2, padx=2)

                self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state =NORMAL, command = statement, image=self.img_arrow_Right).grid(row=3, column =2, pady=2, padx=2)
                #==============================================================Pin Number Button===========================================================================

            
                self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state =NORMAL,command = withdrawcash, image=self.img_arrow_Left).grid(row=0, column =2, pady=2, padx=2)

                self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state =NORMAL,command = withdrawcash, image=self.img_arrow_Left).grid(row=1, column =2, pady=2, padx=2)

                self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state =NORMAL, command = balance, image=self.img_arrow_Left).grid(row=2, column =2, pady=2, padx=2)

                self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state =NORMAL, command = statement, image=self.img_arrow_Left).grid(row=3, column =2, pady=2, padx=2)
                
            else:
                
                 self.txtReceipt.delete("1.0",END)    
                 self.txtReceipt.insert(END,'Invalid Pin Number' + "\n\n")
     
        def clear():

            self.txtReceipt.delete("1.0",END)
            
            self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, image=self.img_arrow_Right).grid(row=0, column =2, pady=2, padx=2)

            self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, image=self.img_arrow_Right).grid(row=1, column =2, pady=2, padx=2)

            self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, image=self.img_arrow_Right).grid(row=2, column =2, pady=2, padx=2)

            self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, image=self.img_arrow_Right).grid(row=3, column =2, pady=2, padx=2)
            #==============================================================Pin Number Button===========================================================================

                
            self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, image=self.img_arrow_Left).grid(row=0, column =2, pady=2, padx=2)

            self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, image=self.img_arrow_Left).grid(row=1, column =2, pady=2, padx=2)

            self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, image=self.img_arrow_Left).grid(row=2, column =2, pady=2, padx=2)

            self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, image=self.img_arrow_Left).grid(row=3, column =2, pady=2, padx=2)

            
        def insert0():
            value0 = 0
            self.txtReceipt.insert(END,value0)

        def insert1():
            value1 = 1
            self.txtReceipt.insert(END,value1)

        def insert2():
            value2 = 2
            self.txtReceipt.insert(END,value2)

        def insert3():
            value3 = 3
            self.txtReceipt.insert(END,value3)

        def insert4():
            value4 = 4
            self.txtReceipt.insert(END,value4)

        def insert5():
            value5 = 5
            self.txtReceipt.insert(END,value5)

        def insert6():
            value6 = 6
            self.txtReceipt.insert(END,value6)

        def insert7():
            value7 = 7
            self.txtReceipt.insert(END,value7)

        def insert8():
            value8 = 8
            self.txtReceipt.insert(END,value8)

        def insert9():
            value9 = 9
            self.txtReceipt.insert(END,value9)

        def cancel():
            cancel = tkinter.messagebox.askyesno("ATM","Confirm if you want to cancel")
            if cancel > 0:
                self.root.destroy()
                return

        def withdrawcash():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def loan():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'Loan $ ')
            self.txtReceipt.focus_set()

        def deposit():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def request_new_pin():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\tWelcome to Bank\n')
            self.txtReceipt.insert(END,'\t\tNew pin will be send to your home address\n')
            self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
            self.txtReceipt.insert(END,'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
            self.txtReceipt.insert(END,'Balance \t\t\t Request New pin' + "\n\n\n\n")
            self.txtReceipt.insert(END,'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")
            self.txtReceipt.insert(END,'\t\tThanks fou using Bank\n')

        def balance():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\tWelcome to Bank\n')
            self.txtReceipt.insert(END,'$1296' + "\n")
            self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
            self.txtReceipt.insert(END,'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
            self.txtReceipt.insert(END,'Balance \t\t\t Request New pin' + "\n\n\n\n")
            self.txtReceipt.insert(END,'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")
            self.txtReceipt.insert(END,'\t\tThanks fou using Bank\n')

        def statement():
            pinNumber1 = str(self.txtReceipt.get("1.0", "end-1c"))
            pinNumber2 = str(pinNumber1)
            pinNumber3 = float(pinNumber2)
            pinNumber4 = float(1296- (pinNumber3))
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\n\t' + str(pinNumber4) + "\t\t")
            self.txtReceipt.insert(END,'\t\t\t\n\n  Account Balance $' + str(pinNumber4) + "\t\t\n")
            self.txtReceipt.insert(END,'Rent \t\t\t\t $1200' + "\n\n")
            self.txtReceipt.insert(END,'Tesco \t\t\t\t $79.36' + "\n\n")
            self.txtReceipt.insert(END,'Rent \t\t\t\t $1200' + "\n\n")
            self.txtReceipt.insert(END,'Sainsbury' + 's \t\t\t\t $53.87' + "\n\n")
            self.txtReceipt.insert(END,'Student Loan \t\t\t\t $69.72' + "\n\n")
            self.txtReceipt.insert(END,'Poundland \t\t\t\t $19.00' + "\n\n")

           
        #=======================================================L WIDGET==========================================================================================
        self.txtReceipt = Text(TopFrame2Mid, height = 17, width=42, bd=12, font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.img_arrow_Left = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\lArrow1.png")

        self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, command = withdrawcash, image=self.img_arrow_Left).grid(row=0, column =2, pady=2, padx=2)

        self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, command = withdrawcash, image=self.img_arrow_Left).grid(row=1, column =2, pady=2, padx=2)

        self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, command = balance, image=self.img_arrow_Left).grid(row=2, column =2, pady=2, padx=2)

        self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state =DISABLED, command = statement, image=self.img_arrow_Left).grid(row=3, column =2, pady=2, padx=2)

        #============================================================R WIDGET============================================================================================

        
        self.img_arrow_Right = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\rArrow1.png")

        self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, command = loan, image=self.img_arrow_Right).grid(row=0, column =2, pady=2, padx=2)

        self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, command = deposit, image=self.img_arrow_Right).grid(row=1, column =2, pady=2, padx=2)

        self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, command = request_new_pin, image=self.img_arrow_Right).grid(row=2, column =2, pady=2, padx=2)

        self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state =DISABLED, command = statement, image=self.img_arrow_Right).grid(row=3, column =2, pady=2, padx=2)

         #==============================================================Pin Number Button===========================================================================

        
        self.img1 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\one1.png")
        self.btn1 = Button(TopFrame1, width=160, height=60, command = insert1, image=self.img1).grid(row=2, column =0, padx=4, pady=4)

        self.img2 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\two2.png")
        self.btn2 = Button(TopFrame1, width=160, height=60, command = insert2, image=self.img2).grid(row=2, column =1, padx=4, pady=4)

        self.img3 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\three3.png")
        self.btn3 = Button(TopFrame1, width=160, height=60, command = insert3, image=self.img3).grid(row=2, column =2, padx=4, pady=4)

        self.imgCancel = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\Cancel.png")
        self.btnCancel = Button(TopFrame1, width=160, height=60,command =  cancel, image=self.imgCancel).grid(row=2, column =3, padx=4, pady=4)

        #==========================================================================================================================================================

        self.img4 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\four4.png")
        self.btn4 = Button(TopFrame1, width=160, height=60, command = insert4, image=self.img4).grid(row=3, column =0, padx=4, pady=4)

        self.img5 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\five5.png")
        self.btn5 = Button(TopFrame1, width=160, height=60, command = insert5, image=self.img5).grid(row=3, column =1, padx=4, pady=4)

        self.img6 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\six6.png")
        self.btn6 = Button(TopFrame1, width=160, height=60,  command = insert6, image=self.img6).grid(row=3, column =2, padx=4, pady=4)

        self.imgClear = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\Clear.png")
        self.btnClear = Button(TopFrame1, width=160, height=60, command = clear, image=self.imgClear).grid(row=3, column =3, padx=4, pady=4)

        #==========================================================================================================================================================

        self.img7 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\seven7.png")
        self.btn7 = Button(TopFrame1, width=160, height=60, command = insert7 ,image=self.img7).grid(row=4, column =0, padx=4, pady=4)

        self.img8 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\eight8.png")
        self.btn8 = Button(TopFrame1, width=160, height=60, command = insert8, image=self.img8).grid(row=4, column =1, padx=4, pady=4)

        self.img9 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\nine9.png")
        self.btn9 = Button(TopFrame1, width=160, height=60,command = insert9, image=self.img9).grid(row=4, column =2, padx=4, pady=4)

        self.imgEnter = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\Enter.png")
        self.btnEnter = Button(TopFrame1, width=160, height=60, command = enter_pin, image=self.imgEnter).grid(row=4, column =3, padx=4, pady=4)

        #==========================================================================================================================================================

        self.imgEmpty0 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\Empty.png")
        self.btnEmpty0 = Button(TopFrame1, width=160, height=60, image=self.imgEmpty0).grid(row=5, column =0, padx=4, pady=4)

        self.img0 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\zero0.png")
        self.btn0 = Button(TopFrame1, width=160, height=60,command = insert0, image=self.img0).grid(row=5, column =1, padx=4, pady=4)

        self.imgEmpty1 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\Empty.png")
        self.btnEmpty1 = Button(TopFrame1, width=160, height=60, image=self.imgEmpty1).grid(row=5, column =2, padx=4, pady=4)

        self.imgEmpty2 = PhotoImage(file = r"C:\Users\medap\OneDrive\Desktop\ATM IMAGES\Empty.png")
        self.btnEmpty2 = Button(TopFrame1, width=160, height=60, image=self.imgEmpty2).grid(row=5, column =3, padx=4, pady=4)







        
        
if __name__=='__main__':
    
    root = Tk()
    application = atm(root)
    root.mainloop()
