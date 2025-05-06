import customtkinter as ctk
from PIL import Image

def open_settings():
    pass

def open_passwords_manager():
    pass

def open_stats():
    pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='white')

        self.title("Menu główne")
        #self.minsize(600,400)
        self.geometry("600x400")
        self.resizable(False, False)

        background = ctk.CTkImage(Image.open('images/typing.jpg'), size=(600, 400))

        self.background = ctk.CTkLabel(self, image=background, text='')
        self.background.place(x=0, y=0)

        self.settings_button = ctk.CTkButton(master=self, text="Ustawienia", command=open_settings, fg_color='black')
        self.settings_button.grid(row=0, column=0, padx=20, pady=10)

        self.manage_passwords_button = ctk.CTkButton(master=self, text="Zarządzaj hasłami", command=open_settings, fg_color='black')
        self.manage_passwords_button.grid(row=0, column=1, padx=20, pady=10)

        self.show_stats_button = ctk.CTkButton(master=self, text="Statystyki", command=open_stats, fg_color='black')
        self.show_stats_button.grid(row=1, column=0,padx=20, pady=10)

        self.colour_mode = ctk.CTkCheckBox(self, text='Motyw ciemny',width=150, height=40)
        self.colour_mode.place(relx=0.05, rely=0.9)
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()