#! usr/bin/env python2.7
# -*- coding:utf-8 -*-

'''
Entrada inicial del Script
utilizaremos el entorno Grafico de Tkinter
que estan en la libreria estandar
'''

__author__ = 'Ing. Jose Florez'
__title__ = 'PyMacros'
__date__ = ''
__version__ = '0.0.1'
__license__ = 'GNU GPLv3'

import sys
import getpass
#from DB import db
from ttk import *
import os
from PIL import Image, ImageTk
import treeView as tv


PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")


class App(tk.Frame):
    def __init__(self, parent=None, conex=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        #self.conex = conex
        #self.conex.query('SELECT `id_sch`, `name_sch`, `state_sch`, \
        #`city_sch`, `add_sch`, `tel_sch`, `contact_sch` FROM `school` ')
        self.ui()
        #self.mainMenu()
        self.estadoBar()
        self.toolBar()
        #self.toolbarLeft()
        self.toolbarleft = tk.Frame(self.parent, relief=tk.GROOVE, bg='white')
                    

    def ui(self):
        '''Aqui van las Macros'''
        self.parent.title('PyMacros V1.0.0')
        #images
        #self.img = Image.open("images/exit.png")
        self.eimg = ImageTk.PhotoImage(Image.open("images/exit.png"))
        self.baseimg = ImageTk.PhotoImage(Image.open("images/access.png"))
        self.runimg = ImageTk.PhotoImage(Image.open("images/run.png"))

    def mainMenu(self):
        #creamos nuestro menu ppal
        menubar = tk.Menu(self.parent, relief=tk.GROOVE)

        # create more pulldown menus
        dbmenu = tk.Menu(menubar, tearoff=0)
        macroNmenu = tk.Menu(dbmenu, tearoff=0)
        macroOmenu = tk.Menu(dbmenu, tearoff=0)

        dbmenu.add_command(label='NewQ2.accdb', command=lambda:
        self.callback('NewQ2.accdb'))

        macroNmenu.add_command(label="Warm Up, (10 Q)", command=self.Mes)
        macroNmenu.add_command(label="SturpShort, (14 Q)",
        command=self.treeView)
        dbmenu.add_cascade(label="NewQ2.accbd, Macros ->", menu=macroNmenu)
        macroOmenu.add_command(label="Macro1, (10 Q)")
        macroOmenu.add_command(label="Macro 2, (14 Q)")
        dbmenu.add_cascade(label="OldQ2.accdb , Macros ->", menu=macroOmenu)
        dbmenu.add_separator()
        dbmenu.add_command(label="Exit", command=self.parent.quit)
        menubar.add_cascade(label="DataBase", menu=dbmenu)

        self.parent.config(menu=menubar)

    def Mes(self):
        otra_ventana = tk.Toplevel(self.parent)
        otra_ventana.resizable(width=False, height=False)
        ## Provoca que la ventana tome el focus
        otra_ventana.focus_set()
        ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        otra_ventana.grab_set()
        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        otra_ventana.transient(master=self.parent)
        ## Crea un widget que permite cerrar la ventana,
        ## para ello indica que el comando a ejecutar es el
        ## metodo destroy de la misma ventana.
        tk.Button(otra_ventana, text="Cerrar", command=otra_ventana.destroy) \
        .grid()
        tk.Label(otra_ventana, text='Bienvenido a nuestra Guia %s'
        % getpass.getuser()) .grid()
        tk.Label(otra_ventana, text='ID:').grid(row=1, column=1, padx=10,
        sticky='n')
        tk.Label(otra_ventana, text='.%d' % self.conex.fetchONE[0]).grid(row=1,
             column=2, padx=10, sticky='s')

    def treeView(self):
        otra = tk.Toplevel(self.parent)
        otra.grab_set()
        #otra.transient(master=self.parent)
        tv.App(otra)

    def estadoBar(self):
        info1 = os.uname()[0]
        info2 = os.uname()[1]
        info3 = os.uname()[2]
        info4 = os.uname()[3]
        info5 = os.uname()[4]
        mensaje = " " + info1 + ": " + info2 + " - " + info3 + \
            " - " + info4 + " - " + info5
        self.barraest = tk.Label(self.parent, text=mensaje, bd=1,
            relief=tk.FLAT, anchor=tk.W)
        self.barraest.pack(side=tk.BOTTOM, fill=tk.X)

    def toolBar(self):
        toolbar = tk.Frame(self.parent)
        b1 = tk.Button(toolbar, text='NewQ2', image=self.baseimg,
            relief=tk.FLAT, compound="top",
            command=lambda: self.toolbarLeft('NewQ2'))
        b1.image = self.eimg
        b1.pack(side=tk.LEFT, padx=0, pady=0)

        b2 = tk.Button(toolbar, text='OldQ2', image=self.baseimg,
            relief=tk.FLAT, compound="top", command=lambda:
            self.toolbarLeft('OldQ2'))
        b2.image = self.eimg
        b2.pack(side=tk.LEFT, padx=0, pady=0)

        base1 = tk.Button(toolbar, text='Exit', image=self.eimg,
            relief=tk.FLAT, command=self.quit, compound="top")
        base1.image = self.eimg
        base1.pack(side=tk.LEFT, padx=0, pady=0)
        toolbar.pack(side=tk.TOP, fill=tk.X)

    def toolbarLeft(self, base=None):
        for elem in self.toolbarleft.winfo_children():
            elem.destroy()    

        canv = tk.Canvas(self.toolbarleft, relief=tk.FLAT,width=150, height=200,
        scrollregion=(0,0,300, 2000), highlightthickness=0)
        canv.scrollY = tk.Scrollbar(self.toolbarleft, orient=tk.VERTICAL)
        canv['yscrollcommand'] = canv.scrollY.set
        canv.scrollY['command'] = canv.yview

        

        if base == 'NewQ2':            
            macros = open('resource/NewQ2Macros.txt', 'r').readlines()            
            nvar = ["m%s" % str(x + 1) for x in range(0, len(macros))]

            nq2Macro1 = tk.Button(self.toolbarleft, text='Warm-Up', relief=tk.FLAT, command=lambda:self.accion('Warm-Up'))
            nq2Macro1.pack(side=tk.TOP, padx=2, pady=2)


            canv.create_window(75, 15, window=nq2Macro1)
            canv.scrollY.pack(side=tk.RIGHT, fill=tk.Y)
            canv.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
            self.toolbarleft.pack(expand=tk.NO, side=tk.LEFT, fill=tk.Y)
            
        else:
            cont = 1
            macros = open('resource/OldQ2Macros.txt', 'r').readlines()
            nvar = ["m%s" % str(x + 1) for x in range(0, len(macros))]

            oq2Macro1 = tk.Button(self.toolbarleft, text='StarmUp', relief=tk.FLAT, command=lambda:self.accion('StarmUp'))
            oq2Macro1.pack(side=tk.TOP, padx=2, pady=2)

            canv.create_window(75,15, window=oq2Macro1)
            canv.scrollY.pack(side=tk.RIGHT, fill=tk.Y)
            canv.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
            self.toolbarleft.pack(expand=tk.NO, side=tk.LEFT, fill=tk.Y)

    def accion(self,macro=None):
        print macro
        

    def callback(self, event):
        if event == 'NewQ2.accdb':
            print ("Debemos Crear un Menu con las opciones de NewQ2")
        else:
            print ("Creamos un Menu con las Opciones de OldQ2")


def main():
    root = tk.Tk()
    conex = db.Base()
    root.geometry('800x600')
    Aplication = App(root, conex)
    Aplication.mainloop()
    conex.desconectar()


if __name__ == "__main__":
    main()
