
import turtle 

class DrawStructures():
    
    def __init__(self,circle_color, square_color):
        self.circle_color = circle_color
        self.square_color = square_color
        self.window = turtle.Screen()
        self.cursor = turtle.Turtle()
        self.window.bgcolor('white')
        self.cursor.shape('turtle')
        self.cursor.speed(2)        
        self.window.exitonclick()
        
    def square(self):

        self.cursor.color(self.square_color)
        
        for i in range(4):
            self.cursor.forward(100)
            self.cursor.right(90)
             
    
    def circle(self):
                
        self.cursor.color(self.circle_color)

        self.cursor.circle(100)
        
        

a = DrawStructures('red', 'blue')
a.circle()
a.square()