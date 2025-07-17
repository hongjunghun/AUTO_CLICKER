from tkinter import *
from tkinter import ttk
import sqlite3
from function import Clicking

click = Clicking()

def initialize_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            sleeping_time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT key, sleeping_time FROM passwords")
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(END, f"{row[0]} {row[1]}")
    conn.close()

def add():

    sleeping_time = float(entry.get())
    button = combo.get()
    text = f"{button} {sleeping_time}"

    # 리스트박스에 추가
    listbox.insert(END, text)

    # DB에 저장
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (key, sleeping_time) VALUES (?, ?)", (button, sleeping_time))
    conn.commit()
    conn.close()

def delete():
    selection = listbox.curselection()
    if not selection:
        return
    index = selection[0]
    item = listbox.get(index)
    listbox.delete(index)

    key, sleep = item.split()
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE key=? AND sleeping_time=?", (key, sleep))
    conn.commit()
    conn.close()

def start():
    selection = listbox.curselection()
    if not selection:
        return
    index = selection[0]
    item = listbox.get(index)
    spliting = item.split()
    key = spliting[0]; click_time = float(spliting[1])
    click.click(key, click_time)


initialize_db()

win = Tk()
win.geometry("400x300")
win.resizable(height=False, width=False)
win.title("매크로")

# 콤보박스
options = ["CapsLock", "Tab", "Shift", "Escape", "Control"]
combo = ttk.Combobox(win, values=options, state="readonly")
combo.current(0)
combo.pack()

# 숫자 입력창
entry = Entry(win)
entry.pack(side="right")

lab = Label(win, text="SLEEPING TIME")
lab.pack(side="right")

# 리스트박스
listbox = Listbox(win, selectmode=SINGLE, width=40, height=15)
listbox.pack()

# 버튼들
btn1 = Button(win, text="🫙", font=(24), width=4, height=2, command=add)
btn1.pack(side="right")

btn2 = Button(win, text="🚩", font=(24), width=4, height=2, command=start)
btn2.pack(side="right")

btn3 = Button(win, text="🗑️", font=(24), width=4, height=2, command=delete)
btn3.pack(side="right")

# DB에서 기존 데이터 불러오기
load_data()


# GUI 실행
win.mainloop()
