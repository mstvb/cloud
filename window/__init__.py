# Created by Manuel Staufer [2022]


import tkinter, customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        ''' -- GEOMETRY X TITLE -- '''
        self.geometry(f"{750}x{500}")
        self.title("HighCloud")


        ''' -- APPEARANCE MODE X COLOR THEME -- '''
        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme("green")
        self.overrideredirect(True)


        ''' -- EXIT BUTTON -- '''
        exit_button = customtkinter.CTkButton(master=self.master, text="Exit", command=exit, width=40)
        exit_button.place(relx=0.96, rely=0.05, anchor=tkinter.CENTER)


        ''' -- WINDOW TITLE -- '''
        window_title = customtkinter.CTkLabel(master=self.master, text="Login", text_font=("Consolas", 22))
        window_title.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)


        ''' -- USERNAME ENTRY -- '''
        username_entry = customtkinter.CTkEntry(master=self.master, placeholder_text="Username", width=200, height=40, border_width=0, corner_radius=15)
        username_entry.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)


        ''' -- PASSWORD ENTRY -- '''
        password_entry = customtkinter.CTkEntry(master=self.master, placeholder_text="Password", width=200, height=40, border_width=0, corner_radius=15)
        password_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


        ''' -- LOGIN BUTTON -- '''
        login_button = customtkinter.CTkButton(master=self.master, text="Login", text_font=("Consolas", 22), corner_radius=15, width=40)
        login_button.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)


app = App()
app.mainloop()