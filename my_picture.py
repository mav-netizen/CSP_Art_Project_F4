import simple_graphics as sg

def draw_cloud(x, y):
    sg.set_outline_color("white")
    sg.set_fill_color("white")
    sg.fill_rectangle(x-60, y-20, 120, 40)
    sg.fill_rectangle(x-40, y-40, 80, 80)
    
    
def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    sg.set_outline_color("green")
    sg.set_fill_color ("green")
    sg.fill_rectangle(0, 280,600, 400)
    sg.set_fill_color("cyan")
    sg.fill_rectangle(0, 0, 600, 280)
    sg.set_fill_color("blue")
    sg.set_outline_color("blue")
    sg.fill_rectangle(450, 280,100, 25)
    sg.fill_rectangle(425, 300,100, 25)
    sg.fill_rectangle(400, 320,100, 25)
    sg.fill_rectangle(375, 340,100, 25)
    sg.fill_rectangle(350, 360,100, 25)
    sg.fill_rectangle(325, 380,100, 25)


if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
