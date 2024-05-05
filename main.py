from mazor import Graphics

def main():
    win = Graphics.Window(800,600)
    l = Graphics.Line(Graphics.Point(50,50),Graphics.Point(400,400))
    win.draw_line(l,"black")
    win.wait_for_close()

if __name__ == '__main__':
    main()