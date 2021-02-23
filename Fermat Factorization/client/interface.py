from tkinter import *
from tkinter import messagebox as mb
from tools.fermat import factorization

# Tkinter interface
class MainForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.parent.resizable(width=False, height=False)

        self.window_w = 400
        self.window_h = 180

        self.centerWindow()
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('Fermat\'s Factorization')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field N
        self.label_n = Label(self.frame, text='Entry N:', bg='#fafafa', font=20)
        self.entry_n = Entry(self.frame, justify='center')

        # Field button
        self.btn_fact= Button(self.frame, text='Factorization', bg='gray', command=self.button_factorization)

        # Field Result
        self.label_result = Label(self.frame, text="N = P*Q:", bg='#fafafa', font=20)

        # Field P
        self.label_p = Label(self.frame, text='P', bg='#fafafa', font=20)
        self.result_p = Text(self.frame)

        # Field Q
        self.label_q = Label(self.frame, text='Q', bg='#fafafa', font=20)
        self.result_q = Text(self.frame)

    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field A
        self.label_n.place(x=20, y=20)
        self.entry_n.place(x=100, y=24, width=260)

        # Field button
        self.btn_fact.place(x=160, y=50, width=110, height=25)

        # Field Result
        self.label_result.place(x=180, y=80)

        # Result P
        self.label_p.place(x=45, y=102)
        self.result_p.place(x=100, y=105, width=260, height=20)

        # Result Q
        self.label_q.place(x=45, y=142)
        self.result_q.place(x=100, y=145, width=260, height=20)

    def button_factorization(self):
        try:
            n = int(self.entry_n.get())
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return

        if not n > 0 or n % 2 == 0:
            mb.showerror("Error", 'Please enter an positive odd number')
            return

        P, Q = factorization(n)

        self.result_p.delete(1.0, END)
        self.result_p.insert(1.0, P)

        self.result_q.delete(1.0, END)
        self.result_q.insert(1.0, Q)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))