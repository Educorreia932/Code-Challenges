## ASCII Table

## Python

171 bytes, 171 chars

```py
D=range
A=print
A(end=f"   {' '.join(map(str,D(2,8)))}\n ")
A('-'*13)
for B in D(16):
	A('%X'%B,end=': ')
	for C in D(2,8):A('DEL'if B+C==22 else chr(C*16+B),end=' ')
	A()
```
