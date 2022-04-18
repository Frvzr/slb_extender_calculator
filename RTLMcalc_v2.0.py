import tkinter
from tkinter import messagebox, RIGHT, END, StringVar, Event, LEFT, SINGLE
import tkinter.ttk as ttk

def langSelect(selection):
    pass

#функция очистки
def clear_data():
    srx_shoulder_entry.delete(0, END)
    xover_length_entry.delete(0, END)
    label_1.place_forget()
    label_in_min.place_forget()
    label_min.place_forget()
    label_in_max.place_forget()
    label_max.place_forget()
    
def delete_srx_shoulder(event):
    srx_shoulder_entry.delete(0,END)
    usercheck=True

def delete_xover_length(event):
    xover_length_entry.delete(0, END)
    passcheck=True
    
#функция для подсчета рзультата    
def get_result():
    input_shoulder_length = float(srx_shoulder_entry.get())
    input_xover_length = float(xover_length_entry.get())
    min_value = float(79)
    inch_to_mm = float(25.4)
    max_value = float(82)
    
    label_1.place(x=40, y=260)
    label_min.place(x = 170, y = 80)
    label_in_min.place(x=170, y=100)
    label_max.place(x=170, y=140)
    label_in_max.place(x=170, y=160)
    
    res_min = float(input_shoulder_length + input_xover_length + min_value)
    label_min["text"] = res_min
    
    res_in_min = float(res_min / inch_to_mm)
    res_in_min = round(res_in_min, 3)
    label_in_min["text"] = res_in_min
    label_in_min.config(font=('Arial',10,'bold'))

    res_max = float(input_shoulder_length + input_xover_length + max_value)
    label_max["text"] = res_max
    
    res_in_max = float(res_max / inch_to_mm)
    res_in_max = round(res_in_max, 3)
    label_in_max["text"] = res_in_max
    label_in_max.config(font=('Arial',10,'bold'))

    res_min_error = res_in_min
    if float(res_min_error) < 41.22:
        label_1["text"] = "Меньше минимально допустимой длины 41.28in"
        label_1.config(font=('Arial', 14, 'bold'), width=40, fg="red")
    elif float(res_min_error) > 44.02:
        label_1["text"] = "Больше максимально допустимой длины 44.02in"
        label_1.config(font=('Arial', 14, 'bold'), width=40, fg="red")
    else:
        label_1["text"] = "Длина в допустимых пределах"
        label_1.config(font=('Arial', 15, 'bold'), width=40, fg="green")

    if srx_shoulder_entry.get() == "0":
        label_1["text"] = "Введите корректные данные"
        label_1.config(font=('Arial', 15, 'bold'), width=40, fg='red')
        label_in_min.place_forget()
        label_min.place_forget()
        label_in_max.place_forget()
        label_max.place_forget()
    elif xover_length_entry.get() == "0":
        label_1["text"] = "Введите корректные данные"
        label_1.config(font=('Arial', 15, 'bold'), width=40, fg="red")
        label_in_min.place_forget()
        label_min.place_forget()
        label_in_max.place_forget()
        label_max.place_forget()
        
def return_result(event):
    get_result()
            
#меню About RTLMcalc
def insert_text():
    messagebox.showinfo("ADS SRX/RTLM calculator", "Version 2.0\nUpdate 05.12.2019\n(c) IKoposhilov, 2019")

