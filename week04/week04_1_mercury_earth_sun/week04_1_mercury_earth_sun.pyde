def setup():
    size(500,500)
  
def draw():  
    background(0)#黑色背景
    fill(255,92,15)#橘紅色太陽
    ellipse(250,250,80,80)#太陽
  
    a,a2=frameCount/36.0,frameCount/36.0# a,a2 是角度
  
    #cos 是 x , sin 是 y
    ellipse(250+200*cos(a),250+200*sin(a),10,10)#地球
  
    ellipse(250+79*cos(a2),250+79*sin(a2),10,10)#水星
