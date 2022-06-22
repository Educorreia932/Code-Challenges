## ASCII Table

## Python

192 bytes, 194 chars

```py
import sys
for B in map(int,sys.argv[1:]):
	C=[1,4,5,9,10,40,50,90,100,400,500,900,1000];A=12;D=''
	while B:D+='I-IVV-IXX-XLL-XCC-CDD-CMM-'[A*2:A*2+2].strip('-')*(B//C[A]);B%=C[A];A-=1
	print(D)
```
