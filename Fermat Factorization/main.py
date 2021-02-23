import tkinter as tk
from client.interface import MainForm

def main():
    root = tk.Tk()
    MainForm(root)
    root.mainloop()

if __name__ == '__main__':
    main()