#Determine the resultant of 4 forces tangential to circle of radius r cm as shown. What will be the location of the resultant with respect to the centre of the compile
import math
r=float(input("ENTER THE RADIUS OF CIRCLE"))
f1=float(input("ENTER THE VALUE OF FIRST TANGETIAL FORCE "))
f2=float(input("ENTER THE VALUE OF SECOND TANGETIAL FORCE"))
f3=float(input("ENTER THE VALUE OF THIRD TANGENTIAL FORCE"))
f4=float(input("ENTER THE VALUE OF FOURTH TANGENTIAL FORCE"))
t1=float(input("enter the angle of normal from centre to the force 1"))
t2=float(input("enter the angle of normal from centre to the force 2"))
t3=float(input("enter the angle of normal from centre to the force 3"))
t4=float(input("enter the angle of normal from centre to the force 4"))
#finding the resultant

fx= (f1*math.cos(90-t1)) + (f2*math.cos(90-t2)) + (f3*math.cos(90-t3)) + (f4*math.cos(90-t4))
fy = (f1*math.sin(90-t1)) + (f2*math.sin(90-t2)) + (f3*math.sin(90-t3)) + (f4*math.sin(90-t4))
fr = ((fx)^2 + (fy)^2)^1/2
print("RESULTANT OF THE FORCES IS =",round(fr))

#finding the position using verignon's theorm
if f1>0:
  v1=(-1*f1*r)
else:
  v1=(f1*r)
if f2>0:
  v2=(-1*f2*r)
else:
  v2=(f2*r)
if f3>0:
  v3=(-1*f1*r)
else:
  v3=(f1*r)
if f4>0:
  v4=(-1*f1*r)
else:
  v4=(f1*r) 

vr=v1 + v2 + v3 + v4
d=(vr/fr)
print("POSITION OF THE RESULTANT WITH RESPECT TO CENTRE IS ",round(d))