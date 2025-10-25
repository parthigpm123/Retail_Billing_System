# REQUIREMENT LIBRARY FOR PROJECT

from tkinter import *            #Tkinter Library
from tkinter import messagebox    #Tkinter Messagebox Library
import os                         #OS MODULE
import smtplib
from tkinter import filedialog   # For file dialog
#==========================================#
#=====CLEAR BUTTON FUNCTION======#
def clear():
      #DELETE ALL ENTRY FIELDS
      bathsoapEntry.delete(0,END)
      facecreamEntry.delete(0,END)
      hairgelEntry.delete(0,END)
      hairsprayEntry.delete(0,END)
      bodyloationEntry.delete(0,END)
      facewashEntry.delete(0,END)
      
      daalEntry.delete(0,END)
      wheatEntry.delete(0,END)
      riceEntry.delete(0,END)
      oilEntry.delete(0,END)
      sugarEntry.delete(0,END)
      teaEntry.delete(0,END)
      
      pepsiEntry.delete(0,END)
      colaEntry.delete(0,END)
      maazaEntry.delete(0,END)
      dewEntry.delete(0,END)
      spriteEntry.delete(0,END)
      frootiEntry.delete(0,END)
      
      #INSERT 0 IN ALL PRODUCT ENTRY FIELDS
      bathsoapEntry.insert(0,0)
      facecreamEntry.insert(0,0)
      hairgelEntry.insert(0,0)
      hairsprayEntry.insert(0,0)
      bodyloationEntry.insert(0,0)
      facewashEntry.insert(0,0)
      
      daalEntry.insert(0,0)
      wheatEntry.insert(0,0)
      riceEntry.insert(0,0)
      oilEntry.insert(0,0)
      sugarEntry.insert(0,0)
      teaEntry.insert(0,0)
      
      pepsiEntry.insert(0,0)
      colaEntry.insert(0,0)
      maazaEntry.insert(0,0)
      dewEntry.insert(0,0)
      spriteEntry.insert(0,0)
      frootiEntry.insert(0,0)
      #DELETE BILL MENU ENTRY FIELDS
      cosmetictaxEntry.delete(0,END)
      grocerytaxEntry.delete(0,END)
      drinkstaxEntry.delete(0,END)
      
      cosmeticpriceEntry.delete(0,END)
      grocerypriceEntry.delete(0,END)
      drinkspriceEntry.delete(0,END)
      
      nameEntry.delete(0,END)
      phoneEntry.delete(0,END)
      billnumberEntry.delete(0,END)
      
      
      textarea.delete(1.0,END)
      
#SEND EMAIL FUNCTION
def send_email():
      def send_gmail():
            try:
                ob=smtplib.SMTP('smtp.gmail.com',587)
                ob.starttls()
                ob.login(senderEntry.get(),passwordEntry.get())
                message=email_textarea.get(1.0,END)
                ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
                ob.quit()
                messagebox.showinfo('Success','Email Sent Successfully',parent=root1)
                root1.destroy()
            except:
                  messagebox.showerror('Error','something went wrong please try again!',parent=root1)    
            
      if textarea.get(1.0,END)=='\n':
             messagebox.showerror("Error","No Bill to Print")
      else:
            root1=Toplevel()
            root1.grab_set()
            root1.title("Send Email")
            root1.config(bg="blue2")
            root1.resizable(0,0)    
            
            
            senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='blue2',fg='gold')
            senderFrame.grid(row=0,column=0,padx=40,pady=20)
            
            senderlabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='blue2',fg='gold')
            senderlabel.grid(row=0,column=0,padx=10,pady=8)
            
            
            senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
            senderEntry.grid(row=0,column=1,padx=10,pady=8)
            
            passwordlabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bd=6,bg='blue2',fg='gold')
            passwordlabel.grid(row=1,column=0,padx=10,pady=8)
            
            
            passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
            passwordEntry.grid(row=1,column=1,padx=10,pady=8)
            
            recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='blue2',fg='gold')
            recipientFrame.grid(row=1,column=0,padx=40,pady=20)
            
            recieverlabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bd=6,bg='blue2',fg='gold')
            recieverlabel.grid(row=0,column=0,padx=10,pady=10)
            
            
            recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
            recieverEntry.grid(row=0,column=1,padx=10,pady=8)
            
            messagelabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bd=6,bg='blue2',fg='gold')
            messagelabel.grid(row=1,column=0,padx=10,pady=8)
            
            email_textarea=Text(recipientFrame, font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
            email_textarea.grid(row=2,column=0,columnspan=2)
            email_textarea.delete(1.0,END)
            email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))
            
            sendbutton=Button(root1,text="SEND",font=('arial',16,"bold"),width=15,command=send_gmail)
            sendbutton.grid(row=2,column=0,pady=20)
            
            
           #FUNCTION CALLING 
            root1.mainloop()
               
      

