# 2023.02.03 全屏色彩 + 2023.02.16 黑屏密码 + 2023.03.19 ChatGLM
# 需要advice.txt文件    

from time import strftime, sleep
import tkinter as tk
import threading as th
from sys import exit
from random import randint

class close():
    def auto_close():
        while True:
            if strftime('%H%M') >= '1350':
                while True:
                    try:
                        root.destroy()
                        break
                    except:
                        pass
                break
            sleep(10)
           
    def delay_close(event):
        sleep(1)
        root.destroy()
        exit()
    
    def on_close(event):
        root.destroy()
        exit()

    def delay(event):
        global counter, total_counter
        button_name = int(event.num)
        if button_name == 1:
            counter += 1
            print(button_name, counter)
            if counter >= 4:
                counter = 0
                total_counter += 1
                root.destroy()
                sleep(60)
                form()

def load_txt():
    try:
        with open('advice.txt', 'r', encoding='utf-8') as f:
            return f.read().split('-'*60)
    except:
        raise FileNotFoundError('advice.txt not found')

def print_data():
    time = int(strftime('%H%M'))
    while time < 1320:
        if time > 1315:
            t3 = th.Thread(target=active_generating).start()
        sleep(30)
        time = int(strftime('%H%M'))
    try:
        textbox.pack()
    except:
        pass
    for reply in text:
        textbox.delete('1.0', 'end')
        for i in reply:
            textbox.insert('end', i)
            sleep(randint(2, 12)/100)
        sleep(10)
    textbox.forget()
    if int(strftime('%H%M')) < 1335:
        sleep(10)
        print_data()

def active_generating():
    try:
        textbox.pack()
    except:
        pass
    for i in range(60):
        active_text = 'Generating' + '.'*(i%4)
        textbox.delete('1.0', 'end')
        textbox.insert('end', active_text)
        sleep(0.5)

def form(width=300, height=200):
    global root, textbox

    def on_keypress(event):
        # nonlocal fullscreen
        key_name = ['b', 'w', 'g', 'c', 'r', 'y', 'p']
        key_action = ['black', '#ecf0f1', '#95a5a6', '#5352ed', '#c0392b', '#f9ca24', '#5f27cd']

        if event.keysym == 'Escape':
            # fullscreen = False
            root.geometry("{}x{}+0+0".format(width, height))
            root.attributes("-fullscreen", False)
        elif event.keysym == 'Tab':
            # fullscreen = True
            root.attributes("-fullscreen", True)
        elif event.keysym in key_name:
            root.config(bg = key_action[key_name.index(event.keysym)])

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.config(bg='black')

    textbox = tk.Text(root, width=width, height=height, bg='black', fg='#424242', font=('楷体', 20))
    textbox.insert('end', '')

    root.bind('<Button-1>', close.delay)
    root.bind("<KeyRelease>", on_keypress)
    root.bind('<Triple-space>', close.on_close)
    root.bind('<Double-space>', close.delay_close)
    root.mainloop()

def main():
    global text, counter, total_counter
    counter = 0
    total_counter = 0
    text = load_txt()
    t1 = th.Thread(target=form).start()
    sleep(2)
    t2 = th.Thread(target=print_data).start()
    close.auto_close()

if __name__ == "__main__":
    main()

