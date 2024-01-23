
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import *
from tkinter import messagebox



# Explicit imports to satisfy Flake8
#from tkinter import Tk, self.canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/run/media/miguel/Data/User/Sem_SO/fkinTkinter/diagnostico_so/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MyGUI:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("668x593")
        self.window.configure(bg = "#FFFFFF")

        
        self.canvas = Canvas(
        self.window,
        bg = "#FFFFFF",
        height = 593,
        width = 668,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            334.0,
            50.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            156.0,
            215.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            454.0,
            215.0,
            image=image_image_3
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            194.5,
            283.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D5D5D5",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=112.0,
            y=265.0,
            width=165.0,
            height=35.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            492.5,
            283.5,
            image=entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D5D5D5",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=410.0,
            y=265.0,
            width=165.0,
            height=35.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("hola"),
            relief="flat"
        )
        self.button_1.place(
            x=75.0,
            y=517.0,
            width=207.0,
            height=40.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.imprimir,
            relief="flat"
        )
        self.button_2.place(
            x=401.0,
            y=517.0,
            width=207.0,
            height=40.0
        )

        self.canvas.create_rectangle(
            63.0,
            336.0,
            620.0,
            496.0,
            fill="#EEE8B7",
            outline="")

        self.canvas.create_text(
            63.0,
            336.0,
            anchor="nw",
            text="test",
            fill="#000000",
            font=("JetBrainsMonoRoman Regular", 15 * -1)
        )

        self.canvas2 = Canvas(
            self.canvas,
            bg = "#EEE8B7",
            height=160,
            width=557,
            bd=0
        )
        self.canvas2.place(x=63.0,y=336.0)

        self.my_label = Label(self.canvas2,
            #63.0,
            #278.0,
            bd=1,
            text = "+\n+++\n++++++\n+++\n++++\n+++++++++++++++",
            font=("Helvetica",18))

        self.my_label.pack()

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            334.0,
            136.0,
            image=image_image_4
        )

        self.clock = self.canvas.create_text(
            282.0,
            105.0,
            anchor="nw",
            text="00:00",
            fill="#FFFFFF",
            font=("JosefinSansRoman Regular", 31)
        )

        self.window.resizable(False, False)
        self.window.mainloop()
    
    def imprimir(self):
        self.sim = self.entry_1.get()
        self.num = self.entry_2.get()
        
        try: #Comprobamos que el numero sea un entero positivo
            num_int = int(self.num)
            if num_int <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error","El número solo puede ser un positivo mayor a cero")
        
        piramide = ""
        for i in range(1, int(self.num) + 1):
            piramide += self.sim * (2*i-1) + "\n" 
               
        
        # piramide = "x\n"+"xxx\n"+"xxxxx\n"
        self.my_label.config(text=piramide)


    def imp_num(self):
        print(self.num)
MyGUI()

