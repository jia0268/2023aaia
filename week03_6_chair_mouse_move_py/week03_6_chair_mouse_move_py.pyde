A=[1.3,2.3,-5.5,-18.8,24.5,39.9,-1.2,5]
B=[12.3,-2.3,35.5,-18.8,4.5,39.9,12.2,5]
N=8
def setup():
  size(500,500)
  frameRate(15)
def draw():
  background(225)
  if mousePressed:
    dx = A[frameCount%N]
    dy = B[frameCount%N]
    rect(200+dx,200+dy,100,100)
  else:
    rect(200,200,100,100)
