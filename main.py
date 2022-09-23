import turtle

def InputInteger(colour):
    while True:
        try:
            if colour == "red":
                userInput = int(input("Enter the RED value: "))
            elif colour == "green":
                userInput = int(input("Enter the GREEN value: "))
            elif colour == "blue":
                userInput = int(input("Enter the BLUE value: "))
        except ValueError:
            print("Error, you must enter an integer.")
        else:
            if userInput < 0 or userInput > 255:
                print("Error, you must enter an integer between 0 and 255.")
            else:
                return userInput

def ConvertRGB(value):
    value = str(hex(value)[2:])
    if len(value) == 1:
        value = "0" + value
    return value

def DrawSquare(board,x,y,width,height,color):
    board.speed(0)

    #Colour of square
    board.fillcolor(color)
    board.begin_fill()
    board.pencolor(color)

    #Go to position
    board.up()
    board.goto(x,y)
    board.down()

    #Draw the sides
    board.forward(width)
    board.right(90)
    board.forward(height)
    board.right(90)
    board.forward(width)
    board.right(90)
    board.forward(height)

    board.end_fill()

red = InputInteger("red"); R = ConvertRGB(red)
green = InputInteger("green"); G = ConvertRGB(green)
blue = InputInteger("blue"); B = ConvertRGB(blue)
initialHex = str("#" + R + G + B)

compRed = 255 - red; compR = ConvertRGB(compRed)
compGreen = 255 - green; compG = ConvertRGB(compGreen)
compBlue = 255 - blue; compB = ConvertRGB(compBlue)
compHex = str("#" + compR + compG + compB)

turtle.setup(400, 200)
turtle.title("Complementary Colour Finder")
turtle.hideturtle()

board = turtle.Turtle()
DrawSquare(board,-200,100,200,200,initialHex)
print("\nOriginal Colour: "); print("  - RGB: " + str(red) + ", " + str(green) + ", " + str(blue)); print("  - HEX:",initialHex)

board = turtle.Turtle()
DrawSquare(board,0,100,200,200,compHex)
print("\nComplementary Colour: "); print("  - RGB: " + str(compRed) + ", " + str(compGreen) + ", " + str(compBlue)); print("  - HEX:",compHex)

turtle.done()