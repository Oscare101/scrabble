from tkinter import *
from tkinter import ttk
from collections import Counter
import re
import webbrowser
# coding: utf8
f = open('word_rus.txt', encoding="utf-8")
letter_weight = {"а": 1, "б": 2, "в": 1, "г": 3, "д": 2, "е": 1, "ё": 3, "ж": 5, "з": 5, "и": 1, "й": 4, "к": 2, "л": 2,
                 "м": 2, "н": 1, "о": 1, "п": 2, "р": 1, "с": 1, "т": 1, "у": 2, "ф": 10, "х": 5, "ц": 5, "ч": 5, "ш": 8,
                 "щ": 10, "ь": 3, "ы": 5, "э": 8, "ъ": 10, "ю": 8, "я": 3}
root = Tk()
root.configure(background="#FFFFE0")
root.geometry("500x500")
root.title("Помошник в игре Эрудит")

nb = ttk.Notebook(root)
nb.pack(fill="both", expand="yes")

f1 = Text(root, bg="#FFFFE0")
f4 = Text(root, bg="#FFFFE0")
f2 = Text(root, bg="#FFFFE0")
f3 = Text(root, bg="#FFFFE0")

f5 = Text(root, bg="#FFFFE0")
nb.add(f1, text='   Игра   ')
nb.add(f4, text='   Проверка слова   ')
nb.add(f2, text='   Вес каждой буквы   ')
nb.add(f3, text='   Правила   ')

nb.add(f5, text='   Поддержка   ')
l1 = Label(f2, text="Вес каждой буквы в игре", fg="black", bg="#FFFFE0", justify="center", font=("Impact", 30, ""),
         anchor="center")
l1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.1)

l1 = Label(f2, text="а:1  б:2  в:1  г:3  д:2  е:1  ё:3 \n"             
                  "ж:5  з:5  и:1  й:4  к:2  л:2  м:2 \n"
                  "н:1  о:1  п:2  р:1  с:1  т:1  у:2 \n"
                  "ф:10  х:5  ц:5  ч:5  ш:8  щ:10 \n"
                  "ь:3  ы:5  э:8  ъ:10  ю:8  я:3", fg="black", bg="#FFFFE0", justify="center", font=("Impact", 25),
         anchor="center")
l1.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.5)
time_list = ["Введи все буквы, нажми ОК","и подожди пару секунд","","На досчет слов к каждой","опорной букве программа",
             "на моем компьютере","потратит 5-7 секунд","На слабых телефонах","может быть и до 20 секунд"]
error_list = ["Проверь, что ты все сделал правльно", "Введи 7 букв в первую сточку ",
              "Во вторую сторку буквы через пробел", "Пиши только кириллицей"]
list_var = StringVar(value=time_list)
Listbox(f1, selectmode=SINGLE, height=10, listvariable=list_var) \
    .place(relx=0.5, rely=0.29, relwidth=0.45, relheight=0.66)
