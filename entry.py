import re
import gdb


#
#
#  0x1063 <_start+19>:	lea    r8,[rip+0x196]        # 0x1200 <__libc_csu_fini>
#  0x106a <_start+26>:	lea    rcx,[rip+0x11f]        # 0x1190<__libc_csu_init>
#  0x1071 <_start+33>:	lea    rdi,[rip+0xd1]        # 0x1149 <main>
#  0x1078 <_start+40>:	call   QWORD PTR [rip+0x2f62]        # 0x3fe0
#
#
#  0x11af:	lea    r8,[rip+0xc1a]        # 0x1dd0  <__libc_csu_fini>
#  0x11b6:	lea    rcx,[rip+0xbb3]        # 0x1d70 <__libc_csu_init>
#  0x11bd:	lea    rdi,[rip+0xae3]        # 0x1ca7 <main>
#  0x11c4:	call   QWORD PTR [rip+0x2e16]        # 0x3fe0
#
#
#  0x20903 <_start+19>:	lea    r8,[rip+0x88096]        # 0xa89a0 <__libc_csu_fini>
#  0x2090a <_start+26>:	lea    rcx,[rip+0x8801f]        # 0xa8930 <__libc_csu_init>
#  0x20911 <_start+33>:	lea    rdi,[rip+0xffffffffffffe738]        # 0x1f050 <main>
#  0x20918 <_start+40>:	call   QWORD PTR [rip+0xb914a]        # 0xd9a68
#
#

gdb.execute("starti")
output = gdb.execute("info files", to_string=True)
entrypoint = re.search("Entry.+ (0x[a-fA-F0-9]+)", output).group(1)
gdb.execute("break *%s" % entrypoint)
gdb.execute("continue")
gdb.execute("stepi")

reg = "$rdi"
while True:
    output = gdb.execute("x/i $pc", to_string=True)
    if "edi" in output:
        reg = "$edi"
    if "call" in output:
        break
    gdb.execute("stepi")

main_addr = gdb.parse_and_eval(reg)
gdb.execute("break *%d" % main_addr)
gdb.execute("continue")
gdb.write("main @ 0x%x\n" % main_addr, gdb.STDLOG)
