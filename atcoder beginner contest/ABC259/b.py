from math import cos, radians, sin

a,b,d = map(int,input().split())

d = radians(d)

a_d = a * cos(d) - b * sin(d)

b_d = b * cos(d) + a * sin(d)

print(a_d,b_d)