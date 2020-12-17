from tools.lenstra import lenstra
from tkinter import *
import time
from win32com.client import GetObject


# Tkinter interface
class Interface(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.window_w = 600
        self.window_h = 400

        self.centerWindow()
        self.initUI()

    def initUI(self):
        self.parent.title('Factorization Lensta')
        self.parent['bg'] = '#fafafa'

        self.parent.resizable(width=False, height=False)

        self.frame = Frame(self.parent, bg='#fafafa')
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field N
        self.label_n = Label(self.frame, text='Entry N:', bg='#fafafa', font=20)
        self.label_n.place(x=20, y=20)
        self.entry_n = Entry(self.frame, width=40, justify='center')
        self.entry_n.place(x=120, y=24)
        self.entry_n.insert(0, 301139059106225493824641)

        # Field B
        self.label_b = Label(self.frame, text='Entry B:', bg='#fafafa', font=20)
        self.label_b.place(x=20, y=60)
        self.entry_b = Entry(self.frame, width=40, justify='center')
        self.entry_b.place(x=120, y=64)
        self.entry_b.insert(0, 900)

        # Field for number of curve
        self.label_c = Label(self.frame, text='Entry curve:', bg='#fafafa', font=20)
        self.label_c.place(x=20, y=100)
        self.entry_c = Entry(self.frame, width=25, justify='center')
        self.entry_c.place(x=210, y=104)
        self.entry_c.insert(0, 10000)

        # Field button
        self.btn = Button(self.frame, text='Factorization', bg='gray', command=self.button_click)
        self.btn.place(x=440, y=50)

        # Field for label of output
        self.output = Text(self.frame, width=70, height=12)
        self.output.place(x=15, y=180)

        # Use win32com.client for get CPU Name on current PC
        root_winmgmts = GetObject("winmgmts:root\cimv2")
        cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
        self.cpu_info = Label(self.frame, text='Info about CPU: {}'.format(cpus[0].Name), bg='#fafafa', font=20)
        self.cpu_info.place(x=15, y=140)


    def button_click(self):
        n = int(self.entry_n.get())
        b = int(self.entry_b.get())
        n_curves = int(self.entry_c.get())

        start_time = time.time()
        res = lenstra(n, b, n_curves, 0)
        stop_time = time.time()
        self.output.delete(1.0, END)

        if res is None:
            self.output.insert(1.0, 'Failed attempt.\n'
                                     'try increasing parameter B or the number of curves.')
            return

        txt = f"Factorization:\n{n} = {res[0][0]} * {res[0][1]}\n\n" \
              f"Tested {res[1]} curves\n\nPoint - P{res[2]}\n\n" \
              f"Curve: {res[3]}\n\nTime working - {stop_time - start_time} seconds"

        self.output.insert(1.0, txt)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))