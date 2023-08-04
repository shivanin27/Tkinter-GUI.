from tkinter import *
from turtle import bgcolor, onclick
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.font as tkFont


root =Tk()
root.geometry("285x500")
root.title("MINDSPACE")
# root.iconbitmap('D:/Shivani/HCI/icon.ico') 
bg = PhotoImage(file = "background.png")
  

label1 = Label( root, image = bg)
label1.place(x =0, y =0 )
frame1 = Frame(root)
frame1.pack(pady = 80 )




def open_prof():
    prof=Toplevel()
    prof.geometry("285x500")
    global imgne
    imgne = ImageTk.PhotoImage(Image.open("background.png"))
    img_labelne = Label(prof, image=imgne)
    img_labelne.place(x=0,y=0)
    # global label11
    # global img
    # global image
    image = Image.open("profimg.png")
 
# Resize the image using resize() method
    resize_image = image.resize((90, 60))
    img = ImageTk.PhotoImage(resize_image)
    label11 = Label(prof,image=img)
    label11.image = img
    label11.place(x=100,y=60)
    
    canvas= Canvas(prof, width= 280, height= 40, bg="#d5f4e6")
    canvas.create_text(140,22, text="Shivani Nyamgoud", fill="black", font=('Helvetica 15 bold'))
    canvas.place(x=5,y=120)
    mycanvas=Canvas(prof,width="280",height="10",bg="white")
    mycanvas.create_line(0,5,280,5,fill="black")
    mycanvas.place(x=5,y=170)
    canvas2= Canvas(prof, width= 280, height= 40, bg="white")
    canvas2.create_text(69,15, text="Full name: \n  Shivani Nyamgoud ", fill="black", font=('Helvetica 10 bold '))
    canvas2.place(x=5,y=190)
    
    canvas3= Canvas(prof, width= 280, height= 40, bg="white")
    canvas3.create_text(103,15, text="E-mail: \n  shivaninyamgoud@gmail.com ", fill="black", font=('Helvetica 10 bold '))
    canvas3.place(x=5,y=250)
  
    canvas4= Canvas(prof, width= 280, height= 40, bg="white")
    canvas4.create_text(67,15, text="Subscription details: \n  Inactive ", fill="black", font=('Helvetica 10 bold '))
    canvas4.place(x=5,y=310)
    

    canvas5= Canvas(prof, width= 280, height= 40, bg="white")
    canvas5.create_text(38,17, text="Language: \n  English ", fill="black", font=('Helvetica 10 bold '))
    canvas5.place(x=5,y=370)
   
   


    btn4 = Button(prof, text='Logout', width=7,height=1,bg="#36486b",font=('Helvetica 15 bold ') ,command=prof.quit)
    btn4.place(x=100, y=450)


logo_ib = ImageTk.PhotoImage(Image.open("profile.png").resize((45, 45)))
logo_ib_label = Label(image=logo_ib).place(x=7,y=80)
b1 = Button(root,text = "Profile",width="5",height="1",bd="3",bg='#d6cbd3',font=('Times', 10),command=open_prof) 
b1.place(x=8,y=125) 

