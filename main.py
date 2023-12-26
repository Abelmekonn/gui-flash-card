from tkinter import*
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
card_choice={}
to_learn={}

try:
    data=pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global card_choice,flip_timer
    window.after_cancel(flip_timer)
    card_choice=random.choice(to_learn)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(words,text=card_choice["French"],fill="black")
    canvas.itemconfig(card_background,image=front_img)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(words,text=card_choice["English"],fill="white")
    canvas.itemconfig(card_background,image=back_img)

def is_known():
    to_learn.remove(card_choice)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv",index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=front_img)
title=canvas.create_text(400,156,text="",font=("Arial",21,"normal"))
words=canvas.create_text(400,250,text="",font=("Arial",30,"normal"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unknown=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown.grid(row=1,column=0)
right_image=PhotoImage(file="images/right.png")
known=Button(image=right_image,highlightthickness=0,command=is_known)
known.grid(row=1,column=1)

next_card()

window.mainloop()