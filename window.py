from tkinter import *
class LabelDemo(Frame):
  '''Sets up the window and widgets'''
  def __init__(self):
    Frame.__init__(self)
    self.master.title('Label Demo')
    self.grid()
    self._label=Label(self,text='Hello world!')
    self._label.grid()
def main():
   '''Instantiate and pop up the window.'''
   LabelDemo().mainloop()
main()