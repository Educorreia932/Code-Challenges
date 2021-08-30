F=range
E=print
C=1000
B=[1]*C
E('2.',end='')
for G in F(C):
	D=0
	for A in F(C-1,-1,-1):B[A]=10*B[A]+D;D=B[A]//(A+2);B[A]=B[A]%(A+2)
	E(D,end='')