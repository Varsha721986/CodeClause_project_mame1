from tkinter import *
import smtplib

def send_message():
    sender_email = "manevarsha468@gmail.com"
    sender_password = "Varsha@123"

    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login(sender_email,sender_password)

    print("Login successful")

    address_info = address.get()

    email_body_info = email_body.get()

    server.sendmail(sender_email,address_info,email_body_info)

    print("Message send")

    address_entry.delete(0,END)

    email_body_entry.delete(0,END)


app = Tk()

app.geometry("500x500")

app.title("python email sending application")

heading = Label(text="python mail sending app" , bg="gray", fg="black", font="10", width="500", height="2")

heading.pack()


address_field = Label(text="Recipent Address :")
email_body_field = Label(text="message :")

address_field.place(x=15,y=70)
email_body_field.place(x=15,y=140)

address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address,width="30")
email_body_entry = Entry(textvariable=email_body,width="30")

address_entry.place(x=15,y=100)
email_body_entry.place(x=15,y=180)

Button = Button(app,text="send message", bg="gray", command=send_message,width="30",height="2")

Button.place(x=15,y=220)


mainloop()
