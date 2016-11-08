import turtle

def make_square(something):
    for i in range(4):
        something.forward(100)
        something.right(90)    

def geometry():
    window = turtle.Screen()
    window.bgcolor('red')
    
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
    
    for i in range(36):
        make_square(brad)
        brad.right(10)
    

#    angie = turtle.Turtle()
#    angie.shape('turtle')
#    angie.color('orange')
#    angie.speed(2)
#    
#    for i in range(4):
#        angie.circle(100)
#        angie.right(90)        
#        
#
#    callo = turtle.Turtle()
#    #callo.shape('turtle')
#    callo.color('purple')
#    callo.speed(2)
#    
#    callo.forward(100)
#    callo.right(90)
#    callo.forward(100)
#    callo.right(135)
#    callo.forward(144.4)    
    
      
    window.exitonclick()



geometry()

