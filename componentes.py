from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *


class Bframe(tb.Frame):
    def __init__(self, master, color = "dark", border = 1):
        super().__init__(master = master, bootstyle = color)
        self.border = border
         
        # Criação da estrutura interna
        self.dentro = tb.Frame(self)
        self.dentro.pack(fill='both', expand=True, padx=self.border, pady= self.border)
        '''self.dentro.grid(padx=self.border_width, pady=self.border_width, sticky=NSEW)'''
       
        

class Lcampo(tb.Frame):
    def __init__(self, master, texto = "", color = "dark", border = 1, width = 0, data = False):
        super().__init__(master = master, bootstyle = color)
        self.texto = texto
        self.border = border
        self.width = width
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)
        self.dentro = tb.Frame(self)
        self.dentro.pack(fill='both', expand=True, padx=self.border, pady= self.border)
        self.dentro.columnconfigure(0,weight=1)
        self.dentro.rowconfigure(0, weight=1)
        self.label = tb.Label(self.dentro, text=texto, anchor="center")
        self.label.grid(padx=5, pady=5, sticky=NSEW)
        if data: 
            self.campo = tb.DateEntry(self.dentro)
            self.campo.entry.delete(0,END)
        else: 
            self.campo = tb.Entry(self.dentro)
        self.campo.grid(padx=5, pady=5, sticky=NSEW)
        if self.width != 0:
            self.campo.configure(width=self.width)

class Lcheck(tb.Frame):
    def __init__(self, master, texto = ""):
        super().__init__(master = master)
        self.texto = texto
        self.var = IntVar()
        self.campo = tb.Checkbutton(self, variable=self.var)
        self.campo.grid(row = 0, column=0, padx=3, pady=5)
        self.var.set(0)
        self.label = tb.Label(self, text=texto)
        self.label.grid(row=0, column=1, pady=5)

class Lcombo(tb.Frame):
    def __init__(self, master, texto = "", opcoes = [], color = "dark", border = 1):
        super().__init__(master = master, bootstyle = color)
        self.texto = texto
        self.opcoes = opcoes
        self.border = border
        self.dentro = tb.Frame(self)
        self.dentro.pack(fill='both', expand=True, padx=self.border, pady= self.border)
        '''self.dentro.grid(padx=self.border, pady=self.border, sticky=NSEW)'''
        self.label = tb.Label(self.dentro, text=texto, anchor="center")
        self.label.grid(padx=5, pady=5, sticky=NSEW)
        self.campo = tb.Combobox(self.dentro, values=self.opcoes)
        self.campo.grid(padx=5, pady=5, sticky=NSEW)






