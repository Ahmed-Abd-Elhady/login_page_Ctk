import customtkinter as ctk
from tkinter import messagebox

# def res(widget, x_percent, y_percent, window):
#     x = int(window.winfo_width() * (x_percent / 100))
#     y = int(window.winfo_height() * (y_percent / 100))
#     widget.place(x=x, y=y)

def button_even(app,username_entry,password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if len(username) > 15 or len(password) > 15:
        messagebox.showerror("❌ Error", "❌ Max Chr is 16 for password and username try again.")
        username_entry.delete(0, ctk.END) 
        password_entry.delete(0, ctk.END) 
        return

    elif password == "void69" and username == "void":
        messagebox.showinfo("State : Login ✅", f"Welcome {username} !! ")
        app.destroy()
    else:
        messagebox.showerror("❌ Error", " ❌ Username or password is Wrong try again !")
        username_entry.delete(0, ctk.END) 
        password_entry.delete(0, ctk.END) 
        return


def res(widget, x_percent, y_percent, window):
    window.update_idletasks()
    widget.update_idletasks()

    # Calculate center x, y positions based on window size
    x = int(window.winfo_width() * (x_percent / 100)) - (widget.winfo_reqwidth() // 2)
    y = int(window.winfo_height() * (y_percent / 100)) - (widget.winfo_reqheight() // 2)
    widget.place(x=x, y=y)



def login_page_function(mode):
    ctk.set_appearance_mode(mode) 
    app = ctk.CTk()
    app.geometry('400x400')
    app.title("State_App | Login Page")
    app.resizable(False, False)
    login_frame = ctk.CTkFrame(app,width=340,height=340,border_width=2,border_color='#fff')
    res(login_frame,50,50,app)

    field_label= ctk.CTkLabel(app,text="Login | State_App@Void",font=("",24))
    res(field_label,60,20,login_frame)

    # in the frame thing
    field_username = ctk.CTkEntry(app,width=300,height=40,corner_radius=30,placeholder_text="admin",font=("",16))
    res(field_username,60,40,login_frame)

    field_password = ctk.CTkEntry(app,width=300,height=40,corner_radius=30,placeholder_text="123",font=("",16))
    res(field_password,60,60,login_frame)


    button = ctk.CTkButton(app,text="Login",hover_color="Green",width=300,height=40,corner_radius=30,font=("",24),command=lambda:button_even(app,field_username,field_password))
    res(button,60,83,login_frame)

    app.mainloop()


login_page_function('dark')