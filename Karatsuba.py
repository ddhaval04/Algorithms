#!/usr/bin/python
def Karatsuba(x,y):
	if x<10 or y<10:
		return x*y;
	m=min(len(str(x))/2,len(str(y))/2)
	bm=10**m
	x1=x/bm
	x2=x%bm
	y1=y/bm
	y2=y%bm
	a=Karatsuba(x1,y1)
	b=Karatsuba(x2,y2)
	c=Karatsuba(x1+x2,y1+y2)-a-b
	return a*(bm**2)+bm*c+b
result=Karatsuba(12,20)
print result
