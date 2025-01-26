from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

class Flash:
    def __init__(self):
        self.d = {}
        self.t = {}

        try:
            data = pd.read_csv("data/ce_sa_invat.csv")
        except FileNotFoundError:
            original_data = pd.read_csv("data/verb_past.csv")
            self.d = original_data.to_dict(orient="records")
        else:
            self.d = data.to_dict(orient="records")

        self.w = Toplevel()
        self.w.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

        self.can = Canvas(self.w, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.img1 = PhotoImage(file="images/card_front.png")
        self.img4 = PhotoImage(file="images/card_back.png")
        self.image = self.can.create_image(400, 263, image=self.img1)
        self.t1 = self.can.create_text(400, 100, font=("Ariel", 40, "italic"), text="Limba")
        self.t2 = self.can.create_text(400, 183, font=("Ariel", 60, "bold"), text="Cuvantul")
        self.t3 = self.can.create_text(400, 263, font=("Ariel", 60, "bold"), text="Cuvantul")
        self.t4 = self.can.create_text(400, 343, font=("Ariel", 60, "bold"), text="Cuvantul")
        self.can.grid(column=0, row=0, columnspan=2)

        self.flipt = self.w.after(7500, self.flip)

        self.img2 = PhotoImage(file="images/right.png")
        self.da = Button(self.w, image=self.img2, highlightthickness=0, command=self.remo)
        self.da.grid(column=1, row=1)

        self.img3 = PhotoImage(file="images/wrong.png")
        self.nu = Button(self.w, image=self.img3, highlightthickness=0, command=self.clickbuttons)
        self.nu.grid(column=0, row=1)

        self.clickbuttons()

        self.w.mainloop()

    def clickbuttons(self):
        self.w.after_cancel(self.flipt)
        self.t = random.choice(self.d)
        self.can.itemconfig(self.image, image=self.img1)
        self.can.itemconfig(self.t1, text="Verb Romana", fill="black")
        self.can.itemconfig(self.t2, text=" ", fill="black")
        self.can.itemconfig(self.t3, text=self.t["Ro"].lower(), fill="black")
        self.can.itemconfig(self.t4, text=" ", fill="black")
        self.flipt = self.w.after(7500, self.flip)

    def flip(self):
        self.can.itemconfig(self.image, image=self.img4)
        self.can.itemconfig(self.t1, text="Verb Engleza", fill="white")
        self.can.itemconfig(self.t2, text=self.t["Inf"].lower(), fill="white")
        self.can.itemconfig(self.t3, text=self.t["Past"].lower(), fill="white")
        self.can.itemconfig(self.t4, text=self.t["Part"].lower(), fill="white")

    def remo(self):
        self.d = [item for item in self.d if item != self.t]
        data = pd.DataFrame(self.d)
        data.to_csv("data/ce_sa_invat.csv", index=False)
        self.clickbuttons()





Flash()
