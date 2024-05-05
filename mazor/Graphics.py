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
        self.__canvas = Canvas(self.__root,height=self.height,width=self.width)
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

    def draw_line(self,line,fill_color):
        line.draw(self.__canvas,fill_color)
    
    def close(self):
        self.__is_running = False 

class Point:
    def __init__(self,x,y):
        # x cooridante(horizontal) in pixels of the point 
        # y coordiante(vertical) in pixels of the point 
        self.x = x
        self.y = y 

    
class Line:
    def __init__(self,point1:Point,point2:Point):
        self.point1 = point1 
        self.point2 = point2
    
    def draw(self,canvas: Canvas,fill_color):
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y,fill=fill_color,width=2)

