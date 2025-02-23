# Version 1.0.0.50
# By YXStudio 2023~2025.
# Feb.22nd,2025


from tkinter import *
import subprocess


root = Tk()

def creatival():
    def crea_wave_g():
        subprocess.run(['python','_internal/crea_wav_g.py'])
    def crea_flat_g():
        subprocess.run(['python','_internal/crea_fla_g.py'])
    def crea_wave_s():
        subprocess.run(['python','_internal/crea_wav_s.py'])
    def crea_flat_s():
        subprocess.run(['python','_internal/crea_fla_s.py'])

    crea = Tk()

    crea.geometry('450x250')
    crea.iconbitmap('_internal/icon/icon.ico')
    crea.title('MINECRAFT 1.0.0.50 - New World - Creatival')


    label1 = Label(crea,text='MINECRAFT',font=('minecrafter',36),foreground='#262626')
    label2 = Label(crea,text='Creatival',font=('minecraft ae pixel',14),foreground='#8F8F8F')

    button1 = Button(crea,command=crea_wave_g,text='Wave And Grass Landform',font=('minecraft',14),width=25,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')
    button2 = Button(crea,command=crea_flat_g,text='Flat And Grass Landform',font=('minecraft',14),width=25,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')
    button3 = Button(crea,command=crea_wave_s,text='Wave And Sand Landform' ,font=('minecraft',14),width=25,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')
    button4 = Button(crea,command=crea_flat_s,text='Flat And Sand Landform' ,font=('minecraft',14),width=25,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')

    label1.pack()
    label2.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

    crea.mainloop()

def survival():
    def random_landform():
        subprocess.run(['python','_internal/survival.py'])
    
    surv = Tk()

    surv.geometry('450x250')
    surv.iconbitmap('_internal/icon/icon.ico')
    surv.title('MINECRAFT 1.0.0.50 - New World - Survival')


    label1 = Label(surv,text='MINECRAFT',font=('minecrafter',36),foreground='#262626')
    label2 = Label(surv,text='Survival',font=('minecraft ae pixel',14),foreground='#8F8F8F')

    button1 = Button(surv,command=random_landform,text='Random Landform',font=('minecraft',14),width=25,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')
    

    label1.pack()
    label2.pack()

    button1.pack()

    surv.mainloop()

def new_world():
    new = Tk()

    new.geometry('600x350')
    new.iconbitmap('_internal/icon/icon.ico')
    new.title('MINECRAFT 1.0.0.50 - New World')


    label1 = Label(new,text='MINECRAFT',font=('minecrafter',48)       ,foreground='#262626')
    label2 = Label(new,text='New World',font=('minecraft ae pixel',20),foreground='#8F8F8F')

    padding1 = Label(new,text='',font=('微软雅黑',18))
    button1 = Button(new,command=creatival,text='Creatival',font=('minecraft',20),width=25,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')
    button2 = Button(new,command=survival ,text='Survival' ,font=('minecraft',20),width=25,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')

    label1.pack()
    label2.pack()

    padding1.pack()
    button1.pack()
    button2.pack()

    new.mainloop()

def about():
    subprocess.run(['python','main/about.py'])


def main():
    root.geometry('850x450')
    root.iconbitmap('_internal/icon/icon.ico')
    root.title('MINECRAFT 1.0.0.50')


    label1 = Label(root,text='MINECRAFT'     ,font=('minecrafter',54)       ,foreground='#262626')
    label2 = Label(root,text='Python Edition',font=('minecraft ae pixel',20),foreground='#8F8F8F')

    padding1 = Label(root,text='',font=('微软雅黑',16))
    button1 = Button(root,command=new_world ,text='New World' ,font=('minecraft',20),width=30,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')
    button2 = Button(root                   ,text='Open World (Will Be Open)',font=('minecraft',20),width=30,height=1,foreground='white',background='#505050',activeforeground='white',activebackground='#505050')

    padding2 = Label(root,text='',font=('微软雅黑',36))
    button3 = Button(root,command=about,text='About',font=('minecraft',20),width=30,height=1,foreground='white',background='grey',activeforeground='white',activebackground='#707070')
    padding3 = Label(root,text='',font=('微软雅黑',12))
    

    label1.pack()
    label2.pack()

    padding1.pack()
    button1.pack()
    button2.pack()

    padding2.pack()
    button3.pack()
    padding3.pack()

    root.mainloop()    

main()