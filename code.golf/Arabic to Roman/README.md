## ASCII Table

## Python

204 bytes, 204 chars

```py
D=print
import sys
for B in map(int,sys.argv[1:]):
	C=[1,4,5,9,10,40,50,90,100,400,500,900,1000];A=12
	while B:D('I-IVV-IXX-XLL-XCC-CDD-CMM-'[A*2:A*2+2].replace('-','')*(B//C[A]),end='');B%=C[A];A-=1
	D()
```
