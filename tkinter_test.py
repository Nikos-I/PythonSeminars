# import tkinter as tk
 
# window = tk.Tk()
 
# label = tk.Label(
#     text="Привет, Tkinter!",
#     fg="white",
#     bg="black",
#     width=200,
#     height=20
# )
 
# label.pack()
# window.mainloop()

import tkinter as tk
 
window = tk.Tk()



# Надпись

label = tk.Label(text="Имя")
text_box = tk.Text(relief=tk.RIDGE, borderwidth=5)

# Поле ввода

e_name = ''
text_box.insert('1.0',e_name)

# Фреймы 

frame_a = tk.Frame(relief=tk.RAISED, borderwidth=5)
frame_b = tk.Frame(relief=tk.RIDGE, borderwidth=5)

entry = tk.Entry(master = frame_a, relief=tk.RIDGE, borderwidth=3)

entry.delete(0, tk.END)
entry.insert(0, 'Иванов')
e_name = entry.get()
 
label_a = tk.Label(master=frame_a, text="I'm in Frame A", relief=tk.RIDGE, borderwidth=5)
label_a.pack()
 
label_b = tk.Label(master=frame_b, text="I'm in Frame B", relief=tk.RAISED, borderwidth=5)
label_b.pack()
# entry.master = frame_a
entry.pack() 

# Кнопка
 
button = tk.Button(
    master=frame_a,
    text="Нажми на меня!",
    width=20,
    height=3,
    bg="blue",
    fg="yellow",
    relief=tk.RAISED, 
    borderwidth=5
)
print(button.master)
button.pack()

frame_a.pack()
frame_b.pack()
 


# entry.setvar(e_name[2,])

label.pack()
text_box.pack()


t_name = text_box.get("1.0", tk.END)
text_box.insert("1.0", "Hello\n")

text_box.insert(tk.END, "\nВставь меня в новую строку!")
# name = entry.get()

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
 
# Рельеф рамки
for relief_name, relief in border_effects.items():
    frame0 = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame0.pack(side=tk.LEFT)
    label = tk.Label(master=frame0, text=relief_name)
    label.pack()
 

frame2 = tk.Frame(master=window, width=150, height=150, relief=tk.RAISED, borderwidth=5)
frame2.pack()
 
label1 = tk.Label(master=frame2, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)
 
label2 = tk.Label(master=frame2, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)




window.mainloop()