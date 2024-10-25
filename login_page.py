import customtkinter as ctk
from tkinter import messagebox

state = False
attempts = 0  # Track the number of attempts
cooldown_time = 10  # 10 minutes in seconds (this is used for the countdown)
is_cooldown = False  # Track if in cooldown

def button_even(app, username_entry, password_entry, cooldown_label, login_button):
    global attempts, is_cooldown  
    username = username_entry.get()
    password = password_entry.get()

    if is_cooldown:
        messagebox.showwarning("Cooldown", "Please wait before trying again.")
        return

    if len(username) > 15 or len(password) > 15:
        messagebox.showerror("❌ Error", "❌ Max Chr is 16 for password and username try again.")
        username_entry.delete(0, ctk.END) 
        password_entry.delete(0, ctk.END) 
        return  

    if password == "void69" and username == "void":
        messagebox.showinfo("State : Login ✅", f"Welcome {username} !! ")
        global state
        state = True  
        app.destroy()  
    else:
        attempts += 1  
        messagebox.showerror("❌ Error", "❌ Username or password is wrong. Try again!")
        username_entry.delete(0, ctk.END) 
        password_entry.delete(0, ctk.END) 

        if attempts >= 5:
            disable_entries(username_entry, password_entry, login_button, cooldown_label)

def disable_entries(username_entry, password_entry, login_button, cooldown_label):
    global is_cooldown
    is_cooldown = True
    username_entry.configure(state='disabled')  
    password_entry.configure(state='disabled')  
    login_button.configure(state='disabled')  

    start_cooldown(cooldown_label, username_entry, password_entry, login_button)

def start_cooldown(cooldown_label, username_entry, password_entry, login_button):
    global cooldown_time
    countdown(cooldown_label, cooldown_time, username_entry, password_entry, login_button)

def countdown(cooldown_label, remaining_time, username_entry, password_entry, login_button):
    if remaining_time > 0:
        cooldown_label.configure(text=f"Cooldown: {remaining_time} seconds")
        cooldown_label.after(1000, countdown, cooldown_label, remaining_time - 1, username_entry, password_entry, login_button)
    else:
        reset_entries(cooldown_label, username_entry, password_entry, login_button)

def reset_entries(cooldown_label, username_entry, password_entry, login_button):
    global is_cooldown, attempts
    is_cooldown = False
    attempts = 0  
    cooldown_label.configure(text="")  
    username_entry.configure(state='normal')  
    password_entry.configure(state='normal')  
    login_button.configure(state='normal')  

def res(widget, x_percent, y_percent, window):
    window.update_idletasks()
    widget.update_idletasks()

    x = int(window.winfo_width() * (x_percent / 100)) - (widget.winfo_reqwidth() // 2)
    y = int(window.winfo_height() * (y_percent / 100)) - (widget.winfo_reqheight() // 2)
    widget.place(x=x, y=y)

def login_page_function(mode):
    global state  
    ctk.set_appearance_mode(mode) 
    app = ctk.CTk()
    app.geometry('400x400')
    app.title("State_App | Login Page")
    app.resizable(False, False)
    
    login_frame = ctk.CTkFrame(app, width=340, height=340, border_width=2, border_color='#fff')
    res(login_frame, 50, 50, app)

    field_label = ctk.CTkLabel(app, text="Login | State_App@Void", font=("", 24))
    res(field_label, 60, 20, login_frame)

    field_username = ctk.CTkEntry(app, width=300, height=40, corner_radius=30, placeholder_text="admin", font=("", 16))
    res(field_username, 60, 40, login_frame)

    field_password = ctk.CTkEntry(app, width=300, height=40, corner_radius=30, placeholder_text="123", font=("", 16))
    res(field_password, 60, 60, login_frame)

    login_button = ctk.CTkButton(app, text="Login", hover_color="Green", width=300, height=40, corner_radius=30, font=("", 24),
                            command=lambda: button_even(app, field_username, field_password, cooldown_label, login_button))
    res(login_button, 60, 83, login_frame)

    cooldown_label = ctk.CTkLabel(app, text="", font=("", 16))
    res(cooldown_label, 60, 95, login_frame)

    app.mainloop()  
    if state:
        return True



login_page_function('dark')