def open_search():
   
    top = Toplevel()
    top.geometry("285x500")
    global imgne
    imgne = ImageTk.PhotoImage(Image.open("background.png"))
    img_labelne = Label(top, image=imgne)
    img_labelne.place(x=0,y=0)
    canvas2= Canvas(top, width= 280, height= 20, bg="white")
    canvas2.create_text(62,15, text="Search for Advice",fill="black", font=('Helvetica 10 bold '))
    canvas2.place(x=0,y=90)
    mycanvas=Canvas(top,width="280",height="10",bg="white")
    mycanvas.create_line(0,5,160,5,fill="black")
    mycanvas.place(x=0,y=110)
    
    
    image = Image.open("one.jpeg")
    resize_image = image.resize((60, 50))
    img = ImageTk.PhotoImage(resize_image)
    label11 = Label(top,image=img)
    label11.image = img
    label11.place(x=25,y=150)
    
    image2 = Image.open("two.jpeg")
    resize_image2 = image2.resize((60, 50))
    img2 = ImageTk.PhotoImage(resize_image2)
    label12 = Label(top,image=img2)
    label12.image2 = img2
    label12.place(x=25,y=220)

    image3 = Image.open("three.jpeg")
    resize_image3 = image3.resize((60, 50))
    img3 = ImageTk.PhotoImage(resize_image3)
    label13 = Label(top,image=img3)
    label13.image3= img3
    label13.place(x=25,y=290)



    label1=Label(top,text="Begining Meditation",bd="1",bg='white',foreground="black",font=("Times  italic bold",14))
    label1.place(x=95,y=160)

    label2=Label(top,text="The Wake up",bd="1",bg='white',foreground="black",font=("Times  italic bold",14))
    label2.place(x=95,y=230)
    
    label3=Label(top,text="For Challenging times",bd="1",bg='white',foreground="black",font=("Times  italic bold",14))
    label3.place(x=95,y=300)
   
    def onClick():
        tk.messagebox.showinfo("Connecting ... ","Choose from our daily plans.." )  
    btn4 = Button(top, text='STRESS', width=8,height=1,bg="#feb236",fg="#4040a1",font=('Helvetica 12 bold ') ,command=onClick)
    btn4.place(x=20, y=350)
    def onClick2():
        tk.messagebox.showinfo("Connecting ... ","Choose from our daily plans.." )  
    btn4 = Button(top, text='ANXIETY', width=8,height=1,bg="#feb236",fg="#4040a1",font=('Helvetica 12 bold ') ,command=onClick2)
    btn4.place(x=180, y=350)
    mycanvas=Canvas(top,width="280",height="10",bg="white")
    mycanvas.create_line(0,5,280,5,fill="black")
    mycanvas.place(x=0,y=385)
    image4 = Image.open("download.jpeg")
    resize_image4 = image4.resize((90, 60))
    img4 = ImageTk.PhotoImage(resize_image4)
    label14 = Label(top,image=img4)
    label14.image4= img4
    label14.place(x=3,y=405)
    label2=Label(top,text="Your only 10 minutes",bd="1",bg='White',font=(" Times italic ",13),fg="#f18973")
    label2.place(x=103,y=405)
    label3=Label(top,text="and one meditation",bd="1",bg='white',font=("Times italic ",13),fg="#f18973")
    label3.place(x=103,y=425)
    label4=Label(top,text="away from good mood🧘",bd="1",bg='white',font=("Times italic ",13),fg="#f18973")
    label4.place(x=103,y=445)
    label5=Label(top,text="Stay Tuned..! ",bd="3",bg='white',font=(" Helvetica 12 bold "),fg="black")
    label5.place(x=80,y=475)
    
    
   
logo_ib2 = ImageTk.PhotoImage(Image.open("search.png").resize((40, 40)))
logo_ib_label2 = Label(image=logo_ib2).place(x=230,y=80)
b2 = Button(root,text = "Search",width="5",height="1",bd="3",bg='#d6cbd3',font=('Times ',10),command=open_search) 
b2.place(x=230,y=125) 

label1=Label(root,text="Boosting",bd="1",bg='white',font=("Times",17))
label1.place(x=100,y=120)

label2=Label(root,text="self-esteem",bd="1",bg='white',font=("Times",17))
label2.place(x=83,y=150)
label3=Label(root,text="Featured",bd="1",bg='white',font=("Times",15))
label3.place(x=17,y=200)

logo_ib3 = ImageTk.PhotoImage(Image.open("image1.png").resize((70, 50)))
logo_ib_label3 = Label(image=logo_ib3).place(x=17,y=250)
label_img1=Label(root,text="Basics",bd="1",bg='white',foreground="blue",font=("Times  italic bold",13))
label_img1.place(x=98,y=255)
label_img1sub=Label(root,text="Course 3-10min",bd="1",bg='white',font=("Times",10))
label_img1sub.place(x=95,y=273)

logo_ib4 = ImageTk.PhotoImage(Image.open("image2.png").resize((70, 60)))
logo_ib_label4 = Label(image=logo_ib4).place(x=17,y=320)
label_img2=Label(root,text="Breathe",bd="1",bg='white',foreground="blue",font=("Times  italic bold",13))
label_img2.place(x=98,y=325)
label_img2sub=Label(root,text="Meditation 3-10min",bd="1",bg='white',font=("Times",10))
label_img2sub.place(x=95,y=343)



logo_ib5= ImageTk.PhotoImage(Image.open("image3.jpeg").resize((70, 60)))
logo_ib_label5= Label(image=logo_ib5).place(x=17,y=390)
label_img3=Label(root,text="Letting Go of stress",bd="1",bg='white',foreground="blue",font=("Times  italic bold",13))
label_img3.place(x=98,y=395)
label_img3sub=Label(root,text=" Course 10-20min",bd="1",bg='white',font=("Times",10))
label_img3sub.place(x=95,y=413)

logo_ib6= ImageTk.PhotoImage(Image.open("medi.jpeg").resize((70, 60)))
logo_ib_label6= Label(image=logo_ib6).place(x=210,y=220)
def onClick():
        tk.messagebox.showinfo("Connecting ... ","Connecting to the bank page." )
b3 = Button(root,text = "Subscribe",width="10",height="1",bd="3",bg='#4040a1',font=('Times italic bold ',12),command=onClick) 
b3.place(x=100,y=460)



    
    

# logo_ib.pack()

root.mainloop()
