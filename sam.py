from sketchpy import canvas
import turtle
s=turtle.getscreen()
t1=turtle.Turtle()

pen= canvas.sketch_from_svg('E:\\myimage\\samir.svg',scale=250)
pen.draw()