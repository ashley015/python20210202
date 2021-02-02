import turtle,time



yy=turtle.Turtle()
yy.color('white')
yy.shape('turtle')
xx=turtle.Screen()
xx.bgcolor('black')

num_sides=int(input('要畫幾邊形(3-10):'))
side_length=70

angle=360.0/num_sides

for i in range(num_sides):
    yy.forward(side_length)
    yy.right(angle)
    time.sleep(1)
    
turtle.done()