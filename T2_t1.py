from tkinter import *
from tkinter import messagebox

def check_temperature():
    try:
        temp = int(entry.get())
        if temp <= 0:
            conclusion = "A cold, isn’t it?"
        elif 0 < temp < 10:
            conclusion = "Cool"
        else:
            conclusion = "Nice weather we’re having.."
        messagebox.showinfo("Висновок", conclusion)
    except ValueError:
        messagebox.showerror("Щось пішло не так...")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

window = Tk()
window.title('Яка погода?')
win_width = 600
win_height = 400
center_window(window, win_width, win_height)
window.resizable(width = False, height = False)
window.config(bg = '#78A577')
photo = PhotoImage(file = 'predictor_logo.png')
window.iconphoto(False, photo)

main_txt = Label(window, 
    text = "Яка у Вас температура?", 
    bg = '#78A577', 
    fg = '#333333', 
    font = ('Comic Sans MS', 24, 'bold', 'italic'),
    pady = 20
    )

main_txt.pack()

entry = Entry(window, font = ('Arial', 20), width = 10, justify = 'center', bd = 2, relief = SOLID, fg = '#333333', bg = '#F0F0F0')
entry.pack(pady = 20)

def on_enter(a):
    check_button['bg'] = '#FFBAA5'

def on_leave(a):
    check_button['bg'] = '#FF8E6B'

check_button = Button(window, 
    text = 'Глянути', 
    command = check_temperature, 
    font = ('Comic Sans MS', 18, 'bold'), 
    bg = '#FF8E6B', 
    fg = '#333333', 
    activebackground = '#FF8E6B', 
    activeforeground = '#FFAB91',
    relief = FLAT,
    bd = 0
)
check_button.pack(pady = 20)
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)

window.mainloop()