from Canvas import Canvas
from Shapes import Rectangle, Square

canvas_height = int(input("Enter the height of your canvas: "))
canvas_width =  int(input("Enter the width of you canvas: "))


colors = {"white": (255,255,255), "black": (0,0,0)}
canvas_color = input("Enter canvas color (white or black): ")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


while True:
    shape_type = input("what shape do you like to draw (Square or Rectangle)? enter Quit to quit? :")
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter X of the rectangle: "))
        rec_y = int(input("Enter Y of the rectangle: "))
        rec_height = int(input("Enter height of your rectangle: "))
        rec_width = int(input("Enter width of your rectangle: "))
        red = int(input("How much red should your rectangle have: "))
        green = int(input("How much green should your rectangle have: "))
        blue = int(input("How much blue should your rectangle have"))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red,green,blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sqr_x = int(input("Enter the x of the square: "))
        sqr_y = int(input("Enter the y of the square: "))
        sqr_side = int(input("Enter the length of side of square: "))
        red = int(input("how much red should your square have: "))
        green = int(input("How much green should your square have: "))
        blue = int(input("How much blue should your square have "))

        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red,green,blue))
        s1.draw(canvas)

    if shape_type.lower() == "quit":
        break

canvas.make("canvas.png")