all_letter = []
def show_start(event):
    while True:
        try:
            have = have_entry.get().lower()
            let = letter_entry.get().lower()
            if re.search(r'[^а-яё]', have) or re.search(r'[^а-яё ]', let) or len(have) != 7:
                list_var = StringVar(value=error_list)
                Listbox(f1, selectmode=SINGLE, height=10, listvariable=list_var) \
                    .place(relx=0.5, rely=0.29, relwidth=0.45, relheight=0.66)
                break
            letter = let.split()
            letter_weight = {"а": 1, "б": 2, "в": 1, "г": 3, "д": 2, "е": 1, "ё": 3, "ж": 5, "з": 5, "и": 1,
                             "й": 4, "к": 2,"л": 2, "м": 2, "н": 1, "о": 1, "п": 2, "р": 1, "с": 1, "т": 1,
                             "у": 2, "ф": 10, "х": 5, "ц": 5, "ч": 5, "ш": 8, "щ": 10, "ь": 3, "ы": 5,
                             "э": 8, "ъ": 10, "ю": 8, "я": 3, "*": 0}
            end = []
            end_list = []
            a = len(letter)
            for g in range(0, a):
                f = open('word_rus.txt', encoding="utf-8")
                all_letter = [have[0], have[1], have[2], have[3], have[4], have[5], have[6], letter[g]]
                for i in range(34011):
                    p = f.readline(i)
                    a_word = p[0:-1]
                    # print(a_word)
                    a_word_list = []
                    all_weight = 0
                    for k in range(len(a_word)):
                        a_word_list.append(a_word[k])
                        c = common_items = list((Counter(a_word_list) & Counter(all_letter)).elements())
                        if len(c) == len(a_word) and a_word not in end and letter[g] in a_word:
                            end.append(a_word)
                            for m in range(len(a_word)):
                                all_weight += (letter_weight[str(a_word[m])])
                            e = (a_word, "-"*all_weight, all_weight)
                            end_list.append(e)
            if len(end_list) == 0:
                end_list = ["Похоже на то,","что у нас нет слов"]
            list_var = StringVar(value=end_list)
            Listbox(f1, selectmode=SINGLE, height=10, listvariable=list_var)\
                .place(relx=0.5, rely=0.29, relwidth=0.45, relheight=0.66)
            f.close()
            break
        except:
            print("Houston!")

def show_have(event):
    l2 = Label(f1, text=("" + have_entry.get().lower()), font=("Impact", 20), bg="#FFFFE0", fg="black")
    l2.place(relx=0.02, rely=0.35, relwidth=0.4, relheight=0.1)
    list_var = StringVar(value=time_list)
    Listbox(f1, selectmode=SINGLE, height=10, listvariable=list_var) \
        .place(relx=0.5, rely=0.29, relwidth=0.45, relheight=0.66)

def show_letter(event):
    l2 = Label(f1, text=("" + letter_entry.get().lower()), font=("Impact", 20), bg="#FFFFE0", fg="black")
    l2.place(relx=0.02, rely=0.45, relwidth=0.4, relheight=0.1)
    list_var = StringVar(value=time_list)
    Listbox(f1, selectmode=SINGLE, height=10, listvariable=list_var) \
        .place(relx=0.5, rely=0.29, relwidth=0.45, relheight=0.66)

have_entry = Entry(f1, bg="white", fg="black", justify="center")
have_entry.place(relx=0.02, rely=0.02, relwidth=0.36, relheight=0.1)
have_button = Button(f1, text="Введите 7 своих букв", bg="#FFFACD", fg="black", activebackground="black",
                   activeforeground="#FFFACD", relief="raised", justify="center", font=("Impact", 7,))
have_button.bind("<Button-1>", show_have)
have_button.place(relx=0.02, rely=0.14, relwidth=0.36, relheight=0.1)

letter_entry = Entry(f1, bg="white", fg="black", justify="center")
letter_entry.place(relx=0.4, rely=0.02, relwidth=0.36, relheight=0.1)
letter_button = Button(f1, text="Введите букву на поле", bg="#FFFACD", fg="black", activebackground="black",
                   activeforeground="#FFFACD", relief="raised", justify="center", font=("Impact", 7,))
letter_button.bind("<Button-1>", show_letter)
letter_button.place(relx=0.4, rely=0.14, relwidth=0.36, relheight=0.1)

start_button = Button(f1, text="go", bg="#FFFACD", fg="black", activebackground="black",
                   activeforeground="#FFFACD", relief="raised", justify="center", font=("Impact", 10,))
start_button.bind("<Button-1>", show_start)
start_button.place(relx=0.78, rely=0.02, relwidth=0.20, relheight=0.22)

l2 = Label(f1, text=("Алгоритм ограничен списком слов из \n\"Толковый словарь Ефремовой\""), font=("Impact", 10), bg="#FFDAB9", fg="black")
l2.place(relx=0, rely=0.8, relwidth=0.5, relheight=0.1)

