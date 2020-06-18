import turtle

def main():
  # initialize all variables
  dec = None
  d = None
  m = None
  s = None
  p = None

  print("* for DMS conversion enter")
  print("  WHOLE NUMBER value for D")
  print()
  print("* for DECIMAL conversion")
  print("  enter DECIMAL value for D")
  print()
  d = float(input("D:"))
  # if d is a whole number, process as DMS conversion
  if d % 1 == 0:
    d = int(d)
    m = int(input("M:"))
    s = int(input("S:"))
    print("P is decimal places")
    print("press EXE for default of 6")
    p = input("P: ")
  
  # if d is a decimal, process as decimal conversion
  else:
    dec = d
    m = (d % 1) * 60
    d = int(d//1)
    s = (m % 1) * 60
    m = int(m // 1)
    # round to nearest second
    s = int(round(s))
    # if s = 60 bump up m by 1, set s to 0
    if s == 60:
      m += 1
      s = 0
  
  
  # if dec == 999 calculate decimal from DMS, otherwise skip
  if dec == None:
    dec = d + (m/60) + (s/3600)
  # display results
  print()
  print("{} Deg {} Min {} Sec".format(d,m,s))
  # build decimal precision formatting
  # where p is the number of decimal places
  # if user didn't enter p, set to 6
  if p == None:
    p = 6
    p = int(p)
  pstr = "{:." + str(p) + "f}"
  print(pstr.format(dec))
  print("EXE to draw angle")
  input()
  
  # draw circle
  r = 50
  def drawpolargrid(rds):
    rr = int(rds)
    i = 1
    turtle.color('grey')
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(rr)
    turtle.pendown()
    turtle.setheading(0)
    # turtle.circle needs integer!
    turtle.circle(int(rr))
    turtle.penup()
    turtle.goto(0,0)
    turtle.penup()
    # draw spokes
    def drawdashedline(length):
      l=5
      for l in range(5, (length/5)+1):
        turtle.pendown()
        turtle.forward(5)
        turtle.penup()
        turtle.forward(5)
    for i in range(1, 9):
      turtle.pendown()
      turtle.right(45)
      drawdashedline(rr)
      turtle.penup()
      turtle.backward(rr)
      turtle.goto(0,0)
  
  drawpolargrid(r)
  
  # center turtle in circle
  turtle.goto(0,0)
  
  # draw initial side
  turtle.color('blue')
  turtle.pendown()
  turtle.forward(r)
  # back up the turtle to vertex
  turtle.penup()
  turtle.backward(r)
  # draw terminal side
  turtle.color('red')
  turtle.pendown()
  turtle.setheading(dec)
  turtle.forward(r)
main()