class tableinmm(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("in = mm")
        self.geometry('220x305')
        self.resizable(0, 0)
        t = SimpleTable(self, 16,2)
        t.pack(side="top", fill="x")
        t.set(0,0,"Inch n/n")
        t.set(0,1, "Inch n.n..")
        t.set(1,0, "1/16")
        t.set(1,1, "0.0625")
        t.set(2,0, "2/16")
        t.set(2,1, "0.125")
        t.set(3,0, "3/16")
        t.set(3,1, "0.1875")
        t.set(4,0, "4/16")
        t.set(4,1, "0.25")
        t.set(5,0, "5/16")
        t.set(5,1, "0.3125")
        t.set(6,0, "6/16")
        t.set(6,1, "0.375")
        t.set(7,0, "7/16")
        t.set(7,1, "0.435")
        t.set(8,0, "8/16")
        t.set(8,1, "0.5")
        t.set(9,0, "9/16")
        t.set(9,1, "0.5625")
        t.set(10,0, "10/16")
        t.set(10,1, "0.625")
        t.set(11,0, "11/16")
        t.set(11,1, "0.6875")
        t.set(12,0, "12/16")
        t.set(12,1, "0.75")
        t.set(13,0, "13/16")
        t.set(13,1, "0.8125")
        t.set(14,0, "14/16")
        t.set(14,1, "0.875")
        t.set(15,0, "15/16")
        t.set(15,1, "0.9375")
        
class SimpleTable(tkinter.Frame):
    def __init__(self, parent, rows=16, columns=2):
        tkinter.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tkinter.Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

#menu Exit
def menu_exit():
    root.destroy()
    exit()
    
def button_exit(event):
    menu_exit()

# Интерфейс

root = tkinter.Tk()
root.title("ADS SRX/RTLM calculator") #название в шапке
root.geometry('550x340')      #размер окна
root.resizable(0, 0) #запрет на изменение размера окна

#меню
main_menu = tkinter.Menu()
root.config(menu=main_menu)

file_menu = tkinter.Menu()
file_menu.add_command(label="About", command = insert_text)
file_menu.add_command(label="in = mm", command = tableinmm)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=menu_exit)

main_menu.add_cascade(label="File", menu = file_menu)

#задаем название лэйблов
srx_shoulder_label = tkinter.Label(text="Расстояние от торца SRX до торца картриджа (без плага)(мм):")
xover_length_label = tkinter.Label(text="Длина переводника между торцами (мм):")
res_lenght_min_label = tkinter.Label(text="Минимальная длина в мм:")
res_lenght_in_min_label = tkinter.Label(text="Минимальная длина в in:")
res_lenght_max_label = tkinter.Label(text="Максимальная длина в мм")
res_lenght_in_max_label = tkinter.Label(text="Максимальная длина в in")
label_el = tkinter.Label(text="____________________________________________________________________________________",font ='arial 8')
label_1 = tkinter.Label()
label_min = tkinter.Label()
label_in_min = tkinter.Label()
label_max = tkinter.Label()
label_in_max = tkinter.Label()
label_el2 = tkinter.Label(text="____________________________________________________________________________________",font ='arial 8')

#задаем положение лэйблов
srx_shoulder_label.place(x = 10, y = 10)
xover_length_label.place(x = 10, y = 35)
res_lenght_min_label.place(x = 10, y = 80)
res_lenght_in_min_label.place(x = 10, y = 100)
res_lenght_max_label.place(x = 10, y = 140)
res_lenght_in_max_label.place(x = 10, y = 160)
label_el.place(x=10, y = 55)
label_1.place(x = 40, y = 270)
label_min.place(x = 170, y = 80)
label_in_min.place(x = 170, y = 100)
label_max.place(x = 170, y = 140)
label_in_max.place(x = 170, y = 160)
label_el2.place(x = 10, y = 180)

z=StringVar()
x=StringVar()
usercheck=False
passcheck=False

#задаем поле для ввода
srx_shoulder_entry = tkinter.Entry(root,textvariable=z, justify=RIGHT)
xover_length_entry = tkinter.Entry(root,textvariable=x, justify=RIGHT)

#выпадающий список v3
lang_label = tkinter.Label(text = 'Выбор языка:')
lang_label.place(x = 380, y = 300)
combobox = ttk.Combobox(values = [u"Rus",u"Eng"],state='readonly', width = 7)
combobox.set(u"Rus")
combobox.place(x = 465, y = 300)

#расположение поля ввода
srx_shoulder_entry.place(x=370, y = 10)
xover_length_entry.place(x=370, y = 35)

#вставка начальных данных
srx_shoulder_entry.insert(0,0)
xover_length_entry.insert(0,0)

#кнопки
display_button = tkinter.Button(text = "Результат", command = get_result)
clear_button = tkinter.Button(text = "Очистить", command = clear_data)

#расположение кнопок
display_button.place(x = 200, y = 220)
clear_button.place(x = 280, y = 220)

srx_shoulder_entry.bind("<Button>",delete_srx_shoulder)
xover_length_entry.bind("<Button>",delete_xover_length)

root.bind("<Return>", return_result)
root.bind("<Escape>", button_exit)

root.mainloop()
