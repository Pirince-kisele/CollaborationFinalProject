import customtkinter 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pay Roll")
        self.geometry("1800x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = customtkinter.CTkFrame(self).grid(
            row=0, column=0, sticky="WENS",  pady=(10, 0))
        self.frame1 = customtkinter.CTkFrame(
            self).grid(row=0, column=1, sticky="WENS")

        self.checkbox_1 = customtkinter.CTkCheckBox(self.frame, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10,
                             pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.frame, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10,
                             pady=(10, 0), sticky="w")
        self.button = customtkinter.CTkButton(
            self.frame1, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()