l1 = Label(f3, text="У Вас на руках есть 7 букв\nВведите их в первую сточку"
                    "\nНа поле выберите букву или буквы,\nк которым хотите приставить слово\n"
                    "Их введите во вторую строчку через пробел\nИ запускайте", fg="black", bg="#FFFFE0", justify="center", font=("Impact", 16, ""),
         anchor="center")
l1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.5)
l1 = Label(f3, text="Программа подбирет слова \nпо имеющимся буквам и одной опорной\nи выдаст количество очков", fg="black", bg="#FFFFE0", justify="center", font=("Impact", 16, ""),
         anchor="center")
l1.place(relx=0.0, rely=0.5, relwidth=1, relheight=0.5)

def show_word(event):
    while True:
        try:
            word = word_entry.get().lower()
            if re.search(r'[^а-яё]', word):
                l2 = Label(f4, text=("Пиши кириллицей\nи без ошибок"), font=("Impact", 12), bg="#FFFFE0", fg="black")
                l2.place(relx=0.02, rely=0.24, relwidth=0.48, relheight=0.1)
                l4 = Label(f4, text='no', font=("Impact", 12), bg="red", fg="black")
                l4.place(relx=0.52, rely=0.14, relwidth=0.46, relheight=0.46)
                break
            f = open('word_rus.txt', encoding="utf-8")
            all_in_word_list = []
            for i in range(34016):
                p = f.readline(i)
                a = p[0:-1]
                all_in_word_list.append(a)
            if word in all_in_word_list:
                l2 = Label(f4, text=("Есть такое слово " + word), font=("Impact", 12), bg="#FFFFE0", fg="black")
                l2.place(relx=0.02, rely=0.24, relwidth=0.48, relheight=0.1)
                l4 = Label(f4, text='yes', font=("Impact", 12), bg="#00FF00", fg="black")
                l4.place(relx=0.52, rely=0.14, relwidth=0.46, relheight=0.46)
            else:
                l2 = Label(f4, text=("Нет такого слова " + word), font=("Impact", 12), bg="#FFFFE0", fg="black")
                l2.place(relx=0.02, rely=0.24, relwidth=0.48, relheight=0.1)
                l4 = Label(f4, text='no', font=("Impact", 12), bg="red", fg="black")
                l4.place(relx=0.52, rely=0.14, relwidth=0.46, relheight=0.46)
            f.close()
            break
        except:
            print("Houston!")

word_entry = Entry(f4, bg="white", fg="black", justify="center")
word_entry.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.1)
word_button = Button(f4, text="Проверить", bg="#FFFACD", fg="black", activebackground="black",
                   activeforeground="#FFFACD", relief="raised", justify="center", font=("Impact", 7,))
word_button.bind("<Button-1>", show_word)
word_button.place(relx=0.52, rely=0.02, relwidth=0.46, relheight=0.1)

l2 = Label(f4, text=("Алгоритм ограничен списком слов из \n\"Толковый словарь Ефремовой\""), font=("Impact", 12), bg="#FFDAB9", fg="black")
l2.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)
def callback_t(event):
    webbrowser.open_new(r"https://t.me/funny_like_panda")
l1 = Label(f5, text="Программа написана для \nсобственного развития\n"
                    "За поддержкой, вопросами и предложениями \nписать в телеграм или на почту"
                    "\n", fg="black", bg="#FFFFE0", justify="left", font=("Impact", 12, ""),
         anchor="sw")
l1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.5)
l8 = Label(f5, text="Telegram ", fg="blue", bg="#FFFFE0", justify="left", cursor="hand2", font=("Impact", 12, ""),
         anchor="nw")
l8.place(relx=0.0, rely=0.5, relwidth=1, relheight=0.5)
l8.bind("<Button-1>", callback_t)
l9 = Label(f5, text="kirillfedortsev2000@gmail.com", fg="black", bg="#FFFFE0", justify="left", cursor="hand2", font=("Impact", 12, ""),
         anchor="nw")
l9.place(relx=0.0, rely=0.55, relwidth=1, relheight=0.5)
f.close()
root.mainloop()