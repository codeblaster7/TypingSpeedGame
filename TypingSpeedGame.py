from tkinter import *
import random
from tkinter import messagebox

def wordTyper():
    global count, typing_words
    text = "Welcome to Typing Test Game"
    if count >= len(text):
        count = 0
        typing_words = ""
    typing_words += text[count]
    count += 1
    font_label.configure(text=typing_words)
    font_label.after(150, wordTyper)

def start_timer():
    global time_left, score, miss
    if time_left >= 11:
        pass
    else:
        time_label_count.configure(fg="red")
    if time_left > 0:
        time_left -= 1
        time_label_count.configure(text=time_left)
        time_label_count.after(1000, start_timer)
    else:
        gameplay_label.configure(text="Hit = {} | Missed = {} | Total score = {}".format(score, miss, score-miss))
        ss = messagebox.askretrycancel('Time Up!', 'To play the game again hit retry button')
        if ss == True:
            score = 0
            time_left = 60
            miss = 0
            time_label_count.configure(text=time_left)
            word_label.configure(text=words[0])
            score_label_count.configure(text=score)

def startGame(event):
    global score, miss
    if time_left == 60:
        start_timer()
    gameplay_label.configure(text="")
    if word_entry.get() == word_label['text']:
        score += 1
        score_label_count.configure(text=score)
    else:
        miss += 1
        print("Miss:", miss)
    random.shuffle(words)
    word_label.configure(text=words[0])
    word_entry.delete(0, END)

# Created Root
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg="peach puff")
root.title("Typing Test Game")
root.iconbitmap("icon.ico")

# Created Variables
score = 0
time_left = 60
count = 0
miss = 0
typing_words = ""
words = ['leave', 'bullet', 'coding', 'programmer', 'two', 'move', 'been',
         'song', 'children', 'way', 'too', 'over', 'good', 'turn', 'even',
         'stop', 'will', 'head', 'call', 'spell', 'city', 'life', 'that',
         'saw', 'too', 'back', 'land', 'see', 'high', 'men', 'father']

# Created Label
font_label = Label(root, text="",
                   font=("AppleSystemUIFont", 25, "italic"),
                   bg="peach puff", fg="gray11", width=40)
font_label.place(x=10, y=10)
wordTyper()

random.shuffle(words)
word_label = Label(root, text=words[0],
                   font=("AppleSystemUIFont", 40),
                   bg="peach puff", fg="MediumPurple4")
word_label.place(x=350, y=200)

score_label = Label(root, text="Your Score : ",
                    font=("AppleSystemUIFont", 25),
                    bg="peach puff", fg="dark slate blue")
score_label.place(x=10, y=100)

score_label_count = Label(root, text=score,
                    font=("AppleSystemUIFont", 25),
                    bg="peach puff", fg="dark slate blue")
score_label_count.place(x=80, y=160)

timer_label = Label(root, text="Time Left : ",
                    font=("AppleSystemUIFont", 25),
                    bg="peach puff", fg="dark slate blue")
timer_label.place(x=610, y=100)

time_label_count = Label(root, text=time_left,
                    font=("AppleSystemUIFont", 25),
                    bg="peach puff", fg="dark slate blue")
time_label_count.place(x=680, y=160)

gameplay_label = Label(root, text="Type the given word and hit enter",
                       font=("AppleSystemUIFont", 30), bg="peach puff", fg="gray43")
gameplay_label.place(x=120, y=450)
# Created Entry
word_entry = Entry(root, font=("AppleSystemUIFont", 25), bd=5, justify="center")
word_entry.place(x=250, y=300)
word_entry.focus_set()

root.bind('<Return>', startGame)

root.mainloop()