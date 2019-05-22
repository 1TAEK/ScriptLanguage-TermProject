# # from tkinter import*
# #
# # window = Tk()
# # window.title('Canvas')
# # window.geometry('400x600')
# # canvas = Canvas(window, bg='white', scrollregion=(0, 0, 400, 20000))
# # canvas.pack(fill='both', expand=True)
# #
# # vbar = Scrollbar(canvas, orient='vertical')
# # vbar.pack(side='right', fill='y')
# # vbar.config(command=canvas.yview)
# #
# # canvas.config(yscrollcommand=vbar.set)
# # canvas.create_text(5, 0, anchor='nw', text="Choose users: ")
# #
# # f = Frame(canvas)
# # canvas.create_window((200, 0), window=f, anchor="n")
# # Label(f,text = "11566156165",width = 10, height = 10,bg="blue").pack()
# #
# # f1 = Frame(canvas)
# # canvas.create_window((200, 0), window=f1, anchor="n")
# # Label(f1,text = "11566156165",bg="blue").pack()
# #
# # window.mainloop()
#
# from tkinter import Scrollbar as tkScrollBar
# from tkinter import Frame as tkFrame
# from tkinter import Canvas as tkCanvas
# from tkinter import Entry as tkEntry
# from tkinter import StringVar as tkStringVar
# from tkinter import Tk, HORIZONTAL, N, S, E, W, RIGHT, LEFT, BOTTOM, X, Y, BOTH
# from tkinter import TOP
#
#
# class Widget(tkFrame):
#     def __init__(self, master=None):
#         tkFrame.__init__(self, master)
#
#         self._str    = tkStringVar()
#         self._widget = tkEntry(self)
#
#         self._widget.config(textvariable=self._str, borderwidth=1, width=0)
#         self._widget.pack(expand=True, fill=X)
#
#     def settext(self, str_):
#         self._str.set(str_)
#
#     def gettext(self):
#         return self._str.get()
#
#
# class Application(tkFrame):
#     def __init__(self, rows, cols, master=None):
#         tkFrame.__init__(self, master)
#
#         yScroll = tkScrollBar(self)
#         xScroll = tkScrollBar(self, orient=HORIZONTAL)
#
#         self._canvas = tkCanvas(self,
#                 yscrollcommand=yScroll.set, xscrollcommand=xScroll.set)
#         yScroll.config(command=self._canvas.yview)
#         xScroll.config(command=self._canvas.xview)
#
#         self._table      = [[0 for x in range(rows)] for x in range(cols)]
#         self._tableFrame = tkFrame(self._canvas)
#
#         for col in range(cols):
#             self._tableFrame.grid_columnconfigure(col, weight=1)
#             for row in range(rows):
#                 self._table[row][col] = Widget(master=self._tableFrame)
#                 self._table[row][col].settext("(%d, %d)" % (row, col))
#                 self._table[row][col].grid(row=row, column=col, sticky=E+W)
#
#         # For debugging
#         self._canvas.config(background="blue")
#         self._tableFrame.config(background="red")
#
#         yScroll.pack(side=RIGHT, fill=Y)
#         xScroll.pack(side=BOTTOM, fill=X)
#
#         self._canvas.create_window(0, 0, window=self._tableFrame, anchor=N+W)
#         self._canvas.pack(side=LEFT, fill=BOTH, expand=True)
#
#
# tkRoot  = Tk()
#
# # Application Size and Center the Application
# appSize = (800, 600)
# w       = tkRoot.winfo_screenwidth()
# h       = tkRoot.winfo_screenheight()
#
# x = w / 2 - appSize[0] / 2
# y = h / 2 - appSize[1] / 2
# tkRoot.geometry("%dx%d+%d+%d" % (appSize + (x, y)))
# tkRoot.update_idletasks() # Force geometry update
#
# app = Application(5, 5, master=tkRoot)
# app.pack(side=TOP, fill=BOTH, expand=True)
# tkRoot.mainloop()

from tkinter import*
from common import scrollLayout

window = Tk()
a = scrollLayout.ScrollLayout(window,(0,0,400,2400))
a.pack()
window.mainloop()