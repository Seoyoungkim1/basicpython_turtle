Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> def circle():
...     for i in range(10):
...         tao.pensize(2)
...         tao.pencolor('green')
...         tao.circle(65)
...         tao.left(35)
... 
...         
>>> def deer():
...     for i in range(8):
...         tao.pensize(3)
...         tao.pencolor('pink')
...         tao.circle(30)
...         tao.left(45)
... 
...         
>>> def nemo():
...     for i in range (4):
...         tao.pensize(8)
...         tao.pencolor('brown')
...         tao.forward(100)
...         tao.left(90)
... 
...         
>>> def go(x,y):
...     tao.penup()
...     tao.goto(x,y)
...     tao.pendown()
... 
...     
>>> deer()
>>> go(100,100)
>>> nemo()
>>> go(200,200)
>>> circle()
