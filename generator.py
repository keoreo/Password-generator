import string
from tkinter import *
import random
 
 
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.master.config(bg="#D9D9D9")
        self.create_widgets()
 
    def create_widgets(self):
        """настройки генератора"""
        # параметры
        setup_frame = Frame(self.master)
        setup_frame.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        setup = LabelFrame(setup_frame, text=" Настройки генератора ")
        setup.grid(ipadx=114)
        self.var_digits = IntVar()
        self.var_small_letters = IntVar()
        self.var_big_letters = IntVar()
        self.var_special_sign = IntVar()
        digits = Checkbutton(setup, text='Цифры', variable=self.var_digits, onvalue=1, offvalue=0)
        small_letters = Checkbutton(setup, text='Строчные буквы', variable=self.var_small_letters, onvalue=1,
                                    offvalue=0)
        big_letters = Checkbutton(setup, text='Прописные буквы', variable=self.var_big_letters, onvalue=1, offvalue=0)
        special_sign = Checkbutton(setup, text='Специальные символы', variable=self.var_special_sign, onvalue=1,
                                   offvalue=0)
        digits.grid(ipady=2, sticky=W)
        small_letters.grid(ipady=2, sticky=W)
        big_letters.grid(ipady=2, sticky=W)
        special_sign.grid(ipady=2, sticky=W)
        self.length = IntVar()
        slider = Scale(setup, variable=self.length, orient=HORIZONTAL, label="Длина пароля", length=130, from_=8, to=30)
        slider.grid(ipady=2, sticky=W)
        # кнопка 'Создать пароль'
        self.btn = Button(text="Создать пароль", command=self.display_password)
        self.btn.grid(row=1, column=0, pady=2, padx=150, ipady=5, sticky=W)
        # пароль
        self.entry_password = StringVar()
        ent = Entry(width=35, textvariable=self.entry_password)
        ent.grid()
        ent.clipboard_append(self.entry_password)
 
    """создание пароля"""
 
    def generate_password(self):
        final_list = []
        d = self.var_digits.get()
        sl = self.var_small_letters.get()
        bl = self.var_big_letters.get()
        ss = self.var_special_sign.get()
        ln = self.length.get()
        if d:
            final_list.append(string.digits)
        if sl:
            final_list.append(string.ascii_lowercase)
        if bl:
            final_list.append(string.ascii_uppercase)
        if ss:
            final_list.append(string.punctuation)
        bound = d + sl + bl + ss
        if not bound:
            return "Не выбраны настройки пароля"
        password = []
        for i in range(ln):
            if i == 0:
                a = 1
            else:
                a = random.randint(1, bound)
            k = final_list[a - 1]
            b = random.randint(0, len(k) - 1)
            password.append(str(k[b]))
        return ''.join(password)
 
    """вставка пароля в текстовое поле"""
 
    def display_password(self):
        self.entry_password.set(self.generate_password())
 
 
def main():
    root = Tk()
    root.title('Генератор паролей')
    root.geometry("400x350")
    root.resizable(FALSE, FALSE)
    app = Application(root)
    root.mainloop()