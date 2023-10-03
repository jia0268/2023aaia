float[]A={1.3,2.3,-5.5,-18.8,24.5,39.9,-1.2,5};
float[]B={12.3,-2.3,35.5,-18.8,4.5,39.9,12.2,5};
PImage chair;
int N=8;
void setup(){
  size(500,500);
  chair = loadImage("chair.png");
  frameRate(15);
}
void draw(){
  background(225);
  if (mousePressed){
    float dx = A[frameCount%N];
    float dy = B[frameCount%N];
    image(chair,80+dx,100+dy,300,300);
  }else{
    image(chair,80,100,300,300);
  }
  //rect(200+dx,200,100,100);
}
