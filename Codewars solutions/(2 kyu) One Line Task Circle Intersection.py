def circleIntersection(a,b,r):import math as m;x=2*m.acos(min(1,m.hypot(b[0]-a[0],b[1]-a[1])/2/r));return (-m.sin(x)+x)*r*r//1
