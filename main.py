# creating a window class 

from tkinter import Tk,BOTH,Canvas 

class Window:
    __is_running = False 
    
    def __init__(self,width,height):
        self.width = width 
        self.height = height 
        # create a new root widget 
        self.__root = Tk()
        # set tht title property of the root widget 
        self.__root.title("maze-solver")
        # canvas widget and set to data member 
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__is_running = False 

    def redraw(self):
        #self.__root.update()
        self.__root.update_idletasks() 
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True 
        self.redraw()

    def close(self):
        self.__is_running = False 
        self.__root = Tk() 
        self.__root.protocol("WM_DELETE_WINDOW",self.close)

def main():
    win = Window(800,600)
    win.wait_for_close()

if __name__ == '__main__':
    main()