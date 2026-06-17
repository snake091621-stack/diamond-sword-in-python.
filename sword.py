from turtle import *
speed(15)
colormode(255)
sc=Screen()
sc.setup(width=1.0,height=1.0)

pixel=20
def s(x,y,color,size):
    penup()
    goto(x,y)
    pendown()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for a in range(4):
        forward(size)
        right(90)
    end_fill()

for b in range(3):
    s(-160+b*20,-160,(6, 34, 30),pixel)

s(-120,-140,(6, 34, 30),pixel)

s(-160,-140,(6, 34, 30),pixel)

for c in range(2):
    s(-160+c*20,-120,(6, 34, 30),pixel)

s(-140,-140,(28, 138, 117),pixel)

s(-120,-120,(103, 76, 28),pixel)

s(-100,-100,(136, 101, 37),pixel)

s(-80,-80,(103, 76, 28),pixel)

for d in range(2):   
    s(-100+d*20,-120+d*20,(40, 30, 10),pixel)

for e in range(2):
    s(-120+e*20,-100+e*20,(71, 52, 19),pixel)

s(-80,-60,(6, 34, 30),pixel)

for f in range(2):
    s(-100,-40+f*20,(6, 34, 30),pixel)

for g in range(2):
    s(-120,0+g*20,(6, 34, 30),pixel)

for h in range(2):
    s(-100+h*20,20-h*20,(6, 34, 30),pixel)

for i in range(2):
    s(-60,-20-i*20,(6, 34, 30),pixel)

for j in range(2):
    s(-40+j*20,-60,(6, 34, 30),pixel)

for k in range(2):
    s(0+k*20,-80-k*20,(6, 34, 30),pixel)

for l in range(2):
    s(20-l*20,-120,(6, 34, 30),pixel)

for m in range(2):
    s(-20-m*20,-100,(6, 34, 30),pixel)

s(-60,-80,(6, 34, 30),pixel)

s(-100,0,(19, 97, 83),pixel)

for n in range(2):
    s(-80,-20-n*20,(28, 138, 117),pixel)

for o in range(2):
    s(-60+o*20,-60-o*20,(28, 138, 117),pixel)

for p in range(2):
    s(-20+p*20,-80-p*20,(19, 97, 83),pixel)

for r in range(8):
    s(-40+r*20,-20+r*20,(49, 232, 201),pixel)

for u in range(9):
    s(-40+u*20,-40+u*20,(41, 198, 171),pixel)

for t in range(8):
    s(-20+t*20,-40+t*20,(49, 232, 201),pixel)

for v in range(8):
    s(-40+v*20,0+v*20,(14, 61, 52),pixel)

for x in range(2):
    s(120+x*20,140,(14, 61, 52),pixel)

s(140,120,(14, 61, 52),pixel)

for w in range(8):
    s(140-w*20,100-w*20,(14, 61, 52),pixel)

left(135)

done()