# FUNCTION THROW ERROR
# Function to calculate total (placeholder)

# def print_bill():
#       if textarea.get(1.0,END)=='\n':
#             messagebox.showerror("Error","No Bill to Print")
#       else:
#             file=tempfile.mktemp('.txt')
#             open(file,'w').write(textarea.get(1.0,END))
#             os.startfile(file,"print")
            
# def print_bill():
#     if textarea.get(1.0, END) == '\n':
#         messagebox.showerror("Error", "No Bill to Print")
#     else:
#         file = tempfile.mktemp(".txt")
#         with open(file, "w") as f:
#             f.write(textarea.get(1.0, END))
#         #os.startfile(file, "Print")
#         os.startfile(file)  # Just open Notepad without print

#PRINT BILL FUNCTION
def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror("Error", "No Bill to Print")
    else:
        # Ask user where to save the file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save Bill As"
        )

        if file_path:  # User selected a path
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(textarea.get(1.0, END))
                messagebox.showinfo("Saved", f"Bill successfully saved as:\n{os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")


#SEARCH BILL BUTTON FUNCTION
def search_bill():
      for i in os.listdir('bills/'):
            if i.split('.')[0]==billnumberEntry.get():
                  f=open(f'bills/{i}','r')
                  textarea.delete(1.0,END)
                  for data in f:
                        textarea.insert(END,data)
                  f.close()
                  break
      else:
            messagebox.showerror("Error","Invalid Bill Number")                  

if not os.path.exists('bills'):
      os.makedirs('bills')
      
#SAVE BILL FUNCTION
def save_bill():
      result=messagebox.askyesno("Confirm","Do you want to save the bill?")
      if result:
            bill_content=textarea.get(1.0,END)
            file = open(f"bills/{billnumberEntry.get()}.txt", "w")
            file.write(bill_content)
            file.close()
            messagebox.showinfo("Saved",f"Bill no. : {billnumberEntry.get()} saved successfully")
            
#GENERATE BILL AREA FUNCTION
def bill_area():
      #SHOW ERROR NULL VALUE
      if nameEntry.get()=="" or phoneEntry.get()=="":
          messagebox.showerror("Error","Customer details should be entered")
      elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
          messagebox.showerror("Error","No Product Purchased")
      elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
          messagebox.showerror("Error","No Product Purchased")
       #GENERATE BILL  
      else:
            textarea.delete(1.0,END)
            textarea.insert(END,"\t\t***Welcome Customers***\n")
            textarea.insert(END,f"\nBill Number : {billnumberEntry.get()}\n")
            textarea.insert(END,f"\nCustomer Name : {nameEntry.get()}\n")
            textarea.insert(END,f"\nCustomer Phone Number : {phoneEntry.get()}\n")
            textarea.insert(END,"\n=======================================================\n")
            textarea.insert(END,"Products\t\t\tQty\t\t\tPrice\n")
            textarea.insert(END,"=======================================================\n")
            #================= Cosmetis Products =============#
            if bathsoapEntry.get()!='0':
                  textarea.insert(END,f"Bath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs\n")
            if facecreamEntry.get()!='0':
                  textarea.insert(END,f"Face Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs\n")
            if facewashEntry.get()!='0':
                  textarea.insert(END,f"Face Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs\n")      
            if hairsprayEntry.get()!='0':
                  textarea.insert(END,f"Hair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs\n")
            if hairgelEntry.get()!='0':
                  textarea.insert(END,f"Hair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs\n")
            if bodyloationEntry.get()!='0':
                  textarea.insert(END,f"Body Lotion\t\t\t{bodyloationEntry.get()}\t\t\t{bodyloationprice} Rs\n")
            #================= Grocery Products =============#      
            if riceEntry.get()!='0':
                  textarea.insert(END,f"Rice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs\n")
            if daalEntry.get()!='0':
                  textarea.insert(END,f"Daal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs\n")
            if oilEntry.get()!='0':
                  textarea.insert(END,f"Oil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs\n")
            if wheatEntry.get()!='0':
                  textarea.insert(END,f"Wheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs\n")
            if sugarEntry.get()!='0':
                  textarea.insert(END,f"Sugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs\n")
            if teaEntry.get()!='0':
                  textarea.insert(END,f"Tea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs\n")
            #================= Cold Drink Products =============#      
            if maazaEntry.get()!='0':
                  textarea.insert(END,f"Maaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs\n")
            if frootiEntry.get()!='0':
                  textarea.insert(END,f"Frooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs\n")
            if dewEntry.get()!='0':
                  textarea.insert(END,f"Dew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs\n")
            if pepsiEntry.get()!='0':                                                                              
                  textarea.insert(END,f"Pepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs\n")
            if spriteEntry.get()!='0':
                  textarea.insert(END,f"Sprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs\n")
            if colaEntry.get()!='0':
                  textarea.insert(END,f"Coca Cola\t\t\t{colaEntry.get()}\t\t\t{cococolaprice} Rs\n")            
            textarea.insert(END,'-------------------------------------------------------')
            if cosmetictaxEntry.get()!='0.0 Rs':
                  textarea.insert(END,f"\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}\n")
            if grocerytaxEntry.get()!='0.0 Rs':
                  textarea.insert(END,f"\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}\n")
            if drinkstaxEntry.get()!='0.0 Rs':
                  textarea.insert(END,f"\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}\n")            
            textarea.insert(END,f'\nTotal Bill\t\t\t\t{totalbill}')
            textarea.insert(END,"\n=======================================================\n")
            save_bill()
            
