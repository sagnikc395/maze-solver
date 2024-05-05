from tkinter import Tk,BOTH,Canvas 

class Window:
    
    def __init__(self,width,height):
        self.width = width 
        self.height = height 
        # create a new root widget 
        self.__root = Tk()
        # set tht title property of the root widget 
        self.__root.title("maze-solver")
        # canvas widget and set to data member 
        self.__canvas = Canvas(self.__root,heigh=self.height,width=self.width)
        self.__canvas.pack()
        self.__is_running = False 
        self.__root.protocol("WM_DELETE_WINDOW",self.close)


    def redraw(self):
        self.__root.update_idletasks() 
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True 
        while self.__is_running:
            self.redraw()
        print("window closed ...")

    def close(self):
        self.__is_running = False 
