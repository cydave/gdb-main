# gdb-main

A utility script which should, in theory, locate the main function of a
stripped x86 32-bit or 64-bit elf binary.

```
(gdb) source ./entry.py 

Program stopped.
0x00007ffff7fd4100 in _start () from /lib64/ld-linux-x86-64.so.2
Breakpoint 1 at 0x555555555050

Breakpoint 1, 0x0000555555555050 in _start ()
0x0000555555555054 in _start ()
0x0000555555555056 in _start ()
0x0000555555555059 in _start ()
0x000055555555505a in _start ()
0x000055555555505d in _start ()
0x0000555555555061 in _start ()
0x0000555555555062 in _start ()
0x0000555555555063 in _start ()
0x000055555555506a in _start ()
0x0000555555555071 in _start ()
0x0000555555555078 in _start ()
Breakpoint 2 at 0x555555555149

Breakpoint 2, 0x0000555555555149 in main ()
main @ 0x555555555149
(gdb) x/20i $rip
=> 0x555555555149 <main>:	push   rbp
   0x55555555514a <main+1>:	mov    rbp,rsp
   0x55555555514d <main+4>:	sub    rsp,0x20
```