# TOTAL BUTTON FUNCTION     
def total():
      #MAKE GLOBAL ENTRY FEILD
      global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodyloationprice
      global riceprice,daalprice,oilprice,sugarprice,teaprice,wheatprice
      global maazaprice,frootiprice,dewprice,pepsiprice,spriteprice,cococolaprice
      global totalbill
      # Calculate cosmetic price
      soapprice=int(bathsoapEntry.get()) * 20
      facecreamprice=int(facecreamEntry.get())*50
      facewashprice=int(facewashEntry.get())*30
      hairsprayprice=int(hairsprayEntry.get())*150
      hairgelprice=int(hairgelEntry.get())*80
      bodyloationprice=int(bodyloationEntry.get())*60
      
      totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodyloationprice
      cosmeticpriceEntry.delete(0,END)
      cosmeticpriceEntry.insert(0,str(totalcosmeticprice)+"Rs")
      cosmetictax=totalcosmeticprice*0.12
      cosmetictaxEntry.delete(0,END)
      cosmetictaxEntry.insert(0,str(cosmetictax)+" Rs")
      # Calculate grocery price
      riceprice=int(riceEntry.get())*200
      daalprice=int(daalEntry.get())*150
      oilprice=int(oilEntry.get())*100
      sugarprice=int(sugarEntry.get())*90
      teaprice=int(teaEntry.get())*120
      wheatprice=int(wheatEntry.get())*180
      
      totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
      grocerypriceEntry.delete(0,END)
      grocerypriceEntry.insert(0,str(totalgroceryprice)+"Rs")
      grocerytax=totalgroceryprice*0.85
      grocerytaxEntry.delete(0,END)
      grocerytaxEntry.insert(0,str(grocerytax)+" Rs")
      
      # Calculate cold drink price
      maazaprice=int(maazaEntry.get())*60
      frootiprice=int(frootiEntry.get())*65
      dewprice=int(dewEntry.get())*50
      pepsiprice=int(pepsiEntry.get())*55
      spriteprice=int(spriteEntry.get())*45
      cococolaprice=int(colaEntry.get())*70
      
      totaldrinkprice=maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cococolaprice
      drinkspriceEntry.delete(0,END)
      drinkspriceEntry.insert(0,str(totaldrinkprice)+"Rs")
      drinkstax=totaldrinkprice *0.08
      drinkstaxEntry.delete(0,END)
      drinkstaxEntry.insert(0,str(drinkstax)+" Rs")
      
      totalbill=totalcosmeticprice+totalgroceryprice+totaldrinkprice+cosmetictax+grocerytax+drinkstax
      

root=Tk()

#=========================== Main Window Setup ============================
root.title("Retail Billing System")
root.geometry("1270x685")

#root.iconbitmap("icon.ico")

headingLabel=Label(root,text="Retail Billing System",font=("times new roman",30,"bold"),bg="blue2",fg="gold",bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="blue2")
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=("times new roman",15,"bold"),bg="blue2",fg="white")
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=("times new roman",15,"bold"),bg="blue2",fg="white")
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=("times new roman",15,"bold"),bg="blue2",fg="white")
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,bg="gold",fg="black",command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

#============COSMETICS====================#
cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='blue2')
cosmeticsFrame.grid(row=0,column=0)


bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=("times new roman",13,"bold"),bg="blue2",fg="white")
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)


