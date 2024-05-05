from mazor import Graphics

Line =Graphics.Line
Point = Graphics.Point

class Cell:
    def __init__(self,win):
        self._x1 = None
        self._x2 = None 
        self._y1 = None  
        self._y2 = None  
        self._win = win 
        self.has_left_wall = True 
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_bottom_wall = True 
    
    def draw(self,x1,y1,x2,y2):
        self._x1 = x1
        self._y1 = y1 
        self._x2 = x2
        self._y2 = y2 
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self._win.draw_line(line)

    def draw_move(self,to_cell,undo=False):
        len1 = abs(self._x2 - self._x1) // 2
        x_center = len1 + self._x1 
        y_center = len1 + self._y1 

        len2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = len2 + to_cell._x1
        y_center2 = len2 + to_cell._y1 

        fill_order = "red"
        if undo:
            fill_order = "gray"
        
        line = Line(Point(x_center,y_center),Point(x_center2,y_center2))
        self._win.draw_line(line,fill_order)
        




    