facecreamLabel=Label(cosmeticsFrame,text='FaceCream',font=("times new roman",13,"bold"),bg="blue2",fg="white")
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='FaceWash',font=("times new roman",13,"bold"),bg="blue2",fg="white")
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
facewashEntry.grid(row=2,column=1,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='HairSpray',font=("times new roman",13,"bold"),bg="blue2",fg="white")
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hairgel',font=("times new roman",13,"bold"),bg="blue2",fg="white")
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,padx=10)
hairgelEntry.insert(0,0)

bodyloationLabel=Label(cosmeticsFrame,text='Body Lotion',font=("times new roman",13,"bold"),bg="blue2",fg="white")
bodyloationLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodyloationEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
bodyloationEntry.grid(row=5,column=1,padx=10)
bodyloationEntry.insert(0,0)


#==========GroceryFrame=====================#
groceryframe=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='blue2')
groceryframe.grid(row=0,column=1)

riceLabel=Label(groceryframe,text='Rice',font=("times new roman",13,"bold"),bg="blue2",fg="white")
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryframe,text='Oil',font=("times new roman",13,"bold"),bg="blue2",fg="white")
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
oilEntry.grid(row=1,column=1,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryframe,text='Daal',font=("times new roman",13,"bold"),bg="blue2",fg="white")
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
daalEntry.grid(row=2,column=1,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryframe,text='Wheat',font=("times new roman",13,"bold"),bg="blue2",fg="white")
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
wheatEntry.grid(row=3,column=1,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryframe,text='Sugar',font=("times new roman",13,"bold"),bg="blue2",fg="white")
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
sugarEntry.grid(row=4,column=1,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryframe,text='Tea',font=("times new roman",13,"bold"),bg="blue2",fg="white")
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
teaEntry.grid(row=5,column=1,padx=10)
teaEntry.insert(0,0)

#========COLD DRINKS FRAME====================#

ColdDrinks=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='blue2')
ColdDrinks.grid(row=0,column=2)

maazaLabel=Label(ColdDrinks,text='Maaza',font=("times new roman",13,"bold"),bg="blue2",fg="white")
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(ColdDrinks,text='Pepsi',font=("times new roman",13,"bold"),bg="blue2",fg="white")
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(ColdDrinks,text='Sprite',font=("times new roman",13,"bold"),bg="blue2",fg="white")
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
spriteEntry.grid(row=2,column=1,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(ColdDrinks,text='Dew',font=("times new roman",13,"bold"),bg="blue2",fg="white")
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
dewEntry.grid(row=3,column=1,padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(ColdDrinks,text='Frooti',font=("times new roman",13,"bold"),bg="blue2",fg="white")
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
frootiEntry.grid(row=4,column=1,padx=10)
frootiEntry.insert(0,0)

colaLabel=Label(ColdDrinks,text='Coco cola',font=("times new roman",13,"bold"),bg="blue2",fg="white")
colaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
colaEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
colaEntry.grid(row=5,column=1,padx=10)
colaEntry.insert(0,0)

#==========BILLFRAME==========#
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

#============BIL AREA lABEL=======#
billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bg="gold",fg="black",bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

#=====TEXT AREAR FRAME========
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=15,width=55,yscrollcommand=scrollbar.set)
textarea.pack()      
scrollbar.config(command=textarea.yview)


#=========BILL MENU FRAME==========
billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='blue2')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=("times new roman",13,"bold"),bg="blue2",fg="white")
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=("times new roman",15,"bold"),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=("times new roman",13,"bold"),bg="blue2",fg="white")
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=("times new roman",15,"bold"),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=("times new roman",13,"bold"),bg="blue2",fg="white")
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
drinkspriceEntry=Entry(billmenuFrame,font=("times new roman",15,"bold"),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

#=====================cosmetic tax FRAME===========
cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=("times new roman",13,"bold"),bg="blue2",fg="white")
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=("times new roman",15,"bold"),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=("times new roman",13,"bold"),bg="blue2",fg="white")
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=("times new roman",15,"bold"),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinkstaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=("times new roman",13,"bold"),bg="blue2",fg="white")
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
drinkstaxEntry=Entry(billmenuFrame,font=("times new roman",15,"bold"),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)

#================BUTTON FRAME==============

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text="Total",font=('arial',16,"bold"),bg="gold",fg="black",bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text="Bill",font=('arial',16,"bold"),bg="gold",fg="black",bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text="Email",font=('arial',16,"bold"),bg="gold",fg="black",bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text="Print",font=('arial',16,"bold"),bg="gold",fg="black",bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text="Clear",font=('arial',16,"bold"),bg="gold",fg="black",bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)
root.mainloop() 